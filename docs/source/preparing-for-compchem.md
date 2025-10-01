---
layout: default
title: Preparing for Computational Chemistry
nav_order: 2
description: "Setting up your computer for HPC access"
permalink: /preparing-for-compchem
has_children: false
---

# Preparing for Computational Chemistry
{: .no_toc }

Setting up your computer for HPC access
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Introduction and Learning Objectives

This guide will help you set up your personal computer to connect to the department's high-performance computing (HPC) system, Steno, where you'll run quantum mechanical calculations throughout this course. By the end of this setup, you will be able to:

- Connect securely to Steno from your laptop using a terminal
- Run computational chemistry software with graphical interfaces

Think of this setup as building a bridge between your laptop and our powerful computational resources. Your laptop will act as a window through which you can control and visualize calculations running on Steno.

## Understanding the Architecture

Steno is a collection of computers, linked together, built for running computational tasks. In essence, Steno is the workhorse that performs your calculations. Connected directly to Steno are four computers called front ends (fend01, fend02, fend03, and fend04). These front ends serve as our communication gateway to Steno.

The connection flow looks like this:

From your personal computer, you will create a secure wireless connection to one of the four front end computers, via which you will then be able to carry out tasks and submit computational jobs using SLURM (the job scheduler) to the cluster of workhorse computers.

## Understanding the Tools

Before we begin the setup, let's understand what each tool does:

**Terminal emulator**: A program that provides a text-based interface to communicate with computers using typed commands rather than clicking buttons. Think of it as having a conversation with the computer where you type instructions and it responds with text. This is how scientists have interacted with computers for decades, and it remains the most powerful way to control computational resources.

**SSH (secure shell)**: A secure method for connecting to remote computers over a network. It's like making an encrypted phone call to another computer, but for sending commands instead of voice. Every command you type and every response you receive is encrypted, ensuring your calculations and data remain secure.

**X11 forwarding**: A system that allows graphical programs running on Steno to display their windows on your screen. Without this, you could only see text output, not the molecular visualization tools like GaussView that we'll use to set up calculations and visualize molecular structures and orbitals.

## Preparation Requirements

Besides a user account (which will be provided at the course start), you need to prepare your personal computer with:

1. An SSH-enabled terminal emulator (to establish the connection)
2. A forwardable version of the X11 window system (to display graphical user interfaces)

The setup process depends on your operating system. Follow the appropriate guide below for your system.

---

## Operating System Specific Setup

### Windows Setup

The easiest and most reliable emulator environment for Windows is the Windows Subsystem for Linux (WSL) program. It is shipped with Windows 10 (and later), so minimum work is needed to install it.

#### Installation Steps

1. Open the start menu and search for "cmd". This should locate the Command Prompt program. Right-click on it and choose the option "Run as administrator".

2. In the Command Prompt, type the following command and press Enter:

   ```bash
   wsl --install -d debian
   ```

   This installs the Windows Subsystem for Linux with Debian, a stable and robust Linux distribution.

3. During the installation, you will be prompted to set up a user account:
   - **Username**: You can use any username you want, but using the same name as your Steno username is strongly recommended for consistency (note that usernames are case-sensitive). Please use your own personal name or some variation of it, NOT your student ID number.
   - **Password**: Choose any secure password you'll remember. You might use the same as your computer password for convenience.

4. Once the installation completes, **reboot your system** to finalize the process.

5. After the reboot, open the start menu and search for "Debian". Open it to access your Linux terminal environment. From now on, this program will be referred to as your terminal.

6. The last step is activating the SSH client. In the terminal, type:

   ```bash
   sudo apt update
   sudo apt install openssh-client
   ```

   Enter your password when prompted. This installs the SSH client that you'll use to connect to Steno. No reboot is needed after this step.

{: .note }
> **Alternative option**: If you have prior experience with PuTTY and prefer to use it, you may continue doing so with Xming for X11 forwarding. However, course support will focus on WSL, which provides a more integrated and modern experience.

### macOS Setup

macOS includes a suitable terminal emulator, but we need to add X11 support for graphical applications through XQuartz.

#### Installation Steps

1. First, check if you have Homebrew (a package manager for macOS) installed. Open Terminal (found in Applications → Utilities) and type:

   ```bash
   brew --version
   ```

2. If you see a version number (like "Homebrew 4.0.0"), skip to step 3. If you see "command not found", you need to install Homebrew:
   - Visit [https://brew.sh](https://brew.sh)
   - Copy and run their one-line installation command in Terminal
   - Follow the on-screen instructions carefully

3. Install XQuartz by typing:

   ```bash
   brew install --cask xquartz
   ```

   This will download and install XQuartz, which may take several minutes.

4. **Important**: After installation completes, you must either:
   - Log out of your Mac account and log back in, or
   - Restart your computer
   
   This step is essential for XQuartz to integrate properly with your system.

5. To verify XQuartz is working correctly:
   - Open XQuartz from your Applications folder
   - Open a new Terminal window
   - Type: `echo $DISPLAY`
   - You should see output similar to `/private/tmp/com.apple.launchd.xxxxx/org.xquartz:0`

{: .important }
> XQuartz must be running in the background when you want to use graphical programs from Steno. The Terminal will automatically detect and use an instance of XQuartz that is running when the Terminal application is started.

### Linux Setup

If you are running a Linux-based operating system (such as Ubuntu, Fedora, or Debian), you should already have a fully functional setup with both a terminal emulator and X11 support. No additional software installation is needed.

You can verify your SSH client is installed by opening a terminal and typing:

```bash
ssh -V
```

If SSH is not installed (unlikely), install it using your distribution's package manager:
- **Ubuntu/Debian**: `sudo apt install openssh-client`
- **Fedora**: `sudo dnf install openssh-clients`
- **Arch**: `sudo pacman -S openssh`

---

## Testing Your Setup

Before the course exercises, verify that your setup works correctly. You need an account on Steno before you can do this.

### Initial Connection Test

1. Open your terminal:
   - **Windows**: Open "Debian" from the Start menu
   - **macOS**: Open Terminal and ensure XQuartz is also running
   - **Linux**: Open your preferred terminal application

2. Test the SSH connection with X11 forwarding:

   ```bash
   ssh -X username@fend01.hpc.ku.dk
   ```

   Replace `username` with your actual Steno username. The `-X` flag enables X11 forwarding for graphical programs.

3. **Important**: On your first connection to any front end, you will see a message about the host's authenticity:

   ```
   The authenticity of host 'fend01.hpc.ku.dk (130.225.xxx.xxx)'
   can't be established.
   ED25519 key fingerprint is SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxx.
   This key is not known by any other names
   Are you sure you want to continue connecting
   (yes/no/[fingerprint])?
   ```

   Copy the displayed fingerprint (the `SHA256:xxx...` string, NOT including the period at the end) and paste it at the prompt, then press Enter.

4. Enter your password when prompted. Note that the password won't display on screen as you type (not even asterisks) – this is a security feature.

5. Once connected, you should see a command prompt like:

   ```
   [username@fend01 ~]$
   ```

### Testing Graphical Display

To verify that X11 forwarding works:

1. While connected to the front end, type:

   ```bash
   /software/kemi/gv6/gaussview
   ```

2. After a moment, the GaussView window should appear on your screen. If it opens successfully, your setup is complete!

3. Close GaussView by pressing Ctrl+C in the terminal or clicking the X button.

4. To disconnect from the front end:

   ```bash
   exit
   ```

---

## Troubleshooting Common Issues

### Windows-Specific Issues

**WSL won't install or gives errors**:
- Run Windows Update to ensure you have the latest Windows version
- Try running `wsl --update` before installation
- If you see "Error: 0x80370102", virtualization is likely disabled in BIOS
- Ensure virtualization is enabled in your BIOS settings
- If nothing works, try installing PuTTY and Xming instead

**Cannot connect after WSL installation**:
- Ensure you're opening the Debian/WSL terminal, not Windows Command Prompt
- Verify SSH is installed by typing `which ssh` in the terminal

### macOS-Specific Issues

**XQuartz won't forward graphics or GaussView won't display**:
- Ensure XQuartz is actually running (look for its icon in the dock)
- Open XQuartz preferences → Security tab → ensure "Allow connections from network clients" is checked
- Try using `ssh -Y` instead of `ssh -X` for trusted connections
- If you just installed XQuartz, make sure you logged out and back in
- Try running: `defaults write org.xquartz.X11 enable_iglx -bool true` in Terminal, then restart

### General Connection Issues

**Connection refused, timeout, or "No route to host"**:
- Verify you're on the university network (see [HPC website](https://hpc.ku.dk) for VPN instructions)
- Check that you're using the correct front-end name (fend01, fend02, fend03, fend04)
- Ensure your username is typed correctly (case-sensitive)
- Try a different front end if one isn't responding

**GaussView won't start or shows "cannot open display"**:
- Verify you used the `-X` flag when connecting
- On Windows, ensure you're using the WSL terminal
- On Mac, confirm XQuartz is running before you connect
- Try `ssh -Y` instead of `ssh -X`

**Password not working**:
- Remember that passwords are case-sensitive
- You won't see anything as you type (this is normal)
- If you've forgotten your password, contact the course administrators

---

## Next Steps

Once you've successfully tested your connection and verified that GaussView displays correctly, you're ready to proceed to the next guide:

[Introduction to the Command-Line Interface →](command-line-intro){: .btn .btn-primary }

---

**Need help?** If you encounter issues that aren't resolved by this guide, contact the course teaching assistant or administrators.
