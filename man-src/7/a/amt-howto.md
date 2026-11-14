---
title: "amt-howto(7)"
name: "amt-howto"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amt-howto/"
---

amt-howto - Intel AMT with linux mini howto

<h2>Description</h2>

<h3>What is AMT and why I should care?</h3>

AMT stands for &quot;Active Management Technology&quot;. It provides some remote management facilities. They are handled by the hardware and firmware, thus they work independant from the operation system. Means: It works before Linux bootet up to the point where it activated the network interface. It works even when your most recent test kernel deadlocked the machine. Which makes it quite useful for development machines ... Intel AMT is part of the vPro Platform. Recent intel-chipset based business machines should have it. My fairly new Intel SDV machine has it too.

<h3>Documentation</h3>

Look here for documentation beyond this mini howto: 
 <a rel="nofollow" HREF="http://www.intel.com/technology/platform-technology/intel-amt/">http://www.intel.com/technology/platform-technology/intel-amt/</a> 
 Most useful to get started: &quot;Intel AMT Deployment and Reference Guide&quot;

<h3>Very short AMT enabling instructions.</h3>

<dl><dt>Enter BIOS Setup.
<dd>* Enable AMT
<dt>Enter ME (Management Extention) Setup. Ctrl-P hotkey works for me.
<dd>* Login, factory default password is &quot;admin&quot;. 
 * Change password. Trivial ones don't work, must include upper- and lowercase letters, digits, special characters. 
 * Enable AMT Managment.
<dt>Reboot, Enter ME Setup again with AMT enabled.
<dd>* Configure AMT (hostname, network config, ...) 
 * Use SMB (Small Business) management mode. The other one (Enterprise) requires Active Directory Service Infrastructure, you don't want that, at least not for your first steps ...</dl>

<h3>Testing AMT</h3>

Take your browser, point it to <a rel="nofollow" HREF="http://machine:16992/.">http://machine:16992/.</a> If you configured AMT to use DHCP (which is the default) the OS and the management stack share the same IP address. You must do that from a remote host as the NIC intercepts network packets for AMT, thus it doesn't work from the local machine as the packets never pass the NIC then. If everything is fine you'll see a greeting page with a button for login. You can login now, using &quot;admin&quot; as username and the password configured during setup. You'll see some pages with informations about the machine. You can also change AMT settings here.

<h3>Control Machine</h3>

You might have noticed already while browing the pages: There is a &quot;Remote Control&quot; page. You can remotely reset and powercycle the machine there, thus recover the machine after booting a b0rken kernel, without having someone walk over to the machine and hit the reset button.

<h3>Serial-over-LAN (SOL) console</h3>

AMT also provides a virtual serial port which can be accessed via network. That gives you a serial console without a serial cable to another machine. If you have activated AMT and SOL the linux kernel should see an additional serial port, like this on my machine: <pre> [root [at] xeni ~]# dmesg | grep ttyS2
 0000:00:03.3: ttyS2 at I/O 0xe000 (irq = 169) is a 16550A</pre>Edit initab, add a line like this: <pre> S2:2345:respawn:/sbin/agetty ttyS2 115200 vt100-nav</pre>You should add the serial port to /etc/securetty too so you are able to login as root. Reload inittab (&quot;init q&quot;). Use amtterm to connect. Tap enter. You should see a login prompt now and be able to login. You can also use that device as console for the linux kernel, using the usual &quot;console=ttyS2,115200&quot; kernel command line argument, so you see the boot messages (and kernel Oopses, if any). You can tell grub to use that serial device, so you can pick a working kernel for the next boot. Usual commands from the grub manual, except that you need &quot;--port=0xe000&quot; instead of &quot;--unit=0&quot; due to the non-standard I/O port for the serial line (my machine, yours might use another port, check linux kernel boot messages). The magic command for the Xen kernel is &quot;com1=115200,8n1,0xe000,0&quot; (again, you might have to replace the I/O port). The final '0' disables the IRQ, otherwise the Xen kernel hangs at boot after enabling interrupts.

<h3>Fun with Xen and AMT</h3>

The AMT network stack seems to become slightly confused when running on a Xen host in DHCP mode. Everything works fine as long as only Dom0 runs. But if one starts a guest OS (with bridged networking) AMT suddenly changes the IP address to the one the guest aquired via DHCP. It is probably a good idea to assign a separate static IP address to AMT then. I didn't manage to switch my machine from DHCP to static IP yet though, the BIOS refuses to accept the settings. The error message doesn't indicate why.

<h3>More fun with AMT</h3>

You might want to download the DTK (Developer Toolkit, source code is available too) and play with it. The .exe is a self-extracting rar archive and can be unpacked on linux using the unrar utility. The Switchbox comes with a linux binary (additionally to the Windows stuff). The GUI tools are written in C#. Trying to make them fly with mono didn't work for me though (mono version 1.2.3 as shipped with Fedora 7). 

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-amtterm/">amtterm</a>(1), <a HREF="/docs/linux/man/1-gamt/">gamt</a>(1), <a HREF="/docs/linux/man/1-amttool/">amttool</a>(1) 

 <a rel="nofollow" HREF="http://www.intel.com/technology/platform-technology/intel-amt/">http://www.intel.com/technology/platform-technology/intel-amt/</a>

<h2>Written By</h2>

Gerd Hoffmann &lt;kraxel [at] redhat.com&gt;
