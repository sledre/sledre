from zipfile import ZipFile, BadZipFile
from contextlib import closing
from django.dispatch import receiver
from django.db.models.signals import post_save

from jobs.models import Job, JobType


class EmptyZipFile(Exception):
    """Raised when a ZipFile is empty (no file present in the archive)"""

    pass


@receiver(post_save, sender=Job)
def job_post_save(sender, instance, *args, **kwargs):
    """post_save signal hook for Job instance.
    The goal is to check if a ZipFile provided by a PESieve worker is empty or not.

    Args:
        sender (class): the signal sender
        instance (Job): the concerned job instance

    Raises:
        EmptyZipFile:
    """
    if instance.job_type == JobType.PESIEVE and instance.results.name:
        try:
            with closing(ZipFile(instance.results)) as z:
                count = len(z.infolist())
            if count == 0:
                raise EmptyZipFile()
        except (BadZipFile, EmptyZipFile):
            instance.results.delete()
            instance.save()
