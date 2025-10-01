---
layout: default
title: Home
nav_order: 1
description: "Computational chemistry teaching materials for HPC-based quantum mechanical calculations"
permalink: /
---

# Introduction to high-performance computing in chemistry

Welcome to the computational chemistry teaching materials for the University of Copenhagen's MSc course. This documentation will guide you from initial setup through running quantum mechanical calculations on the Steno HPC system.

## About this guide

This guide is written to help you get started with high-performance computing (HPC) for computational chemistry, using the Steno HPC system. While specifically configured for the University of Copenhagen's infrastructure, the documentation and teaching approach provide a foundation that students and researchers at other institutions may find valuable.

You will learn how to:
- Set up your personal computer to connect securely to Steno
- Navigate and work efficiently in the command-line environment
- Submit and manage computational chemistry jobs
- Use the SLURM scheduler and understand HPC architecture
- Build valuable skills in scientific computing that extend beyond this course

By following the step-by-step examples, you will not only be able to run Gaussian and other software on Steno, but also build transferable computational skills.

## Getting started

The guides are organized to take you through the learning process systematically:

### 1. [Preparing for Computational Chemistry](preparing-for-compchem.md)
**Start here if you're new to HPC and remote computing**

Learn how to set up your personal computer (Windows, macOS, or Linux) to connect to the Steno HPC system. This guide covers:
- Installing terminal emulators and SSH clients
- Configuring X11 forwarding for graphical programs
- Testing your connection
- Troubleshooting common issues

### 2. [Introduction to the Command-Line Interface](command-line-intro.md)
**Essential skills for everyone**

Master the fundamentals of working in a terminal environment:
- Understanding the terminal session and prompt
- Navigating the file system
- Managing files and directories
- Text editing with nano and vim
- Using shortcuts and efficient workflows

### 3. [Introduction to Steno](steno-intro.md)
**Understanding the HPC environment**

Learn how the Steno system works and how to use it effectively:
- HPC architecture and the SLURM scheduler
- Submitting and monitoring jobs
- Resource allocation and optimization
- Job arrays for multiple calculations
- Best practices for shared computing

## Additional Resources

### Configuration files
Ready-to-use configuration files are provided in the [config directory](https://github.com/zliasi/compchem/tree/main/config):
- `bashrc` - Shell configuration with helpful aliases
- `vimrc` - Vim editor configuration with syntax highlighting
- `nanorc` - Nano editor configuration

### Submission scripts
Pre-built SLURM submission scripts for common quantum chemistry packages are available in the [scripts directory](https://github.com/zliasi/compchem/tree/main/scripts):
- Gaussian 16 submission script
- Dalton submission script

### Examples
Completed exercise solutions with input files, output files, and explanatory notes can be found in the [examples directory](https://github.com/zliasi/compchem/tree/main/examples) (coming soon).

## Getting help

If you encounter difficulties:
1. Check the troubleshooting sections in each guide
2. Review the [GitHub repository issues](https://github.com/zliasi/compchem/issues)
3. Contact course instructors through normal course channels

For errors in documentation or suggestions for improvement, please [open an issue](https://github.com/zliasi/compchem/issues/new) on GitHub.

## Using these materials

### For Students
Follow the guides in order, starting with preparation and setup. The documentation assumes no prior experience with terminals or remote computing, introducing concepts gradually with clear explanations.

### For instructors
These materials are provided openly for educational purposes. If you adapt them for your institution, attribution to this repository and the University of Copenhagen's Department of Chemistry is appreciated. Note that the submission scripts are specifically configured for Steno and will require modification for other HPC systems.

---

**Author**: Zacharias Liasi  
**Institution**: University of Copenhagen, Department of Chemistry  
**Course**: Computational Chemistry (MSc)  
**Last Updated**: October 2025

Ready to begin? Start with [Preparing for Computational Chemistry](preparing-for-compchem.md)
