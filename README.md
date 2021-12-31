<p align="center">
  <img width="200" height="200" src="https://sled.re/images/favicon.png">
</p>

[![Release](https://github.com/sledre/sledre/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/sledre/sledre/actions/workflows/release.yml)
[![Linter](https://github.com/sledre/sledre/actions/workflows/linter.yml/badge.svg?branch=main)](https://github.com/sledre/sledre/actions/workflows/linter.yml)
# SledRE

***This project is in alpha version. It can be buggy and many improvements can be done. If you wish, do not hesitate to make a contribution.***

## Introduction

[SledRE](https://github.com/sledre/sledre) is a scalable application for Windows malware analysis. It allows to run multiples jobs in parallels.
At the moment, two jobs are available:
- [PESieve](https://github.com/hasherezade/pe-sieve): this job goal is to unpack a Windows PE malware using PESieve.
- [Detours](https://github.com/microsoft/Detours): this job goal is to hook and trace syscalls of Windows PE malware (more than a thousand common syscalls). Theses traces can be used to create artificial intelligence models. But they can also be directly imported to Ghidra using [ghidra-sledre](https://github.com/sledre/ghidra-sledre/) extension to help reverse engineers.   

## Main features
* Windows 7 sandbox using qemu and Linux containers
* Automated installation using a script to build the VM with required binaries
* Scalability of the Windows workers depending on the host resources
* Windows syscall hooking to generate traces
* Malware unpacking using PESieve
* Tag creation based on hook traces
* Dataset generation
* Ghidra extension to import SledRE traces

## Installation & Usage
The installation and usage procedures are covered by the documentation.  
The project documentation is available at [SledRE Documentation](https://sled.re/).

## Architecture
<p align="center">
  <img height="500" src="https://sled.re/images/SledREArchi.png">
</p>


## Contributing
If you wish to make a contribution, you should check out the [Development Documentation](https://sled.re/development/)
