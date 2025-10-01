# Computational Chemistry Teaching Materials

Welcome to the computational chemistry teaching materials for the University of Copenhagen's MSc course. This documentation will guide you from initial setup through running quantum mechanical calculations on the Steno HPC system.

## About This Guide

This guide helps you get started with high-performance computing (HPC) for computational chemistry using the Steno HPC system. You will learn how to:

- Set up your personal computer to connect securely to Steno
- Navigate and work efficiently in the command-line environment
- Submit and manage computational chemistry jobs
- Use the SLURM scheduler and understand HPC architecture
- Build valuable skills in scientific computing that extend beyond this course

By following the step-by-step examples, you will not only be able to run Gaussian and other software on Steno, but also develop transferable computational skills valuable throughout your research career.

## Getting Started

The guides are organized to take you through the learning process systematically:

```{toctree}
:maxdepth: 2
:caption: Guides

preparing-for-compchem
command-line-intro
steno-intro
```

```{toctree}
:maxdepth: 1
:caption: Resources

GitHub Repository <https://github.com/zliasi/compchem>
```

### 1. Preparing for Computational Chemistry
**Start here if you're new to HPC and remote computing**

Learn how to set up your personal computer (Windows, macOS, or Linux) to connect to the Steno HPC system. This guide covers installing terminal emulators, configuring X11 forwarding, testing your connection, and troubleshooting common issues.

{doc}`Read the preparation guide →<preparing-for-compchem>`

### 2. Introduction to the Command-Line Interface
**Essential skills for everyone**

Master the fundamentals of working in a terminal environment including understanding the terminal session, navigating the file system, managing files and directories, text editing with nano and vim, and using efficient workflows.

{doc}`Read the CLI guide →<command-line-intro>`

### 3. Introduction to Steno
**Understanding the HPC environment**

Learn how the Steno system works and how to use it effectively, including HPC architecture, the SLURM scheduler, submitting and monitoring jobs, resource allocation strategies, and best practices for shared computing.

{doc}`Read the Steno guide →<steno-intro>`

## Additional Resources

### Configuration Files
Ready-to-use configuration files are provided in the repository:
- `bashrc` - Shell configuration with helpful aliases
- `vimrc` - Vim editor configuration with syntax highlighting  
- `nanorc` - Nano editor configuration

### Submission Scripts
Pre-built SLURM submission scripts for common quantum chemistry packages:
- Gaussian 16 submission script
- Dalton submission script

### Examples
Completed exercise solutions with input files, output files, and explanatory notes (coming soon).

## Getting Help

If you encounter difficulties:
1. Check the troubleshooting sections in each guide
2. Review the [GitHub repository issues](https://github.com/zliasi/compchem/issues)
3. Contact course instructors through normal course channels

For errors in documentation or suggestions for improvement, please [open an issue](https://github.com/zliasi/compchem/issues/new) on GitHub.

## About These Materials

These materials are specifically configured for the University of Copenhagen's infrastructure and the Steno HPC system. While the submission scripts require modification for other HPC systems, the documentation and teaching approach provide a foundation that may be valuable for students and researchers at other institutions.

If you use or adapt these materials in your teaching or research, attribution to this repository and the University of Copenhagen's Department of Chemistry is appreciated.

---

**Author**: Zacharias Liasi  
**Institution**: University of Copenhagen, Department of Chemistry  
**Course**: Computational Chemistry (MSc)  
**Last Updated**: October 2025

**License**: MIT License

