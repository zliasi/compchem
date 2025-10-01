# Computational Chemistry

This repository contains submission scripts, configuration files, documentation, and exercise materials for the MSc course Computational Chemistry at the University of Copenhagen, Department of Chemistry. The course teaches students how to use quantum mechanical calculations to study molecular structure, properties, and reactivity using the [Steno high-performance computing system](https://hpc.ku.dk/index.html). For official course information, including prerequisites and learning objectives, consult the [course catalogue](https://kurser.ku.dk/#q=Computational+Chemistry&education=&programme=&volume=&departments=&faculty=&studyBlockId=&teachingLanguage=&period=&schedules=&studyId=&openUniversityInternational=0&searched=1).

While these materials are specifically configured for the University of Copenhagen's HPC infrastructure, the documentation and teaching approach provide a foundation that students and researchers at other institutions may find valuable when setting up their own computational chemistry workflows.

## What's included

This repository provides everything you need to start running quantum mechanical calculations on the Steno HPC system. The **scripts** directory contains SLURM submission scripts for Gaussian (Release 16, Revision A.03) and Dalton (Release 2020.1) that handle job submission, resource management, and output organization. These scripts include features like automatic backup of existing output files and support for job arrays to run multiple calculations efficiently. The **config** directory provides configuration files for bash, vim, and nano that make working on the command line more comfortable and efficient, with syntax highlighting, helpful aliases, and a cleaner terminal environment. The **docs** directory contains comprehensive guides that walk you through every step from setting up your computer to connect to Steno, through learning basic command-line usage, to understanding how to submit and monitor your calculations. The **examples** directory includes completed versions of all course exercises with input files, output files, and tips to help you understand what successful calculations should look like and how to interpret the results.

## For students: Getting started

If you are enrolled in the Computational Chemistry course, your journey with these materials begins with preparing your personal computer to connect to the Steno HPC system. You will need to install a terminal emulator and set up X11 forwarding so you can run graphical programs like GaussView remotely. The first document you should read is the **Preparing for Computational Chemistry** guide in the docs directory, which provides detailed, step-by-step instructions tailored to your operating system (Windows, macOS, or Linux). This guide assumes no prior experience with terminals or remote computing and walks you through every installation step with explanations of what each tool does and why you need it.

Once your computer is set up and you can successfully connect to Steno, you should work through the **Introduction to the Command-Line Interface** guide. Many students arrive at this course having never used a terminal before, and the command line can feel intimidating at first. This guide introduces commands gradually, explaining not just how to use them but why they work the way they do. You will learn how to navigate directories, create and edit files, and manage your computational work. Even if you have some command-line experience, this guide is worth reading because it highlights patterns specific to working on HPC systems.

After you are comfortable with basic command-line operations, read the **Introduction to Steno** guide, which explains how the HPC system is organized, how to submit jobs through the SLURM scheduler, and how to monitor your calculations as they run. Finally, before starting the course exercises, review the **Guide to the Submission Scripts** documentation, which explains how to use the provided Gaussian and Dalton scripts to run your calculations efficiently.

The documentation website at [https://zliasi.github.io/compchem](https://zliasi.github.io/compchem) presents these guides in a formatted, easy-to-navigate interface. Alternatively, the **Introduction to high-performance computing in chemistry** document is available, containing all guides in one.  

## Accessing the materials

The recommended way for students, is to clone this repository directly to your account on Steno. Open your terminal, connect to Steno, and run the following command:

```bash
$ git clone https://github.com/zliasi/compchem.git
```

This command creates a directory called *compchem* in your current location and downloads all the repository contents into it. To install the submission scripts and configuration files so they are ready to use, navigate into this directory and run the setup script:

```bash
$ cd compchem
$ ./setup
```

The setup script copies the submission scripts to your *bin* directory so you can run them from anywhere, and it installs the configuration files in your home directory. If you already have a bashrc or vimrc file, the setup script will overwrite them, so backup your existing configurations if you want to save them.

If you want to keep your local copy synchronized with future updates, Git provides a simple way to fetch the latest changes. From within your compchem directory on Steno, run:

```bash
git pull
```

This command downloads any new materials or script improvements that have been added since you first cloned the repository.

## Understanding what these scripts do

The submission scripts in this repository do much more than simply start a calculation. When you submit a Gaussian or Dalton job using these scripts, they automatically create an organized output directory, back up any existing output files so you do not accidentally overwrite previous results, set up temporary scratch space for the calculation's working files, run the actual quantum chemistry program with appropriate resource allocation, move checkpoint files to permanent storage, clean up temporary files, and generate a summary of the computational resources your job actually used. This automation means you can focus on the science rather than the technical details of job management, though understanding what happens behind the scenes helps you troubleshoot problems and optimize your calculations.

The configuration files similarly aim to make your command-line experience more pleasant and productive. The bashrc file sets up useful aliases like sq to quickly view your job queue and pinfo to check partition availability. It also configures your prompt to show your current location in the filesystem more clearly. The vimrc file enables syntax highlighting for code and input files, shows line numbers, and sets up sensible indentation and search behavior so editing text files becomes more intuitive.

## Updates and version history

This repository is actively maintained. When important updates are made -- such as bug fixes in the submission scripts, improvements to the documentation, or new example calculations -- they will be documented in the CHANGELOG.md file. You can review this file periodically to see what has changed since you last accessed the materials. If you cloned the repository using Git, you can easily update to the latest version as described in the previous section.

## Getting help

If you encounter difficulties while working through these materials, several support pathways are available. For technical problems with the submission scripts or questions about how to use the materials, you can open an issue on this GitHub repository describing the problem you are experiencing. Include relevant details like error messages you received, what you were trying to accomplish, and what you have already tried. For course-specific questions or problems connecting to Steno, contact the course TA or instructors through the normal course communication channels.

If you notice errors in the documentation, unclear explanations, or have suggestions for improving these materials, opening a GitHub issue is the best way to bring these to attention. Your feedback helps improve the materials for future students and for others who might use these resources. Alternatively, write an email to zachliasi@gmail.com, or to one of the course instructors via either UCPH email or Absalon.

## License and citation

These materials are provided for educational purposes. If you use or adapt these materials in your own teaching or research workflows, attribution to this repository is greatly appreciated.

---

**Author**: Zacharias Liasi  
**Contact**: zachliasi@gmail.com
**GitHub**: [github.com/zliasi](https://github.com/zliasi)  
**Last Updated**: October 2025
