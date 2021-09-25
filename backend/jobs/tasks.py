import jsonlines

from celery import shared_task

from jobs.models import Job, JobType
from tags.rule import RULES_PATHS, get_rules, get_apicalls_from_traces


@shared_task
def process_results(job):
    """Celery task to compute extra results from worker submission.

    Args:
        job (UUID): Job UUID (primary key).
    """
    job = Job.objects.filter(pk=job).get()

    if job.job_type == JobType.DETOURS:
        tags = process_detours_results(job)
    elif job.job_type == JobType.PESIEVE:
        tags = process_pesieve_results(job)

    job.extras_results["tags"] = tags
    job.save()


def process_detours_results(job):
    """Compute tags from detours traces and provided rules.

    Args:
        job (Job): Job where results should be analyzed

    Returns:
        list: list of tags corresponding to rules that matched
    """
    rules = get_rules(RULES_PATHS)

    with jsonlines.open(job.results.path) as jl_reader:
        api_calls = get_apicalls_from_traces(jl_reader)

    tags = set()
    for rule in rules:
        for pattern in rule.patterns:
            if pattern in api_calls:
                tags.add(rule.tag)

    return list(tags)


def process_pesieve_results(job):
    """Compute tags depending on PESieve being able to extract shellcodes.

    Args:
        job (Job): Job where results should be analyzed

    Returns:
        list: Success or Empty depending on PESieve results
    """
    return ["Success"] if job.results.name else ["Empty"]
