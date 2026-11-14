---
title: "salt(7)"
name: "salt"
section: "7"
letter: "s"
url: "/docs/linux/man/7-salt/"
description: "salt – Salt Documentation"
---

<h2 id="name">NAME</h2>
<p> salt &#8211; Salt Documentation</p>
<h2 id="INTRODUCTION TO SALT"></h2>
<p> Weâre not just talking about NaCl..SS The 30 second summary </p>
<p> Salt is:</p>
<dl>
<dt>&bull;</p>
<dd> a configuration management system, capable of maintaining remote nodes in defined states (for example, ensuring that specific packages are installed and specific services are running)</p>
<dt>&bull;</p>
<dd> a distributed remote execution system used to execute commands and query data on remote nodes, either individually or by arbitrary selection criteria </p>
<p> It was developed in order to bring the best solutions found in the world of remote execution together and make them better, faster, and more malleable. Salt accomplishes this through its ability to handle large loads of information, and not just dozens but hundreds and even thousands of individual servers quickly through a simple and manageable interface.</dl>
<h3>Simplicity</h3>
<p> Providing versatility between massive scale deployments and smaller systems may seem daunting, but Salt is very simple to set up and maintain, regardless of the size of the project. The architecture of Salt is designed to work with any number of servers, from a handful of local network systems to international deployments across different data centers. The topology is a simple server/client model with the needed functionality built into a single set of daemons. While the default configuration will work with little to no modification, Salt can be fine tuned to meet specific needs.</p>
<h3>Parallel execution</h3>
<p> The core functions of Salt:</p>
<dl>
<dt>&bull;</p>
<dd> enable commands to remote systems to be called in parallel rather than serially</p>
<dt>&bull;</p>
<dd> use a secure and encrypted protocol</p>
<dt>&bull;</p>
<dd> use the smallest and fastest network payloads possible</p>
<dt>&bull;</p>
<dd> provide a simple programming interface </p>
<p> Salt also introduces more granular controls to the realm of remote execution, allowing systems to be targeted not just by hostname, but also by system properties.</dl>
<h3>Building on proven technology</h3>
<p> Salt takes advantage of a number of technologies and techniques. The networking layer is built with the excellent <i>ZeroMQ</i> networking library, so the Salt daemon includes a viable and transparent AMQ broker. Salt uses public keys for authentication with the master daemon, then uses faster <i>AES</i> encryption for payload communication; authentication and encryption are integral to Salt. Salt takes advantage of communication via <i>msgpack</i>, enabling fast and light network traffic.</p>
<h3>Python client interface</h3>
<p> In order to allow for simple expansion, Salt execution routines can be written as plain Python modules. The data collected from Salt executions can be sent back to the master server, or to any arbitrary program. Salt can be called from a simple Python API, or from the command line, so that Salt can be used to execute one-off commands as well as operate as an integral part of a larger application.</p>
<h3>Fast, flexible, scalable</h3>
<p> The result is a system that can execute commands at high speed on target server groups ranging from one to very many servers. Salt is very fast, easy to set up, amazingly malleable and provides a single remote execution architecture that can manage the diverse requirements of any number of servers. The Salt infrastructure brings together the best of the remote execution world, amplifies its capabilities and expands its range, resulting in a system that is as versatile as it is practical, suitable for any network.</p>
<h3>Open</h3>
<p> Salt is developed under the <i>Apache 2.0 license</i>, and can be used for open and proprietary projects. Please submit your expansions back to the Salt project so that we can all benefit together as Salt grows. Please feel free to sprinkle Salt around your systems and let the deliciousness come forth.</p>
<h3>Salt Community</h3>
<p> Join the Salt! </p>
<p> There are many ways to participate in and communicate with the Salt community. </p>
<p> Salt has an active IRC channel and a mailing list.</p>
<h3>Mailing List</h3>
<p> Join the <i>salt-users mailing list</i>. It is the best place to ask questions about Salt and see whats going on with Salt development! The Salt mailing list is hosted by Google Groups. It is open to new members. </p>
<p> <i><a rel="nofollow noopener" href="https://groups.google.com/forum/#!forum/salt-users" target="_blank">https://groups.google.com/forum/#!forum/salt-users</a></i> </p>
<p> There is also a low-traffic list used to announce new releases called <i>salt-announce</i> </p>
<p> <i><a rel="nofollow noopener" href="https://groups.google.com/forum/#!forum/salt-announce" target="_blank">https://groups.google.com/forum/#!forum/salt-announce</a></i></p>
<h3>IRC</h3>
<p> The <code>#salt</code> IRC channel is hosted on the popular <i>Freenode</i> network. You can use the <i>Freenode webchat client</i> right from your browser. </p>
<p> <i>Logs of the IRC channel activity</i> are being collected courtesy of Moritz Lenz. </p>
<p> If you wish to discuss the development of Salt itself join us in <code>#salt-devel</code>.</p>
<h3>Follow on Github</h3>
<p> The Salt code is developed via Github. Follow Salt for constant updates on what is happening in Salt development: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt" target="_blank">https://github.com/saltstack/salt</a></i></p>
<h3>Blogs</h3>
<p> SaltStack Inc. keeps a <i>blog</i> with recent news and advancements: </p>
<p> <i><a rel="nofollow noopener" href="http://www.saltstack.com/blog/" target="_blank">http://www.saltstack.com/blog/</a></i> </p>
<p> Thomas Hatch also shares news and thoughts on Salt and related projects in his personal blog <i>The Red45</i>: </p>
<p> <i><a rel="nofollow noopener" href="http://red45.wordpress.com/" target="_blank">http://red45.wordpress.com/</a></i></p>
<h3>Example Salt States</h3>
<p> The official <code>salt-states</code> repository is: <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-states" target="_blank">https://github.com/saltstack/salt-states</a></i> </p>
<p> A few examples of salt states from the community:</p>
<dl>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/blast-hardcheese/blast-salt-states" target="_blank">https://github.com/blast-hardcheese/blast-salt-states</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/kevingranade/kevingranade-salt-state" target="_blank">https://github.com/kevingranade/kevingranade-salt-state</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/uggedal/states" target="_blank">https://github.com/uggedal/states</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/mattmcclean/salt-openstack/tree/master/salt" target="_blank">https://github.com/mattmcclean/salt-openstack/tree/master/salt</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/rentalita/ubuntu-setup/" target="_blank">https://github.com/rentalita/ubuntu-setup/</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/brutasse/states" target="_blank">https://github.com/brutasse/states</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/bclermont/states" target="_blank">https://github.com/bclermont/states</a></i></p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow noopener" href="https://github.com/pcrews/salt-data" target="_blank">https://github.com/pcrews/salt-data</a></i></dl>
<h3>Follow on ohloh</h3>
<p> <i><a rel="nofollow noopener" href="https://www.ohloh.net/p/salt" target="_blank">https://www.ohloh.net/p/salt</a></i></p>
<h3>Other community links</h3>
<dl>
<dt>&bull;</p>
<dd> <i>Salt Stack Inc.</i></p>
<dt>&bull;</p>
<dd> <i>Subreddit</i></p>
<dt>&bull;</p>
<dd> <i>Google+</i></p>
<dt>&bull;</p>
<dd> <i>YouTube</i></p>
<dt>&bull;</p>
<dd> <i>Facebook</i></p>
<dt>&bull;</p>
<dd> <i>Twitter</i></p>
<dt>&bull;</p>
<dd> <i>Wikipedia page</i></dl>
<h3>Hack the Source</h3>
<p> If you want to get involved with the development of source code or the documentation efforts, please review the <code>hacking section</code>!</p>
<h2 id="INSTALLATION"></h2>
<p> <code>SEE ALSO:</code> <code>Installing Salt for development</code> and contributing to the project.</p>
<h3>Quick Install</h3>
<p> On most distributions, you can set up a <code>Salt Minion</code> with the <i>Salt Bootstrap</i>.</p>
<h3>Platform-specific Installation Instructions</h3>
<p> These guides go into detail how to install Salt on a given platform.</p>
<h3>Arch Linux</h3>
<h3>Installation</h3>
<p> Salt (stable) is currently available via the Arch Linux Official repositories. There are currently -git packages available in the Arch User repositories (AUR) as well.</p>
<h3>Stable Release</h3>
<p> Install Salt stable releases from the Arch Linux Official repositories as follows: </p>
<pre>
pacman -S salt-zmq
</pre>
<p> To install Salt stable releases using the <code>RAET protocol</code>, use the following: </p>
<pre>
pacman -S salt-raet
</pre>
<h3>Tracking develop</h3>
<p> To install the bleeding edge version of Salt (<code>may include bugs!</code>), use the -git package. Installing the -git package as follows: </p>
<pre>
wget <a rel="nofollow noopener" href="https://aur.archlinux.org/packages/sa/salt-git/salt-git.tar.gz" target="_blank">https://aur.archlinux.org/packages/sa/salt-git/salt-git.tar.gz</a>
tar xf salt-git.tar.gz
cd salt-git/
makepkg -is
</pre>
<p> <code>NOTE:</code> yaourt </p>
<p> If a tool such as <i>Yaourt</i> is used, the dependencies will be gathered and built automatically. </p>
<p> The command to install salt using the yaourt tool is: </p>
<pre>
yaourt salt-git
</pre>
<h3>Post-installation tasks</h3>
<p> <code>systemd</code> </p>
<p> Activate the Salt Master and/or Minion via <code>systemctl</code> as follows: </p>
<pre>
systemctl enable salt-master.service
systemctl enable salt-minion.service
</pre>
<p> <code>Start the Master</code> </p>
<p> Once you&#8217;ve completed all of these steps you&#8217;re ready to start your Salt Master. You should be able to start your Salt Master now using the command seen here: </p>
<pre>
systemctl start salt-master
</pre>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>Debian Installation</h3>
<p> Currently the latest packages for Debian Old Stable, Stable, and Unstable (Squeeze, Wheezy, and Sid) are published in our (saltstack.com) Debian repository.</p>
<h3>Configure Apt</h3>
<h3>Squeeze (Old Stable)</h3>
<p> For squeeze, you will need to enable the Debian backports repository as well as the debian.saltstack.com repository. To do so, add the following to <code>/etc/apt/sources.list</code> or a file in <code>/etc/apt/sources.list.d</code>: </p>
<pre>
deb <a rel="nofollow noopener" href="http://debian.saltstack.com/debian" target="_blank">http://debian.saltstack.com/debian</a> squeeze-saltstack main
deb <a rel="nofollow noopener" href="http://backports.debian.org/debian-backports" target="_blank">http://backports.debian.org/debian-backports</a> squeeze-backports main contrib non-free
</pre>
<h3>Wheezy (Stable)</h3>
<p> For wheezy, the following line is needed in either <code>/etc/apt/sources.list</code> or a file in <code>/etc/apt/sources.list.d</code>: </p>
<pre>
deb <a rel="nofollow noopener" href="http://debian.saltstack.com/debian" target="_blank">http://debian.saltstack.com/debian</a> wheezy-saltstack main
</pre>
<h3>Jessie (Testing)</h3>
<p> For jessie, the following line is needed in either <code>/etc/apt/sources.list</code> or a file in <code>/etc/apt/sources.list.d</code>: </p>
<pre>
deb <a rel="nofollow noopener" href="http://debian.saltstack.com/debian" target="_blank">http://debian.saltstack.com/debian</a> jessie-saltstack main
</pre>
<h3>Sid (Unstable)</h3>
<p> For sid, the following line is needed in either <code>/etc/apt/sources.list</code> or a file in <code>/etc/apt/sources.list.d</code>: </p>
<pre>
deb <a rel="nofollow noopener" href="http://debian.saltstack.com/debian" target="_blank">http://debian.saltstack.com/debian</a> unstable main
</pre>
<h3>Import the repository key.</h3>
<p> You will need to import the key used for signing. </p>
<pre>
wget -q -O- &quot;<a rel="nofollow noopener" href="http://debian.saltstack.com/debian-salt-team-joehealy.gpg.key" target="_blank">http://debian.saltstack.com/debian-salt-team-joehealy.gpg.key</a>&quot; | apt-key add -
</pre>
<p> <code>NOTE:</code> You can optionally verify the key integrity with <code>sha512sum</code> using the public key signature shown here. E.g: </p>
<pre>
echo &quot;b702969447140d5553e31e9701be13ca11cc0a7ed5fe2b30acb8491567560ee62f834772b5095d735dfcecb2384a5c1a20045f52861c417f50b68dd5ff4660e6  debian-salt-team-joehealy.gpg.key&quot; | sha512sum -c
</pre>
<h3>Update the package database</h3>
<pre>
apt-get update
</pre>
<h3>Install packages</h3>
<p> Install the Salt master, minion, or syndic from the repository with the apt-get command. These examples each install one daemon, but more than one package name may be given at a time: </p>
<pre>
apt-get install salt-master
</pre>
<pre>
apt-get install salt-minion
</pre>
<pre>
apt-get install salt-syndic
</pre>
<h3>Post-installation tasks</h3>
<p> Now, go to the <code>Configuring Salt</code> page.</p>
<h3>Notes</h3>
<p> 1. These packages will be backported from the packages intended to be uploaded into Debian unstable. This means that the packages will be built for unstable first and then backported over the next day or so. </p>
<p> 2. These packages will be tracking the released versions of salt rather than maintaining a stable fixed feature set. If a fixed version is what you desire, then either pinning or manual installation may be more appropriate for you. </p>
<p> 3. The version numbering and backporting process should provide clean upgrade paths between Debian versions. </p>
<p> If you have any questions regarding these, please email the mailing list or look for joehh on IRC.</p>
<h3>Fedora</h3>
<p> Beginning with version 0.9.4, Salt has been available in the primary Fedora repositories and <i>EPEL</i>. It is installable using yum. Fedora will have more up to date versions of Salt than other members of the Red Hat family, which makes it a great place to help improve Salt! </p>
<p> <code>WARNING</code>: Fedora 19 comes with systemd 204. Systemd has known bugs fixed in later revisions that prevent the salt-master from starting reliably or opening the network connections that it needs to. It&#8217;s not likely that a salt-master will start or run reliably on any distribution that uses systemd version 204 or earlier. Running salt-minions should be OK.</p>
<h3>Installation</h3>
<p> Salt can be installed using <code>yum</code> and is available in the standard Fedora repositories.</p>
<h3>Stable Release</h3>
<p> Salt is packaged separately for the minion and the master. It is necessary only to install the appropriate package for the role the machine will play. Typically, there will be one master and multiple minions. </p>
<pre>
yum install salt-master
yum install salt-minion
</pre>
<h3>Installing from <code>updates-testing</code></h3>
<p> When a new Salt release is packaged, it is first admitted into the <code>updates-testing</code> repository, before being moved to the stable repo. </p>
<p> To install from <code>updates-testing</code>, use the <code>enablerepo</code> argument for yum: </p>
<pre>
yum --enablerepo=updates-testing install salt-master
yum --enablerepo=updates-testing install salt-minion
</pre>
<h3>Installation Using pip</h3>
<p> Since Salt is on <i>PyPI</i>, it can be installed using pip, though most users prefer to install using a package manager. </p>
<p> Installing from pip has a few additional requirements:</p>
<dl>
<dt>&bull;</p>
<dd> Install the group &#8216;Development Tools&#8217;, <code>dnf groupinstall &#8216;Development Tools&#8217;</code></p>
<dt>&bull;</p>
<dd> Install the &#8216;zeromq-devel&#8217; package if it fails on linking against that afterwards as well. </p>
<p> A pip install does not make the init scripts or the /etc/salt directory, and you will need to provide your own systemd service unit. </p>
<p> Installation from pip: </p>
<pre>
pip install salt
</pre>
<p> <code>WARNING:</code> If installing from pip (or from source using <code>setup.py install</code>), be advised that the <code>yum-utils</code> package is needed for Salt to manage packages. Also, if the Python dependencies are not already installed, then you will need additional libraries/tools installed to build some of them. More information on this can be found here.</dl>
<h3>Post-installation tasks</h3>
<p> <code>Master</code> </p>
<p> To have the Master start automatically at boot time: </p>
<pre>
systemctl enable salt-master.service
</pre>
<p> To start the Master: </p>
<pre>
systemctl start salt-master.service
</pre>
<p> <code>Minion</code> </p>
<p> To have the Minion start automatically at boot time: </p>
<pre>
systemctl enable salt-minion.service
</pre>
<p> To start the Minion: </p>
<pre>
systemctl start salt-minion.service
</pre>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>FreeBSD</h3>
<p> Salt was added to the FreeBSD ports tree Dec 26th, 2011 by Christer Edwards &lt;<i>christer.edwards [at] gmail.com</i>&gt;. It has been tested on FreeBSD 7.4, 8.2, 9.0, and 9.1 releases. </p>
<p> Salt is dependent on the following additional ports. These will be installed as dependencies of the <code>sysutils/py-salt</code> port: </p>
<pre>
/devel/py-yaml
/devel/py-pyzmq
/devel/py-Jinja2
/devel/py-msgpack
/security/py-pycrypto
/security/py-m2crypto
</pre>
<h3>Installation</h3>
<p> On FreeBSD 10 and later, to install Salt from the FreeBSD pkgng repo, use the command: </p>
<pre>
pkg install py27-salt
</pre>
<p> On older versions of FreeBSD, to install Salt from the FreeBSD ports tree, use the command: </p>
<pre>
make -C /usr/ports/sysutils/py-salt install clean
</pre>
<h3>Post-installation tasks</h3>
<p> <code>Master</code> </p>
<p> Copy the sample configuration file: </p>
<pre>
cp /usr/local/etc/salt/master.sample /usr/local/etc/salt/master
</pre>
<p> <code>rc.conf</code> </p>
<p> Activate the Salt Master in <code>/etc/rc.conf</code> or <code>/etc/rc.conf.local</code> and add: </p>
<pre>
+ salt_master_enable=&quot;YES&quot;
</pre>
<p> <code>Start the Master</code> </p>
<p> Start the Salt Master as follows: </p>
<pre>
service salt_master start
</pre>
<p> <code>Minion</code> </p>
<p> Copy the sample configuration file: </p>
<pre>
cp /usr/local/etc/salt/minion.sample /usr/local/etc/salt/minion
</pre>
<p> <code>rc.conf</code> </p>
<p> Activate the Salt Minion in <code>/etc/rc.conf</code> or <code>/etc/rc.conf.local</code> and add: </p>
<pre>
+ salt_minion_enable=&quot;YES&quot;
+ salt_minion_paths=&quot;/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin&quot;
</pre>
<p> <code>Start the Minion</code> </p>
<p> Start the Salt Minion as follows: </p>
<pre>
service salt_minion start
</pre>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>Gentoo</h3>
<p> Salt can be easily installed on Gentoo via Portage: </p>
<pre>
emerge app-admin/salt
</pre>
<h3>Post-installation tasks</h3>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>OpenBSD</h3>
<p> Salt was added to the OpenBSD ports tree on Aug 10th 2013. It has been tested on OpenBSD 5.5 onwards. </p>
<p> Salt is dependent on the following additional ports. These will be installed as dependencies of the <code>sysutils/salt</code> port: </p>
<pre>
devel/py-futures
devel/py-progressbar
net/py-msgpack
net/py-zmq
security/py-crypto
security/py-M2Crypto
textproc/py-MarkupSafe
textproc/py-yaml
www/py-jinja2
www/py-requests
www/py-tornado
</pre>
<h3>Installation</h3>
<p> To install Salt from the OpenBSD pkg repo, use the command: </p>
<pre>
pkg_add salt
</pre>
<h3>Post-installation tasks</h3>
<p> <code>Master</code> </p>
<p> To have the Master start automatically at boot time: </p>
<pre>
rcctl enable salt_master
</pre>
<p> To start the Master: </p>
<pre>
rcctl start salt_master
</pre>
<p> <code>Minion</code> </p>
<p> To have the Minion start automatically at boot time: </p>
<pre>
rcctl enable salt_minion
</pre>
<p> To start the Minion: </p>
<pre>
rcctl start salt_minion
</pre>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>OS X</h3>
<h3>Dependency Installation</h3>
<p> It should be noted that Homebrew explicitly discourages the <i>use of sudo</i>: Homebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause. Please donât file a bug report unless you can reproduce it after reinstalling Homebrew from scratch without using sudo </p>
<p> So when using Homebrew, if you want support from the Homebrew community, install this way: </p>
<pre>
brew install saltstack
</pre>
<p> When using MacPorts, install this way: </p>
<pre>
sudo port install salt
</pre>
<p> When only using the OS X system&#8217;s pip, install this way: </p>
<pre>
sudo pip install salt
</pre>
<h3>Salt-Master Customizations</h3>
<p> To run salt-master on OS X, the root user maxfiles limit must be increased: </p>
<pre>
sudo launchctl limit maxfiles 4096 8192
</pre>
<p> And sudo add this configuration option to the /etc/salt/master file: </p>
<pre>
max_open_files: 8192
</pre>
<p> Now the salt-master should run without errors: </p>
<pre>
sudo salt-master --log-level=all
</pre>
<h3>Post-installation tasks</h3>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>RHEL / CentOS / Scientific Linux / Amazon Linux / Oracle Linux</h3>
<h3>Installation from Repository</h3>
<h3>RHEL/CentOS 5</h3>
<p> Due to the removal of some of Salt&#8217;s dependencies from EPEL5, we have created a repository on <i>Fedora COPR</i>. Moving forward, this will be the official means of installing Salt on RHEL5-based systems. Information on how to enable this repository can be found <i>here</i>.</p>
<h3>RHEL/CentOS 6 and 7, Scientific Linux, etc.</h3>
<p> Beginning with version 0.9.4, Salt has been available in <i>EPEL</i>. It is installable using yum. Salt should work properly with all mainstream derivatives of RHEL, including CentOS, Scientific Linux, Oracle Linux and Amazon Linux. Report any bugs or issues on the <i>issue tracker</i>. </p>
<p> On RHEL6, the proper Jinja package &#8216;python-jinja2&#8217; was moved from EPEL to the &quot;RHEL Server Optional Channel&quot;. Verify this repository is enabled before installing salt on RHEL6.</p>
<h3>Enabling EPEL</h3>
<p> If the EPEL repository is not installed on your system, you can download the RPM from <i>here</i> for RHEL/CentOS 6 (or <i>here</i> for RHEL/CentOS 7) and install it using the following command: </p>
<pre>
rpm -Uvh epel-release-X-Y.rpm
</pre>
<p> Replace <code>epel-release-X-Y.rpm</code> with the appropriate filename.</p>
<h3>Installing Stable Release</h3>
<p> Salt is packaged separately for the minion and the master. It is necessary only to install the appropriate package for the role the machine will play. Typically, there will be one master and multiple minions. </p>
<p> On the salt-master, run this: </p>
<pre>
yum install salt-master
</pre>
<p> On each salt-minion, run this: </p>
<pre>
yum install salt-minion
</pre>
<h3>Installing from <code>epel-testing</code></h3>
<p> When a new Salt release is packaged, it is first admitted into the <code>epel-testing</code> repository, before being moved to the stable repo. </p>
<p> To install from <code>epel-testing</code>, use the <code>enablerepo</code> argument for yum: </p>
<pre>
yum --enablerepo=epel-testing install salt-minion
</pre>
<h3>Installation Using pip</h3>
<p> Since Salt is on <i>PyPI</i>, it can be installed using pip, though most users prefer to install using RPMs (which can be installed from <i>EPEL</i>). </p>
<p> Installing from pip has a few additional requirements:</p>
<dl>
<dt>&bull;</p>
<dd> Install the group &#8216;Development Tools&#8217;, <code>yum groupinstall &#8216;Development Tools&#8217;</code></p>
<dt>&bull;</p>
<dd> Install the &#8216;zeromq-devel&#8217; package if it fails on linking against that afterwards as well. </p>
<p> A pip install does not make the init scripts or the /etc/salt directory, and you will need to provide your own systemd service unit. </p>
<p> Installation from pip: </p>
<pre>
pip install salt
</pre>
<p> <code>WARNING:</code> If installing from pip (or from source using <code>setup.py install</code>), be advised that the <code>yum-utils</code> package is needed for Salt to manage packages. Also, if the Python dependencies are not already installed, then you will need additional libraries/tools installed to build some of them. More information on this can be found here.</dl>
<h3>ZeroMQ 4</h3>
<p> We recommend using ZeroMQ 4 where available. SaltStack provides ZeroMQ 4.0.4 and pyzmq 14.3.1 in a <i>COPR</i> repository. Instructions for adding this repository (as well as for upgrading ZeroMQ and pyzmq on existing minions) can be found <i>here</i>. </p>
<p> If this repo is added <i>before</i> Salt is installed, then installing either <code>salt-master</code> or <code>salt-minion</code> will automatically pull in ZeroMQ 4.0.4, and additional states to upgrade ZeroMQ and pyzmq are unnecessary. </p>
<p> <code>WARNING:</code> RHEL/CentOS 5 Users Using COPR repos on RHEL/CentOS 5 requires that the <code>python-hashlib</code> package be installed. Not having it present will result in checksum errors because YUM will not be able to process the SHA256 checksums used by COPR. </p>
<p> <code>NOTE:</code> For RHEL/CentOS 5 installations, if using the new repository to install Salt (as detailed <i>above</i>), then it is not necessary to enable the zeromq4 COPR, as the new EL5 repository includes ZeroMQ 4.</p>
<h3>Package Management</h3>
<p> Salt&#8217;s interface to <code>yum</code> makes heavy use of the <code>repoquery</code> utility, from the <i>yum-utils</i> package. This package will be installed as a dependency if salt is installed via EPEL. However, if salt has been installed using pip, or a host is being managed using salt-ssh, then as of version 2014.7.0 <i>yum-utils</i> will be installed automatically to satisfy this dependency.</p>
<h3>Post-installation tasks</h3>
<p> <code>Master</code> </p>
<p> To have the Master start automatically at boot time: </p>
<pre>
chkconfig salt-master on
</pre>
<p> To start the Master: </p>
<pre>
service salt-master start
</pre>
<p> <code>Minion</code> </p>
<p> To have the Minion start automatically at boot time: </p>
<pre>
chkconfig salt-minion on
</pre>
<p> To start the Minion: </p>
<pre>
service salt-minion start
</pre>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>Solaris</h3>
<p> Salt was added to the OpenCSW package repository in September of 2012 by Romeo Theriault &lt;<i>romeot [at] hawaii.edu</i>&gt; at version 0.10.2 of Salt. It has mainly been tested on Solaris 10 (sparc), though it is built for and has been tested minimally on Solaris 10 (x86), Solaris 9 (sparc/x86) and 11 (sparc/x86). (Please let me know if you&#8217;re using it on these platforms!) Most of the testing has also just focused on the minion, though it has verified that the master starts up successfully on Solaris 10. </p>
<p> Comments and patches for better support on these platforms is very welcome. </p>
<p> As of version 0.10.4, Solaris is well supported under salt, with all of the following working well:</p>
<dl>
<dt>1.</p>
<dd> remote execution</p>
<dt>2.</p>
<dd> grain detection</p>
<dt>3.</p>
<dd> service control with SMF</p>
<dt>4.</p>
<dd> &#8216;pkg&#8217; states with &#8216;pkgadd&#8217; and &#8216;pkgutil&#8217; modules</p>
<dt>5.</p>
<dd> cron modules/states</p>
<dt>6.</p>
<dd> user and group modules/states</p>
<dt>7.</p>
<dd> shadow password management modules/states </p>
<p> Salt is dependent on the following additional packages. These will automatically be installed as dependencies of the <code>py_salt</code> package:</p>
<dt>&bull;</p>
<dd> py_yaml</p>
<dt>&bull;</p>
<dd> py_pyzmq</p>
<dt>&bull;</p>
<dd> py_jinja2</p>
<dt>&bull;</p>
<dd> py_msgpack_python</p>
<dt>&bull;</p>
<dd> py_m2crypto</p>
<dt>&bull;</p>
<dd> py_crypto</p>
<dt>&bull;</p>
<dd> python</dl>
<h3>Installation</h3>
<p> To install Salt from the OpenCSW package repository you first need to install <i>pkgutil</i> assuming you don&#8217;t already have it installed: </p>
<p> On Solaris 10: </p>
<pre>
pkgadd -d <a rel="nofollow noopener" href="http://get.opencsw.org/now" target="_blank">http://get.opencsw.org/now</a>
</pre>
<p> On Solaris 9: </p>
<pre>
wget <a rel="nofollow noopener" href="http://mirror.opencsw.org/opencsw/pkgutil.pkg" target="_blank">http://mirror.opencsw.org/opencsw/pkgutil.pkg</a>
pkgadd -d pkgutil.pkg all
</pre>
<p> Once pkgutil is installed you&#8217;ll need to edit it&#8217;s config file <code>/etc/opt/csw/pkgutil.conf</code> to point it at the unstable catalog: </p>
<pre>
- #mirror=<a rel="nofollow noopener" href="http://mirror.opencsw.org/opencsw/testing" target="_blank">http://mirror.opencsw.org/opencsw/testing</a>
+ mirror=<a rel="nofollow noopener" href="http://mirror.opencsw.org/opencsw/unstable" target="_blank">http://mirror.opencsw.org/opencsw/unstable</a>
</pre>
<p> OK, time to install salt. </p>
<pre>
# Update the catalog
root&gt; /opt/csw/bin/pkgutil -U
# Install salt
root&gt; /opt/csw/bin/pkgutil -i -y py_salt
</pre>
<h3>Minion Configuration</h3>
<p> Now that salt is installed you can find it&#8217;s configuration files in <code>/etc/opt/csw/salt/</code>. </p>
<p> You&#8217;ll want to edit the minion config file to set the name of your salt master server: </p>
<pre>
- #master: salt
+ master: your-salt-server
</pre>
<p> If you would like to use <i>pkgutil</i> as the default package provider for your Solaris minions, you can do so using the <code>providers</code> option in the minion config file. </p>
<p> You can now start the salt minion like so: </p>
<p> On Solaris 10: </p>
<pre>
svcadm enable salt-minion
</pre>
<p> On Solaris 9: </p>
<pre>
/etc/init.d/salt-minion start
</pre>
<p> You should now be able to log onto the salt master and check to see if the salt-minion key is awaiting acceptance: </p>
<pre>
salt-key -l un
</pre>
<p> Accept the key: </p>
<pre>
salt-key -a &lt;your-salt-minion&gt;
</pre>
<p> Run a simple test against the minion: </p>
<pre>
salt '&lt;your-salt-minion&gt;' test.ping
</pre>
<h3>Troubleshooting</h3>
<p> Logs are in <code>/var/log/salt</code></p>
<h3>Ubuntu Installation</h3>
<h3>Add repository</h3>
<p> The latest packages for Ubuntu are published in the saltstack PPA. If you have the <code>add-apt-repository</code> utility, you can add the repository and import the key in one step: </p>
<pre>
sudo add-apt-repository ppa:saltstack/salt
</pre>
<dl>
<dt>add-apt-repository: command not found?</p>
<dd>
<p> The <code>add-apt-repository</code> command is not always present on Ubuntu systems. This can be fixed by installing <i>python-software-properties</i>: </p>
<pre>
sudo apt-get install python-software-properties
</pre>
<p> The following may be required as well: </p>
<pre>
sudo apt-get install software-properties-common
</pre>
<p> Note that since Ubuntu 12.10 (Raring Ringtail), <code>add-apt-repository</code> is found in the <i>software-properties-common</i> package, and is part of the base install. Thus, <code>add-apt-repository</code> should be able to be used out-of-the-box to add the PPA. </p>
<p> Alternately, manually add the repository and import the PPA key with these commands: </p>
<pre>
echo deb <a rel="nofollow noopener" href="http://ppa.launchpad.net/saltstack/salt/ubuntu" target="_blank">http://ppa.launchpad.net/saltstack/salt/ubuntu</a> `lsb_release -sc` main | sudo tee /etc/apt/sources.list.d/saltstack.list
wget -q -O- &quot;<a rel="nofollow noopener" href="http://keyserver.ubuntu.com:11371/pks/lookup?op=get" target="_blank">http://keyserver.ubuntu.com:11371/pks/lookup?op=get</a>&amp;search=0x4759FA960E27C0A6&quot; | sudo apt-key add -
</pre>
<p> After adding the repository, update the package management database: </p>
<pre>
sudo apt-get update
</pre>
</dl>
<h3>Install packages</h3>
<p> Install the Salt master, minion, or syndic from the repository with the apt-get command. These examples each install one daemon, but more than one package name may be given at a time: </p>
<pre>
sudo apt-get install salt-master
</pre>
<pre>
sudo apt-get install salt-minion
</pre>
<pre>
sudo apt-get install salt-syndic
</pre>
<h3>ZeroMQ 4</h3>
<p> ZeroMQ 4 is available by default for Ubuntu 14.04 and newer. However, for Ubuntu 12.04 LTS, starting with Salt version <code>2014.7.5</code>, ZeroMQ 4 is included with the Salt installation package and nothing additional needs to be done.</p>
<h3>Post-installation tasks</h3>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>Windows</h3>
<p> Salt has full support for running the Salt Minion on Windows. </p>
<p> There are no plans for the foreseeable future to develop a Salt Master on Windows. For now you must run your Salt Master on a supported operating system to control your Salt Minions on Windows. </p>
<p> Many of the standard Salt modules have been ported to work on Windows and many of the Salt States currently work on Windows, as well.</p>
<h3>Windows Installer</h3>
<p> Salt Minion Windows installers can be found here. The output of <i>md5sum &lt;salt minion exe&gt;</i> should match the contents of the corresponding md5 file. </p>
<p> <code>Latest stable build from the selected branch</code>: </p>
<p> <i>Earlier builds from supported branches</i> </p>
<p> <i>Archived builds from unsupported branches</i> </p>
<p> <code>NOTE:</code> The installation executable installs dependencies that the Salt minion requires. </p>
<p> The 64bit installer has been tested on Windows 7 64bit and Windows Server 2008R2 64bit. The 32bit installer has been tested on Windows 2003 Server 32bit. Please file a bug report on our GitHub repo if issues for other platforms are found. </p>
<p> The installer asks for 2 bits of information; the master hostname and the minion name. The installer will update the minion config with these options and then start the minion. </p>
<p> The <i>salt-minion</i> service will appear in the Windows Service Manager and can be started and stopped there or with the command line program <i>sc</i> like any other Windows service. </p>
<p> If the minion won&#8217;t start, try installing the Microsoft Visual C++ 2008 x64 SP1 redistributable. Allow all Windows updates to run salt-minion smoothly.</p>
<h3>Silent Installer options</h3>
<p> The installer can be run silently by providing the <i>/S</i> option at the command line. The installer also accepts the following options for configuring the Salt Minion silently:</p>
<dl>
<dt>&bull;</p>
<dd> <i>/master=</i> A string value to set the IP address or host name of the master. Default value is &#8216;salt&#8217;</p>
<dt>&bull;</p>
<dd> <i>/minion-name=</i> A string value to set the minion name. Default is &#8216;hostname&#8217;</p>
<dt>&bull;</p>
<dd> <i>/start-service=</i> Either a 1 or 0. &#8216;1&#8217; will start the service, &#8216;0&#8217; will not. Default is to start the service after installation. </p>
<p> Here&#8217;s an example of using the silent installer: </p>
<pre>
Salt-Minion-2015.5.6-Setup-amd64.exe /S /master=yoursaltmaster /minion-name=yourminionname /start-service=0
</pre>
</dl>
<h3>Running the Salt Minion on Windows as an Unprivileged User</h3>
<p> Notes: &#8211; These instructions were tested with Windows Server 2008 R2 &#8211; They are generalizable to any version of Windows that supports a salt-minion</p>
<h3>A. Create the Unprivileged User that the Salt Minion will Run As</h3>
<dl>
<dt>1.</p>
<dd> Click &quot;Start&quot;, &quot;Control Panel&quot;, &quot;User Accounts&quot;</p>
<dt>2.</p>
<dd> Click &quot;Add or remove user accounts&quot;</p>
<dt>3.</p>
<dd> Click &quot;Create new account&quot;</p>
<dt>4.</p>
<dd> Enter &quot;salt-user&quot; (or a name of your preference) in the &quot;New account name&quot; field</p>
<dt>5.</p>
<dd> Select the &quot;Standard user&quot; radio button</p>
<dt>6.</p>
<dd> Click the &quot;Create Account&quot; button</p>
<dt>7.</p>
<dd> Click on the newly created user account</p>
<dt>8.</p>
<dd> Click the &quot;Create a password&quot; link</p>
<dt>9.</p>
<dd> In the &quot;New password&quot; and &quot;Confirm new password&quot; fields, provide a password (e.g &quot;SuperSecretMinionPassword4Me!&quot;)</p>
<dt>10.</p>
<dd> In the &quot;Type a password hint&quot; field, provide appropriate text (e.g. &quot;My Salt Password&quot;)</p>
<dt>11.</p>
<dd> Click the &quot;Create password&quot; button</p>
<dt>12.</p>
<dd> Close the &quot;Change an Account&quot; window</dl>
<h3>B. Add the New User to the Access Control List for the Salt Folder</h3>
<dl>
<dt>1.</p>
<dd> In a File Explorer window, browse to the path where Salt is installed (the default path is C:Salt)</p>
<dt>2.</p>
<dd> Right-click on the &quot;Salt&quot; folder and select &quot;Properties&quot;</p>
<dt>3.</p>
<dd> Click on the &quot;Security&quot; tab</p>
<dt>4.</p>
<dd> Click the &quot;Edit&quot; button</p>
<dt>5.</p>
<dd> Click the &quot;Add&quot; button</p>
<dt>6.</p>
<dd> Type the name of your designated Salt user and click the &quot;OK&quot; button</p>
<dt>7.</p>
<dd> Check the box to &quot;Allow&quot; the &quot;Modify&quot; permission</p>
<dt>8.</p>
<dd> Click the &quot;OK&quot; button</p>
<dt>9.</p>
<dd> Click the &quot;OK&quot; button to close the &quot;Salt Properties&quot; window</dl>
<h3>C. Update the Windows Service User for the salt-minion Service</h3>
<dl>
<dt>1.</p>
<dd> Click &quot;Start&quot;, &quot;Administrative Tools&quot;, &quot;Services&quot;</p>
<dt>2.</p>
<dd> In the list of Services, Right-Click on &quot;salt-minion&quot; and select &quot;Properties&quot;</p>
<dt>3.</p>
<dd> Click the &quot;Log On&quot; tab</p>
<dt>4.</p>
<dd> Click the &quot;This account&quot; radio button</p>
<dt>5.</p>
<dd> Provide the account credentials created in section A</p>
<dt>6.</p>
<dd> Click the &quot;OK&quot; button</p>
<dt>7.</p>
<dd> Click the &quot;OK&quot; button to the prompt confirming that the user &quot;has been granted the Log On As A Service right&quot;</p>
<dt>8.</p>
<dd> Click the &quot;OK&quot; button to the prompt confirming that &quot;The new logon name will not take effect until you stop and restart the service&quot;</p>
<dt>9.</p>
<dd> Right-Click on &quot;salt-minion&quot; and select &quot;Stop&quot;</p>
<dt>10.</p>
<dd> Right-Click on &quot;salt-minion&quot; and select &quot;Start&quot;</dl>
<h3>Setting up a Windows build environment</h3>
<p> This document will explain how to set up a development environment for salt on Windows. The development environment allows you to work with the source code to customize or fix bugs. It will also allow you to build your own installation.</p>
<h3>The Easy Way</h3>
<h3>Prerequisite Software</h3>
<p> To do this the easy way you only need to install <i>Git for Windows</i>.</p>
<h3>Create the Build Environment</h3>
<dl>
<dt>1.</p>
<dd> Clone the <i>Salt-Windows-Dev</i> repo from github. </p>
<p> Open a command line and type: </p>
<pre>
git clone <a rel="nofollow noopener" href="https://github.com/saltstack/salt-windows-dev" target="_blank">https://github.com/saltstack/salt-windows-dev</a>
</pre>
<dt>2.</p>
<dd> Build the Python Environment </p>
<p> Go into the salt-windows-dev directory. Right-click the file named <code>dev_env.ps1</code> and select <code>Run with PowerShell</code> </p>
<p> If you get an error, you may need to change the execution policy. </p>
<p> Open a powershell window and type the following: </p>
<pre>
Set-ExecutionPolicy RemoteSigned
</pre>
<p> This will download and install Python with all the dependencies needed to develop and build salt.</p>
<dt>3.</p>
<dd> Build the Salt Environment </p>
<p> Right-click on the file named <code>dev_env_salt.ps1</code> and select <code>Run with Powershell</code> </p>
<p> This will clone salt into <code>C:\Salt-Dev\salt</code> and set it to the 2015.5 branch. You could optionally run the command from a powershell window with a <code>-Version</code> switch to pull a different version. For example: </p>
<pre>
dev_env_salt.ps1 -Version '2014.7'
</pre>
<p> To view a list of available branches and tags, open a command prompt in your <i>C:Salt-Devsalt</i> directory and type: </p>
<pre>
git branch -a
git tag -n
</pre>
</dl>
<h3>The Hard Way</h3>
<h3>Prerequisite Software</h3>
<p> Install the following software:</p>
<dl>
<dt>1.</p>
<dd> <i>Git for Windows</i></p>
<dt>2.</p>
<dd> <i>Nullsoft Installer</i> </p>
<p> Download the Prerequisite zip file for your CPU architecture from the SaltStack download site:</p>
<dt>&bull;</p>
<dd> <i>Salt32.zip</i></p>
<dt>&bull;</p>
<dd> <i>Salt64.zip</i> </p>
<p> These files contain all sofware required to build and develop salt. Unzip the contents of the file to <code>C:\Salt-Dev\temp</code>.</dl>
<h3>Create the Build Environment</h3>
<dl>
<dt>1.</p>
<dd> Build the Python Environment</p>
<dt>&bull;</p>
<dd> Install Python: </p>
<p> Browse to the <code>C:\Salt-Dev\temp</code> directory and find the Python installation file for your CPU Architecture under the corresponding subfolder. Double-click the file to install python. </p>
<p> Make sure the following are in your <code>PATH</code> environment variable: </p>
<pre>
C:\Python27
C:\Python27\Scripts
</pre>
<dt>&bull;</p>
<dd> Install Pip </p>
<p> Open a command prompt and navigate to <code>C:\Salt-Dev\temp</code> Run the following command: </p>
<pre>
python get-pip.py
</pre>
<dt>&bull;</p>
<dd> Easy Install compiled binaries. </p>
<p> M2Crypto, PyCrypto, and PyWin32 need to be installed using Easy Install. Open a command prompt and navigate to <code>C:\Salt-Dev\temp\&lt;cpuarch&gt;</code>. Run the following commands: </p>
<pre>
easy_install -Z &lt;M2Crypto file name&gt;
easy_install -Z &lt;PyCrypto file name&gt;
easy_install -Z &lt;PyWin32 file name&gt;
</pre>
<p> <code>NOTE:</code> You can type the first part of the file name and then press the tab key to auto-complete the name of the file.</p>
<dt>&bull;</p>
<dd> Pip Install Additional Prerequisites </p>
<p> All remaining prerequisites need to be pip installed. These prerequisites are as follow:</p>
<dt>&bull;</p>
<dd> MarkupSafe</p>
<dt>&bull;</p>
<dd> Jinja</p>
<dt>&bull;</p>
<dd> MsgPack</p>
<dt>&bull;</p>
<dd> PSUtil</p>
<dt>&bull;</p>
<dd> PyYAML</p>
<dt>&bull;</p>
<dd> PyZMQ</p>
<dt>&bull;</p>
<dd> WMI</p>
<dt>&bull;</p>
<dd> Requests</p>
<dt>&bull;</p>
<dd> Certifi </p>
<p> Open a command prompt and navigate to <code>C:\Salt-Dev\temp</code>. Run the following commands: </p>
<pre>
pip install &lt;cpuarch&gt;\&lt;MarkupSafe file name&gt;
pip install &lt;Jinja file name&gt;
pip install &lt;cpuarch&gt;\&lt;MsgPack file name&gt;
pip install &lt;cpuarch&gt;\&lt;psutil file name&gt;
pip install &lt;cpuarch&gt;\&lt;PyYAML file name&gt;
pip install &lt;cpuarch&gt;\&lt;pyzmq file name&gt;
pip install &lt;WMI file name&gt;
pip install &lt;requests file name&gt;
pip install &lt;certifi file name&gt;
</pre>
<dt>2.</p>
<dd> Build the Salt Environment</p>
<dt>&bull;</p>
<dd> Clone Salt </p>
<p> Open a command prompt and navigate to <code>C:\Salt-Dev</code>. Run the following command to clone salt: </p>
<pre>
git clone <a rel="nofollow noopener" href="https://github.com/saltstack/salt" target="_blank">https://github.com/saltstack/salt</a>
</pre>
<dt>&bull;</p>
<dd> Checkout Branch </p>
<p> Checkout the branch or tag of salt you want to work on or build. Open a command prompt and navigate to <code>C:\Salt-Dev\salt</code>. Get a list of available tags and branches by running the following commands: </p>
<pre>
git fetch --all
To view a list of available branches:
git branch -a
To view a list of availabel tags:
git tag -n
</pre>
<p> Checkout the branch or tag by typing the following command: </p>
<pre>
git checkout &lt;branch/tag name&gt;
</pre>
<dt>&bull;</p>
<dd> Clean the Environment </p>
<p> When switching between branches residual files can be left behind that will interfere with the functionality of salt. Therefore, after you check out the branch you want to work on, type the following commands to clean the salt environment:</dl>
<h3>Developing with Salt</h3>
<p> There are two ways to develop with salt. You can run salt&#8217;s setup.py each time you make a change to source code or you can use the setup tools develop mode.</p>
<h3>Configure the Minion</h3>
<p> Both methods require that the minion configuration be in the <code>C:\salt</code> directory. Copy the conf and var directories from <code>C:\Salt-Dev\salt\pkg\ windows\buildenv</code> to <code>C:\salt</code>. Now go into the <code>C:\salt\conf</code> directory and edit the file name <code>minion</code> (no extension). You need to configure the master and id parameters in this file. Edit the following lines: </p>
<pre>
master: &lt;ip or name of your master&gt;
id: &lt;name of your minion&gt;
</pre>
<h3>Setup.py Method</h3>
<p> Go into the <code>C:\Salt-Dev\salt</code> directory from a cmd prompt and type: </p>
<pre>
python setup.py install --force
</pre>
<p> This will install python into your python installation at <code>C:\Python27</code>. Everytime you make an edit to your source code, you&#8217;ll have to stop the minion, run the setup, and start the minion. </p>
<p> To start the salt-minion go into <code>C:\Python27\Scripts</code> from a cmd prompt and type: </p>
<pre>
salt-minion
</pre>
<p> For debug mode type: </p>
<pre>
salt-minion -l debug
</pre>
<p> To stop the minion press Ctrl+C.</p>
<h3>Setup Tools Develop Mode (Preferred Method)</h3>
<p> To use the Setup Tools Develop Mode go into <code>C:\Salt-Dev\salt</code> from a cmd prompt and type: </p>
<pre>
pip install -e .
</pre>
<p> This will install pointers to your source code that resides at <code>C:\Salt-Dev\salt</code>. When you edit your source code you only have to restart the minion.</p>
<h3>Build the windows installer</h3>
<p> This is the method of building the installer as of version 2014.7.4.</p>
<h3>Clean the Environment</h3>
<p> Make sure you don&#8217;t have any leftover salt files from previous versions of salt in your Python directory.</p>
<dl>
<dt>1.</p>
<dd> Remove all files that start with salt in the <code>C:\Python27\Scripts</code> directory</p>
<dt>2.</p>
<dd> Remove all files and directorys that start with salt in the <code>C:\Python27\Lib\site-packages</code> directory</dl>
<h3>Install Salt</h3>
<p> Install salt using salt&#8217;s setup.py. From the <code>C:\Salt-Dev\salt</code> directory type the following command: </p>
<pre>
python setup.py install --force
</pre>
<h3>Build the Installer</h3>
<p> From cmd prompt go into the <code>C:\Salt-Dev\salt\pkg\windows</code> directory. Type the following command for the branch or tag of salt you&#8217;re building: </p>
<pre>
BuildSalt.bat &lt;branch or tag&gt;
</pre>
<p> This will copy python with salt installed to the <code>buildenv\bin</code> directory, make it portable, and then create the windows installer . The .exe for the windows installer will be placed in the <code>installer</code> directory.</p>
<h3>Testing the Salt minion</h3>
<dl>
<dt>1.</p>
<dd> Create the directory C:\salt (if it doesn&#8217;t exist already)</p>
<dt>2.</p>
<dd> Copy the example <code>conf</code> and <code>var</code> directories from <code>pkg/windows/buildenv/</code> into C:\salt</p>
<dt>3.</p>
<dd> Edit C:\salt\conf\minion </p>
<pre>
master: ipaddress or hostname of your salt-master
</pre>
<dt>4.</p>
<dd> Start the salt-minion </p>
<pre>
cd C:\Python27\Scripts
python salt-minion
</pre>
<dt>5.</p>
<dd> On the salt-master accept the new minion&#8217;s key </p>
<pre>
sudo salt-key -A
</pre>
<p> This accepts all unaccepted keys. If you&#8217;re concerned about security just accept the key for this specific minion.</p>
<dt>6.</p>
<dd> Test that your minion is responding </p>
<p> On the salt-master run: </p>
<pre>
sudo salt '*' test.ping
</pre>
<p> You should get the following response: <code>{&#8216;your minion hostname&#8217;: True}</code></dl>
<h3>Single command bootstrap script</h3>
<p> On a 64 bit Windows host the following script makes an unattended install of salt, including all dependencies:</p>
<dl>
<dt>Not up to date.</p>
<dd>
<p> This script is not up to date. Please use the installer found above </p>
<pre>
# (All in one line.)
&quot;PowerShell (New-Object System.Net.WebClient).DownloadFile('<a rel="nofollow noopener" href="http://csa-net.dk/salt/bootstrap64.bat&#039;,&#039;C:\bootstrap.bat&#039;);(New-Object" target="_blank">http://csa-net.dk/salt/bootstrap64.bat','C:\bootstrap.bat');(New-Object</a> -com Shell.Application).ShellExecute('C:\bootstrap.bat');&quot;
</pre>
<p> You can execute the above command remotely from a Linux host using winexe: </p>
<pre>
winexe -U &quot;administrator&quot; //fqdn &quot;PowerShell (New-Object ......);&quot;
</pre>
<p> For more info check <i><a rel="nofollow noopener" href="http://csa-net.dk/salt" target="_blank">http://csa-net.dk/salt</a></i></dl>
<h3>Packages management under Windows 2003</h3>
<p> On windows Server 2003, you need to install optional component &quot;wmi windows installer provider&quot; to have full list of installed packages. If you don&#8217;t have this, salt-minion can&#8217;t report some installed softwares.</p>
<h3>SUSE Installation</h3>
<p> With openSUSE 13.2, Salt 2014.1.11 is available in the primary repositories. The devel:language:python repo will have more up to date versions of salt, all package development will be done there.</p>
<h3>Installation</h3>
<p> Salt can be installed using <code>zypper</code> and is available in the standard openSUSE repositories.</p>
<h3>Stable Release</h3>
<p> Salt is packaged separately for the minion and the master. It is necessary only to install the appropriate package for the role the machine will play. Typically, there will be one master and multiple minions. </p>
<pre>
zypper install salt-master
zypper install salt-minion
</pre>
<h3>Post-installation tasks openSUSE</h3>
<p> <code>Master</code> </p>
<p> To have the Master start automatically at boot time: </p>
<pre>
systemctl enable salt-master.service
</pre>
<p> To start the Master: </p>
<pre>
systemctl start salt-master.service
</pre>
<p> <code>Minion</code> </p>
<p> To have the Minion start automatically at boot time: </p>
<pre>
systemctl enable salt-minion.service
</pre>
<p> To start the Minion: </p>
<pre>
systemctl start salt-minion.service
</pre>
<h3>Post-installation tasks SLES</h3>
<p> <code>Master</code> </p>
<p> To have the Master start automatically at boot time: </p>
<pre>
chkconfig salt-master on
</pre>
<p> To start the Master: </p>
<pre>
rcsalt-master start
</pre>
<p> <code>Minion</code> </p>
<p> To have the Minion start automatically at boot time: </p>
<pre>
chkconfig salt-minion on
</pre>
<p> To start the Minion: </p>
<pre>
rcsalt-minion start
</pre>
<h3>Unstable Release</h3>
<h3>openSUSE</h3>
<p> For openSUSE Factory run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/openSUSE_Factory/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/openSUSE_Factory/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<p> For openSUSE 13.2 run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/openSUSE_13.2/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/openSUSE_13.2/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<p> For openSUSE 13.1 run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/openSUSE_13.1/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/openSUSE_13.1/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<p> For bleeding edge python Factory run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/bleeding_edge_python_Factory/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/bleeding_edge_python_Factory/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<h3>Suse Linux Enterprise</h3>
<p> For SLE 12 run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/SLE_12/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/SLE_12/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<p> For SLE 11 SP3 run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/SLE_11_SP3/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/SLE_11_SP3/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<p> For SLE 11 SP2 run the following as root: </p>
<pre>
zypper addrepo <a rel="nofollow noopener" href="http://download.opensuse.org/repositories/devel:languages:python/SLE_11_SP2/devel:languages:python.repo" target="_blank">http://download.opensuse.org/repositories/devel:languages:python/SLE_11_SP2/devel:languages:python.repo</a>
zypper refresh
zypper install salt salt-minion salt-master
</pre>
<p> Now go to the <code>Configuring Salt</code> page.</p>
<h3>Dependencies</h3>
<p> Salt should run on any Unix-like platform so long as the dependencies are met.</p>
<dl>
<dt>&bull;</p>
<dd> <i>Python 2.6</i> &gt;= 2.6 &lt;3.0</p>
<dt>&bull;</p>
<dd> <i>msgpack-python</i> &#8211; High-performance message interchange format</p>
<dt>&bull;</p>
<dd> <i>YAML</i> &#8211; Python YAML bindings</p>
<dt>&bull;</p>
<dd> <i>Jinja2</i> &#8211; parsing Salt States (configurable in the master settings)</p>
<dt>&bull;</p>
<dd> <i>MarkupSafe</i> &#8211; Implements a XML/HTML/XHTML Markup safe string for Python</p>
<dt>&bull;</p>
<dd> <i>apache-libcloud</i> &#8211; Python lib for interacting with many of the popular cloud service providers using a unified API</p>
<dt>&bull;</p>
<dd> <i>Requests</i> &#8211; HTTP library </p>
<p> Depending on the chosen Salt transport, <i>ZeroMQ</i> or <i>RAET</i>, dependencies vary:</p>
<dt>&bull;</p>
<dd> ZeroMQ:</p>
<dt>&bull;</p>
<dd> <i>ZeroMQ</i> &gt;= 3.2.0</p>
<dt>&bull;</p>
<dd> <i>pyzmq</i> &gt;= 2.2.0 &#8211; ZeroMQ Python bindings</p>
<dt>&bull;</p>
<dd> <i>PyCrypto</i> &#8211; The Python cryptography toolkit</p>
<dt>&bull;</p>
<dd> <i>M2Crypto</i> &#8211; &quot;Me Too Crypto&quot; &#8211; Python OpenSSL wrapper</p>
<dt>&bull;</p>
<dd> RAET:</p>
<dt>&bull;</p>
<dd> <i>libnacl</i> &#8211; Python bindings to <i>libsodium</i></p>
<dt>&bull;</p>
<dd> <i>ioflo</i> &#8211; The flo programming interface raet and salt-raet is built on</p>
<dt>&bull;</p>
<dd> <i>RAET</i> &#8211; The worlds most awesome UDP protocol </p>
<p> Salt defaults to the <i>ZeroMQ</i> transport, and the choice can be made at install time, for example: </p>
<pre>
python setup.py install --salt-transport=raet
</pre>
<p> This way, only the required dependencies are pulled by the setup script if need be. </p>
<p> If installing using pip, the <code>&#8211;salt-transport</code> install option can be provided like: </p>
<pre>
pip install --install-option=&quot;--salt-transport=raet&quot; salt
</pre>
</dl>
<h3>Optional Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> <i>mako</i> &#8211; an optional parser for Salt States (configurable in the master settings)</p>
<dt>&bull;</p>
<dd> gcc &#8211; dynamic <i>Cython</i> module compiling</dl>
<h3>Upgrading Salt</h3>
<p> When upgrading Salt, the master(s) should always be upgraded first. Backward compatibility for minions running newer versions of salt than their masters is not guaranteed. </p>
<p> Whenever possible, backward compatibility between new masters and old minions will be preserved. Generally, the only exception to this policy is in case of a security vulnerability.</p>
<h2 id="TUTORIALS"></h2>
<h3>Introduction</h3>
<h3>Salt Masterless Quickstart</h3>
<p> Running a masterless salt-minion lets you use Salt&#8217;s configuration management for a single machine without calling out to a Salt master on another machine. </p>
<p> Since the Salt minion contains such extensive functionality it can be useful to run it standalone. A standalone minion can be used to do a number of things:</p>
<dl>
<dt>&bull;</p>
<dd> Stand up a master server via States (Salting a Salt Master)</p>
<dt>&bull;</p>
<dd> Use salt-call commands on a system without connectivity to a master</p>
<dt>&bull;</p>
<dd> Masterless States, run states entirely from files local to the minion </p>
<p> It is also useful for testing out state trees before deploying to a production setup.</dl>
<h3>Bootstrap Salt Minion</h3>
<p> The <i>salt-bootstrap</i> script makes bootstrapping a server with Salt simple for any OS with a Bourne shell: </p>
<pre>
wget -O - <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh
</pre>
<p> See the <i>salt-bootstrap</i> documentation for other one liners. When using <i>Vagrant</i> to test out salt, the <i>Vagrant salt provisioner</i> will provision the VM for you.</p>
<h3>Telling Salt to Run Masterless</h3>
<p> To instruct the minion to not look for a master, the <code>file_client</code> configuration option needs to be set in the minion configuration file. By default the <code>file_client</code> is set to <code>remote</code> so that the minion gathers file server and pillar data from the salt master. When setting the <code>file_client</code> option to <code>local</code> the minion is configured to not gather this data from the master. </p>
<pre>
file_client: local
</pre>
<p> Now the salt minion will not look for a master and will assume that the local system has all of the file and pillar resources. </p>
<p> <code>NOTE:</code> When running Salt in masterless mode, do not run the salt-minion daemon. Otherwise, it will attempt to connect to a master and fail. The salt-call command stands on its own and does not need the salt-minion daemon.</p>
<h3>Create State Tree</h3>
<p> Following the successful installation of a salt-minion, the next step is to create a state tree, which is where the SLS files that comprise the possible states of the minion are stored. </p>
<p> The following example walks through the steps necessary to create a state tree that ensures that the server has the Apache webserver installed. </p>
<p> <code>NOTE:</code> For a complete explanation on Salt States, see the <i>tutorial</i>.</p>
<dl>
<dt>1.</p>
<dd> Create the <code>top.sls</code> file: </p>
<p> <code>/srv/salt/top.sls:</code> </p>
<pre>
base:
  '*':
    - webserver
</pre>
<dt>2.</p>
<dd> Create the webserver state tree: </p>
<p> <code>/srv/salt/webserver.sls:</code> </p>
<pre>
apache:               # ID declaration
  pkg:                # state declaration
    - installed       # function declaration
</pre>
<p> <code>NOTE:</code> The apache package has different names on different platforms, for instance on Debian/Ubuntu it is apache2, on Fedora/RHEL it is httpd and on Arch it is apache </p>
<p> The only thing left is to provision our minion using salt-call and the highstate command.</dl>
<h3>Salt-call</h3>
<p> The salt-call command is used to run module functions locally on a minion instead of executing them from the master. Normally the salt-call command checks into the master to retrieve file server and pillar data, but when running standalone salt-call needs to be instructed to not check the master for this data: </p>
<pre>
salt-call --local state.highstate
</pre>
<p> The <code>&#8211;local</code> flag tells the salt-minion to look for the state tree in the local file system and not to contact a Salt Master for instructions. </p>
<p> To provide verbose output, use <code>-l debug</code>: </p>
<pre>
salt-call --local state.highstate -l debug
</pre>
<p> The minion first examines the <code>top.sls</code> file and determines that it is a part of the group matched by <code>*</code> glob and that the <code>webserver</code> SLS should be applied. </p>
<p> It then examines the <code>webserver.sls</code> file and finds the <code>apache</code> state, which installs the Apache package. </p>
<p> The minion should now have Apache installed, and the next step is to begin learning how to write <code>more complex states</code>.</p>
<h3>Basics</h3>
<h3>Standalone Minion</h3>
<p> Since the Salt minion contains such extensive functionality it can be useful to run it standalone. A standalone minion can be used to do a number of things:</p>
<dl>
<dt>&bull;</p>
<dd> Use salt-call commands on a system without connectivity to a master</p>
<dt>&bull;</p>
<dd> Masterless States, run states entirely from files local to the minion </p>
<p> <code>NOTE:</code> When running Salt in masterless mode, do not run the salt-minion daemon. Otherwise, it will attempt to connect to a master and fail. The salt-call command stands on its own and does not need the salt-minion daemon.</dl>
<h3>Telling Salt Call to Run Masterless</h3>
<p> The salt-call command is used to run module functions locally on a minion instead of executing them from the master. Normally the salt-call command checks into the master to retrieve file server and pillar data, but when running standalone salt-call needs to be instructed to not check the master for this data. To instruct the minion to not look for a master when running salt-call the <code>file_client</code> configuration option needs to be set. By default the <code>file_client</code> is set to <code>remote</code> so that the minion knows that file server and pillar data are to be gathered from the master. When setting the <code>file_client</code> option to <code>local</code> the minion is configured to not gather this data from the master. </p>
<pre>
file_client: local
</pre>
<p> Now the salt-call command will not look for a master and will assume that the local system has all of the file and pillar resources.</p>
<h3>Running States Masterless</h3>
<p> The state system can be easily run without a Salt master, with all needed files local to the minion. To do this the minion configuration file needs to be set up to know how to return file_roots information like the master. The file_roots setting defaults to /srv/salt for the base environment just like on the master: </p>
<pre>
file_roots:
  base:
    - /srv/salt
</pre>
<p> Now set up the Salt State Tree, top file, and SLS modules in the same way that they would be set up on a master. Now, with the <code>file_client</code> option set to <code>local</code> and an available state tree then calls to functions in the state module will use the information in the file_roots on the minion instead of checking in with the master. </p>
<p> Remember that when creating a state tree on a minion there are no syntax or path changes needed, SLS modules written to be used from a master do not need to be modified in any way to work with a minion. </p>
<p> This makes it easy to &quot;script&quot; deployments with Salt states without having to set up a master, and allows for these SLS modules to be easily moved into a Salt master as the deployment grows. </p>
<p> The declared state can now be executed with: </p>
<pre>
salt-call state.highstate
</pre>
<p> Or the salt-call command can be executed with the <code>&#8211;local</code> flag, this makes it unnecessary to change the configuration file: </p>
<pre>
salt-call state.highstate --local
</pre>
<h3>External Pillars</h3>
<p> External pillars are supported when running in masterless mode.</p>
<h3>Opening the Firewall up for Salt</h3>
<p> The Salt master communicates with the minions using an AES-encrypted ZeroMQ connection. These communications are done over TCP ports <code>4505</code> and <code>4506</code>, which need to be accessible on the master only. This document outlines suggested firewall rules for allowing these incoming connections to the master. </p>
<p> <code>NOTE:</code> No firewall configuration needs to be done on Salt minions. These changes refer to the master only.</p>
<h3>Fedora 18 and beyond / RHEL 7 / CentOS 7</h3>
<p> Starting with Fedora 18 <i>FirewallD</i> is the tool that is used to dynamically manage the firewall rules on a host. It has support for IPv4/6 settings and the separation of runtime and permanent configurations. To interact with FirewallD use the command line client <code>firewall-cmd</code>. </p>
<p> <code>firewall-cmd example</code>: </p>
<pre>
firewall-cmd --permanent --zone=&lt;zone&gt; --add-port=4505-4506/tcp
</pre>
<p> Please choose the desired zone according to your setup. Don&#8217;t forget to reload after you made your changes. </p>
<pre>
firewall-cmd --reload
</pre>
<h3>RHEL 6 / CentOS 6</h3>
<p> The <code>lokkit</code> command packaged with some Linux distributions makes opening iptables firewall ports very simple via the command line. Just be careful to not lock out access to the server by neglecting to open the ssh port. </p>
<p> <code>lokkit example</code>: </p>
<pre>
lokkit -p 22:tcp -p 4505:tcp -p 4506:tcp
</pre>
<p> The <code>system-config-firewall-tui</code> command provides a text-based interface to modifying the firewall. </p>
<p> <code>system-config-firewall-tui</code>: </p>
<pre>
system-config-firewall-tui
</pre>
<h3>openSUSE</h3>
<p> Salt installs firewall rules in <i>/etc/sysconfig/SuSEfirewall2.d/services/salt</i>. Enable with: </p>
<pre>
SuSEfirewall2 open
SuSEfirewall2 start
</pre>
<p> If you have an older package of Salt where the above configuration file is not included, the <code>SuSEfirewall2</code> command makes opening iptables firewall ports very simple via the command line. </p>
<p> <code>SuSEfirewall example</code>: </p>
<pre>
SuSEfirewall2 open EXT TCP 4505
SuSEfirewall2 open EXT TCP 4506
</pre>
<p> The firewall module in YaST2 provides a text-based interface to modifying the firewall. </p>
<p> <code>YaST2</code>: </p>
<pre>
yast2 firewall
</pre>
<h3>iptables</h3>
<p> Different Linux distributions store their <i>iptables</i> (also known as <i>netfilter</i>) rules in different places, which makes it difficult to standardize firewall documentation. Included are some of the more common locations, but your mileage may vary. </p>
<p> <code>Fedora / RHEL / CentOS</code>: </p>
<pre>
/etc/sysconfig/iptables
</pre>
<p> <code>Arch Linux</code>: </p>
<pre>
/etc/iptables/iptables.rules
</pre>
<p> <code>Debian</code> </p>
<p> Follow these instructions: <i><a rel="nofollow noopener" href="https://wiki.debian.org/iptables" target="_blank">https://wiki.debian.org/iptables</a></i> </p>
<p> Once you&#8217;ve found your firewall rules, you&#8217;ll need to add the two lines below to allow traffic on <code>tcp/4505</code> and <code>tcp/4506</code>: </p>
<pre><code>
- A INPUT - m state-- state new - m tcp - p tcp-- dport 4505 - j ACCEPT - A INPUT - m state-- state new - m tcp - p tcp-- dport 4506 - j ACCEPT
</code></pre>
<p> <code>Ubuntu</code> </p>
<p> Salt installs firewall rules in <i>/etc/ufw/applications.d/salt.ufw</i>. Enable with: </p>
<pre>
ufw allow salt
</pre>
<h3>pf.conf</h3>
<p> The BSD-family of operating systems uses <i>packet filter (pf)</i>. The following example describes the additions to <code>pf.conf</code> needed to access the Salt master. </p>
<pre>
pass in on $int_if proto tcp from any to $int_if port 4505
pass in on $int_if proto tcp from any to $int_if port 4506
</pre>
<p> Once these additions have been made to the <code>pf.conf</code> the rules will need to be reloaded. This can be done using the <code>pfctl</code> command. </p>
<pre>
pfctl -vf /etc/pf.conf
</pre>
<h3>Whitelist communication to Master</h3>
<p> There are situations where you want to selectively allow Minion traffic from specific hosts or networks into your Salt Master. The first scenario which comes to mind is to prevent unwanted traffic to your Master out of security concerns, but another scenario is to handle Minion upgrades when there are backwards incompatible changes between the installed Salt versions in your environment. </p>
<p> Here is an example <i>Linux iptables</i> ruleset to be set on the Master: </p>
<p>#Allow Minions from these networks<br />
&#8211; I INPUT &#8211; s 10.1.2.0 / 24 &#8211; p tcp &#8211; m multiport&#8211; dports 4505, 4506 &#8211; j ACCEPT &#8211; I INPUT &#8211; s 10.1.3.0 / 24 &#8211; p tcp &#8211; m multiport&#8211; dports 4505, 4506 &#8211; j ACCEPT<br />
#Allow Salt to communicate with Master on the loopback interface<br />
                                                                                                                                                      &#8211; A INPUT &#8211; i lo &#8211; p tcp &#8211; m multiport&#8211; dports 4505,<br />
    4506 &#8211; j ACCEPT<br />
#Reject everything else<br />
        &#8211; A INPUT &#8211; p tcp &#8211; m multiport&#8211; dports 4505,<br />
    4506 &#8211; j REJECT</p>
<p> <code>NOTE:</code> The important thing to note here is that the <code>salt</code> command needs to communicate with the listening network socket of <code>salt-master</code> on the <i>loopback</i> interface. Without this you will see no outgoing Salt traffic from the master, even for a simple <code>salt &#8216;*&#8217; test.ping</code>, because the <code>salt</code> client never reached the <code>salt-master</code> to tell it to carry out the execution.</p>
<h3>Using cron with Salt</h3>
<p> The Salt Minion can initiate its own highstate using the <code>salt-call</code> command. </p>
<pre>
$ salt-call state.highstate
</pre>
<p> This will cause the minion to check in with the master and ensure it is in the correct &#8216;state&#8217;.</p>
<h3>Use cron to initiate a highstate</h3>
<p> If you would like the Salt Minion to regularly check in with the master you can use the venerable cron to run the <code>salt-call</code> command. </p>
<pre>
# PATH=/bin:/sbin:/usr/bin:/usr/sbin
00 00 * * * salt-call state.highstate
</pre>
<p> The above cron entry will run a highstate every day at midnight. </p>
<p> <code>NOTE:</code> Be aware that you may need to ensure the PATH for cron includes any scripts or commands that need to be executed.</p>
<h3>Remote execution tutorial</h3>
<p> <code>Before continuing</code> make sure you have a working Salt installation by following the <code>installation</code> and the <code>configuration</code> instructions.</p>
<dl>
<dt>Stuck?</p>
<dd>
<p> There are many ways to get help from the Salt community including our <i>mailing list</i> and our <i>IRC channel</i> #salt.</dl>
<h3>Order your minions around</h3>
<p> Now that you have a master and at least one minion communicating with each other you can perform commands on the minion via the <code>salt</code> command. Salt calls are comprised of three main components: </p>
<pre>
salt '&lt;target&gt;' &lt;function&gt; [arguments]
</pre>
<p> <code>SEE ALSO:</code> <code>salt manpage</code></p>
<h3>target</h3>
<p> The target component allows you to filter which minions should run the following function. The default filter is a glob on the minion id. For example: </p>
<pre>
salt '*' test.ping
salt '*.example.org' test.ping
</pre>
<p> Targets can be based on minion system information using the Grains system: </p>
<pre>
salt -G 'os:Ubuntu' test.ping
</pre>
<p> <code>SEE ALSO:</code> <code>Grains system</code> </p>
<p> Targets can be filtered by regular expression: </p>
<pre>
salt -E 'virtmach[0-9]' test.ping
</pre>
<p> Targets can be explicitly specified in a list: </p>
<pre>
salt -L 'foo,bar,baz,quo' test.ping
</pre>
<p> Or Multiple target types can be combined in one command: </p>
<pre>
salt -C 'G@os:Ubuntu and webser* or E@database.*' test.ping
</pre>
<h3>function</h3>
<p> A function is some functionality provided by a module. Salt ships with a large collection of available functions. List all available functions on your minions: </p>
<pre>
salt '*' sys.doc
</pre>
<p> Here are some examples: </p>
<p> Show all currently available minions: </p>
<pre>
salt '*' test.ping
</pre>
<p> Run an arbitrary shell command: </p>
<pre>
salt '*' cmd.run 'uname -a'
</pre>
<p> <code>SEE ALSO:</code> <code>the full list of modules</code></p>
<h3>arguments</h3>
<p> Space-delimited arguments to the function: </p>
<pre>
salt '*' cmd.exec_code python 'import sys; print sys.version'
</pre>
<p> Optional, keyword arguments are also supported: </p>
<pre>
salt '*' pip.install salt timeout=5 upgrade=True
</pre>
<p> They are always in the form of <code>kwarg=argument</code>.</p>
<h3>Pillar Walkthrough</h3>
<p> <code>NOTE:</code> This walkthrough assumes that the reader has already completed the initial Salt <code>walkthrough</code>. </p>
<p> Pillars are tree-like structures of data defined on the Salt Master and passed through to minions. They allow confidential, targeted data to be securely sent only to the relevant minion. </p>
<p> <code>NOTE:</code> Grains and Pillar are sometimes confused, just remember that Grains are data about a minion which is stored or generated from the minion. This is why information like the OS and CPU type are found in Grains. Pillar is information about a minion or many minions stored or generated on the Salt Master. </p>
<p> Pillar data is useful for:</p>
<dl>
<dt><code>Highly Sensitive Data:</code></p>
<dd> Information transferred via pillar is guaranteed to only be presented to the minions that are targeted, making Pillar suitable for managing security information, such as cryptographic keys and passwords.</p>
<dt><code>Minion Configuration:</code></p>
<dd> Minion modules such as the execution modules, states, and returners can often be configured via data stored in pillar.</p>
<dt><code>Variables:</code></p>
<dd> Variables which need to be assigned to specific minions or groups of minions can be defined in pillar and then accessed inside sls formulas and template files.</p>
<dt><code>Arbitrary Data:</code></p>
<dd> Pillar can contain any basic data structure in dictionary format, so a key/value store can be defined making it easy to iterate over a group of values in sls formulas. </p>
<p> Pillar is therefore one of the most important systems when using Salt. This walkthrough is designed to get a simple Pillar up and running in a few minutes and then to dive into the capabilities of Pillar and where the data is available.</dl>
<h3>Setting Up Pillar</h3>
<p> The pillar is already running in Salt by default. To see the minion&#8217;s pillar data: </p>
<pre>
salt '*' pillar.items
</pre>
<p> <code>NOTE:</code> Prior to version 0.16.2, this function is named <code>pillar.data</code>. This function name is still supported for backwards compatibility. </p>
<p> By default the contents of the master configuration file are loaded into pillar for all minions. This enables the master configuration file to be used for global configuration of minions. </p>
<p> Similar to the state tree, the pillar is comprised of sls files and has a top file. The default location for the pillar is in /srv/pillar. </p>
<p> <code>NOTE:</code> The pillar location can be configured via the <i>pillar_roots</i> option inside the master configuration file. It must not be in a subdirectory of the state tree or file_roots. If the pillar is under file_roots, any pillar targeting can be bypassed by minions. </p>
<p> To start setting up the pillar, the /srv/pillar directory needs to be present: </p>
<pre>
mkdir /srv/pillar
</pre>
<p> Now create a simple top file, following the same format as the top file used for states: </p>
<p> <code>/srv/pillar/top.sls</code>: </p>
<pre>
base:
  '*':
    - data
</pre>
<p> This top file associates the data.sls file to all minions. Now the <code>/srv/pillar/data.sls</code> file needs to be populated: </p>
<p> <code>/srv/pillar/data.sls</code>: </p>
<pre>
info: some data
</pre>
<p> To ensure that the minions have the new pillar data, issue a command to them asking that they fetch their pillars from the master: </p>
<pre>
salt '*' saltutil.refresh_pillar
</pre>
<p> Now that the minions have the new pillar, it can be retrieved: </p>
<pre>
salt '*' pillar.items
</pre>
<p> The key <code>info</code> should now appear in the returned pillar data.</p>
<h3>More Complex Data</h3>
<p> Unlike states, pillar files do not need to define <code>formulas</code>. This example sets up user data with a UID: </p>
<p> <code>/srv/pillar/users/init.sls</code>: </p>
<pre>
users:
  thatch: 1000
  shouse: 1001
  utahdave: 1002
  redbeard: 1003
</pre>
<p> <code>NOTE:</code> The same directory lookups that exist in states exist in pillar, so the file <code>users/init.sls</code> can be referenced with <code>users</code> in the top file. </p>
<p> The top file will need to be updated to include this sls file: </p>
<p> <code>/srv/pillar/top.sls</code>: </p>
<pre>
base:
  '*':
    - data
    - users
</pre>
<p> Now the data will be available to the minions. To use the pillar data in a state, you can use Jinja: </p>
<p> <code>/srv/salt/users/init.sls</code> </p>
<p>{% for user, uid in pillar.get(&#8216;users&#8217;, {}).items() %<br />
}<br />
&#123;&#123;user}} : user.present : -uid : &#123;&#123;uid}}<br />
{<br />
    % endfor %<br />
}</p>
<p> This approach allows for users to be safely defined in a pillar and then the user data is applied in an sls file.</p>
<h3>Parameterizing States With Pillar</h3>
<p> Pillar data can be accessed in state files to customise behavior for each minion. All pillar (and grain) data applicable to each minion is substituted into the state files through templating before being run. Typical uses include setting directories appropriate for the minion and skipping states that don&#8217;t apply. </p>
<p> A simple example is to set up a mapping of package names in pillar for separate Linux distributions: </p>
<p> <code>/srv/pillar/pkg/init.sls</code>: </p>
<p>pkgs:<br />
{<br />
    % if grains[&#8216;os_family&#8217;] == &#8216;RedHat&#8217; %<br />
}<br />
apache : httpd<br />
             vim : vim &#8211;<br />
                   enhanced{ % elif grains[&#8216;os_family&#8217;] == &#8216;Debian&#8217; % } apache : apache2<br />
                                                                                     vim : vim{ % elif grains[&#8216;os&#8217;] == &#8216;Arch&#8217; % } apache : apache<br />
                                                                                                                                               vim : vim<br />
{<br />
    % endif %<br />
}</p>
<p> The new <code>pkg</code> sls needs to be added to the top file: </p>
<p> <code>/srv/pillar/top.sls</code>: </p>
<pre>
base:
  '*':
    - data
    - users
    - pkg
</pre>
<p> Now the minions will auto map values based on respective operating systems inside of the pillar, so sls files can be safely parameterized: </p>
<p> <code>/srv/salt/apache/init.sls</code>: </p>
<p>apache : pkg.installed : -name:<br />
{<br />
    {<br />
        pillar[&#8216;pkgs&#8217;][&#8216;apache&#8217;]<br />
    }<br />
}</p>
<p> Or, if no pillar is available a default can be set as well: </p>
<p> <code>NOTE:</code> The function <code>pillar.get</code> used in this example was added to Salt in version 0.14.0 </p>
<p> <code>/srv/salt/apache/init.sls</code>: </p>
<p>apache : pkg.installed : -name:<br />
{<br />
    {<br />
        salt[&#8216;pillar.get&#8217;](&#8216;pkgs:apache&#8217;, &#8216;httpd&#8217;)<br />
    }<br />
}</p>
<p> In the above example, if the pillar value <code>pillar[&#8216;pkgs&#8217;][&#8216;apache&#8217;]</code> is not set in the minion&#8217;s pillar, then the default of <code>httpd</code> will be used. </p>
<p> <code>NOTE:</code> Under the hood, pillar is just a Python dict, so Python dict methods such as <i>get</i> and <i>items</i> can be used.</p>
<h3>Pillar Makes Simple States Grow Easily</h3>
<p> One of the design goals of pillar is to make simple sls formulas easily grow into more flexible formulas without refactoring or complicating the states. </p>
<p> A simple formula: </p>
<p> <code>/srv/salt/edit/vim.sls</code>: </p>
<pre>
vim:
  pkg.installed: []
/etc/vimrc:
  file.managed:
    - source: <a href="salt://edit/vimrc" rel="nofollow">salt://edit/vimrc</a>
    - mode: 644
    - user: root
    - group: root
    - require:
      - pkg: vim
</pre>
<p> Can be easily transformed into a powerful, parameterized formula: </p>
<p> <code>/srv/salt/edit/vim.sls</code>: </p>
<p>vim : pkg.installed : -name : &#123;&#123;pillar[&#8216;pkgs&#8217;][&#8216;vim&#8217;]}} / etc / vimrc : file.managed : -source : &#123;&#123;pillar[&#8216;vimrc&#8217;]}} &#8211; mode : 644 &#8211; user : root &#8211; group : root &#8211; require : -pkg : vim</p>
<p> Where the vimrc source location can now be changed via pillar: </p>
<p> <code>/srv/pillar/edit/vim.sls</code>: </p>
<p>{<br />
    % if grains[&#8216;id&#8217;].startswith(&#8216;dev&#8217;) %<br />
}<br />
vimrc : salt :                                                                                      // edit/dev_vimrc<br />
               { % elif grains[&#8216;id&#8217;].startswith(&#8216;qa&#8217;) % } vimrc : salt :                            // edit/qa_vimrc<br />
                                                                         { % else % } vimrc : salt: // edit/vimrc<br />
{<br />
    % endif %<br />
}</p>
<p> Ensuring that the right vimrc is sent out to the correct minions.</p>
<h3>Setting Pillar Data on the Command Line</h3>
<p> Pillar data can be set on the command line like so: </p>
<pre>
salt '*' state.highstate pillar='{&quot;foo&quot;: &quot;bar&quot;}'
</pre>
<p> The <code>state.sls</code> command can also be used to set pillar values via the command line: </p>
<pre>
salt '*' state.sls my_sls_file pillar='{&quot;hello&quot;: &quot;world&quot;}'
</pre>
<p> <code>NOTE:</code> If a key is passed on the command line that already exists on the minion, the key that is passed in will overwrite the entire value of that key, rather than merging only the specified value set via the command line. </p>
<p> The example below will swap the value for vim with telnet in the previously specified list, notice the nested pillar dict: </p>
<p>salt &#8216;*&#8217; state.sls edit.vim pillar = &#8216;{&#8220;pkgs&#8221;: {&#8220;vim&#8221;: &#8220;telnet&#8221;}}&#8217;</p>
<p> <code>NOTE:</code> This will attempt to install telnet on your minions, feel free to uninstall the package or replace telnet value with anything else.</p>
<h3>More On Pillar</h3>
<p> Pillar data is generated on the Salt master and securely distributed to minions. Salt is not restricted to the pillar sls files when defining the pillar but can retrieve data from external sources. This can be useful when information about an infrastructure is stored in a separate location. </p>
<p> Reference information on pillar and the external pillar interface can be found in the Salt documentation: </p>
<p> <code>Pillar</code></p>
<h3>States</h3>
<h3>How Do I Use Salt States?</h3>
<p> Simplicity, Simplicity, Simplicity </p>
<p> Many of the most powerful and useful engineering solutions are founded on simple principles. Salt States strive to do just that: K.I.S.S. (Keep It Stupidly Simple) </p>
<p> The core of the Salt State system is the SLS, or <code>S</code>a<code>L</code>t <code>S</code>tate file. The SLS is a representation of the state in which a system should be in, and is set up to contain this data in a simple format. This is often called configuration management. </p>
<p> <code>NOTE:</code> This is just the beginning of using states, make sure to read up on pillar <code>Pillar</code> next.</p>
<h3>It is All Just Data</h3>
<p> Before delving into the particulars, it will help to understand that the SLS file is just a data structure under the hood. While understanding that the SLS is just a data structure isn&#8217;t critical for understanding and making use of Salt States, it should help bolster knowledge of where the real power is. </p>
<p> SLS files are therefore, in reality, just <i>dictionaries</i>, <i>lists</i>, <i>strings</i>, and <i>numbers</i>. By using this approach Salt can be much more flexible. As one writes more state files, it becomes clearer exactly what is being written. The result is a system that is easy to understand, yet grows with the needs of the admin or developer.</p>
<h3>The Top File</h3>
<p> The example SLS files in the below sections can be assigned to hosts using a file called <code>top.sls</code>. This file is described in-depth <code>here</code>.</p>
<h3>Default Data &#8211; YAML</h3>
<p> By default Salt represents the SLS data in what is one of the simplest serialization formats available &#8211; <i>YAML</i>. </p>
<p> A typical SLS file will often look like this in YAML: </p>
<p> <code>NOTE:</code> These demos use some generic service and package names, different distributions often use different names for packages and services. For instance <i>apache</i> should be replaced with <i>httpd</i> on a Red Hat system. Salt uses the name of the init script, systemd name, upstart name etc. based on what the underlying service management for the platform. To get a list of the available service names on a platform execute the service.get_all salt function. </p>
<p> Information on how to make states work with multiple distributions is later in the tutorial. </p>
<pre>
apache:
  pkg.installed: []
  service.running:
    - require:
      - pkg: apache
</pre>
<p> This SLS data will ensure that the package named apache is installed, and that the apache service is running. The components can be explained in a simple way. </p>
<p> The first line is the ID for a set of data, and it is called the ID Declaration. This ID sets the name of the thing that needs to be manipulated. </p>
<p> The second and third lines contain the state module function to be run, in the format <code>&lt;state_module&gt;.&lt;function&gt;</code>. The <code>pkg.installed</code> state module function ensures that a software package is installed via the system&#8217;s native package manager. The <code>service.running</code> state module function ensures that a given system daemon is running. </p>
<p> Finally, on line five, is the word <code>require</code>. This is called a Requisite Statement, and it makes sure that the Apache service is only started after a successful installation of the apache package.</p>
<h3>Adding Configs and Users</h3>
<p> When setting up a service like an Apache web server, many more components may need to be added. The Apache configuration file will most likely be managed, and a user and group may need to be set up. </p>
<pre>
apache:
  pkg.installed: []
  service.running:
    - watch:
      - pkg: apache
      - file: /etc/httpd/conf/httpd.conf
      - user: apache
  user.present:
    - uid: 87
    - gid: 87
    - home: /var/www/html
    - shell: /bin/nologin
    - require:
      - group: apache
  group.present:
    - gid: 87
    - require:
      - pkg: apache
/etc/httpd/conf/httpd.conf:
  file.managed:
    - source: <a href="salt://apache/httpd.conf" rel="nofollow">salt://apache/httpd.conf</a>
    - user: root
    - group: root
    - mode: 644
</pre>
<p> This SLS data greatly extends the first example, and includes a config file, a user, a group and new requisite statement: <code>watch</code>. </p>
<p> Adding more states is easy, since the new user and group states are under the Apache ID, the user and group will be the Apache user and group. The <code>require</code> statements will make sure that the user will only be made after the group, and that the group will be made only after the Apache package is installed. </p>
<p> Next, the <code>require</code> statement under service was changed to watch, and is now watching 3 states instead of just one. The watch statement does the same thing as require, making sure that the other states run before running the state with a watch, but it adds an extra component. The <code>watch</code> statement will run the state&#8217;s watcher function for any changes to the watched states. So if the package was updated, the config file changed, or the user uid modified, then the service state&#8217;s watcher will be run. The service state&#8217;s watcher just restarts the service, so in this case, a change in the config file will also trigger a restart of the respective service.</p>
<h3>Moving Beyond a Single SLS</h3>
<p> When setting up Salt States in a scalable manner, more than one SLS will need to be used. The above examples were in a single SLS file, but two or more SLS files can be combined to build out a State Tree. The above example also references a file with a strange source &#8211; <code><a href="salt://apache/httpd.conf" rel="nofollow">salt://apache/httpd.conf</a></code>. That file will need to be available as well. </p>
<p> The SLS files are laid out in a directory structure on the Salt master; an SLS is just a file and files to download are just files. </p>
<p> The Apache example would be laid out in the root of the Salt file server like this: </p>
<pre>
apache/init.sls
apache/httpd.conf
</pre>
<p> So the httpd.conf is just a file in the apache directory, and is referenced directly. </p>
<p> But when using more than one single SLS file, more components can be added to the toolkit. Consider this SSH example: </p>
<p> <code>ssh/init.sls:</code> </p>
<pre>
openssh-client:
  pkg.installed
/etc/ssh/ssh_config:
  file.managed:
    - user: root
    - group: root
    - mode: 644
    - source: <a href="salt://ssh/ssh_config" rel="nofollow">salt://ssh/ssh_config</a>
    - require:
      - pkg: openssh-client
</pre>
<p> <code>ssh/server.sls:</code> </p>
<pre>
include:
  - ssh
openssh-server:
  pkg.installed
sshd:
  service.running:
    - require:
      - pkg: openssh-client
      - pkg: openssh-server
      - file: /etc/ssh/banner
      - file: /etc/ssh/sshd_config
/etc/ssh/sshd_config:
  file.managed:
    - user: root
    - group: root
    - mode: 644
    - source: <a href="salt://ssh/sshd_config" rel="nofollow">salt://ssh/sshd_config</a>
    - require:
      - pkg: openssh-server
/etc/ssh/banner:
  file:
    - managed
    - user: root
    - group: root
    - mode: 644
    - source: <a href="salt://ssh/banner" rel="nofollow">salt://ssh/banner</a>
    - require:
      - pkg: openssh-server
</pre>
<p> <code>NOTE:</code> Notice that we use two similar ways of denoting that a file is managed by Salt. In the <i>/etc/ssh/sshd_config</i> state section above, we use the <i>file.managed</i> state declaration whereas with the <i>/etc/ssh/banner</i> state section, we use the <i>file</i> state declaration and add a <i>managed</i> attribute to that state declaration. Both ways produce an identical result; the first way &#8212; using <i>file.managed</i> &#8212; is merely a shortcut. </p>
<p> Now our State Tree looks like this: </p>
<pre>
apache/init.sls
apache/httpd.conf
ssh/init.sls
ssh/server.sls
ssh/banner
ssh/ssh_config
ssh/sshd_config
</pre>
<p> This example now introduces the <code>include</code> statement. The include statement includes another SLS file so that components found in it can be required, watched or as will soon be demonstrated &#8211; extended. </p>
<p> The include statement allows for states to be cross linked. When an SLS has an include statement it is literally extended to include the contents of the included SLS files. </p>
<p> Note that some of the SLS files are called init.sls, while others are not. More info on what this means can be found in the States Tutorial.</p>
<h3>Extending Included SLS Data</h3>
<p> Sometimes SLS data needs to be extended. Perhaps the apache service needs to watch additional resources, or under certain circumstances a different file needs to be placed. </p>
<p> In these examples, the first will add a custom banner to ssh and the second will add more watchers to apache to include mod_python. </p>
<p> <code>ssh/custom-server.sls:</code> </p>
<pre>
include:
  - ssh.server
extend:
  /etc/ssh/banner:
    file:
      - source: <a href="salt://ssh/custom-banner" rel="nofollow">salt://ssh/custom-banner</a>
</pre>
<p> <code>python/mod_python.sls:</code> </p>
<pre>
include:
  - apache
extend:
  apache:
    service:
      - watch:
        - pkg: mod_python
mod_python:
  pkg.installed
</pre>
<p> The <code>custom-server.sls</code> file uses the extend statement to overwrite where the banner is being downloaded from, and therefore changing what file is being used to configure the banner. </p>
<p> In the new mod_python SLS the mod_python package is added, but more importantly the apache service was extended to also watch the mod_python package.</p>
<dl>
<dt>Using extend with require or watch</p>
<dd>
<p> The <code>extend</code> statement works differently for <code>require</code> or <code>watch</code>. It appends to, rather than replacing the requisite component.</dl>
<h3>Understanding the Render System</h3>
<p> Since SLS data is simply that (data), it does not need to be represented with YAML. Salt defaults to YAML because it is very straightforward and easy to learn and use. But the SLS files can be rendered from almost any imaginable medium, so long as a renderer module is provided. </p>
<p> The default rendering system is the <code>yaml_jinja</code> renderer. The <code>yaml_jinja</code> renderer will first pass the template through the <i>Jinja2</i> templating system, and then through the YAML parser. The benefit here is that full programming constructs are available when creating SLS files. </p>
<p> Other renderers available are <code>yaml_mako</code> and <code>yaml_wempy</code> which each use the <i>Mako</i> or <i>Wempy</i> templating system respectively rather than the jinja templating system, and more notably, the pure Python or <code>py</code>, <code>pydsl</code> &amp; <code>pyobjects</code> renderers. The <code>py</code> renderer allows for SLS files to be written in pure Python, allowing for the utmost level of flexibility and power when preparing SLS data; while the <code>pydsl</code> renderer provides a flexible, domain-specific language for authoring SLS data in Python; and the <code>pyobjects</code> renderer gives you a <i>&quot;Pythonic&quot;</i> interface to building state data. </p>
<p> <code>NOTE:</code> The templating engines described above aren&#8217;t just available in SLS files. They can also be used in <code>file.managed</code> states, making file management much more dynamic and flexible. Some examples for using templates in managed files can be found in the documentation for the <code>file states</code>, as well as the <i>MooseFS example</i> below.</p>
<h3>Getting to Know the Default &#8211; yaml_jinja</h3>
<p> The default renderer &#8211; <code>yaml_jinja</code>, allows for use of the jinja templating system. A guide to the Jinja templating system can be found here: <i><a rel="nofollow noopener" href="http://jinja.pocoo.org/docs" target="_blank">http://jinja.pocoo.org/docs</a></i> </p>
<p> When working with renderers a few very useful bits of data are passed in. In the case of templating engine based renderers, three critical components are available, <code>salt</code>, <code>grains</code>, and <code>pillar</code>. The <code>salt</code> object allows for any Salt function to be called from within the template, and <code>grains</code> allows for the Grains to be accessed from within the template. A few examples: </p>
<p> <code>apache/init.sls:</code> </p>
<p>apache : pkg.installed:<br />
{<br />
    % if grains[&#8216;os&#8217;] == &#8216;RedHat&#8217; %<br />
}<br />
&#8211; name:httpd{ % endif % } service.running:<br />
{<br />
    % if grains[&#8216;os&#8217;] == &#8216;RedHat&#8217; %<br />
}<br />
&#8211; name:httpd{ % endif % } &#8211; watch:<br />
                                &#8211;<br />
        pkg:apache &#8211;<br />
       file: / etc / httpd / conf / httpd.conf &#8211; user:apache<br />
                                                          user.<br />
    present:<br />
        &#8211;<br />
        uid:87 &#8211;<br />
        gid:87 &#8211; home: / var / www / html &#8211; shell: / bin / nologin &#8211; require:<br />
                                                                         &#8211;<br />
      group:apache<br />
                group.<br />
    present:<br />
        &#8211;<br />
        gid:87 &#8211;<br />
    require:<br />
        &#8211;<br />
        pkg:apache / etc / httpd / conf / httpd.<br />
       conf:<br />
           file.<br />
    managed:<br />
        &#8211;<br />
     source:<br />
       salt: // apache/httpd.conf<br />
           &#8211;<br />
       user:root &#8211;<br />
      group:root &#8211; mode:644</p>
<p> This example is simple. If the <code>os</code> grain states that the operating system is Red Hat, then the name of the Apache package and service needs to be httpd. </p>
<p> A more aggressive way to use Jinja can be found here, in a module to set up a MooseFS distributed filesystem chunkserver: </p>
<p> <code>moosefs/chunk.sls:</code> </p>
<p>include : -moosefs<br />
{% for mnt in salt[&#8216;cmd.run&#8217;](&#8216;ls /dev/data/moose*&#8217;).split() %<br />
}<br />
/ mnt / moose&#123;&#123;mnt[-1]}} : mount.mounted : -device : &#123;&#123;mnt}} &#8211; fstype : xfs &#8211; mkmnt : True file.directory : -user : mfs &#8211; group : mfs &#8211; require : -user : mfs &#8211; group : mfs{ % endfor % } / etc / mfshdd.cfg : file.managed : -source : salt : // moosefs/mfshdd.cfg<br />
                                                                                                                                                                                                                                               -user : root &#8211;<br />
                                                                                                                                                          group : root &#8211; mode : 644 &#8211; template : jinja &#8211; require : -pkg : mfs &#8211; chunkserver / etc / mfschunkserver.cfg : file.managed : -source : salt : // moosefs/mfschunkserver.cfg<br />
                                                                                                                                                                                                                                                                                                         -user : root &#8211;<br />
                                                                                                                                                                                                                          group : root &#8211; mode : 644 &#8211; template : jinja &#8211; require : -pkg : mfs &#8211; chunkserver mfs &#8211; chunkserver : pkg.installed : [] mfschunkserver : service.running : -require:<br />
{% for mnt in salt[&#8216;cmd.run&#8217;](&#8216;ls /dev/data/moose*&#8217;) %<br />
}<br />
&#8211; mount: / mnt / moose&#123;&#123;mnt[-1]}} &#8211; file: / mnt / moose&#123;&#123;mnt[-1]}} { % endfor % } &#8211; file: / etc / mfschunkserver.cfg &#8211; file: / etc / mfshdd.cfg &#8211; file: / var / lib / mfs</p>
<p> This example shows much more of the available power of Jinja. Multiple for loops are used to dynamically detect available hard drives and set them up to be mounted, and the <code>salt</code> object is used multiple times to call shell commands to gather data.</p>
<h3>Introducing the Python, PyDSL, and the Pyobjects Renderers</h3>
<p> Sometimes the chosen default renderer might not have enough logical power to accomplish the needed task. When this happens, the Python renderer can be used. Normally a YAML renderer should be used for the majority of SLS files, but an SLS file set to use another renderer can be easily added to the tree. </p>
<p> This example shows a very basic Python SLS file: </p>
<p> <code>python/django.sls:</code> </p>
<p>#!py<br />
def run()<br />
    :<br />
    &#8221;&#8217; Install the django package<br />
    &#8221;&#8217; return<br />
{<br />
    &#8216;include&#8217; : [&#8216;python&#8217;],<br />
                &#8216;django&#8217;:<br />
    {<br />
        &#8216;pkg&#8217; : [&#8216;installed&#8217;]<br />
    }<br />
}</p>
<p> This is a very simple example; the first line has an SLS shebang that tells Salt to not use the default renderer, but to use the <code>py</code> renderer. Then the run function is defined, the return value from the run function must be a Salt friendly data structure, or better known as a Salt <code>HighState data structure</code>. </p>
<p> Alternatively, using the <code>pydsl</code> renderer, the above example can be written more succinctly as: </p>
<pre>
#!pydsl
include('python', delayed=True)
state('django').pkg.installed()
</pre>
<p> The <code>pyobjects</code> renderer provides an <i>&quot;Pythonic&quot;</i> object based approach for building the state data. The above example could be written as: </p>
<pre>
#!pyobjects
include('python')
Pkg.installed(&quot;django&quot;)
</pre>
<p> This Python examples would look like this if they were written in YAML: </p>
<pre>
include:
  - python
django:
  pkg.installed
</pre>
<p> This example clearly illustrates that; one, using the YAML renderer by default is a wise decision and two, unbridled power can be obtained where needed by using a pure Python SLS.</p>
<h3>Running and debugging salt states.</h3>
<p> Once the rules in an SLS are ready, they should be tested to ensure they work properly. To invoke these rules, simply execute <code>salt &#8216;*&#8217; state.highstate</code> on the command line. If you get back only hostnames with a <code>:</code> after, but no return, chances are there is a problem with one or more of the sls files. On the minion, use the <code>salt-call</code> command: <code>salt-call state.highstate -l debug</code> to examine the output for errors. This should help troubleshoot the issue. The minions can also be started in the foreground in debug mode: <code>salt-minion -l debug</code>.</p>
<h3>Next Reading</h3>
<p> With an understanding of states, the next recommendation is to become familiar with Salt&#8217;s pillar interface: <code>Pillar Walkthrough</code></p>
<h3>States tutorial, part 1 &#8211; Basic Usage</h3>
<p> The purpose of this tutorial is to demonstrate how quickly you can configure a system to be managed by Salt States. For detailed information about the state system please refer to the full <code>states reference</code>. </p>
<p> This tutorial will walk you through using Salt to configure a minion to run the Apache HTTP server and to ensure the server is running. </p>
<p> <code>Before continuing</code> make sure you have a working Salt installation by following the <code>installation</code> and the <code>configuration</code> instructions.</p>
<dl>
<dt>Stuck?</p>
<dd>
<p> There are many ways to get help from the Salt community including our <i>mailing list</i> and our <i>IRC channel</i> #salt.</dl>
<h3>Setting up the Salt State Tree</h3>
<p> States are stored in text files on the master and transferred to the minions on demand via the master&#8217;s File Server. The collection of state files make up the <code>State Tree</code>. </p>
<p> To start using a central state system in Salt, the Salt File Server must first be set up. Edit the master config file (<code>file_roots</code>) and uncomment the following lines: </p>
<pre>
file_roots:
  base:
    - /srv/salt
</pre>
<p> <code>NOTE:</code> If you are deploying on FreeBSD via ports, the <code>file_roots</code> path defaults to <code>/usr/local/etc/salt/states</code>. </p>
<p> Restart the Salt master in order to pick up this change: </p>
<pre>
pkill salt-master
salt-master -d
</pre>
<h3>Preparing the Top File</h3>
<p> On the master, in the directory uncommented in the previous step, (<code>/srv/salt</code> by default), create a new file called <code>top.sls</code> and add the following: </p>
<pre>
base:
  '*':
    - webserver
</pre>
<p> The top file is separated into environments (discussed later). The default environment is <code>base</code>. Under the <code>base</code> environment a collection of minion matches is defined; for now simply specify all hosts (<code>*</code>).</p>
<dl>
<dt>Targeting minions</p>
<dd>
<p> The expressions can use any of the targeting mechanisms used by Salt â minions can be matched by glob, PCRE regular expression, or by <code>grains</code>. For example: </p>
<pre>
base:
  'os:Fedora':
    - match: grain
    - webserver
</pre>
</dl>
<h3>Create an <code>sls</code> file</h3>
<p> In the same directory as the top file, create a file named <code>webserver.sls</code>, containing the following: </p>
<pre>
apache:                 # ID declaration
  pkg:                  # state declaration
    - installed         # function declaration
</pre>
<p> The first line, called the id-declaration, is an arbitrary identifier. In this case it defines the name of the package to be installed. </p>
<p> <code>NOTE:</code> The package name for the Apache httpd web server may differ depending on OS or distro â for example, on Fedora it is <code>httpd</code> but on Debian/Ubuntu it is <code>apache2</code>. </p>
<p> The second line, called the state-declaration, defines which of the Salt States we are using. In this example, we are using the <code>pkg state</code> to ensure that a given package is installed. </p>
<p> The third line, called the function-declaration, defines which function in the <code>pkg state</code> module to call.</p>
<dl>
<dt>Renderers</p>
<dd>
<p> States <code>sls</code> files can be written in many formats. Salt requires only a simple data structure and is not concerned with how that data structure is built. Templating languages and <i>DSLs</i> are a dime-a-dozen and everyone has a favorite. </p>
<p> Building the expected data structure is the job of Salt <code>renderers</code> and they are dead-simple to write. </p>
<p> In this tutorial we will be using YAML in Jinja2 templates, which is the default format. The default can be changed by editing <code>renderer</code> in the master configuration file.</dl>
<h3>Install the package</h3>
<p> Next, let&#8217;s run the state we created. Open a terminal on the master and run: </p>
<pre>
% salt '*' state.highstate
</pre>
<p> Our master is instructing all targeted minions to run <code>state.highstate</code>. When a minion executes a highstate call it will download the top file and attempt to match the expressions. When it does match an expression the modules listed for it will be downloaded, compiled, and executed. </p>
<p> Once completed, the minion will report back with a summary of all actions taken and all changes made. </p>
<p> <code>WARNING:</code> If you have created custom grain modules, they will not be available in the top file until after the first <i>highstate</i>. To make custom grains available on a minion&#8217;s first highstate, it is recommended to use this example to ensure that the custom grains are synced when the minion starts.</p>
<dl>
<dt>SLS File Namespace</p>
<dd>
<p> Note that in the <i>example</i> above, the SLS file <code>webserver.sls</code> was referred to simply as <code>webserver</code>. The namespace for SLS files follows a few simple rules:</p>
<dt>1.</p>
<dd> The <code>.sls</code> is discarded (i.e. <code>webserver.sls</code> becomes <code>webserver</code>).</p>
<dt>2.</p>
<dd>
<dt><code>Subdirectories can be used for better organization.</code></p>
<dd>
<dt>a.</p>
<dd> Each subdirectory is represented by a dot.</p>
<dt>b.</p>
<dd> <code>webserver/dev.sls</code> is referred to as <code>webserver.dev</code>.</p>
<dt>3.</p>
<dd> A file called <code>init.sls</code> in a subdirectory is referred to by the path of the directory. So, <code>webserver/init.sls</code> is referred to as <code>webserver</code>.</p>
<dt>4.</p>
<dd> If both <code>webserver.sls</code> and <code>webserver/init.sls</code> happen to exist, <code>webserver/init.sls</code> will be ignored and <code>webserver.sls</code> will be the file referred to as <code>webserver</code>.</p>
<dt>Troubleshooting Salt</p>
<dd>
<p> If the expected output isn&#8217;t seen, the following tips can help to narrow down the problem.</p>
<dt><code>Turn up logging</code></p>
<dd> Salt can be quite chatty when you change the logging setting to <code>debug</code>: </p>
<pre>
salt-minion -l debug
</pre>
<dt><code>Run the minion in the foreground</code></p>
<dd> By not starting the minion in daemon mode (<code>-d</code>) one can view any output from the minion as it works: </p>
<pre>
salt-minion &amp;
</pre>
<p> Increase the default timeout value when running <code>salt</code>. For example, to change the default timeout to 60 seconds: </p>
<pre>
salt -t 60
</pre>
<p> For best results, combine all three: </p>
<pre>
salt-minion -l debug &amp;          # On the minion
salt '*' state.highstate -t 60  # On the master
</pre>
</dl>
<h3>Next steps</h3>
<p> This tutorial focused on getting a simple Salt States configuration working. <code>Part 2</code> will build on this example to cover more advanced <code>sls</code> syntax and will explore more of the states that ship with Salt.</p>
<h3>States tutorial, part 2 &#8211; More Complex States, Requisites</h3>
<p> <code>NOTE:</code> This tutorial builds on topics covered in <code>part 1</code>. It is recommended that you begin there. </p>
<p> In the <code>last part</code> of the Salt States tutorial we covered the basics of installing a package. We will now modify our <code>webserver.sls</code> file to have requirements, and use even more Salt States.</p>
<h3>Call multiple States</h3>
<p> You can specify multiple state-declaration under an id-declaration. For example, a quick modification to our <code>webserver.sls</code> to also start Apache if it is not running: </p>
<pre>
apache:
  pkg.installed: []
  service.running:
    - require:
      - pkg: apache
</pre>
<p> Try stopping Apache before running <code>state.highstate</code> once again and observe the output. </p>
<p> <code>NOTE:</code> For those running RedhatOS derivatives (Centos, AWS), you will want to specify the service name to be httpd. More on state service here, <code>service state</code>. With the example above, just add &quot;- name: httpd&quot; above the require line and with the same spacing.</p>
<h3>Require other states</h3>
<p> We now have a working installation of Apache so let&#8217;s add an HTML file to customize our website. It isn&#8217;t exactly useful to have a website without a webserver so we don&#8217;t want Salt to install our HTML file until Apache is installed and running. Include the following at the bottom of your <code>webserver/init.sls</code> file: </p>
<pre>
apache:
  pkg.installed: []
  service.running:
    - require:
      - pkg: apache
/var/www/index.html:                        # ID declaration
  file:                                     # state declaration
    - managed                               # function
    - source: <a href="salt://webserver/index.html" rel="nofollow">salt://webserver/index.html</a>   # function arg
    - require:                              # requisite declaration
      - pkg: apache                         # requisite reference
</pre>
<p> <code>line 9</code> is the id-declaration. In this example it is the location we want to install our custom HTML file. (<code>Note:</code> the default location that Apache serves may differ from the above on your OS or distro. <code>/srv/www</code> could also be a likely place to look.) </p>
<p> <code>Line 10</code> the state-declaration. This example uses the Salt <code>file state</code>. </p>
<p> <code>Line 11</code> is the function-declaration. The <code>managed function</code> will download a file from the master and install it in the location specified. </p>
<p> <code>Line 12</code> is a function-arg-declaration which, in this example, passes the <code>source</code> argument to the <code>managed function</code>. </p>
<p> <code>Line 13</code> is a requisite-declaration. </p>
<p> <code>Line 14</code> is a requisite-reference which refers to a state and an ID. In this example, it is referring to the <code>ID declaration</code> from our example in <code>part 1</code>. This declaration tells Salt not to install the HTML file until Apache is installed. </p>
<p> Next, create the <code>index.html</code> file and save it in the <code>webserver</code> directory: </p>
<pre>
&lt;html&gt;
    &lt;head&gt;&lt;title&gt;Salt rocks&lt;/title&gt;&lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;This file brought to you by Salt&lt;/h1&gt;
    &lt;/body&gt;
&lt;/html&gt;
</pre>
<p> Last, call <code>state.highstate</code> again and the minion will fetch and execute the highstate as well as our HTML file from the master using Salt&#8217;s File Server: </p>
<pre>
salt '*' state.highstate
</pre>
<p> Verify that Apache is now serving your custom HTML.</p>
<dl>
<dt><code>require</code> vs. <code>watch</code></p>
<dd>
<p> There are two requisite-declaration, ârequireâ, and âwatchâ. Not every state supports âwatchâ. The <code>service state</code> does support âwatchâ and will restart a service based on the watch condition. </p>
<p> For example, if you use Salt to install an Apache virtual host configuration file and want to restart Apache whenever that file is changed you could modify our Apache example from earlier as follows: </p>
<pre>
/etc/httpd/extra/httpd-vhosts.conf:
  file.managed:
    - source: <a href="salt://webserver/httpd-vhosts.conf" rel="nofollow">salt://webserver/httpd-vhosts.conf</a>
apache:
  pkg.installed: []
  service.running:
    - watch:
      - file: /etc/httpd/extra/httpd-vhosts.conf
    - require:
      - pkg: apache
</pre>
<p> If the pkg and service names differ on your OS or distro of choice you can specify each one separately using a name-declaration which explained in <code>Part 3</code>.</dl>
<h3>Next steps</h3>
<p> In <code>part 3</code> we will discuss how to use includes, extends, and templating to make a more complete State Tree configuration.</p>
<h3>States tutorial, part 3 &#8211; Templating, Includes, Extends</h3>
<p> <code>NOTE:</code> This tutorial builds on topics covered in <code>part 1</code> and <code>part 2</code>. It is recommended that you begin there. </p>
<p> This part of the tutorial will cover more advanced templating and configuration techniques for <code>sls</code> files.</p>
<h3>Templating SLS modules</h3>
<p> SLS modules may require programming logic or inline execution. This is accomplished with module templating. The default module templating system used is <i>Jinja2</i> and may be configured by changing the <code>renderer</code> value in the master config. </p>
<p> All states are passed through a templating system when they are initially read. To make use of the templating system, simply add some templating markup. An example of an sls module with templating markup may look like this: </p>
<p>{% for usr in [&#8216;moe&#8217;,&#8217;larry&#8217;,&#8217;curly&#8217;] %<br />
}<br />
&#123;&#123;usr}} : user.present<br />
{<br />
    % endfor %<br />
}</p>
<p> This templated sls file once generated will look like this: </p>
<pre>
moe:
  user.present
larry:
  user.present
curly:
  user.present
</pre>
<p> Here&#8217;s a more complex example: </p>
<p>#Comments in yaml start with a hash symbol.<br />
#Since jinja rendering occurs before yaml parsing, if you want to include jinja<br />
#in the comments you may need to escape them using &#8216;jinja&#8217; comments to prevent<br />
#jinja from trying to render something which is not well &#8211; defined jinja.<br />
#e.g.<br />
#{#iterate over the Three Stooges using a{% for % }..{% endfor % } loop<br />
#with the iterator variable&#123;&#123;usr } } becoming the state ID.#}<br />
{% for usr in &#8216;moe&#8217;,&#8217;larry&#8217;,&#8217;curly&#8217; %<br />
}<br />
&#123;&#123;usr}} : group : -present<br />
                      user : -present &#8211;<br />
                             gid_from_name : True &#8211; require : -group : &#123;&#123;usr}}<br />
{<br />
    % endfor %<br />
}</p>
<h3>Using Grains in SLS modules</h3>
<p> Often times a state will need to behave differently on different systems. <code>Salt grains</code> objects are made available in the template context. The <i>grains</i> can be used from within sls modules: </p>
<p>apache : pkg.installed:<br />
{<br />
    % if grains[&#8216;os&#8217;] == &#8216;RedHat&#8217; %<br />
}<br />
&#8211; name:httpd{ % elif grains[&#8216;os&#8217;] == &#8216;Ubuntu&#8217; % } &#8211; name:apache2<br />
{<br />
    % endif %<br />
}</p>
<h3>Using Environment Variables in SLS modules</h3>
<p> You can use <code>salt[&#8216;environ.get&#8217;](&#8216;VARNAME&#8217;)</code> to use an environment variable in a Salt state. </p>
<pre>
MYENVVAR=&quot;world&quot; salt-call state.template test.sls
</pre>
<p>Create a file with contents from an environment variable : file.managed : -name : / tmp / hello &#8211; contents:<br />
{<br />
    {<br />
        salt[&#8216;environ.get&#8217;](&#8216;MYENVVAR&#8217;)<br />
    }<br />
}</p>
<p> Error checking: </p>
<p>{ % set myenvvar = salt[&#8216;environ.get&#8217;](&#8216;MYENVVAR&#8217;) % } {<br />
    % if myenvvar %<br />
}<br />
Create a file with contents from an environment variable : file.managed : -name : / tmp / hello &#8211; contents : &#123;&#123;salt[&#8216;environ.get&#8217;](&#8216;MYENVVAR&#8217;)}} { % else % } Fail &#8211; no environment passed in : test : A.fail_without_changes<br />
{<br />
    % endif %<br />
}</p>
<h3>Calling Salt modules from templates</h3>
<p> All of the Salt modules loaded by the minion are available within the templating system. This allows data to be gathered in real time on the target system. It also allows for shell commands to be run easily from within the sls modules. </p>
<p> The Salt module functions are also made available in the template context as <code>salt:</code> </p>
<p>moe : user.present : -gid:<br />
{<br />
    {<br />
        salt[&#8216;file.group_to_gid&#8217;](&#8216;some_group_that_exists&#8217;)<br />
    }<br />
}</p>
<p> Note that for the above example to work, <code>some_group_that_exists</code> must exist before the state file is processed by the templating engine. </p>
<p> Below is an example that uses the <code>network.hw_addr</code> function to retrieve the MAC address for eth0: </p>
<pre>
salt['network.hw_addr']('eth0')
</pre>
<h3>Advanced SLS module syntax</h3>
<p> Lastly, we will cover some incredibly useful techniques for more complex State trees.</p>
<h3>Include declaration</h3>
<p> A previous example showed how to spread a Salt tree across several files. Similarly, <code>requisites</code> span multiple files by using an include-declaration. For example: </p>
<p> <code>python/python-libs.sls:</code> </p>
<pre>
python-dateutil:
  pkg.installed
</pre>
<p> <code>python/django.sls:</code> </p>
<pre>
include:
  - python.python-libs
django:
  pkg.installed:
    - require:
      - pkg: python-dateutil
</pre>
<h3>Extend declaration</h3>
<p> You can modify previous declarations by using an extend-declaration. For example the following modifies the Apache tree to also restart Apache when the vhosts file is changed: </p>
<p> <code>apache/apache.sls:</code> </p>
<pre>
apache:
  pkg.installed
</pre>
<p> <code>apache/mywebsite.sls:</code> </p>
<pre>
include:
  - apache.apache
extend:
  apache:
    service:
      - running
      - watch:
        - file: /etc/httpd/extra/httpd-vhosts.conf
/etc/httpd/extra/httpd-vhosts.conf:
  file.managed:
    - source: <a href="salt://apache/httpd-vhosts.conf" rel="nofollow">salt://apache/httpd-vhosts.conf</a>
</pre>
<dl>
<dt>Using extend with require or watch</p>
<dd>
<p> The <code>extend</code> statement works differently for <code>require</code> or <code>watch</code>. It appends to, rather than replacing the requisite component.</dl>
<h3>Name declaration</h3>
<p> You can override the id-declaration by using a name-declaration. For example, the previous example is a bit more maintainable if rewritten as follows: </p>
<p> <code>apache/mywebsite.sls:</code> </p>
<pre>
include:
  - apache.apache
extend:
  apache:
    service:
      - running
      - watch:
        - file: mywebsite
mywebsite:
  file.managed:
    - name: /etc/httpd/extra/httpd-vhosts.conf
    - source: <a href="salt://apache/httpd-vhosts.conf" rel="nofollow">salt://apache/httpd-vhosts.conf</a>
</pre>
<h3>Names declaration</h3>
<p> Even more powerful is using a names-declaration to override the id-declaration for multiple states at once. This often can remove the need for looping in a template. For example, the first example in this tutorial can be rewritten without the loop: </p>
<pre>
stooges:
  user.present:
    - names:
      - moe
      - larry
      - curly
</pre>
<h3>Next steps</h3>
<p> In <code>part 4</code> we will discuss how to use salt&#8217;s <code>file_roots</code> to set up a workflow in which states can be &quot;promoted&quot; from dev, to QA, to production.</p>
<h3>States tutorial, part 4</h3>
<p> <code>NOTE:</code> This tutorial builds on topics covered in <code>part 1</code>, <code>part 2</code> and <code>part 3</code>. It is recommended that you begin there. </p>
<p> This part of the tutorial will show how to use salt&#8217;s <code>file_roots</code> to set up a workflow in which states can be &quot;promoted&quot; from dev, to QA, to production.</p>
<h3>Salt fileserver path inheritance</h3>
<p> Salt&#8217;s fileserver allows for more than one root directory per environment, like in the below example, which uses both a local directory and a secondary location shared to the salt master via NFS: </p>
<pre>
# In the master config file (/etc/salt/master)
file_roots:
  base:
    - /srv/salt
    - /mnt/salt-nfs/base
</pre>
<p> Salt&#8217;s fileserver collapses the list of root directories into a single virtual environment containing all files from each root. If the same file exists at the same relative path in more than one root, then the top-most match &quot;wins&quot;. For example, if <code>/srv/salt/foo.txt</code> and <code>/mnt/salt-nfs/base/foo.txt</code> both exist, then <code><a href="salt://foo.txt" rel="nofollow noopener" target="_blank">salt://foo.txt</a></code> will point to <code>/srv/salt/foo.txt</code>. </p>
<p> <code>NOTE:</code> When using multiple fileserver backends, the order in which they are listed in the <code>fileserver_backend</code> parameter also matters. If both <code>roots</code> and <code>git</code> backends contain a file with the same relative path, and <code>roots</code> appears before <code>git</code> in the <code>fileserver_backend</code> list, then the file in <code>roots</code> will &quot;win&quot;, and the file in gitfs will be ignored. </p>
<p> A more thorough explanation of how Salt&#8217;s modular fileserver works can be found here. We recommend reading this.</p>
<h3>Environment configuration</h3>
<p> Configure a multiple-environment setup like so: </p>
<pre>
file_roots:
  base:
    - /srv/salt/prod
  qa:
    - /srv/salt/qa
    - /srv/salt/prod
  dev:
    - /srv/salt/dev
    - /srv/salt/qa
    - /srv/salt/prod
</pre>
<p> Given the path inheritance described above, files within <code>/srv/salt/prod</code> would be available in all environments. Files within <code>/srv/salt/qa</code> would be available in both <code>qa</code>, and <code>dev</code>. Finally, the files within <code>/srv/salt/dev</code> would only be available within the <code>dev</code> environment. </p>
<p> Based on the order in which the roots are defined, new files/states can be placed within <code>/srv/salt/dev</code>, and pushed out to the dev hosts for testing. </p>
<p> Those files/states can then be moved to the same relative path within <code>/srv/salt/qa</code>, and they are now available only in the <code>dev</code> and <code>qa</code> environments, allowing them to be pushed to QA hosts and tested. </p>
<p> Finally, if moved to the same relative path within <code>/srv/salt/prod</code>, the files are now available in all three environments.</p>
<h3>Practical Example</h3>
<p> As an example, consider a simple website, installed to <code>/var/www/foobarcom</code>. Below is a top.sls that can be used to deploy the website: </p>
<p> <code>/srv/salt/prod/top.sls:</code> </p>
<pre>
base:
  'web*prod*':
    - webserver.foobarcom
qa:
  'web*qa*':
    - webserver.foobarcom
dev:
  'web*dev*':
    - webserver.foobarcom
</pre>
<p> Using pillar, roles can be assigned to the hosts: </p>
<p> <code>/srv/pillar/top.sls:</code> </p>
<pre>
base:
  'web*prod*':
    - webserver.prod
  'web*qa*':
    - webserver.qa
  'web*dev*':
    - webserver.dev
</pre>
<p> <code>/srv/pillar/webserver/prod.sls:</code> </p>
<pre>
webserver_role: prod
</pre>
<p> <code>/srv/pillar/webserver/qa.sls:</code> </p>
<pre>
webserver_role: qa
</pre>
<p> <code>/srv/pillar/webserver/dev.sls:</code> </p>
<pre>
webserver_role: dev
</pre>
<p> And finally, the SLS to deploy the website: </p>
<p> <code>/srv/salt/prod/webserver/foobarcom.sls:</code> </p>
<p>{<br />
    % if pillar.get(&#8216;webserver_role&#8217;, &#8221;) %<br />
}<br />
/ var / www / foobarcom : file.recurse : -source : salt : // webserver/src/foobarcom<br />
                                                          -env : &#123;&#123;pillar[&#8216;webserver_role&#8217;]}} &#8211;<br />
    user : www &#8211; group : www &#8211; dir_mode : 755 &#8211; file_mode : 644<br />
{<br />
    % endif %<br />
}</p>
<p> Given the above SLS, the source for the website should initially be placed in <code>/srv/salt/dev/webserver/src/foobarcom</code>. </p>
<p> First, let&#8217;s deploy to dev. Given the configuration in the top file, this can be done using <code>state.highstate</code>: </p>
<pre>
salt --pillar 'webserver_role:dev' state.highstate
</pre>
<p> However, in the event that it is not desirable to apply all states configured in the top file (which could be likely in more complex setups), it is possible to apply just the states for the <code>foobarcom</code> website, using <code>state.sls</code>: </p>
<pre>
salt --pillar 'webserver_role:dev' state.sls webserver.foobarcom
</pre>
<p> Once the site has been tested in dev, then the files can be moved from <code>/srv/salt/dev/webserver/src/foobarcom</code> to <code>/srv/salt/qa/webserver/src/foobarcom</code>, and deployed using the following: </p>
<pre>
salt --pillar 'webserver_role:qa' state.sls webserver.foobarcom
</pre>
<p> Finally, once the site has been tested in qa, then the files can be moved from <code>/srv/salt/qa/webserver/src/foobarcom</code> to <code>/srv/salt/prod/webserver/src/foobarcom</code>, and deployed using the following: </p>
<pre>
salt --pillar 'webserver_role:prod' state.sls webserver.foobarcom
</pre>
<p> Thanks to Salt&#8217;s fileserver inheritance, even though the files have been moved to within <code>/srv/salt/prod</code>, they are still available from the same <code>salt://</code> URI in both the qa and dev environments.</p>
<h3>Continue Learning</h3>
<p> The best way to continue learning about Salt States is to read through the <code>reference documentation</code> and to look through examples of existing state trees. Many pre-configured state trees can be found on Github in the <i>saltstack-formulas</i> collection of repositories. </p>
<p> If you have any questions, suggestions, or just want to chat with other people who are using Salt, we have a very active community and we&#8217;d love to hear from you. </p>
<p> In addition, by continuing to <code>part 5</code>, you can learn about the powerful orchestration of which Salt is capable.</p>
<h3>States Tutorial, Part 5 &#8211; Orchestration with Salt</h3>
<p> <code>NOTE:</code> This tutorial builds on some of the topics covered in the earlier <code>States Walkthrough</code> pages. It is recommended to start with <code>Part 1</code> if you are not familiar with how to use states. </p>
<p> Orchestration is accomplished in salt primarily through the <i>Orchestrate Runner</i>. Added in version 0.17.0, this Salt <code>Runner</code> can use the full suite of <code>requisites</code> available in states, and can also execute states/functions using salt-ssh. This runner replaces the <i>OverState</i>.</p>
<h3>The Orchestrate Runner</h3>
<p> New in version 0.17.0. </p>
<p> <code>NOTE:</code> Orchestrate Deprecates OverState </p>
<p> The Orchestrate Runner (originally called the state.sls runner) offers all the functionality of the OverState, but with some advantages:</p>
<dl>
<dt>&bull;</p>
<dd> All <code>requisites</code> available in states can be used.</p>
<dt>&bull;</p>
<dd> The states/functions will also work on salt-ssh minions. </p>
<p> The Orchestrate Runner was added with the intent to eventually deprecate the OverState system, however the OverState will still be maintained until Salt Boron. </p>
<p> The orchestrate runner generalizes the Salt state system to a Salt master context. Whereas the <code>state.sls</code>, <code>state.highstate</code>, et al functions are concurrently and independently executed on each Salt minion, the <code>state.orchestrate</code> runner is executed on the master, giving it a master-level view and control over requisites, such as state ordering and conditionals. This allows for inter minion requisites, like ordering the application of states on different minions that must not happen simultaneously, or for halting the state run on all minions if a minion fails one of its states. </p>
<p> If you want to setup a load balancer in front of a cluster of web servers, for example, you can ensure the load balancer is setup before the web servers or stop the state run altogether if one of the minions does not set up correctly. </p>
<p> The <code>state.sls</code>, <code>state.highstate</code>, et al functions allow you to statefully manage each minion and the <code>state.orchestrate</code> runner allows you to statefully manage your entire infrastructure.</dl>
<h3>Executing the Orchestrate Runner</h3>
<p> The Orchestrate Runner command format is the same as for the <code>state.sls</code> function, except that since it is a runner, it is executed with <code>salt-run</code> rather than <code>salt</code>. Assuming you have a state.sls file called <code>/srv/salt/orch/webserver.sls</code> the following command run on the master will apply the states defined in that file. </p>
<pre>
salt-run state.orchestrate orch.webserver
</pre>
<p> <code>NOTE:</code> <code>state.orch</code> is a synonym for <code>state.orchestrate</code> </p>
<p> Changed in version 2014.1.1: The runner function was renamed to <code>state.orchestrate</code> to avoid confusion with the <code>state.sls</code> execution function. In versions 0.17.0 through 2014.1.0, <code>state.sls</code> must be used. </p>
<h3>Examples</h3>
<h3>Function</h3>
<p> To execute a function, use <code>salt.function</code>: </p>
<pre>
# /srv/salt/orch/cleanfoo.sls
cmd.run:
  salt.function:
    - tgt: '*'
    - arg:
      - rm -rf /tmp/foo
</pre>
<pre>
salt-run state.orchestrate orch.cleanfoo
</pre>
<h3>State</h3>
<p> To execute a state, use <code>salt.state</code>. </p>
<pre>
# /srv/salt/orch/webserver.sls
install_nginx:
  salt.state:
    - tgt: 'web*'
    - sls:
      - nginx
</pre>
<pre>
salt-run state.orchestrate orch.webserver
</pre>
<h3>Highstate</h3>
<p> To run a highstate, set <code>highstate: True</code> in your state config: </p>
<pre>
# /srv/salt/orch/web_setup.sls
webserver_setup:
  salt.state:
    - tgt: 'web*'
    - highstate: True
</pre>
<pre>
salt-run state.orchestrate orch.web_setup
</pre>
<h3>More Complex Orchestration</h3>
<p> Many states/functions can be configured in a single file, which when combined with the full suite of <code>requisites</code>, can be used to easily configure complex orchestration tasks. Additionally, the states/functions will be executed in the order in which they are defined, unless prevented from doing so by any <code>requisites</code>, as is the default in SLS files since 0.17.0. </p>
<pre>
cmd.run:
  salt.function:
    - tgt: 10.0.0.0/24
    - tgt_type: ipcidr
    - arg:
      - bootstrap
storage_setup:
  salt.state:
    - tgt: 'role:storage'
    - tgt_type: grain
    - sls: ceph
    - require:
      - salt: webserver_setup
webserver_setup:
  salt.state:
    - tgt: 'web*'
    - highstate: True
</pre>
<p> Given the above setup, the orchestration will be carried out as follows:</p>
<dl>
<dt>1.</p>
<dd> The shell command <code>bootstrap</code> will be executed on all minions in the 10.0.0.0/24 subnet.</p>
<dt>2.</p>
<dd> A Highstate will be run on all minions whose ID starts with &quot;web&quot;, since the <code>storage_setup</code> state requires it.</p>
<dt>3.</p>
<dd> Finally, the <code>ceph</code> SLS target will be executed on all minions which have a grain called <code>role</code> with a value of <code>storage</code>.</dl>
<h3>The OverState System</h3>
<p> <code>WARNING:</code> The OverState runner is deprecated, and will be removed in the feature release of Salt codenamed Boron. (Three feature releases after 2014.7.0, which is codenamed Helium) </p>
<p> Often, servers need to be set up and configured in a specific order, and systems should only be set up if systems earlier in the sequence have been set up without any issues. </p>
<p> The OverState system can be used to orchestrate deployment in a smooth and reliable way across multiple systems in small to large environments.</p>
<h3>The OverState SLS</h3>
<p> The OverState system is managed by an SLS file named <code>overstate.sls</code>, located in the root of a Salt fileserver environment. </p>
<p> The overstate.sls configures an unordered list of stages, each stage defines the minions on which to execute the state, and can define what sls files to run, execute a <code>state.highstate</code>, or execute a function. Here&#8217;s a sample <code>overstate.sls</code>: </p>
<pre>
mysql:
  match: 'db*'
  sls:
    - mysql.server
    - drbd
webservers:
  match: 'web*'
  require:
    - mysql
all:
  match: '*'
  require:
    - mysql
    - webservers
</pre>
<p> <code>NOTE:</code> The <code>match</code> argument uses compound matching </p>
<p> Given the above setup, the OverState will be carried out as follows:</p>
<dl>
<dt>1.</p>
<dd> The <code>mysql</code> stage will be executed first because it is required by the <code>webservers</code> and <code>all</code> stages. It will execute <code>state.sls</code> once for each of the two listed SLS targets (<code>mysql.server</code> and <code>drbd</code>). These states will be executed on all minions whose minion ID starts with &quot;db&quot;.</p>
<dt>2.</p>
<dd> The <code>webservers</code> stage will then be executed, but only if the <code>mysql</code> stage executes without any failures. The <code>webservers</code> stage will execute a <code>state.highstate</code> on all minions whose minion IDs start with &quot;web&quot;.</p>
<dt>3.</p>
<dd> Finally, the <code>all</code> stage will execute, running <code>state.highstate</code> on all systems, if, and only if the <code>mysql</code> and <code>webservers</code> stages completed without any failures. </p>
<p> Any failure in the above steps would cause the requires to fail, preventing the dependent stages from executing.</dl>
<h3>Using Functions with OverState</h3>
<p> In the above example, you&#8217;ll notice that the stages lacking an <code>sls</code> entry run a <code>state.highstate</code>. As mentioned earlier, it is also possible to execute other functions in a stage. This functionality was added in version 0.15.0. </p>
<p> Running a function is easy: </p>
<pre>
http:
  function:
    pkg.install:
      - httpd
</pre>
<p> The list of function arguments are defined after the declared function. So, the above stage would run <code>pkg.install http</code>. Requisites only function properly if the given function supports returning a custom return code.</p>
<h3>Executing an OverState</h3>
<p> Since the OverState is a <code>Runner</code>, it is executed using the <code>salt-run</code> command. The runner function for the OverState is <code>state.over</code>. </p>
<pre>
salt-run state.over
</pre>
<p> The function will by default look in the root of the <code>base</code> environment (as defined in <code>file_roots</code>) for a file called <code>overstate.sls</code>, and then execute the stages defined within that file. </p>
<p> Different environments and paths can be used as well, by adding them as positional arguments: </p>
<pre>
salt-run state.over dev /root/other-overstate.sls
</pre>
<p> The above would run an OverState using the <code>dev</code> fileserver environment, with the stages defined in <code>/root/other-overstate.sls</code>. </p>
<p> <code>WARNING:</code> Since these are positional arguments, when defining the path to the overstate file the environment must also be specified, even if it is the <code>base</code> environment. </p>
<p> <code>NOTE:</code> Remember, salt-run is always executed on the master.</p>
<h3>Syslog-ng usage</h3>
<h3>Overview</h3>
<p> Syslog_ng state module is for generating syslog-ng configurations. You can do the following things:</p>
<dl>
<dt>&bull;</p>
<dd> generate syslog-ng configuration from YAML,</p>
<dt>&bull;</p>
<dd> use non-YAML configuration,</p>
<dt>&bull;</p>
<dd> start, stop or reload syslog-ng. </p>
<p> There is also an execution module, which can check the syntax of the configuration, get the version and other information about syslog-ng.</dl>
<h3>Configuration</h3>
<p> Users can create syslog-ng configuration statements with the <code>syslog_ng.config</code> function. It requires a <i>name</i> and a <i>config</i> parameter. The <i>name</i> parameter determines the name of the generated statement and the <i>config</i> parameter holds a parsed YAML structure. </p>
<p> A statement can be declared in the following forms (both are equivalent): </p>
<pre>
source.s_localhost:
  syslog_ng.config:
    - config:
        - tcp:
          - ip: &quot;127.0.0.1&quot;
          - port: 1233
</pre>
<pre>
s_localhost:
  syslog_ng.config:
    - config:
        source:
          - tcp:
            - ip: &quot;127.0.0.1&quot;
            - port: 1233
</pre>
<p> The first one is called short form, because it needs less typing. Users can use lists and dictionaries to specify their configuration. The format is quite self describing and there are more examples [at the end](#examples) of this document.</p>
<h3>Quotation</h3>
<dl>
<dt><code>The quotation can be tricky sometimes but here are some rules to follow:</code></p>
<dd>
<dt>&bull;</p>
<dd> when a string meant to be <code>&quot;string&quot;</code> in the generated configuration, it should be like <code>&#8216;&quot;string&quot;&#8217;</code> in the YAML document</p>
<dt>&bull;</p>
<dd> similarly, users should write <code>&quot;&#8217;string&#8217;&quot;</code> to get <code>&#8216;string&#8217;</code> in the generated configuration</dl>
<h3>Full example</h3>
<p> The following configuration is an example, how a complete syslog-ng configuration looks like: </p>
<pre>
# Set the location of the configuration file
set_location:
  module.run:
    - name: syslog_ng.set_config_file
    - m_name: &quot;/home/tibi/install/syslog-ng/etc/syslog-ng.conf&quot;
# The syslog-ng and syslog-ng-ctl binaries are here. You needn't use
# this method if these binaries can be found in a directory in your PATH.
set_bin_path:
  module.run:
    - name: syslog_ng.set_binary_path
    - m_name: &quot;/home/tibi/install/syslog-ng/sbin&quot;
# Writes the first lines into the config file, also erases its previous
# content
write_version:
  module.run:
    - name: syslog_ng.write_version
    - m_name: &quot;3.6&quot;
# There is a shorter form to set the above variables
set_variables:
  module.run:
    - name: syslog_ng.set_parameters
    - version: &quot;3.6&quot;
    - binary_path: &quot;/home/tibi/install/syslog-ng/sbin&quot;
    - config_file: &quot;/home/tibi/install/syslog-ng/etc/syslog-ng.conf&quot;
# Some global options
options.global_options:
  syslog_ng.config:
    - config:
        - time_reap: 30
        - mark_freq: 10
        - keep_hostname: &quot;yes&quot;
source.s_localhost:
  syslog_ng.config:
    - config:
        - tcp:
          - ip: &quot;127.0.0.1&quot;
          - port: 1233
destination.d_log_server:
  syslog_ng.config:
    - config:
        - tcp:
          - &quot;127.0.0.1&quot;
          - port: 1234
log.l_log_to_central_server:
  syslog_ng.config:
    - config:
        - source: s_localhost
        - destination: d_log_server
some_comment:
  module.run:
    - name: syslog_ng.write_config
    - config: |
        # Multi line
        # comment
# An other mode to use comments or existing configuration snippets
config.other_comment_form:
  syslog_ng.config:
    - config: |
        # Multi line
        # comment
</pre>
<p> The <code>syslog_ng.reloaded</code> function can generate syslog-ng configuration from YAML. If the statement (source, destination, parser, etc.) has a name, this function uses the id as the name, otherwise (log statement) it&#8217;s purpose is like a mandatory comment. </p>
<p> After execution this example the syslog_ng state will generate this file: </p>
<p>#Generated by Salt on 2014 &#8211; 08 &#8211; 18 00 : 11 : 11<br />
@version : 3.6 options<br />
{<br />
    time_reap(<br />
        30);<br />
    mark_freq(<br />
        10);<br />
    keep_hostname(<br />
        yes);<br />
};<br />
source s_localhost<br />
{<br />
    tcp(<br />
        ip(<br />
            127.0.0.1),<br />
        port(<br />
            1233));<br />
};<br />
destination d_log_server<br />
{<br />
    tcp(<br />
        127.0.0.1,<br />
        port(<br />
            1234));<br />
};<br />
log<br />
{<br />
    source(<br />
        s_localhost);<br />
    destination(<br />
        d_log_server);<br />
};<br />
#Multi line<br />
#comment<br />
#Multi line<br />
#comment</p>
<p> Users can include arbitrary texts in the generated configuration with using the <code>config</code> statement (see the example above).</p>
<h3>Syslog_ng module functions</h3>
<p> You can use <code>syslog_ng.set_binary_path</code> to set the directory which contains the syslog-ng and syslog-ng-ctl binaries. If this directory is in your PATH, you don&#8217;t need to use this function. There is also a <code>syslog_ng.set_config_file</code> function to set the location of the configuration file.</p>
<h3>Examples</h3>
<h3>Simple source</h3>
<p>source s_tail<br />
{<br />
    file(<br />
        &#8220;/var/log/apache/access.log&#8221;,<br />
        follow_freq(1),<br />
        flags(no &#8211; parse, validate &#8211; utf8));<br />
};</p>
<pre>
s_tail:
  # Salt will call the source function of syslog_ng module
  syslog_ng.config:
    - config:
        source:
          - file:
            - file: ''&quot;/var/log/apache/access.log&quot;''
            - follow_freq : 1
            - flags:
              - no-parse
              - validate-utf8
</pre>
<p> OR </p>
<pre>
s_tail:
  syslog_ng.config:
    - config:
        source:
            - file:
              - ''&quot;/var/log/apache/access.log&quot;''
              - follow_freq : 1
              - flags:
                - no-parse
                - validate-utf8
</pre>
<p> OR </p>
<pre>
source.s_tail:
  syslog_ng.config:
    - config:
        - file:
          - ''&quot;/var/log/apache/access.log&quot;''
          - follow_freq : 1
          - flags:
            - no-parse
            - validate-utf8
</pre>
<h3>Complex source</h3>
<p>source s_gsoc2014<br />
{<br />
    tcp(<br />
        ip(&#8220;0.0.0.0&#8221;),<br />
        port(1234),<br />
        flags(no &#8211; parse));<br />
};</p>
<pre>
s_gsoc2014:
  syslog_ng.config:
    - config:
        source:
          - tcp:
            - ip: 0.0.0.0
            - port: 1234
            - flags: no-parse
</pre>
<h3>Filter</h3>
<p>filter f_json<br />
{<br />
    match(<br />
        &#8220;@json:&#8221;);<br />
};</p>
<pre>
f_json:
  syslog_ng.config:
    - config:
        filter:
          - match:
            - ''&quot;@json:&quot;''
</pre>
<h3>Template</h3>
<p>template t_demo_filetemplate<br />
{<br />
    template(<br />
        &#8220;$ISODATE $HOST $MSG &#8220;);<br />
    template_escape(<br />
        no);<br />
};</p>
<pre>
t_demo_filetemplate:
  syslog_ng.config:
    -config:
        template:
          - template:
            - '&quot;$ISODATE $HOST $MSG\n&quot;'
          - template_escape:
            - &quot;no&quot;
</pre>
<h3>Rewrite</h3>
<p>rewrite r_set_message_to_MESSAGE<br />
{<br />
    set(<br />
        &#8220;${.json.message}&#8221;,<br />
        value(&#8220;$MESSAGE&#8221;));<br />
};</p>
<pre>
r_set_message_to_MESSAGE:
  syslog_ng.config:
    - config:
        rewrite:
          - set:
            - '&quot;${.json.message}&quot;'
            - value : '&quot;$MESSAGE&quot;'
</pre>
<h3>Global options</h3>
<p>options<br />
{<br />
    time_reap(30);<br />
    mark_freq(10);<br />
    keep_hostname(yes);<br />
};</p>
<pre>
global_options:
  syslog_ng.config:
    - config:
        options:
          - time_reap: 30
          - mark_freq: 10
          - keep_hostname: &quot;yes&quot;
</pre>
<h3>Log</h3>
<p>log<br />
{<br />
    source(s_gsoc2014);<br />
    junction<br />
    {<br />
        channel<br />
        {<br />
            filter(f_json);<br />
            parser(p_json);<br />
            rewrite(r_set_json_tag);<br />
            rewrite(r_set_message_to_MESSAGE);<br />
            destination<br />
            {<br />
                file(<br />
                    &#8220;/tmp/json-input.log&#8221;,<br />
                    template(t_gsoc2014));<br />
            };<br />
            flags(final);<br />
        };<br />
        channel<br />
        {<br />
            filter(f_not_json);<br />
            parser<br />
            {<br />
                syslog &#8211; parser();<br />
            };<br />
            rewrite(r_set_syslog_tag);<br />
            flags(final);<br />
        };<br />
    };<br />
    destination<br />
    {<br />
        file(<br />
            &#8220;/tmp/all.log&#8221;,<br />
            template(t_gsoc2014));<br />
    };<br />
};</p>
<pre>
l_gsoc2014:
  syslog_ng.config:
    - config:
        log:
          - source: s_gsoc2014
          - junction:
            - channel:
              - filter: f_json
              - parser: p_json
              - rewrite: r_set_json_tag
              - rewrite: r_set_message_to_MESSAGE
              - destination:
                - file:
                  - '&quot;/tmp/json-input.log&quot;'
                  - template: t_gsoc2014
              - flags: final
            - channel:
              - filter: f_not_json
              - parser:
                - syslog-parser: []
              - rewrite: r_set_syslog_tag
              - flags: final
          - destination:
            - file:
              - &quot;/tmp/all.log&quot;
              - template: t_gsoc2014
</pre>
<h3>Advanced Topics</h3>
<h3>SaltStack Walk-through</h3>
<p> <code>NOTE:</code> Welcome to SaltStack! I am excited that you are interested in Salt and starting down the path to better infrastructure management. I developed (and am continuing to develop) Salt with the goal of making the best software available to manage computers of almost any kind. I hope you enjoy working with Salt and that the software can solve your real world needs!</p>
<dl>
<dt>&bull;</p>
<dd> Thomas S Hatch</p>
<dt>&bull;</p>
<dd> Salt creator and Chief Developer</p>
<dt>&bull;</p>
<dd> CTO of SaltStack, Inc.</dl>
<h3>Getting Started</h3>
<h3>What is Salt?</h3>
<p> Salt is a different approach to infrastructure management, founded on the idea that high-speed communication with large numbers of systems can open up new capabilities. This approach makes Salt a powerful multitasking system that can solve many specific problems in an infrastructure. </p>
<p> The backbone of Salt is the remote execution engine, which creates a high-speed, secure and bi-directional communication net for groups of systems. On top of this communication system, Salt provides an extremely fast, flexible, and easy-to-use configuration management system called <code>Salt States</code>.</p>
<h3>Installing Salt</h3>
<p> SaltStack has been made to be very easy to install and get started. The <code>installation documents</code> contain instructions for all supported platforms.</p>
<h3>Starting Salt</h3>
<p> Salt functions on a master/minion topology. A master server acts as a central control bus for the clients, which are called <code>minions</code>. The minions connect back to the master.</p>
<h3>Setting Up the Salt Master</h3>
<p> Turning on the Salt Master is easy &#8212; just turn it on! The default configuration is suitable for the vast majority of installations. The Salt Master can be controlled by the local Linux/Unix service manager: </p>
<p> On Systemd based platforms (OpenSuse, Fedora): </p>
<pre>
systemctl start salt-master
</pre>
<p> On Upstart based systems (Ubuntu, older Fedora/RHEL): </p>
<pre>
service salt-master start
</pre>
<p> On SysV Init systems (Debian, Gentoo etc.): </p>
<pre>
/etc/init.d/salt-master start
</pre>
<p> Alternatively, the Master can be started directly on the command-line: </p>
<pre>
salt-master -d
</pre>
<p> The Salt Master can also be started in the foreground in debug mode, thus greatly increasing the command output: </p>
<pre>
salt-master -l debug
</pre>
<p> The Salt Master needs to bind to two TCP network ports on the system. These ports are <code>4505</code> and <code>4506</code>. For more in depth information on firewalling these ports, the firewall tutorial is available <code>here</code>.</p>
<h3>Setting up a Salt Minion</h3>
<p> <code>NOTE:</code> The Salt Minion can operate with or without a Salt Master. This walk-through assumes that the minion will be connected to the master, for information on how to run a master-less minion please see the master-less quick-start guide: </p>
<p> <code>Masterless Minion Quickstart</code> </p>
<p> The Salt Minion only needs to be aware of one piece of information to run, the network location of the master. </p>
<p> By default the minion will look for the DNS name <code>salt</code> for the master, making the easiest approach to set internal DNS to resolve the name <code>salt</code> back to the Salt Master IP. </p>
<p> Otherwise, the minion configuration file will need to be edited so that the configuration option <code>master</code> points to the DNS name or the IP of the Salt Master: </p>
<p> <code>NOTE:</code> The default location of the configuration files is <code>/etc/salt</code>. Most platforms adhere to this convention, but platforms such as FreeBSD and Microsoft Windows place this file in different locations. </p>
<p> <code>/etc/salt/minion:</code> </p>
<pre>
master: saltmaster.example.com
</pre>
<p> Now that the master can be found, start the minion in the same way as the master; with the platform init system or via the command line directly: </p>
<p> As a daemon: </p>
<pre>
salt-minion -d
</pre>
<p> In the foreground in debug mode: </p>
<pre>
salt-minion -l debug
</pre>
<p> When the minion is started, it will generate an <code>id</code> value, unless it has been generated on a previous run and cached in the configuration directory, which is <code>/etc/salt</code> by default. This is the name by which the minion will attempt to authenticate to the master. The following steps are attempted, in order to try to find a value that is not <code>localhost</code>:</p>
<dl>
<dt>1.</p>
<dd> The Python function <code>socket.getfqdn()</code> is run</p>
<dt>2.</p>
<dd> <code>/etc/hostname</code> is checked (non-Windows only)</p>
<dt>3.</p>
<dd> <code>/etc/hosts</code> (<code>%WINDIR%\system32\drivers\etc\hosts</code> on Windows hosts) is checked for hostnames that map to anything within <code>127.0.0.0/8</code>. </p>
<p> If none of the above are able to produce an id which is not <code>localhost</code>, then a sorted list of IP addresses on the minion (excluding any within <code>127.0.0.0/8</code>) is inspected. The first publicly-routable IP address is used, if there is one. Otherwise, the first privately-routable IP address is used. </p>
<p> If all else fails, then <code>localhost</code> is used as a fallback. </p>
<p> <code>NOTE:</code> Overriding the <code>id</code> </p>
<p> The minion id can be manually specified using the <code>id</code> parameter in the minion config file. If this configuration value is specified, it will override all other sources for the <code>id</code>. </p>
<p> Now that the minion is started, it will generate cryptographic keys and attempt to connect to the master. The next step is to venture back to the master server and accept the new minion&#8217;s public key.</dl>
<h3>Using salt-key</h3>
<p> Salt authenticates minions using public-key encryption and authentication. For a minion to start accepting commands from the master, the minion keys need to be accepted by the master. </p>
<p> The <code>salt-key</code> command is used to manage all of the keys on the master. To list the keys that are on the master: </p>
<pre>
salt-key -L
</pre>
<p> The keys that have been rejected, accepted, and pending acceptance are listed. The easiest way to accept the minion key is to accept all pending keys: </p>
<pre>
salt-key -A
</pre>
<p> <code>NOTE:</code> Keys should be verified! Print the master key fingerprint by running <code>salt-key -F master</code> on the Salt master. Copy the <code>master.pub</code> fingerprint from the Local Keys section, and then set this value as the <code>master_finger</code> in the minion configuration file. Restart the Salt minion. </p>
<p> On the master, run <code>salt-key -f minion-id</code> to print the fingerprint of the minion&#8217;s public key that was received by the master. On the minion, run <code>salt-call key.finger &#8211;local</code> to print the fingerprint of the minion key. </p>
<p> On the master: </p>
<pre>
# salt-key -f foo.domain.com
Unaccepted Keys:
foo.domain.com:  39:f9:e4:8a:aa:74:8d:52:1a:ec:92:03:82:09:c8:f9
</pre>
<p> On the minion: </p>
<pre>
# salt-call key.finger --local
local:
    39:f9:e4:8a:aa:74:8d:52:1a:ec:92:03:82:09:c8:f9
</pre>
<p> If they match, approve the key with <code>salt-key -a foo.domain.com</code>.</p>
<h3>Sending the First Commands</h3>
<p> Now that the minion is connected to the master and authenticated, the master can start to command the minion. </p>
<p> Salt commands allow for a vast set of functions to be executed and for specific minions and groups of minions to be targeted for execution. </p>
<p> The <code>salt</code> command is comprised of command options, target specification, the function to execute, and arguments to the function. </p>
<p> A simple command to start with looks like this: </p>
<pre>
salt '*' test.ping
</pre>
<p> The <code>*</code> is the target, which specifies all minions. </p>
<p> <code>test.ping</code> tells the minion to run the <code>test.ping</code> function. </p>
<p> In the case of <code>test.ping</code>, <code>test</code> refers to a <code>execution module</code>. <code>ping</code> refers to the <code>ping</code> function contained in the aforementioned <code>test</code> module. </p>
<p> <code>NOTE:</code> Execution modules are the workhorses of Salt. They do the work on the system to perform various tasks, such as manipulating files and restarting services. </p>
<p> The result of running this command will be the master instructing all of the minions to execute <code>test.ping</code> in parallel and return the result. </p>
<p> This is not an actual ICMP ping, but rather a simple function which returns <code>True</code>. Using <code>test.ping</code> is a good way of confirming that a minion is connected. </p>
<p> <code>NOTE:</code> Each minion registers itself with a unique minion ID. This ID defaults to the minion&#8217;s hostname, but can be explicitly defined in the minion config as well by using the <code>id</code> parameter. </p>
<p> Of course, there are hundreds of other modules that can be called just as <code>test.ping</code> can. For example, the following would return disk usage on all targeted minions: </p>
<pre>
salt '*' disk.usage
</pre>
<h3>Getting to Know the Functions</h3>
<p> Salt comes with a vast library of functions available for execution, and Salt functions are self-documenting. To see what functions are available on the minions execute the <code>sys.doc</code> function: </p>
<pre>
salt '*' sys.doc
</pre>
<p> This will display a very large list of available functions and documentation on them. </p>
<p> <code>NOTE:</code> Module documentation is also available <code>on the web</code>. </p>
<p> These functions cover everything from shelling out to package management to manipulating database servers. They comprise a powerful system management API which is the backbone to Salt configuration management and many other aspects of Salt. </p>
<p> <code>NOTE:</code> Salt comes with many plugin systems. The functions that are available via the <code>salt</code> command are called <code>Execution Modules</code>.</p>
<h3>Helpful Functions to Know</h3>
<p> The <code>cmd</code> module contains functions to shell out on minions, such as <code>cmd.run</code> and <code>cmd.run_all</code>: </p>
<pre>
salt '*' cmd.run 'ls -l /etc'
</pre>
<p> The <code>pkg</code> functions automatically map local system package managers to the same salt functions. This means that <code>pkg.install</code> will install packages via <code>yum</code> on Red Hat based systems, <code>apt</code> on Debian systems, etc.: </p>
<pre>
salt '*' pkg.install vim
</pre>
<p> <code>NOTE:</code> Some custom Linux spins and derivatives of other distributions are not properly detected by Salt. If the above command returns an error message saying that <code>pkg.install</code> is not available, then you may need to override the pkg provider. This process is explained <code>here</code>. </p>
<p> The <code>network.interfaces</code> function will list all interfaces on a minion, along with their IP addresses, netmasks, MAC addresses, etc: </p>
<pre>
salt '*' network.interfaces
</pre>
<h3>Changing the Output Format</h3>
<p> The default output format used for most Salt commands is called the <code>nested</code> outputter, but there are several other outputters that can be used to change the way the output is displayed. For instance, the <code>pprint</code> outputter can be used to display the return data using Python&#8217;s <code>pprint</code> module: </p>
<p>root[at] saltmaster : ~#salt myminion grains.item pythonpath&#8211; out = pprint<br />
{<br />
    &#8216;myminion&#8217;:<br />
    {<br />
        &#8216;pythonpath&#8217; : [ &#8216;/usr/lib64/python2.7&#8217;,<br />
                         &#8216;/usr/lib/python2.7/plat-linux2&#8217;,<br />
                         &#8216;/usr/lib64/python2.7/lib-tk&#8217;,<br />
                         &#8216;/usr/lib/python2.7/lib-tk&#8217;,<br />
                         &#8216;/usr/lib/python2.7/site-packages&#8217;,<br />
                         &#8216;/usr/lib/python2.7/site-packages/gst-0.10&#8217;,<br />
                         &#8216;/usr/lib/python2.7/site-packages/gtk-2.0&#8217; ]<br />
    }<br />
}</p>
<p> The full list of Salt outputters, as well as example output, can be found here.</p>
<h3><code>salt-call</code></h3>
<p> The examples so far have described running commands from the Master using the <code>salt</code> command, but when troubleshooting it can be more beneficial to login to the minion directly and use <code>salt-call</code>. </p>
<p> Doing so allows you to see the minion log messages specific to the command you are running (which are <i>not</i> part of the return data you see when running the command from the Master using <code>salt</code>), making it unnecessary to tail the minion log. More information on <code>salt-call</code> and how to use it can be found here.</p>
<h3>Grains</h3>
<p> Salt uses a system called <code>Grains</code> to build up static data about minions. This data includes information about the operating system that is running, CPU architecture and much more. The grains system is used throughout Salt to deliver platform data to many components and to users. </p>
<p> Grains can also be statically set, this makes it easy to assign values to minions for grouping and managing. </p>
<p> A common practice is to assign grains to minions to specify what the role or roles a minion might be. These static grains can be set in the minion configuration file or via the <code>grains.setval</code> function.</p>
<h3>Targeting</h3>
<p> Salt allows for minions to be targeted based on a wide range of criteria. The default targeting system uses globular expressions to match minions, hence if there are minions named <code>larry1</code>, <code>larry2</code>, <code>curly1</code>, and <code>curly2</code>, a glob of <code>larry*</code> will match <code>larry1</code> and <code>larry2</code>, and a glob of <code>*1</code> will match <code>larry1</code> and <code>curly1</code>. </p>
<p> Many other targeting systems can be used other than globs, these systems include:</p>
<dl>
<dt><code>Regular Expressions</code></p>
<dd> Target using PCRE-compliant regular expressions</p>
<dt><code>Grains</code></p>
<dd> Target based on grains data: <code>Targeting with Grains</code></p>
<dt><code>Pillar</code></p>
<dd> Target based on pillar data: <code>Targeting with Pillar</code></p>
<dt><code>IP</code></p>
<dd> Target based on IP address/subnet/range</p>
<dt><code>Compound</code></p>
<dd> Create logic to target based on multiple targets: <code>Targeting with Compound</code></p>
<dt><code>Nodegroup</code></p>
<dd> Target with nodegroups: <code>Targeting with Nodegroup</code> </p>
<p> The concepts of targets are used on the command line with Salt, but also function in many other areas as well, including the state system and the systems used for ACLs and user permissions.</dl>
<h3>Passing in Arguments</h3>
<p> Many of the functions available accept arguments which can be passed in on the command line: </p>
<pre>
salt '*' pkg.install vim
</pre>
<p> This example passes the argument <code>vim</code> to the pkg.install function. Since many functions can accept more complex input then just a string, the arguments are parsed through YAML, allowing for more complex data to be sent on the command line: </p>
<pre>
salt '*' test.echo 'foo: bar'
</pre>
<p> In this case Salt translates the string &#8216;foo: bar&#8217; into the dictionary &quot;{&#8216;foo&#8217;: &#8216;bar&#8217;}&quot; </p>
<p> <code>NOTE:</code> Any line that contains a newline will not be parsed by YAML.</p>
<h3>Salt States</h3>
<p> Now that the basics are covered the time has come to evaluate <code>States</code>. Salt <code>States</code>, or the <code>State System</code> is the component of Salt made for configuration management. </p>
<p> The state system is already available with a basic Salt setup, no additional configuration is required. States can be set up immediately. </p>
<p> <code>NOTE:</code> Before diving into the state system, a brief overview of how states are constructed will make many of the concepts clearer. Salt states are based on data modeling and build on a low level data structure that is used to execute each state function. Then more logical layers are built on top of each other. </p>
<p> The high layers of the state system which this tutorial will cover consists of everything that needs to be known to use states, the two high layers covered here are the <i>sls</i> layer and the highest layer <i>highstate</i>. </p>
<p> Understanding the layers of data management in the State System will help with understanding states, but they never need to be used. Just as understanding how a compiler functions assists when learning a programming language, understanding what is going on under the hood of a configuration management system will also prove to be a valuable asset.</p>
<h3>The First SLS Formula</h3>
<p> The state system is built on SLS formulas. These formulas are built out in files on Salt&#8217;s file server. To make a very basic SLS formula open up a file under /srv/salt named vim.sls. The following state ensures that vim is installed on a system to which that state has been applied. </p>
<p> <code>/srv/salt/vim.sls:</code> </p>
<pre>
vim:
  pkg.installed
</pre>
<p> Now install vim on the minions by calling the SLS directly: </p>
<pre>
salt '*' state.sls vim
</pre>
<p> This command will invoke the state system and run the <code>vim</code> SLS. </p>
<p> Now, to beef up the vim SLS formula, a <code>vimrc</code> can be added: </p>
<p> <code>/srv/salt/vim.sls:</code> </p>
<pre>
vim:
  pkg.installed: []
/etc/vimrc:
  file.managed:
    - source: <a href="salt://vimrc" rel="nofollow">salt://vimrc</a>
    - mode: 644
    - user: root
    - group: root
</pre>
<p> Now the desired <code>vimrc</code> needs to be copied into the Salt file server to <code>/srv/salt/vimrc</code>. In Salt, everything is a file, so no path redirection needs to be accounted for. The <code>vimrc</code> file is placed right next to the <code>vim.sls</code> file. The same command as above can be executed to all the vim SLS formulas and now include managing the file. </p>
<p> <code>NOTE:</code> Salt does not need to be restarted/reloaded or have the master manipulated in any way when changing SLS formulas. They are instantly available.</p>
<h3>Adding Some Depth</h3>
<p> Obviously maintaining SLS formulas right in a single directory at the root of the file server will not scale out to reasonably sized deployments. This is why more depth is required. Start by making an nginx formula a better way, make an nginx subdirectory and add an init.sls file: </p>
<p> <code>/srv/salt/nginx/init.sls:</code> </p>
<pre>
nginx:
  pkg.installed: []
  service.running:
    - require:
      - pkg: nginx
</pre>
<p> A few concepts are introduced in this SLS formula. </p>
<p> First is the service statement which ensures that the <code>nginx</code> service is running. </p>
<p> Of course, the nginx service can&#8217;t be started unless the package is installed &#8212; hence the <code>require</code> statement which sets up a dependency between the two. </p>
<p> The <code>require</code> statement makes sure that the required component is executed before and that it results in success. </p>
<p> <code>NOTE:</code> The <i>require</i> option belongs to a family of options called <i>requisites</i>. Requisites are a powerful component of Salt States, for more information on how requisites work and what is available see: <code>Requisites</code> </p>
<p> Also evaluation ordering is available in Salt as well: <code>Ordering States</code> </p>
<p> This new sls formula has a special name &#8212; <code>init.sls</code>. When an SLS formula is named <code>init.sls</code> it inherits the name of the directory path that contains it. This formula can be referenced via the following command: </p>
<pre>
salt '*' state.sls nginx
</pre>
<p> <code>NOTE:</code> Reminder! </p>
<p> Just as one could call the <code>test.ping</code> or <code>disk.usage</code> execution modules, <code>state.sls</code> is simply another execution module. It simply takes the name of an SLS file as an argument. </p>
<p> Now that subdirectories can be used, the <code>vim.sls</code> formula can be cleaned up. To make things more flexible, move the <code>vim.sls</code> and vimrc into a new subdirectory called <code>edit</code> and change the <code>vim.sls</code> file to reflect the change: </p>
<p> <code>/srv/salt/edit/vim.sls:</code> </p>
<pre>
vim:
  pkg.installed
/etc/vimrc:
  file.managed:
    - source: <a href="salt://edit/vimrc" rel="nofollow">salt://edit/vimrc</a>
    - mode: 644
    - user: root
    - group: root
</pre>
<p> Only the source path to the vimrc file has changed. Now the formula is referenced as <code>edit.vim</code> because it resides in the edit subdirectory. Now the edit subdirectory can contain formulas for emacs, nano, joe or any other editor that may need to be deployed.</p>
<h3>Next Reading</h3>
<p> Two walk-throughs are specifically recommended at this point. First, a deeper run through States, followed by an explanation of Pillar.</p>
<dl>
<dt>1.</p>
<dd> <code>Starting States</code></p>
<dt>2.</p>
<dd> <code>Pillar Walkthrough</code> </p>
<p> An understanding of Pillar is extremely helpful in using States.</dl>
<h3>Getting Deeper Into States</h3>
<p> Two more in-depth States tutorials exist, which delve much more deeply into States functionality.</p>
<dl>
<dt>1.</p>
<dd> <code>How Do I Use Salt States?</code>, covers much more to get off the ground with States.</p>
<dt>2.</p>
<dd> The <code>States Tutorial</code> also provides a fantastic introduction. </p>
<p> These tutorials include much more in-depth information including templating SLS formulas etc.</dl>
<h3>So Much More!</h3>
<p> This concludes the initial Salt walk-through, but there are many more things still to learn! These documents will cover important core aspects of Salt:</p>
<dl>
<dt>&bull;</p>
<dd> <code>Pillar</code></p>
<dt>&bull;</p>
<dd> <code>Job Management</code> </p>
<p> A few more tutorials are also available:</p>
<dt>&bull;</p>
<dd> <code>Remote Execution Tutorial</code></p>
<dt>&bull;</p>
<dd> <code>Standalone Minion</code> </p>
<p> This still is only scratching the surface, many components such as the reactor and event systems, extending Salt, modular components and more are not covered here. For an overview of all Salt features and documentation, look at the <code>Table of Contents</code>.</dl>
<h3>MinionFS Backend Walkthrough</h3>
<h3>Propagating Files</h3>
<p> New in version 2014.1.0. </p>
<p> Sometimes, one might need to propagate files that are generated on a minion. Salt already has a feature to send files from a minion to the master.</p>
<h3>Enabling File Propagation</h3>
<p> To enable propagation, the <code>file_recv</code> option needs to be set to <code>True</code>. </p>
<pre>
file_recv: True
</pre>
<p> These changes require a restart of the master, then new requests for the <code><a href="salt://minion-id/" rel="nofollow">salt://minion-id/</a></code> protocol will send files that are pushed by <code>cp.push</code> from <code>minion-id</code> to the master. </p>
<pre>
salt 'minion-id' cp.push /path/to/the/file
</pre>
<p> This command will store the file, including its full path, under <code>cachedir</code> <code>/master/minions/minion-id/files</code>. With the default <code>cachedir</code> the example file above would be stored as <i>/var/cache/salt/master/minions/minion-id/files/path/to/the/file</i>. </p>
<p> <code>NOTE:</code> This walkthrough assumes basic knowledge of Salt and <code>cp.push</code>. To get up to speed, check out the <code>walkthrough</code>.</p>
<h3>MinionFS Backend</h3>
<p> Since it is not a good idea to expose the whole <code>cachedir</code>, MinionFS should be used to send these files to other minions.</p>
<h3>Simple Configuration</h3>
<p> To use the minionfs backend only two configuration changes are required on the master. The <code>fileserver_backend</code> option needs to contain a value of <code>minion</code> and <code>file_recv</code> needs to be set to true: </p>
<pre>
fileserver_backend:
  - roots
  - minion
file_recv: True
</pre>
<p> These changes require a restart of the master, then new requests for the <code><a href="salt://minion-id/" rel="nofollow">salt://minion-id/</a></code> protocol will send files that are pushed by <code>cp.push</code> from <code>minion-id</code> to the master. </p>
<p> <code>NOTE:</code> All of the files that are pushed to the master are going to be available to all of the minions. If this is not what you want, please remove <code>minion</code> from <code>fileserver_backend</code> in the master config file. </p>
<p> <code>NOTE:</code> Having directories with the same name as your minions in the root that can be accessed like <code><a href="salt://minion-id/" rel="nofollow">salt://minion-id/</a></code> might cause confusion.</p>
<h3>Commandline Example</h3>
<p> Lets assume that we are going to generate SSH keys on a minion called <code>minion-source</code> and put the public part in <code>~/.ssh/authorized_keys</code> of root user of a minion called <code>minion-destination</code>. </p>
<p> First, lets make sure that <code>/root/.ssh</code> exists and has the right permissions: </p>
<p>[root[at] salt &#8211; master file] #salt &#8216;*&#8217; file.mkdir dir_path = / root /.ssh user = root group = root mode = 700 minion &#8211; source : None minion &#8211; destination : None</p>
<p> We create an RSA key pair without a passphrase [*]: </p>
<p>[root[at] salt &#8211; master file] #salt &#8216;minion-source&#8217; cmd.run &#8216;ssh-keygen -N &#8220;&#8221; -f /root/.ssh/id_rsa&#8217; minion &#8211; source : Generating public / private rsa key pair.Your identification has been saved in / root /.ssh / id_rsa.Your public key has been saved in / root /.ssh / id_rsa.pub.The key fingerprint is : 9b : cd : 1c : b9 : c2 : 93 : 8e : ad : a3 : 52 : a0 : 8b : 0a : cc : d4 : 9b root[at] minion &#8211; source The key&#8217;s randomart image is: + &#8211;[RSA 2048]&#8211; &#8211;+ | |<br />
    | |<br />
    | |<br />
    | o.|<br />
    | o o S o |<br />
    |= +.B o |<br />
       | o + E B = |<br />
                   | +..+ o |<br />
                   | o&#8230; ooo |<br />
                   +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+</p>
<p> and we send the public part to the master to be available to all minions: </p>
<p>[root[at] salt &#8211; master file] #salt &#8216;minion-source&#8217; cp.push / root /.ssh / id_rsa.pub minion &#8211; source : True</p>
<p> now it can be seen by everyone: </p>
<p>[root[at] salt &#8211; master file] #salt &#8216;minion-destination&#8217; cp.list_master_dirs<br />
        minion &#8211;<br />
    destination : -.- etc &#8211; minion &#8211; source / root &#8211; minion &#8211; source / root /.ssh</p>
<p> Lets copy that as the only authorized key to <code>minion-destination</code>: </p>
<p>[root[at] salt &#8211; master file] #salt &#8216;minion-destination&#8217; cp.get_file salt : // minion-source/root/.ssh/id_rsa.pub /root/.ssh/authorized_keys<br />
                                                                            minion &#8211;<br />
    destination : / root /.ssh / authorized_keys</p>
<p> Or we can use a more elegant and salty way to add an SSH key: </p>
<p>[root[at] salt &#8211; master file] #salt &#8216;minion-destination&#8217; ssh.set_auth_key_from_file user = root source = salt : // minion-source/root/.ssh/id_rsa.pub<br />
                                                                                                                minion &#8211;<br />
                                                                                                                destination : new</p>
<dl>
<dt>[*]</p>
<dd> Yes, that was the actual key on my server, but the server is already destroyed.</dl>
<h3>Automatic Updates / Frozen Deployments</h3>
<p> New in version 0.10.3.d. </p>
<p> Salt has support for the <i>Esky</i> application freezing and update tool. This tool allows one to build a complete zipfile out of the salt scripts and all their dependencies &#8211; including shared objects / DLLs.</p>
<h3>Getting Started</h3>
<p> To build frozen applications, suitable build environment will be needed for each platform. You should probably set up a virtualenv in order to limit the scope of Q/A. </p>
<p> This process does work on Windows. Directions are available at <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-windows-install" target="_blank">https://github.com/saltstack/salt-windows-install</a></i> for details on installing Salt in Windows. Only the 32-bit Python and dependencies have been tested, but they have been tested on 64-bit Windows. </p>
<p> Install <code>bbfreeze</code>, and then <code>esky</code> from PyPI in order to enable the <code>bdist_esky</code> command in <code>setup.py</code>. Salt itself must also be installed, in addition to its dependencies.</p>
<h3>Building and Freezing</h3>
<p> Once you have your tools installed and the environment configured, use <code>setup.py</code> to prepare the distribution files. </p>
<pre>
python setup.py sdist
python setup.py bdist
</pre>
<p> Once the distribution files are in place, Esky can be used traverse the module tree and pack all the scripts up into a redistributable. </p>
<pre>
python setup.py bdist_esky
</pre>
<p> There will be an appropriately versioned <code>salt-VERSION.zip</code> in <code>dist/</code> if everything went smoothly.</p>
<h3>Windows</h3>
<p> <code>C:\Python27\lib\site-packages\zmq</code> will need to be added to the PATH variable. This helps bbfreeze find the zmq DLL so it can pack it up.</p>
<h3>Using the Frozen Build</h3>
<p> Unpack the zip file in the desired install location. Scripts like <code>salt-minion</code> and <code>salt-call</code> will be in the root of the zip file. The associated libraries and bootstrapping will be in the directories at the same level. (Check the <i>Esky</i> documentation for more information) </p>
<p> To support updating your minions in the wild, put the builds on a web server that the minions can reach. <code>salt.modules.saltutil.update()</code> will trigger an update and (optionally) a restart of the minion service under the new version.</p>
<h3>Troubleshooting</h3>
<h3>A Windows minion isn&#8217;t responding</h3>
<p> The process dispatch on Windows is slower than it is on *nix. It may be necessary to add &#8216;-t 15&#8217; to salt commands to give minions plenty of time to return.</p>
<h3>Windows and the Visual Studio Redist</h3>
<p> The Visual C++ 2008 32-bit redistributable will need to be installed on all Windows minions. Esky has an option to pack the library into the zipfile, but OpenSSL does not seem to acknowledge the new location. If a <code>no OPENSSL_Applink</code> error appears on the console when trying to start a frozen minion, the redistributable is not installed.</p>
<h3>Mixed Linux environments and Yum</h3>
<p> The Yum Python module doesn&#8217;t appear to be available on any of the standard Python package mirrors. If RHEL/CentOS systems need to be supported, the frozen build should created on that platform to support all the Linux nodes. Remember to build the virtualenv with <code>&#8211;system-site-packages</code> so that the <code>yum</code> module is included.</p>
<h3>Automatic (Python) module discovery</h3>
<p> Automatic (Python) module discovery does not work with the late-loaded scheme that Salt uses for (Salt) modules. Any misbehaving modules will need to be explicitly added to the <code>freezer_includes</code> in Salt&#8217;s <code>setup.py</code>. Always check the zipped application to make sure that the necessary modules were included.</p>
<h3>Multi Master Tutorial</h3>
<p> As of Salt 0.16.0, the ability to connect minions to multiple masters has been made available. The multi-master system allows for redundancy of Salt masters and facilitates multiple points of communication out to minions. When using a multi-master setup, all masters are running hot, and any active master can be used to send commands out to the minions. </p>
<p> <code>NOTE:</code> If you need failover capabilities with multiple masters, there is also a MultiMaster-PKI setup available, that uses a different topology <i>MultiMaster-PKI with Failover Tutorial</i> </p>
<p> In 0.16.0, the masters do not share any information, keys need to be accepted on both masters, and shared files need to be shared manually or use tools like the git fileserver backend to ensure that the <code>file_roots</code> are kept consistent.</p>
<h3>Summary of Steps</h3>
<dl>
<dt>1.</p>
<dd> Create a redundant master server</p>
<dt>2.</p>
<dd> Copy primary master key to redundant master</p>
<dt>3.</p>
<dd> Start redundant master</p>
<dt>4.</p>
<dd> Configure minions to connect to redundant master</p>
<dt>5.</p>
<dd> Restart minions</p>
<dt>6.</p>
<dd> Accept keys on redundant master</dl>
<h3>Prepping a Redundant Master</h3>
<p> The first task is to prepare the redundant master. If the redundant master is already running, stop it. There is only one requirement when preparing a redundant master, which is that masters share the same private key. When the first master was created, the master&#8217;s identifying key pair was generated and placed in the master&#8217;s <code>pki_dir</code>. The default location of the master&#8217;s key pair is <code>/etc/salt/pki/master/</code>. Take the private key, <code>master.pem</code>, and copy it to the same location on the redundant master. Do the same for the master&#8217;s public key, <code>master.pub</code>. Assuming that no minions have yet been connected to the new redundant master, it is safe to delete any existing key in this location and replace it. </p>
<p> <code>NOTE:</code> There is no logical limit to the number of redundant masters that can be used. </p>
<p> Once the new key is in place, the redundant master can be safely started.</p>
<h3>Configure Minions</h3>
<p> Since minions need to be master-aware, the new master needs to be added to the minion configurations. Simply update the minion configurations to list all connected masters: </p>
<pre>
master:
  - saltmaster1.example.com
  - saltmaster2.example.com
</pre>
<p> Now the minion can be safely restarted. </p>
<p> Now the minions will check into the original master and also check into the new redundant master. Both masters are first-class and have rights to the minions. </p>
<p> <code>NOTE:</code> Minions can automatically detect failed masters and attempt to reconnect to reconnect to them quickly. To enable this functionality, set <i>master_alive_interval</i> in the minion config and specify a number of seconds to poll the masters for connection status. </p>
<p> If this option is not set, minions will still reconnect to failed masters but the first command sent after a master comes back up may be lost while the minion authenticates.</p>
<h3>Sharing Files Between Masters</h3>
<p> Salt does not automatically share files between multiple masters. A number of files should be shared or sharing of these files should be strongly considered.</p>
<h3>Minion Keys</h3>
<p> Minion keys can be accepted the normal way using <code>salt-key</code> on both masters. Keys accepted, deleted, or rejected on one master will NOT be automatically managed on redundant masters; this needs to be taken care of by running salt-key on both masters or sharing the <code>/etc/salt/pki/master/{minions,minions_pre,minions_rejected}</code> directories between masters. </p>
<p> <code>NOTE:</code> While sharing the <code>/etc/salt/pki/master</code> directory will work, it is strongly discouraged, since allowing access to the <code>master.pem</code> key outside of Salt creates a <i>SERIOUS</i> security risk.</p>
<h3>File_Roots</h3>
<p> The <code>file_roots</code> contents should be kept consistent between masters. Otherwise state runs will not always be consistent on minions since instructions managed by one master will not agree with other masters. </p>
<p> The recommended way to sync these is to use a fileserver backend like gitfs or to keep these files on shared storage.</p>
<h3>Pillar_Roots</h3>
<p> Pillar roots should be given the same considerations as <code>file_roots</code>.</p>
<h3>Master Configurations</h3>
<p> While reasons may exist to maintain separate master configurations, it is wise to remember that each master maintains independent control over minions. Therefore, access controls should be in sync between masters unless a valid reason otherwise exists to keep them inconsistent. </p>
<p> These access control options include but are not limited to:</p>
<dl>
<dt>&bull;</p>
<dd> external_auth</p>
<dt>&bull;</p>
<dd> client_acl</p>
<dt>&bull;</p>
<dd> peer</p>
<dt>&bull;</p>
<dd> peer_run</dl>
<h3>Multi-Master-PKI Tutorial With Failover</h3>
<p> This tutorial will explain, how to run a salt-environment where a single minion can have multiple masters and fail-over between them if its current master fails. </p>
<p> The individual steps are</p>
<dl>
<dt>&bull;</p>
<dd> setup the master(s) to sign its auth-replies</p>
<dt>&bull;</p>
<dd> setup minion(s) to verify master-public-keys</p>
<dt>&bull;</p>
<dd> enable multiple masters on minion(s)</p>
<dt>&bull;</p>
<dd> enable master-check on minion(s) Please note, that it is advised to have good knowledge of the salt- authentication and communication-process to understand this tutorial. All of the settings described here, go on top of the default authentication/communication process.</dl>
<h3>Motivation</h3>
<p> The default behaviour of a salt-minion is to connect to a master and accept the masters public key. With each publication, the master sends his public-key for the minion to check and if this public-key ever changes, the minion complains and exits. Practically this means, that there can only be a single master at any given time. </p>
<p> Would it not be much nicer, if the minion could have any number of masters (1:n) and jump to the next master if its current master died because of a network or hardware failure? </p>
<p> <code>NOTE:</code> There is also a MultiMaster-Tutorial with a different approach and topology than this one, that might also suite your needs or might even be better suited <i>Multi-Master Tutorial</i> </p>
<p> It is also desirable, to add some sort of authenticity-check to the very first public key a minion receives from a master. Currently a minions takes the first masters public key for granted.</p>
<h3>The Goal</h3>
<p> Setup the master to sign the public key it sends to the minions and enable the minions to verify this signature for authenticity.</p>
<h3>Prepping the master to sign its public key</h3>
<p> For signing to work, both master and minion must have the signing and/or verification settings enabled. If the master signs the public key but the minion does not verify it, the minion will complain and exit. The same happens, when the master does not sign but the minion tries to verify. </p>
<p> The easiest way to have the master sign its public key is to set </p>
<pre>
master_sign_pubkey: True
</pre>
<p> After restarting the salt-master service, the master will automatically generate a new key-pair </p>
<pre>
master_sign.pem
master_sign.pub
</pre>
<p> A custom name can be set for the signing key-pair by setting </p>
<pre>
master_sign_key_name: &lt;name_without_suffix&gt;
</pre>
<p> The master will then generate that key-pair upon restart and use it for creating the public keys signature attached to the auth-reply. </p>
<p> The computation is done for every auth-request of a minion. If many minions auth very often, it is advised to use conf_master:<i>master_pubkey_signature</i> and conf_master:<i>master_use_pubkey_signature</i> settings described below. </p>
<p> If multiple masters are in use and should sign their auth-replies, the signing key-pair master_sign.* has to be copied to each master. Otherwise a minion will fail to verify the masters public when connecting to a different master than it did initially. That is because the public keys signature was created with a different signing key-pair.</p>
<h3>Prepping the minion to verify received public keys</h3>
<p> The minion must have the public key (and only that one!) available to be able to verify a signature it receives. That public key (defaults to master_sign.pub) must be copied from the master to the minions pki-directory. </p>
<pre>
/etc/salt/pki/minion/master_sign.pub
DO NOT COPY THE master_sign.pem FILE. IT MUST STAY ON THE MASTER AND
ONLY THERE!
</pre>
<p> When that is done, enable the signature checking in the minions configuration </p>
<pre>
verify_master_pubkey_sign: True
</pre>
<p> and restart the minion. For the first try, the minion should be run in manual debug mode. </p>
<pre>
$ salt-minion -l debug
</pre>
<p> Upon connecting to the master, the following lines should appear on the output: </p>
<p>[DEBUG] Attempting to authenticate with the Salt Master at 172.16.0.10<br />
        [DEBUG] Loaded minion key : /<br />
                                    etc / salt / pki / minion / minion.pem[DEBUG] salt.crypt.verify_signature : Loading public key[DEBUG] salt.crypt.verify_signature : Verifying signature[DEBUG] Successfully verified signature of master public key with verification public key master_sign.pub[INFO] Received signed and verified master pubkey from master 172.16.0.10 [DEBUG] Decrypting the current master AES key</p>
<p> If the signature verification fails, something went wrong and it will look like this </p>
<p>[DEBUG] Attempting to authenticate with the Salt Master at 172.16.0.10<br />
        [DEBUG] Loaded minion key : /<br />
                                    etc / salt / pki / minion / minion.pem[DEBUG] salt.crypt.verify_signature : Loading public key[DEBUG] salt.crypt.verify_signature : Verifying signature[DEBUG] Failed to verify signature of public key[CRITICAL] The Salt Master server&#8217;s public key did not authenticate!</p>
<p> In a case like this, it should be checked, that the verification pubkey (master_sign.pub) on the minion is the same as the one on the master. </p>
<p> Once the verification is successful, the minion can be started in daemon mode again. </p>
<p> For the paranoid among us, its also possible to verify the public whenever it is received from the master. That is, for every single auth-attempt which can be quite frequent. For example just the start of the minion will force the signature to be checked 6 times for various things like auth, mine, highstate, etc. </p>
<p> If that is desired, enable the setting </p>
<pre>
always_verify_signature: True
</pre>
<h3>Multiple Masters For A Minion</h3>
<p> Configuring multiple masters on a minion is done by specifying two settings:</p>
<dl>
<dt>&bull;</p>
<dd> a list of masters addresses</p>
<dt>&bull;</p>
<dd> what type of master is defined </p>
<pre>
master:
    - 172.16.0.10
    - 172.16.0.11
    - 172.16.0.12
</pre>
<pre>
master_type: failover
</pre>
<p> This tells the minion that all the master above are available for it to connect to. When started with this configuration, it will try the master in the order they are defined. To randomize that order, set </p>
<pre>
master_shuffle: True
</pre>
<p> The master-list will then be shuffled before the first connection attempt. </p>
<p> The first master that accepts the minion, is used by the minion. If the master does not yet know the minion, that counts as accepted and the minion stays on that master. </p>
<p> For the minion to be able to detect if its still connected to its current master enable the check for it </p>
<pre>
master_alive_interval: &lt;seconds&gt;
</pre>
<p> If the loss of the connection is detected, the minion will temporarily remove the failed master from the list and try one of the other masters defined (again shuffled if that is enabled).</dl>
<h3>Testing the setup</h3>
<p> At least two running masters are needed to test the failover setup. </p>
<p> Both masters should be running and the minion should be running on the command line in debug mode </p>
<pre>
$ salt-minion -l debug
</pre>
<p> The minion will connect to the first master from its master list </p>
<p>[DEBUG] Attempting to authenticate with the Salt Master at 172.16.0.10<br />
        [DEBUG] Loaded minion key : /<br />
                                    etc / salt / pki / minion / minion.pem[DEBUG] salt.crypt.verify_signature : Loading public key[DEBUG] salt.crypt.verify_signature : Verifying signature[DEBUG] Successfully verified signature of master public key with verification public key master_sign.pub[INFO] Received signed and verified master pubkey from master 172.16.0.10 [DEBUG] Decrypting the current master AES key</p>
<p> A test.ping on the master the minion is currently connected to should be run to test connectivity. </p>
<p> If successful, that master should be turned off. A firewall-rule denying the minions packets will also do the trick. </p>
<p> Depending on the configured conf_minion:<i>master_alive_interval</i>, the minion will notice the loss of the connection and log it to its logfile. </p>
<p>[INFO] Connection to master 172.16.0.10 lost<br />
        [INFO] Trying to tune in to next master from master &#8211;<br />
    list</p>
<p> The minion will then remove the current master from the list and try connecting to the next master </p>
<p>[INFO] Removing possibly failed master 172.16.0.10 from list of masters<br />
    [WARNING] Master ip address changed from 172.16.0.10 to 172.16.0.11<br />
        [DEBUG] Attempting to authenticate with the Salt Master at 172.16.0.11</p>
<p> If everything is configured correctly, the new masters public key will be verified successfully </p>
<p>[DEBUG] Loaded minion key : / etc / salt / pki / minion / minion.pem[DEBUG] salt.crypt.verify_signature : Loading public key[DEBUG] salt.crypt.verify_signature : Verifying signature[DEBUG] Successfully verified signature of master public key with verification public key master_sign.pub</p>
<p> the authentication with the new master is successful </p>
<p>[INFO] Received signed and verified master pubkey from master 172.16.0.11<br />
        [DEBUG] Decrypting the current master AES key<br />
            [DEBUG] Loaded minion key : /<br />
                                        etc / salt / pki / minion / minion.pem[INFO] Authentication with master successful !</p>
<p> and the minion can be pinged again from its new master.</p>
<h3>Performance Tuning</h3>
<p> With the setup described above, the master computes a signature for every auth-request of a minion. With many minions and many auth-requests, that can chew up quite a bit of CPU-Power. </p>
<p> To avoid that, the master can use a pre-created signature of its public-key. The signature is saved as a base64 encoded string which the master reads once when starting and attaches only that string to auth-replies. </p>
<p> Enabling this also gives paranoid users the possibility, to have the signing key-pair on a different system than the actual salt-master and create the public keys signature there. Probably on a system with more restrictive firewall rules, without internet access, less users, etc. </p>
<p> That signature can be created with </p>
<pre>
$ salt-key --gen-signature
</pre>
<p> This will create a default signature file in the master pki-directory </p>
<pre>
/etc/salt/pki/master/master_pubkey_signature
</pre>
<p> It is a simple text-file with the binary-signature converted to base64. </p>
<p> If no signing-pair is present yet, this will auto-create the signing pair and the signature file in one call </p>
<pre>
$ salt-key --gen-signature --auto-create
</pre>
<p> Telling the master to use the pre-created signature is done with </p>
<pre>
master_use_pubkey_signature: True
</pre>
<p> That requires the file &#8216;master_pubkey_signature&#8217; to be present in the masters pki-directory with the correct signature. </p>
<p> If the signature file is named differently, its name can be set with </p>
<pre>
master_pubkey_signature: &lt;filename&gt;
</pre>
<p> With many masters and many public-keys (default and signing), it is advised to use the salt-masters hostname for the signature-files name. Signatures can be easily confused because they do not provide any information about the key the signature was created from. </p>
<p> Verifying that everything works is done the same way as above.</p>
<h3>How the signing and verification works</h3>
<p> The default key-pair of the salt-master is </p>
<pre>
/etc/salt/pki/master/master.pem
/etc/salt/pki/master/master.pub
</pre>
<p> To be able to create a signature of a message (in this case a public-key), another key-pair has to be added to the setup. Its default name is: </p>
<pre>
master_sign.pem
master_sign.pub
</pre>
<p> The combination of the master.* and master_sign.* key-pairs give the possibility of generating signatures. The signature of a given message is unique and can be verified, if the public-key of the signing-key-pair is available to the recipient (the minion). </p>
<p> The signature of the masters public-key in master.pub is computed with </p>
<pre>
master_sign.pem
master.pub
M2Crypto.EVP.sign_update()
</pre>
<p> This results in a binary signature which is converted to base64 and attached to the auth-reply send to the minion. </p>
<p> With the signing-pairs public-key available to the minion, the attached signature can be verified with </p>
<pre>
master_sign.pub
master.pub
M2Cryptos EVP.verify_update().
</pre>
<p> When running multiple masters, either the signing key-pair has to be present on all of them, or the master_pubkey_signature has to be pre-computed for each master individually (because they all have different public-keys). DO NOT PUT THE SAME master.pub ON ALL MASTERS FOR EASE OF USE.</p>
<h3>Preseed Minion with Accepted Key</h3>
<p> In some situations, it is not convenient to wait for a minion to start before accepting its key on the master. For instance, you may want the minion to bootstrap itself as soon as it comes online. You may also want to to let your developers provision new development machines on the fly. </p>
<p> <code>SEE ALSO:</code> Many ways to preseed minion keys </p>
<p> Salt has other ways to generate and pre-accept minion keys in addition to the manual steps outlined below. </p>
<p> salt-cloud performs these same steps automatically when new cloud VMs are created (unless instructed not to). </p>
<p> salt-api exposes an HTTP call to Salt&#8217;s REST API to <code>generate and download the new minion keys as a tarball</code>. </p>
<p> There is a general four step process to do this:</p>
<dl>
<dt>1.</p>
<dd> Generate the keys on the master: </p>
<p>root[at] saltmaster #salt &#8211; key&#8211; gen &#8211; keys = [key_name]</p>
<p> Pick a name for the key, such as the minion&#8217;s id.</p>
<dt>2.</p>
<dd> Add the public key to the accepted minion folder: </p>
<p>root[at] saltmaster #cp key_name.pub / etc / salt / pki / master / minions / [minion_id]</p>
<p> It is necessary that the public key file has the same name as your minion id. This is how Salt matches minions with their keys. Also note that the pki folder could be in a different location, depending on your OS or if specified in the master config file.</p>
<dt>3.</p>
<dd> Distribute the minion keys. </p>
<p> There is no single method to get the keypair to your minion. The difficulty is finding a distribution method which is secure. For Amazon EC2 only, an AWS best practice is to use IAM Roles to pass credentials. (See blog post, <i><a rel="nofollow noopener" href="http://blogs.aws.amazon.com/security/post/Tx610S2MLVZWEA/Using-IAM-roles-to-distribute-non-AWS-credentials-to-your-EC2-instances" target="_blank">http://blogs.aws.amazon.com/security/post/Tx610S2MLVZWEA/Using-IAM-roles-to-distribute-non-AWS-credentials-to-your-EC2-instances</a></i> )</p>
<dt>Security Warning</p>
<dd>
<p> Since the minion key is already accepted on the master, distributing the private key poses a potential security risk. A malicious party will have access to your entire state tree and other sensitive data if they gain access to a preseeded minion key.</p>
<dt>4.</p>
<dd> Preseed the Minion with the keys </p>
<p> You will want to place the minion keys before starting the salt-minion daemon: </p>
<pre>
/etc/salt/pki/minion/minion.pem
/etc/salt/pki/minion/minion.pub
</pre>
<p> Once in place, you should be able to start salt-minion and run <code>salt-call state.highstate</code> or any other salt commands that require master authentication.</dl>
<h3>Salt Bootstrap</h3>
<p> The Salt Bootstrap script allows for a user to install the Salt Minion or Master on a variety of system distributions and versions. This shell script known as <code>bootstrap-salt.sh</code> runs through a series of checks to determine the operating system type and version. It then installs the Salt binaries using the appropriate methods. The Salt Bootstrap script installs the minimum number of packages required to run Salt. This means that in the event you run the bootstrap to install via package, Git will not be installed. Installing the minimum number of packages helps ensure the script stays as lightweight as possible, assuming the user will install any other required packages after the Salt binaries are present on the system. The script source is available on GitHub: <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-bootstrap" target="_blank">https://github.com/saltstack/salt-bootstrap</a></i></p>
<h3>Supported Operating Systems</h3>
<dl>
<dt>&bull;</p>
<dd> Amazon Linux 2012.09</p>
<dt>&bull;</p>
<dd> Arch</p>
<dt>&bull;</p>
<dd> CentOS 5/6</p>
<dt>&bull;</p>
<dd> Debian 6.x/7.x/8(git installations only)</p>
<dt>&bull;</p>
<dd> Fedora 17/18</p>
<dt>&bull;</p>
<dd> FreeBSD 9.1/9.2/10</p>
<dt>&bull;</p>
<dd> Gentoo</p>
<dt>&bull;</p>
<dd> Linaro</p>
<dt>&bull;</p>
<dd> Linux Mint 13/14</p>
<dt>&bull;</p>
<dd> OpenSUSE 12.x</p>
<dt>&bull;</p>
<dd> Oracle Linux 5/5</p>
<dt>&bull;</p>
<dd> Red Hat 5/6</p>
<dt>&bull;</p>
<dd> Red Hat Enterprise 5/6</p>
<dt>&bull;</p>
<dd> Scientific Linux 5/6</p>
<dt>&bull;</p>
<dd> SmartOS</p>
<dt>&bull;</p>
<dd> SuSE 11 SP1/11 SP2</p>
<dt>&bull;</p>
<dd> Ubuntu 10.x/11.x/12.x/13.04/13.10</p>
<dt>&bull;</p>
<dd> Elementary OS 0.2 </p>
<p> <code>NOTE:</code> In the event you do not see your distribution or version available please review the develop branch on Github as it main contain updates that are not present in the stable release: <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-bootstrap/tree/develop" target="_blank">https://github.com/saltstack/salt-bootstrap/tree/develop</a></i></dl>
<h3>Example Usage</h3>
<p> If you&#8217;re looking for the <i>one-liner</i> to install salt, please scroll to the bottom and use the instructions for <i>Installing via an Insecure One-Liner</i> </p>
<p> <code>NOTE:</code> In every two-step example, you would be well-served to examine the downloaded file and examine it to ensure that it does what you expect. </p>
<p> Using <code>curl</code> to install latest git: </p>
<pre>
curl -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> -o install_salt.sh
sudo sh install_salt.sh git develop
</pre>
<p> Using <code>wget</code> to install your distribution&#8217;s stable packages: </p>
<pre>
wget -O install_salt.sh <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>
sudo sh install_salt.sh
</pre>
<p> Install a specific version from git using <code>wget</code>: </p>
<pre>
wget -O install_salt.sh <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>
sudo sh install_salt.sh -P git v0.16.4
</pre>
<p> If you already have python installed, <code>python 2.6</code>, then it&#8217;s as easy as: </p>
<pre>
python -m urllib &quot;<a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>&quot; &gt; install_salt.sh
sudo sh install_salt.sh git develop
</pre>
<p> All python versions should support the following one liner: </p>
<pre>
python -c 'import urllib; print urllib.urlopen(&quot;<a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>&quot;).read()' &gt; install_salt.sh
sudo sh install_salt.sh git develop
</pre>
<p> On a FreeBSD base system you usually don&#8217;t have either of the above binaries available. You <code>do</code> have <code>fetch</code> available though: </p>
<pre>
fetch -o install_salt.sh <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>
sudo sh install_salt.sh
</pre>
<p> If all you want is to install a <code>salt-master</code> using latest git: </p>
<pre>
curl -o install_salt.sh -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>
sudo sh install_salt.sh -M -N git develop
</pre>
<p> If you want to install a specific release version (based on the git tags): </p>
<pre>
curl -o install_salt.sh -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>
sudo sh install_salt.sh git v0.16.4
</pre>
<p> To install a specific branch from a git fork: </p>
<pre>
curl -o install_salt.sh -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>
sudo sh install_salt.sh -g <a rel="nofollow noopener" href="https://github.com/myuser/salt.git" target="_blank">https://github.com/myuser/salt.git</a> git mybranch
</pre>
<h3>Installing via an Insecure One-Liner</h3>
<p> The following examples illustrate how to install Salt via a one-liner. </p>
<p> <code>NOTE:</code> Warning! These methods do not involve a verification step and assume that the delivered file is trustworthy.</p>
<h3>Examples</h3>
<p> Installing the latest develop branch of Salt: </p>
<pre>
curl -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh -s -- git develop
</pre>
<p> Any of the example above which use two-lines can be made to run in a single-line configuration with minor modifications.</p>
<h3>Example Usage</h3>
<p> The Salt Bootstrap script has a wide variety of options that can be passed as well as several ways of obtaining the bootstrap script itself. </p>
<p> For example, using <code>curl</code> to install your distribution&#8217;s stable packages: </p>
<pre>
curl -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh
</pre>
<p> Using <code>wget</code> to install your distribution&#8217;s stable packages: </p>
<pre>
wget -O - <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh
</pre>
<p> Installing the latest version available from git with <code>curl</code>: </p>
<pre>
curl -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh -s -- git develop
</pre>
<p> Install a specific version from git using <code>wget</code>: </p>
<pre>
wget -O - <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sh -s -- -P git v0.16.4
</pre>
<p> If you already have python installed, <code>python 2.6</code>, then it&#8217;s as easy as: </p>
<pre>
python -m urllib &quot;<a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>&quot; | sudo sh -s -- git develop
</pre>
<p> All python versions should support the following one liner: </p>
<pre>
python -c 'import urllib; print urllib.urlopen(&quot;<a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a>&quot;).read()' | \
sudo  sh -s -- git develop
</pre>
<p> On a FreeBSD base system you usually don&#8217;t have either of the above binaries available. You <code>do</code> have <code>fetch</code> available though: </p>
<pre>
fetch -o - <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh
</pre>
<p> If all you want is to install a <code>salt-master</code> using latest git: </p>
<pre>
curl -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh -s -- -M -N git develop
</pre>
<p> If you want to install a specific release version (based on the git tags): </p>
<pre>
curl -L <a rel="nofollow noopener" href="https://bootstrap.saltstack.com" target="_blank">https://bootstrap.saltstack.com</a> | sudo sh -s -- git v0.16.4
</pre>
<p> Downloading the develop branch (from here standard command line options may be passed): </p>
<pre>
wget <a rel="nofollow noopener" href="https://bootstrap.saltstack.com/develop" target="_blank">https://bootstrap.saltstack.com/develop</a>
</pre>
<h3>Command Line Options</h3>
<p> Here&#8217;s a summary of the command line options: </p>
<p>$ sh bootstrap-salt.sh -h<br />
  Usage :  bootstrap-salt.sh [options] &lt;install-type&gt; &lt;install-type-args&gt;<br />
  Installation types:<br />
    &#8211; stable (default)<br />
    &#8211; daily  (ubuntu specific)<br />
    &#8211; git<br />
  Examples:<br />
    $ bootstrap-salt.sh<br />
    $ bootstrap-salt.sh stable<br />
    $ bootstrap-salt.sh daily<br />
    $ bootstrap-salt.sh git<br />
    $ bootstrap-salt.sh git develop<br />
    $ bootstrap-salt.sh git v0.17.0<br />
    $ bootstrap-salt.sh git 8c3fadf15ec183e5ce8c63739850d543617e4357<br />
  Options:<br />
  -h  Display this message<br />
  -v  Display script version<br />
  -n  No colours.<br />
  -D  Show debug output.<br />
  -c  Temporary configuration directory<br />
  -g  Salt repository URL. (default: git://github.com/saltstack/salt.git)<br />
  -k  Temporary directory holding the minion keys which will pre-seed<br />
      the master.<br />
  -M  Also install salt-master<br />
  -S  Also install salt-syndic<br />
  -N  Do not install salt-minion<br />
  -X  Do not start daemons after installation<br />
  -C  Only run the configuration function. This option automatically<br />
      bypasses any installation.<br />
  -P  Allow pip based installations. On some distributions the required salt<br />
      packages or its dependencies are not available as a package for that<br />
      distribution. Using this flag allows the script to use pip as a last<br />
      resort method. NOTE: This only works for functions which actually<br />
      implement pip based installations.<br />
  -F  Allow copied files to overwrite existing(config, init.d, etc)<br />
  -U  If set, fully upgrade the system prior to bootstrapping salt<br />
  -K  If set, keep the temporary files in the temporary directories specified<br />
      with -c and -k.<br />
  -I  If set, allow insecure connections while downloading any files. For<br />
      example, pass &#8216;&#8211;no-check-certificate&#8217; to &#8216;wget&#8217; or &#8216;&#8211;insecure&#8217; to &#8216;curl&#8217;<br />
  -A  Pass the salt-master DNS name or IP. This will be stored under<br />
      ${BS_SALT_ETC_DIR}/minion.d/99-master-address.conf<br />
  -i  Pass the salt-minion id. This will be stored under<br />
      ${BS_SALT_ETC_DIR}/minion_id<br />
  -L  Install the Apache Libcloud package if possible(required for salt-cloud)<br />
  -p  Extra-package to install while installing salt dependencies. One package<br />
      per -p flag. You&#8217;re responsible for providing the proper package name.</p>
<h3>Git Fileserver Backend Walkthrough</h3>
<p> <code>NOTE:</code> This walkthrough assumes basic knowledge of Salt. To get up to speed, check out the <code>Salt Walkthrough</code>. </p>
<p> The gitfs backend allows Salt to serve files from git repositories. It can be enabled by adding <code>git</code> to the <code>fileserver_backend</code> list, and configuring one or more repositories in <code>gitfs_remotes</code>. </p>
<p> Branches and tags become Salt fileserver environments.</p>
<h3>Installing Dependencies</h3>
<p> Beginning with version 2014.7.0, both <i>pygit2</i> and <i>Dulwich</i> are supported as alternatives to <i>GitPython</i>. The desired provider can be configured using the <code>gitfs_provider</code> parameter in the master config file. </p>
<p> If <code>gitfs_provider</code> is not configured, then Salt will prefer <i>pygit2</i> if a suitable version is available, followed by <i>GitPython</i> and <i>Dulwich</i>. </p>
<p> <code>NOTE:</code> It is recommended to always run the most recent version of any the below dependencies. Certain features of gitfs may not be available without the most recent version of the chosen library.</p>
<h3>pygit2</h3>
<p> The minimum supported version of <i>pygit2</i> is 0.20.3. Availability for this version of <i>pygit2</i> is still limited, though the SaltStack team is working to get compatible versions available for as many platforms as possible. </p>
<p> For the Fedora/EPEL versions which have a new enough version packaged, the following command would be used to install <i>pygit2</i>: </p>
<pre>
# yum install python-pygit2
</pre>
<p> Provided a valid version is packaged for Debian/Ubuntu (which is not currently the case), the package name would be the same, and the following command would be used to install it: </p>
<pre>
# apt-get install python-pygit2
</pre>
<p> If <i>pygit2</i> is not packaged for the platform on which the Master is running, the <i>pygit2</i> website has installation instructions <i>here</i>. Keep in mind however that following these instructions will install libgit2 and <i>pygit2</i> without system packages. Additionally, keep in mind that <i>SSH authentication in pygit2</i> requires <i>libssh2</i> (<i>not</i> libssh) development libraries to be present before libgit2 is built.</p>
<h3>GitPython</h3>
<p> <i>GitPython</i> 0.3.0 or newer is required to use GitPython for gitfs. For RHEL-based Linux distros, a compatible version is available in EPEL, and can be easily installed on the master using yum: </p>
<pre>
# yum install GitPython
</pre>
<p> Ubuntu 14.04 LTS and Debian Wheezy (7.x) also have a compatible version packaged: </p>
<pre>
# apt-get install python-git
</pre>
<p> If your master is running an older version (such as Ubuntu 12.04 LTS or Debian Squeeze), then you will need to install GitPython using either <i>pip</i> or easy_install (it is recommended to use pip). Version 0.3.2.RC1 is now marked as the stable release in PyPI, so it should be a simple matter of running <code>pip install GitPython</code> (or <code>easy_install GitPython</code>) as root. </p>
<p> <code>WARNING:</code> Keep in mind that if GitPython has been previously installed on the master using pip (even if it was subsequently uninstalled), then it may still exist in the build cache (typically <code>/tmp/pip-build-root/GitPython</code>) if the cache is not cleared after installation. The package in the build cache will override any requirement specifiers, so if you try upgrading to version 0.3.2.RC1 by running <code>pip install &#8216;GitPython==0.3.2.RC1&#8217;</code> then it will ignore this and simply install the version from the cache directory. Therefore, it may be necessary to delete the GitPython directory from the build cache in order to ensure that the specified version is installed.</p>
<h3>Dulwich</h3>
<p> Dulwich 0.9.4 or newer is required to use Dulwich as backend for gitfs. </p>
<p> Dulwich is available in EPEL, and can be easily installed on the master using yum: </p>
<pre>
# yum install python-dulwich
</pre>
<p> For APT-based distros such as Ubuntu and Debian: </p>
<pre>
# apt-get install python-dulwich
</pre>
<p> <code>IMPORTANT:</code> If switching to Dulwich from GitPython/pygit2, or switching from GitPython/pygit2 to Dulwich, it is necessary to clear the gitfs cache to avoid unpredictable behavior. This is probably a good idea whenever switching to a new <code>gitfs_provider</code>, but it is less important when switching between GitPython and pygit2. </p>
<p> Beginning in version 2015.5.0, the gitfs cache can be easily cleared using the <code>fileserver.clear_cache</code> runner. </p>
<pre>
salt-run fileserver.clear_cache backend=git
</pre>
<p> If the Master is running an earlier version, then the cache can be cleared by removing the <code>gitfs</code> and <code>file_lists/gitfs</code> directories (both paths relative to the master cache directory, usually <code>/var/cache/salt/master</code>). </p>
<pre>
rm -rf /var/cache/salt/master{,/file_lists}/gitfs
</pre>
<h3>Simple Configuration</h3>
<p> To use the gitfs backend, only two configuration changes are required on the master:</p>
<dl>
<dt>1.</p>
<dd> Include <code>git</code> in the <code>fileserver_backend</code> list in the master config file: </p>
<pre>
fileserver_backend:
  - git
</pre>
<dt>2.</p>
<dd> Specify one or more <code>git://</code>, <code>https://</code>, <code>file://</code>, or <code>ssh://</code> URLs in <code>gitfs_remotes</code> to configure which repositories to cache and search for requested files: </p>
<pre>
gitfs_remotes:
  - <a rel="nofollow noopener" href="https://github.com/saltstack-formulas/salt-formula.git" target="_blank">https://github.com/saltstack-formulas/salt-formula.git</a>
</pre>
<p> SSH remotes can also be configured using scp-like syntax: </p>
<pre>
gitfs_remotes:
  - git [at] github.com:user/repo.git
  - <a href="ssh://user@domain.tld/path/to/repo.git" rel="nofollow noopener" target="_blank">ssh://user@domain.tld/path/to/repo.git</a>
</pre>
<p> Information on how to authenticate to SSH remotes can be found <i>here</i>. </p>
<p> <code>NOTE:</code> Dulwich does not recognize <code>ssh://</code> URLs, <code>git+ssh://</code> must be used instead. Salt version 2015.5.0 and later will automatically add the <code>git+</code> to the beginning of these URLs before fetching, but earlier Salt versions will fail to fetch unless the URL is specified using <code>git+ssh://</code>.</p>
<dt>3.</p>
<dd> Restart the master to load the new configuration. </p>
<p> <code>NOTE:</code> In a master/minion setup, files from a gitfs remote are cached once by the master, so minions do not need direct access to the git repository.</dl>
<h3>Multiple Remotes</h3>
<p> The <code>gitfs_remotes</code> option accepts an ordered list of git remotes to cache and search, in listed order, for requested files. </p>
<p> A simple scenario illustrates this cascading lookup behavior: </p>
<p> If the <code>gitfs_remotes</code> option specifies three remotes: </p>
<pre>
gitfs_remotes:
  - <a href="git://github.com/example/first.git" rel="nofollow noopener" target="_blank">git://github.com/example/first.git</a>
  - <a rel="nofollow noopener" href="https://github.com/example/second.git" target="_blank">https://github.com/example/second.git</a>
  - file:///root/third
</pre>
<p> And each repository contains some files: </p>
<pre>
first.git:
    top.sls
    edit/vim.sls
    edit/vimrc
    nginx/init.sls
second.git:
    edit/dev_vimrc
    haproxy/init.sls
third:
    haproxy/haproxy.conf
    edit/dev_vimrc
</pre>
<p> Salt will attempt to lookup the requested file from each gitfs remote repository in the order in which they are defined in the configuration. The <code><a href="git://github.com/example/first.git" rel="nofollow noopener" target="_blank">git://github.com/example/first.git</a></code> remote will be searched first. If the requested file is found, then it is served and no further searching is executed. For example:</p>
<dl>
<dt>&bull;</p>
<dd> A request for the file <code><a href="salt://haproxy/init.sls" rel="nofollow">salt://haproxy/init.sls</a></code> will be served from the <code><a rel="nofollow noopener" href="https://github.com/example/second.git" target="_blank">https://github.com/example/second.git</a></code> git repo.</p>
<dt>&bull;</p>
<dd> A request for the file <code><a href="salt://haproxy/haproxy.conf" rel="nofollow">salt://haproxy/haproxy.conf</a></code> will be served from the <code>file:///root/third</code> repo. </p>
<p> <code>NOTE:</code> This example is purposefully contrived to illustrate the behavior of the gitfs backend. This example should not be read as a recommended way to lay out files and git repos. </p>
<p> The <code>file://</code> prefix denotes a git repository in a local directory. However, it will still use the given <code>file://</code> URL as a remote, rather than copying the git repo to the salt cache. This means that any refs you want accessible must exist as <i>local</i> refs in the specified repo. </p>
<p> <code>WARNING:</code> Salt versions prior to 2014.1.0 are not tolerant of changing the order of remotes or modifying the URI of existing remotes. In those versions, when modifying remotes it is a good idea to remove the gitfs cache directory (<code>/var/cache/salt/master/gitfs</code>) before restarting the salt-master service.</dl>
<h3>Per-remote Configuration Parameters</h3>
<p> New in version 2014.7.0. </p>
<p> The following master config parameters are global (that is, they apply to all configured gitfs remotes):</p>
<dl>
<dt>&bull;</p>
<dd> <code>gitfs_base</code></p>
<dt>&bull;</p>
<dd> <code>gitfs_root</code></p>
<dt>&bull;</p>
<dd> <code>gitfs_mountpoint</code> (new in 2014.7.0)</p>
<dt>&bull;</p>
<dd> <code>gitfs_user</code> (<code>pygit2 only</code>, new in 2014.7.0)</p>
<dt>&bull;</p>
<dd> <code>gitfs_password</code> (<code>pygit2 only</code>, new in 2014.7.0)</p>
<dt>&bull;</p>
<dd> <code>gitfs_insecure_auth</code> (<code>pygit2 only</code>, new in 2014.7.0)</p>
<dt>&bull;</p>
<dd> <code>gitfs_pubkey</code> (<code>pygit2 only</code>, new in 2014.7.0)</p>
<dt>&bull;</p>
<dd> <code>gitfs_privkey</code> (<code>pygit2 only</code>, new in 2014.7.0)</p>
<dt>&bull;</p>
<dd> <code>gitfs_passphrase</code> (<code>pygit2 only</code>, new in 2014.7.0) </p>
<p> These parameters can now be overridden on a per-remote basis. This allows for a tremendous amount of customization. Here&#8217;s some example usage: </p>
<pre>
gitfs_provider: pygit2
gitfs_base: develop
gitfs_remotes:
  - <a rel="nofollow noopener" href="https://foo.com/foo.git" target="_blank">https://foo.com/foo.git</a>
  - <a rel="nofollow noopener" href="https://foo.com/bar.git:" target="_blank">https://foo.com/bar.git:</a>
    - root: salt
    - mountpoint: <a href="salt://foo/bar/baz" rel="nofollow">salt://foo/bar/baz</a>
    - base: salt-base
  - <a rel="nofollow noopener" href="http://foo.com/baz.git:" target="_blank">http://foo.com/baz.git:</a>
    - root: salt/states
    - user: joe
    - password: mysupersecretpassword
    - insecure_auth: True
</pre>
<p> <code>IMPORTANT:</code> There are two important distinctions which should be noted for per-remote configuration:</p>
<dt>1.</p>
<dd> The URL of a remote which has per-remote configuration must be suffixed with a colon.</p>
<dt>2.</p>
<dd> Per-remote configuration parameters are named like the global versions, with the <code>gitfs_</code> removed from the beginning. </p>
<p> In the example configuration above, the following is true:</p>
<dt>1.</p>
<dd> The first and third gitfs remotes will use the <code>develop</code> branch/tag as the <code>base</code> environment, while the second one will use the <code>salt-base</code> branch/tag as the <code>base</code> environment.</p>
<dt>2.</p>
<dd> The first remote will serve all files in the repository. The second remote will only serve files from the <code>salt</code> directory (and its subdirectories), while the third remote will only serve files from the <code>salt/states</code> directory (and its subdirectories).</p>
<dt>3.</p>
<dd> The files from the second remote will be located under <code><a href="salt://foo/bar/baz" rel="nofollow">salt://foo/bar/baz</a></code>, while the files from the first and third remotes will be located under the root of the Salt fileserver namespace (<code>salt://</code>).</p>
<dt>4.</p>
<dd> The third remote overrides the default behavior of <i>not authenticating to insecure (non-HTTPS) remotes</i>.</dl>
<h3>Serving from a Subdirectory</h3>
<p> The <code>gitfs_root</code> parameter allows files to be served from a subdirectory within the repository. This allows for only part of a repository to be exposed to the Salt fileserver. </p>
<p> Assume the below layout: </p>
<pre>
.gitignore
README.txt
foo/
foo/bar/
foo/bar/one.txt
foo/bar/two.txt
foo/bar/three.txt
foo/baz/
foo/baz/top.sls
foo/baz/edit/vim.sls
foo/baz/edit/vimrc
foo/baz/nginx/init.sls
</pre>
<p> The below configuration would serve only the files under <code>foo/baz</code>, ignoring the other files in the repository: </p>
<pre>
gitfs_remotes:
  - <a href="git://mydomain.com/stuff.git" rel="nofollow noopener" target="_blank">git://mydomain.com/stuff.git</a>
gitfs_root: foo/baz
</pre>
<p> The root can also be configured on a <i>per-remote basis</i>.</p>
<h3>Mountpoints</h3>
<p> New in version 2014.7.0. </p>
<p> The <code>gitfs_mountpoint</code> parameter will prepend the specified path to the files served from gitfs. This allows an existing repository to be used, rather than needing to reorganize a repository or design it around the layout of the Salt fileserver. </p>
<p> Before the addition of this feature, if a file being served up via gitfs was deeply nested within the root directory (for example, <code><a href="salt://webapps/foo/files/foo.conf" rel="nofollow">salt://webapps/foo/files/foo.conf</a></code>, it would be necessary to ensure that the file was properly located in the remote repository, and that all of the the parent directories were present (for example, the directories <code>webapps/foo/files/</code> would need to exist at the root of the repository). </p>
<p> The below example would allow for a file <code>foo.conf</code> at the root of the repository to be served up from the Salt fileserver path <code><a href="salt://webapps/foo/files/foo.conf" rel="nofollow">salt://webapps/foo/files/foo.conf</a></code>. </p>
<pre>
gitfs_remotes:
  - <a rel="nofollow noopener" href="https://mydomain.com/stuff.git" target="_blank">https://mydomain.com/stuff.git</a>
gitfs_mountpoint: <a href="salt://webapps/foo/files" rel="nofollow">salt://webapps/foo/files</a>
</pre>
<p> Mountpoints can also be configured on a <i>per-remote basis</i>.</p>
<h3>Using gitfs Alongside Other Backends</h3>
<p> Sometimes it may make sense to use multiple backends; for instance, if <code>sls</code> files are stored in git but larger files are stored directly on the master. </p>
<p> The cascading lookup logic used for multiple remotes is also used with multiple backends. If the <code>fileserver_backend</code> option contains multiple backends: </p>
<pre>
fileserver_backend:
  - roots
  - git
</pre>
<p> Then the <code>roots</code> backend (the default backend of files in <code>/srv/salt</code>) will be searched first for the requested file; then, if it is not found on the master, each configured git remote will be searched.</p>
<h3>Branches, Environments, and Top Files</h3>
<p> When using the gitfs backend, branches, and tags will be mapped to environments using the branch/tag name as an identifier. </p>
<p> There is one exception to this rule: the <code>master</code> branch is implicitly mapped to the <code>base</code> environment. </p>
<p> So, for a typical <code>base</code>, <code>qa</code>, <code>dev</code> setup, the following branches could be used: </p>
<pre>
master
qa
dev
</pre>
<p> <code>top.sls</code> files from different branches will be merged into one at runtime. Since this can lead to overly complex configurations, the recommended setup is to have the <code>top.sls</code> file only in the master branch and use environment-specific branches for state definitions. </p>
<p> To map a branch other than <code>master</code> as the <code>base</code> environment, use the <code>gitfs_base</code> parameter. </p>
<pre>
gitfs_base: salt-base
</pre>
<p> The base can also be configured on a <i>per-remote basis</i>.</p>
<h3>Environment Whitelist/Blacklist</h3>
<p> New in version 2014.7.0. </p>
<p> The <code>gitfs_env_whitelist</code> and <code>gitfs_env_blacklist</code> parameters allow for greater control over which branches/tags are exposed as fileserver environments. Exact matches, globs, and regular expressions are supported, and are evaluated in that order. If using a regular expression, <code>^</code> and <code>$</code> must be omitted, and the expression must match the entire branch/tag. </p>
<pre>
gitfs_env_whitelist:
  - base
  - v1.*
  - 'mybranch\d+'
</pre>
<p> <code>NOTE:</code> <code>v1.*</code>, in this example, will match as both a glob and a regular expression (though it will have been matched as a glob, since globs are evaluated before regular expressions). </p>
<p> The behavior of the blacklist/whitelist will differ depending on which combination of the two options is used:</p>
<dl>
<dt>&bull;</p>
<dd> If only <code>gitfs_env_whitelist</code> is used, then <code>only</code> branches/tags which match the whitelist will be available as environments</p>
<dt>&bull;</p>
<dd> If only <code>gitfs_env_blacklist</code> is used, then the branches/tags which match the blacklist will <code>not</code> be available as environments</p>
<dt>&bull;</p>
<dd> If both are used, then the branches/tags which match the whitelist, but do <code>not</code> match the blacklist, will be available as environments.</dl>
<h3>Authentication</h3>
<h3>pygit2</h3>
<p> New in version 2014.7.0. </p>
<p> Both HTTPS and SSH authentication are supported as of version 0.20.3, which is the earliest version of <i>pygit2</i> supported by Salt for gitfs. </p>
<p> <code>NOTE:</code> The examples below make use of per-remote configuration parameters, a feature new to Salt 2014.7.0. More information on these can be found <i>here</i>.</p>
<h3>HTTPS</h3>
<p> For HTTPS repositories which require authentication, the username and password can be provided like so: </p>
<pre>
gitfs_remotes:
  - <a rel="nofollow noopener" href="https://domain.tld/myrepo.git:" target="_blank">https://domain.tld/myrepo.git:</a>
    - user: git
    - password: mypassword
</pre>
<p> If the repository is served over HTTP instead of HTTPS, then Salt will by default refuse to authenticate to it. This behavior can be overridden by adding an <code>insecure_auth</code> parameter: </p>
<pre>
gitfs_remotes:
  - <a rel="nofollow noopener" href="http://domain.tld/insecure_repo.git:" target="_blank">http://domain.tld/insecure_repo.git:</a>
    - user: git
    - password: mypassword
    - insecure_auth: True
</pre>
<h3>SSH</h3>
<p> SSH repositories can be configured using the <code>ssh://</code> protocol designation, or using scp-like syntax. So, the following two configurations are equivalent:</p>
<dl>
<dt>&bull;</p>
<dd> <code><a href="ssh://git@github.com/user/repo.git" rel="nofollow noopener" target="_blank">ssh://git@github.com/user/repo.git</a></code></p>
<dt>&bull;</p>
<dd> <code>git [at] github.com:user/repo.git</code> </p>
<p> Both <code>gitfs_pubkey</code> and <code>gitfs_privkey</code> (or their <i>per-remote counterparts</i>) must be configured in order to authenticate to SSH-based repos. If the private key is protected with a passphrase, it can be configured using <code>gitfs_passphrase</code> (or simply <code>passphrase</code> if being configured <i>per-remote</i>). For example: </p>
<pre>
gitfs_remotes:
  - git [at] github.com:user/repo.git:
    - pubkey: /root/.ssh/id_rsa.pub
    - privkey: /root/.ssh/id_rsa
    - passphrase: myawesomepassphrase
</pre>
<p> Finally, the SSH host key must be <i>added to the known_hosts file</i>.</dl>
<h3>GitPython</h3>
<p> With <i>GitPython</i>, only passphrase-less SSH public key authentication is supported. <code>The auth parameters (pubkey, privkey, etc.) shown in the pygit2 authentication examples above do not work with GitPython.</code> </p>
<pre>
gitfs_remotes:
  - <a href="ssh://git@github.com/example/salt-states.git" rel="nofollow noopener" target="_blank">ssh://git@github.com/example/salt-states.git</a>
</pre>
<p> Since <i>GitPython</i> wraps the git CLI, the private key must be located in <code>~/.ssh/id_rsa</code> for the user under which the Master is running, and should have permissions of <code>0600</code>. Also, in the absence of a user in the repo URL, <i>GitPython</i> will (just as SSH does) attempt to login as the current user (in other words, the user under which the Master is running, usually <code>root</code>). </p>
<p> If a key needs to be used, then <code>~/.ssh/config</code> can be configured to use the desired key. Information on how to do this can be found by viewing the manpage for <code>ssh_config</code>. Here&#8217;s an example entry which can be added to the <code>~/.ssh/config</code> to use an alternate key for gitfs: </p>
<pre>
Host github.com
    IdentityFile /root/.ssh/id_rsa_gitfs
</pre>
<p> The <code>Host</code> parameter should be a hostname (or hostname glob) that matches the domain name of the git repository. </p>
<p> It is also necessary to <i>add the SSH host key to the known_hosts file</i>. The exception to this would be if strict host key checking is disabled, which can be done by adding <code>StrictHostKeyChecking no</code> to the entry in <code>~/.ssh/config</code> </p>
<pre>
Host github.com
    IdentityFile /root/.ssh/id_rsa_gitfs
    StrictHostKeyChecking no
</pre>
<p> However, this is generally regarded as insecure, and is not recommended.</p>
<h3>Adding the SSH Host Key to the known_hosts File</h3>
<p> To use SSH authentication, it is necessary to have the remote repository&#8217;s SSH host key in the <code>~/.ssh/known_hosts</code> file. If the master is also a minion, this can be done using the <code>ssh.set_known_host</code> function: </p>
<p>#salt mymaster ssh.set_known_host user = root hostname = github.com<br />
mymaster : &#8212; &#8212; &#8212; &#8212; &#8211;new : &#8212; &#8212; &#8212; &#8212; &#8211;enc : ssh &#8211; rsa<br />
                                                             fingerprint : 16 : 27 : ac : a5 : 76 : 28 : 2d : 36 : 63 : 1b : 56 : 4d : eb : df : a6 : 48 hostname : |<br />
                                                                                                                                                                    1 | OiefWWqOD4kwO3BhoIGa0loR5AA = | BIXVtmcTbPER + 68HvXmceodDcfI =<br />
                                                                                                                                                                                                          key : AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa + PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31 / yMf + Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB + weqqUUmpaaasXVal72J + UX2B + 2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi / w4yCE6gbODqnTWlg7 + wC604ydGXA8VJiS5ap43JXiUFFAaQ ==<br />
                                                                                                                                                                                                          old : None<br />
                                                                                                                                                                                                                    status : updated</p>
<p> If not, then the easiest way to add the key is to su to the user (usually <code>root</code>) under which the salt-master runs and attempt to login to the server via SSH: </p>
<pre>
$ su
Password:
# ssh github.com
The authenticity of host 'github.com (192.30.252.128)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.128' (RSA) to the list of known hosts.
Permission denied (publickey).
</pre>
<p> It doesn&#8217;t matter if the login was successful, as answering <code>yes</code> will write the fingerprint to the known_hosts file.</p>
<h3>Verifying the Fingerprint</h3>
<p> To verify that the correct fingerprint was added, it is a good idea to look it up. One way to do this is to use nmap: </p>
<pre>
$ nmap github.com --script ssh-hostkey
Starting Nmap 5.51 ( <a rel="nofollow noopener" href="http://nmap.org" target="_blank">http://nmap.org</a> ) at 2014-08-18 17:47 CDT
Nmap scan report for github.com (192.30.252.129)
Host is up (0.17s latency).
Not shown: 996 filtered ports
PORT     STATE SERVICE
22/tcp   open  ssh
| ssh-hostkey: 1024 ad:1c:08:a4:40:e3:6f:9c:f5:66:26:5d:4b:33:5d:8c (DSA)
|_2048 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48 (RSA)
80/tcp   open  http
443/tcp  open  https
9418/tcp open  git
Nmap done: 1 IP address (1 host up) scanned in 28.78 seconds
</pre>
<p> Another way is to check one&#8217;s own known_hosts file, using this one-liner: </p>
<pre>
$ ssh-keygen -l -f /dev/stdin &lt;&lt;&lt;`ssh-keyscan -t rsa github.com 2&gt;/dev/null` | awk '{print $2}'
16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48
</pre>
<h3>Refreshing gitfs Upon Push</h3>
<p> By default, Salt updates the remote fileserver backends every 60 seconds. However, if it is desirable to refresh quicker than that, the Reactor System can be used to signal the master to update the fileserver on each push, provided that the git server is also a Salt minion. There are three steps to this process:</p>
<dl>
<dt>1.</p>
<dd> On the master, create a file <code>/srv/reactor/update_fileserver.sls</code>, with the following contents: </p>
<pre>
update_fileserver:
  runner.fileserver.update
</pre>
<dt>2.</p>
<dd> Add the following reactor configuration to the master config file: </p>
<pre>
reactor:
  - 'salt/fileserver/gitfs/update':
    - /srv/reactor/update_fileserver.sls
</pre>
<dt>3.</p>
<dd> On the git server, add a <i>post-receive hook</i> with the following contents: </p>
<pre>
#!/usr/bin/env sh
salt-call event.fire_master update salt/fileserver/gitfs/update
</pre>
<p> The <code>update</code> argument right after <code>event.fire_master</code> in this example can really be anything, as it represents the data being passed in the event, and the passed data is ignored by this reactor. </p>
<p> Similarly, the tag name <code>salt/fileserver/gitfs/update</code> can be replaced by anything, so long as the usage is consistent.</dl>
<h3>Using Git as an External Pillar Source</h3>
<p> Git repositories can also be used to provide <code>Pillar</code> data, using the <code>External Pillar</code> system. Note that this is different from gitfs, and is not yet at feature parity with it. </p>
<p> To define a git external pillar, add a section like the following to the salt master config file: </p>
<pre>
ext_pillar:
  - git: &lt;branch&gt; &lt;repo&gt; [root=&lt;gitroot&gt;]
</pre>
<p> Changed in version 2014.7.0: The optional <code>root</code> parameter was added </p>
<p> The <code>&lt;branch&gt;</code> param is the branch containing the pillar SLS tree. The <code>&lt;repo&gt;</code> param is the URI for the repository. To add the <code>master</code> branch of the specified repo as an external pillar source: </p>
<pre>
ext_pillar:
  - git: master <a rel="nofollow noopener" href="https://domain.com/pillar.git" target="_blank">https://domain.com/pillar.git</a>
</pre>
<p> Use the <code>root</code> parameter to use pillars from a subdirectory of a git repository: </p>
<pre>
ext_pillar:
  - git: master <a rel="nofollow noopener" href="https://domain.com/pillar.git" target="_blank">https://domain.com/pillar.git</a> root=subdirectory
</pre>
<p> More information on the git external pillar can be found in the <code>salt.pillar.git_pillar docs</code>.</p>
<h3>Why aren&#8217;t my custom modules/states/etc. syncing to my Minions?</h3>
<p> In versions 0.16.3 and older, when using the <code>git fileserver backend</code>, certain versions of GitPython may generate errors when fetching, which Salt fails to catch. While not fatal to the fetch process, these interrupt the fileserver update that takes place before custom types are synced, and thus interrupt the sync itself. Try disabling the git fileserver backend in the master config, restarting the master, and attempting the sync again. </p>
<p> This issue is worked around in Salt 0.16.4 and newer.</p>
<h3>The MacOS X (Maverick) Developer Step By Step Guide To Salt Installation</h3>
<p> This document provides a step-by-step guide to installing a Salt cluster consisting of one master, and one minion running on a local VM hosted on Mac OS X. </p>
<p> <code>NOTE:</code> This guide is aimed at developers who wish to run Salt in a virtual machine. The official (Linux) walkthrough can be found <i>here</i>.</p>
<h3>The 5 Cent Salt Intro</h3>
<p> Since you&#8217;re here you&#8217;ve probably already heard about Salt, so you already know Salt lets you configure and run commands on hordes of servers easily. Here&#8217;s a brief overview of a Salt cluster:</p>
<dl>
<dt>&bull;</p>
<dd> Salt works by having a &quot;master&quot; server sending commands to one or multiple &quot;minion&quot; servers [1]. The master server is the &quot;command center&quot;. It is going to be the place where you store your configuration files, aka: &quot;which server is the db, which is the web server, and what libraries and software they should have installed&quot;. The minions receive orders from the master. Minions are the servers actually performing work for your business.</p>
<dt>&bull;</p>
<dd> Salt has two types of configuration files: </p>
<p> 1. the &quot;salt communication channels&quot; or &quot;meta&quot; or &quot;config&quot; configuration files (not official names): one for the master (usually is /etc/salt/master , <code>on the master server</code>), and one for minions (default is /etc/salt/minion or /etc/salt/minion.conf, <code>on the minion servers</code>). Those files are used to determine things like the Salt Master IP, port, Salt folder locations, etc.. If these are configured incorrectly, your minions will probably be unable to receive orders from the master, or the master will not know which software a given minion should install. </p>
<p> 2. the &quot;business&quot; or &quot;service&quot; configuration files (once again, not an official name): these are configuration files, ending with &quot;.sls&quot; extension, that describe which software should run on which server, along with particular configuration properties for the software that is being installed. These files should be created in the /srv/salt folder by default, but their location can be changed using &#8230; /etc/salt/master configuration file! </p>
<p> <code>NOTE:</code> This tutorial contains a third important configuration file, not to be confused with the previous two: the virtual machine provisioning configuration file. This in itself is not specifically tied to Salt, but it also contains some Salt configuration. More on that in step 3. Also note that all configuration files are YAML files. So indentation matters.</p>
<dt>[1]</p>
<dd> Salt also works with &quot;masterless&quot; configuration where a minion is autonomous (in which case salt can be seen as a local configuration tool), or in &quot;multiple master&quot; configuration. See the documentation for more on that.</dl>
<h3>Before Digging In, The Architecture Of The Salt Cluster</h3>
<h3>Salt Master</h3>
<p> The &quot;Salt master&quot; server is going to be the Mac OS machine, directly. Commands will be run from a terminal app, so Salt will need to be installed on the Mac. This is going to be more convenient for toying around with configuration files.</p>
<h3>Salt Minion</h3>
<p> We&#8217;ll only have one &quot;Salt minion&quot; server. It is going to be running on a Virtual Machine running on the Mac, using VirtualBox. It will run an Ubuntu distribution.</p>
<h3>Step 1 &#8211; Configuring The Salt Master On Your Mac</h3>
<p> <i>official documentation</i> </p>
<p> Because Salt has a lot of dependencies that are not built in Mac OS X, we will use Homebrew to install Salt. Homebrew is a package manager for Mac, it&#8217;s great, use it (for this tutorial at least!). Some people spend a lot of time installing libs by hand to better understand dependencies, and then realize how useful a package manager is once they&#8217;re configuring a brand new machine and have to do it all over again. It also lets you <i>uninstall</i> things easily. </p>
<p> <code>NOTE:</code> Brew is a Ruby program (Ruby is installed by default with your Mac). Brew downloads, compiles, and links software. The linking phase is when compiled software is deployed on your machine. It may conflict with manually installed software, especially in the /usr/local directory. It&#8217;s ok, remove the manually installed version then refresh the link by typing <code>brew link &#8216;packageName&#8217;</code>. Brew has a <code>brew doctor</code> command that can help you troubleshoot. It&#8217;s a great command, use it often. Brew requires xcode command line tools. When you run brew the first time it asks you to install them if they&#8217;re not already on your system. Brew installs software in /usr/local/bin (system bins are in /usr/bin). In order to use those bins you need your $PATH to search there first. Brew tells you if your $PATH needs to be fixed. </p>
<p> <code>TIP:</code> Use the keyboard shortcut <code>cmd + shift + period</code> in the &quot;open&quot; Mac OS X dialog box to display hidden files and folders, such as .profile.</p>
<h3>Install Homebrew</h3>
<p> Install Homebrew here <i><a rel="nofollow noopener" href="http://brew.sh/" target="_blank">http://brew.sh/</a></i> Or just type </p>
<pre>
ruby -e &quot;$(curl -fsSL <a rel="nofollow noopener" href="https://raw.github.com/Homebrew/homebrew/go/install)" target="_blank">https://raw.github.com/Homebrew/homebrew/go/install)</a>&quot;
</pre>
<p> Now type the following commands in your terminal (you may want to type <code>brew doctor</code> after each to make sure everything&#8217;s fine): </p>
<pre>
brew install python
brew install swig
brew install zmq
</pre>
<p> <code>NOTE:</code> zmq is ZeroMQ. It&#8217;s a fantastic library used for server to server network communication and is at the core of Salt efficiency.</p>
<h3>Install Salt</h3>
<p> You should now have everything ready to launch this command: </p>
<pre>
pip install salt
</pre>
<p> <code>NOTE:</code> There should be no need for <code>sudo pip install salt</code>. Brew installed Python for your user, so you should have all the access. In case you would like to check, type <code>which python</code> to ensure that it&#8217;s /usr/local/bin/python, and <code>which pip</code> which should be /usr/local/bin/pip. </p>
<p> Now type <code>python</code> in a terminal then, <code>import salt</code>. There should be no errors. Now exit the Python terminal using <code>exit()</code>.</p>
<h3>Create The Master Configuration</h3>
<p> If the default /etc/salt/master configuration file was not created, copy-paste it from here: <i><a rel="nofollow noopener" href="http://docs.saltstack.com/ref/configuration/examples.html#configuration-examples-master" target="_blank">http://docs.saltstack.com/ref/configuration/examples.html#configuration-examples-master</a></i> </p>
<p> <code>NOTE:</code> <code>/etc/salt/master</code> is a file, not a folder. </p>
<p> Salt Master configuration changes. The Salt master needs a few customization to be able to run on Mac OS X: </p>
<pre>
sudo launchctl limit maxfiles 4096 8192
</pre>
<p> In the /etc/salt/master file, change max_open_files to 8192 (or just add the line: <code>max_open_files: 8192</code> (no quote) if it doesn&#8217;t already exists). </p>
<p> You should now be able to launch the Salt master: </p>
<pre>
sudo salt-master --log-level=all
</pre>
<p> There should be no errors when running the above command. </p>
<p> <code>NOTE:</code> This command is supposed to be a daemon, but for toying around, we&#8217;ll keep it running on a terminal to monitor the activity. </p>
<p> Now that the master is set, let&#8217;s configure a minion on a VM.</p>
<h3>Step 2 &#8211; Configuring The Minion VM</h3>
<p> The Salt minion is going to run on a Virtual Machine. There are a lot of software options that let you run virtual machines on a mac, But for this tutorial we&#8217;re going to use VirtualBox. In addition to virtualBox, we will use Vagrant, which allows you to create the base VM configuration. </p>
<p> Vagrant lets you build ready to use VM images, starting from an OS image and customizing it using &quot;provisioners&quot;. In our case, we&#8217;ll use it to:</p>
<dl>
<dt>&bull;</p>
<dd> Download the base Ubuntu image</p>
<dt>&bull;</p>
<dd> Install salt on that Ubuntu image (Salt is going to be the &quot;provisioner&quot; for the VM).</p>
<dt>&bull;</p>
<dd> Launch the VM</p>
<dt>&bull;</p>
<dd> SSH into the VM to debug</p>
<dt>&bull;</p>
<dd> Stop the VM once you&#8217;re done.</dl>
<h3>Install VirtualBox</h3>
<p> Go get it here: <i><a rel="nofollow noopener" href="https://www.virtualBox.org/wiki/Downloads" target="_blank">https://www.virtualBox.org/wiki/Downloads</a></i> (click on VirtualBox for OS X hosts =&gt; x86/amd64)</p>
<h3>Install Vagrant</h3>
<p> Go get it here: <i><a rel="nofollow noopener" href="http://downloads.vagrantup.com/" target="_blank">http://downloads.vagrantup.com/</a></i> and choose the latest version (1.3.5 at time of writing), then the .dmg file. Double-click to install it. Make sure the <code>vagrant</code> command is found when run in the terminal. Type <code>vagrant</code>. It should display a list of commands.</p>
<h3>Create The Minion VM Folder</h3>
<p> Create a folder in which you will store your minion&#8217;s VM. In this tutorial, it&#8217;s going to be a minion folder in the $home directory. </p>
<pre>
cd $home
mkdir minion
</pre>
<h3>Initialize Vagrant</h3>
<p> From the minion folder, type </p>
<pre>
vagrant init
</pre>
<p> This command creates a default Vagrantfile configuration file. This configuration file will be used to pass configuration parameters to the Salt provisioner in Step 3.</p>
<h3>Import Precise64 Ubuntu Box</h3>
<pre>
vagrant box add precise64 <a rel="nofollow noopener" href="http://files.vagrantup.com/precise64.box" target="_blank">http://files.vagrantup.com/precise64.box</a>
</pre>
<p> <code>NOTE:</code> This box is added at the global Vagrant level. You only need to do it once as each VM will use this same file.</p>
<h3>Modify the Vagrantfile</h3>
<p> Modify ./minion/Vagrantfile to use th precise64 box. Change the <code>config.vm.box</code> line to: </p>
<pre>
config.vm.box = &quot;precise64&quot;
</pre>
<p> Uncomment the line creating a host-only IP. This is the ip of your minion (you can change it to something else if that IP is already in use): </p>
<pre>
config.vm.network :private_network, ip: &quot;192.168.33.10&quot;
</pre>
<p> At this point you should have a VM that can run, although there won&#8217;t be much in it. Let&#8217;s check that.</p>
<h3>Checking The VM</h3>
<p> From the $home/minion folder type: </p>
<pre>
vagrant up
</pre>
<p> A log showing the VM booting should be present. Once it&#8217;s done you&#8217;ll be back to the terminal: </p>
<pre>
ping 192.168.33.10
</pre>
<p> The VM should respond to your ping request. </p>
<p> Now log into the VM in ssh using Vagrant again: </p>
<pre>
vagrant ssh
</pre>
<p> You should see the shell prompt change to something similar to <code>vagrant [at] precise64:~$</code> meaning you&#8217;re inside the VM. From there, enter the following: </p>
<pre>
ping 10.0.2.2
</pre>
<p> <code>NOTE:</code> That ip is the ip of your VM host (the Mac OS X OS). The number is a VirtualBox default and is displayed in the log after the Vagrant ssh command. We&#8217;ll use that IP to tell the minion where the Salt master is. Once you&#8217;re done, end the ssh session by typing <code>exit</code>. </p>
<p> It&#8217;s now time to connect the VM to the salt master</p>
<h3>Step 3 &#8211; Connecting Master and Minion</h3>
<h3>Creating The Minion Configuration File</h3>
<p> Create the <code>/etc/salt/minion</code> file. In that file, put the following lines, giving the ID for this minion, and the IP of the master: </p>
<pre>
master: 10.0.2.2
id: 'minion1'
file_client: remote
</pre>
<p> Minions authenticate with the master using keys. Keys are generated automatically if you don&#8217;t provide one and can accept them later on. However, this requires accepting the minion key every time the minion is destroyed or created (which could be quite often). A better way is to create those keys in advance, feed them to the minion, and authorize them once.</p>
<h3>Preseed minion keys</h3>
<p> From the minion folder on your Mac run: </p>
<pre>
sudo salt-key --gen-keys=minion1
</pre>
<p> This should create two files: minion1.pem, and minion1.pub. Since those files have been created using sudo, but will be used by vagrant, you need to change ownership: </p>
<pre>
sudo chown youruser:yourgroup minion1.pem
sudo chown youruser:yourgroup minion1.pub
</pre>
<p> Then copy the .pub file into the list of accepted minions: </p>
<pre>
sudo cp minion1.pub /etc/salt/pki/master/minions/minion1
</pre>
<h3>Modify Vagrantfile to Use Salt Provisioner</h3>
<p> Let&#8217;s now modify the Vagrantfile used to provision the Salt VM. Add the following section in the Vagrantfile (note: it should be at the same indentation level as the other properties): </p>
<pre>
# salt-vagrant config
config.vm.provision :salt do |salt|
    salt.run_highstate = true
    salt.minion_config = &quot;/etc/salt/minion&quot;
    salt.minion_key = &quot;./minion1.pem&quot;
    salt.minion_pub = &quot;./minion1.pub&quot;
end
</pre>
<p> Now destroy the vm and recreate it from the /minion folder: </p>
<pre>
vagrant destroy
vagrant up
</pre>
<p> If everything is fine you should see the following message: </p>
<pre>
&quot;Bootstrapping Salt... (this may take a while)
Salt successfully configured and installed!&quot;
</pre>
<h3>Checking Master-Minion Communication</h3>
<p> To make sure the master and minion are talking to each other, enter the following: </p>
<pre>
sudo salt '*' test.ping
</pre>
<p> You should see your minion answering the ping. It&#8217;s now time to do some configuration.</p>
<h3>Step 4 &#8211; Configure Services to Install On the Minion</h3>
<p> In this step we&#8217;ll use the Salt master to instruct our minion to install Nginx.</p>
<h3>Checking the system&#8217;s original state</h3>
<p> First, make sure that an HTTP server is not installed on our minion. When opening a browser directed at <code><a rel="nofollow" href="http://192.168.33.10/">http://192.168.33.10/</a></code> You should get an error saying the site cannot be reached.</p>
<h3>Initialize the top.sls file</h3>
<p> System configuration is done in the /srv/salt/top.sls file (and subfiles/folders), and then applied by running the <code>state.highstate</code> command to have the Salt master give orders so minions will update their instructions and run the associated commands. </p>
<p> First Create an empty file on your Salt master (Mac OS X machine): </p>
<pre>
touch /srv/salt/top.sls
</pre>
<p> When the file is empty, or if no configuration is found for our minion an error is reported: </p>
<pre>
sudo salt 'minion1' state.highstate
</pre>
<p> Should return an error stating: &quot;No Top file or external nodes data matches found&quot;.</p>
<h3>Create The Nginx Configuration</h3>
<p> Now is finally the time to enter the real meat of our server&#8217;s configuration. For this tutorial our minion will be treated as a web server that needs to have Nginx installed. </p>
<p> Insert the following lines into the <code>/srv/salt/top.sls</code> file (which should current be empty). </p>
<pre>
base:
  'minion1':
    - bin.nginx
</pre>
<p> Now create a <code>/srv/salt/bin/nginx.sls</code> file containing the following: </p>
<pre>
nginx:
  pkg.installed:
    - name: nginx
  service.running:
    - enable: True
    - reload: True
</pre>
<h3>Check Minion State</h3>
<p> Finally run the state.highstate command again: </p>
<pre>
sudo salt 'minion1' state.highstate
</pre>
<p> You should see a log showing that the Nginx package has been installed and the service configured. To prove it, open your browser and navigate to <i><a rel="nofollow" href="http://192.168.33.10/">http://192.168.33.10/</a></i>, you should see the standard Nginx welcome page. </p>
<p> Congratulations!</p>
<h3>Where To Go From Here</h3>
<p> A full description of configuration management within Salt (sls files among other things) is available here: <i><a rel="nofollow noopener" href="http://docs.saltstack.com/index.html#configuration-management" target="_blank">http://docs.saltstack.com/index.html#configuration-management</a></i></p>
<h3>Writing Salt Tests</h3>
<p> <code>NOTE:</code> THIS TUTORIAL IS A WORK IN PROGRESS </p>
<p> Salt comes with a powerful integration and unit test suite. The test suite allows for the fully automated run of integration and/or unit tests from a single interface. The integration tests are surprisingly easy to write and can be written to be either destructive or non-destructive.</p>
<h3>Getting Set Up For Tests</h3>
<p> To walk through adding an integration test, start by getting the latest development code and the test system from GitHub: </p>
<p> <code>NOTE:</code> The develop branch often has failing tests and should always be considered a staging area. For a checkout that tests should be running perfectly on, please check out a specific release tag (such as v2014.1.4). </p>
<pre>
git clone git [at] github.com:saltstack/salt.git
pip install git+<a rel="nofollow noopener" href="https://github.com/saltstack/salt-testing.git#egg=SaltTesting" target="_blank">https://github.com/saltstack/salt-testing.git#egg=SaltTesting</a>
</pre>
<p> Now that a fresh checkout is available run the test suite</p>
<h3>Destructive vs Non-destructive</h3>
<p> Since Salt is used to change the settings and behavior of systems, often, the best approach to run tests is to make actual changes to an underlying system. This is where the concept of destructive integration tests comes into play. Tests can be written to alter the system they are running on. This capability is what fills in the gap needed to properly test aspects of system management like package installation. </p>
<p> To write a destructive test import and use the <i>destructiveTest</i> decorator for the test method: </p>
<pre>
import integration
from salttesting.helpers import destructiveTest
class PkgTest(integration.ModuleCase):
    @destructiveTest
    def test_pkg_install(self):
        ret = self.run_function('pkg.install', name='finch')
        self.assertSaltTrueReturn(ret)
        ret = self.run_function('pkg.purge', name='finch')
        self.assertSaltTrueReturn(ret)
</pre>
<h3>Automated Test Runs</h3>
<p> SaltStack maintains a Jenkins server which can be viewed at <i><a rel="nofollow noopener" href="http://jenkins.saltstack.com" target="_blank">http://jenkins.saltstack.com</a></i>. The tests executed from this Jenkins server create fresh virtual machines for each test run, then execute the destructive tests on the new clean virtual machine. This allows for the execution of tests across supported platforms.</p>
<h3>HTTP Modules</h3>
<p> This tutorial demonstrates using the various HTTP modules available in Salt. These modules wrap the Python <code>urllib2</code> and <code>requests</code> libraries, extending them in a manner that is more consistent with Salt workflows.</p>
<h3>The <code>salt.utils.http</code> Library</h3>
<p> This library forms the core of the HTTP modules. Since it is designed to be used from the minion as an execution module, in addition to the master as a runner, it was abstracted into this multi-use library. This library can also be imported by 3rd-party programs wishing to take advantage of its extended functionality. </p>
<p> Core functionality of the execution, state, and runner modules is derived from this library, so common usages between them are described here. Documentation specific to each module is described below. </p>
<p> This library can be imported with: </p>
<pre>
import salt.utils.http
</pre>
<h3>Configuring Libraries</h3>
<p> This library can make use of either <code>urllib2</code>, which ships with Python, or <code>requests</code>, which can be installed separately. By default, <code>urllib2</code> will be used. In order to switch to <code>requests</code>, set the following variable: </p>
<pre>
requests_lib: True
</pre>
<p> This can be set in the master or minion configuration file, or passed as an option directly to any <code>http.query()</code> functions.</p>
<h3><code>salt.utils.http.query()</code></h3>
<p> This function forms a basic query, but with some add-ons not present in the <code>urllib2</code> and <code>requests</code> libraries. Not all functionality currently available in these libraries has been added, but can be in future iterations. </p>
<p> A basic query can be performed by calling this function with no more than a single URL: </p>
<pre>
salt.utils.http.query('<a rel="nofollow" href="http://example.com&#039;)">http://example.com')</a>
</pre>
<p> By default the query will be performed with a <code>GET</code> method. The method can be overridden with the <code>method</code> argument: </p>
<pre>
salt.utils.http.query('<a rel="nofollow noopener" href="http://example.com/delete/url&#039;," target="_blank">http://example.com/delete/url',</a> 'DELETE')
</pre>
<p> When using the <code>POST</code> method (and others, such as <code>PUT</code>), extra data is usually sent as well. This data can be sent directly, in whatever format is required by the remote server (XML, JSON, plain text, etc). </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow noopener" href="http://example.com/delete/url&#039;," target="_blank">http://example.com/delete/url',</a>
    method='POST',
    data=json.loads(mydict)
)
</pre>
<p> Bear in mind that this data must be sent pre-formatted; this function will not format it for you. However, a templated file stored on the local system may be passed through, along with variables to populate it with. To pass through only the file (untemplated): </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow noopener" href="http://example.com/post/url&#039;," target="_blank">http://example.com/post/url',</a>
    method='POST',
    data_file='/srv/salt/somefile.xml'
)
</pre>
<p> To pass through a file that contains jinja + yaml templating (the default): </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow noopener" href="http://example.com/post/url&#039;," target="_blank">http://example.com/post/url',</a>
    method='POST',
    data_file='/srv/salt/somefile.jinja',
    data_render=True,
    template_data={'key1': 'value1', 'key2': 'value2'}
)
</pre>
<p> To pass through a file that contains mako templating: </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow noopener" href="http://example.com/post/url&#039;," target="_blank">http://example.com/post/url',</a>
    method='POST',
    data_file='/srv/salt/somefile.mako',
    data_render=True,
    data_renderer='mako',
    template_data={'key1': 'value1', 'key2': 'value2'}
)
</pre>
<p> Because this function uses Salt&#8217;s own rendering system, any Salt renderer can be used. Because Salt&#8217;s renderer requires <code>__opts__</code> to be set, an <code>opts</code> dictionary should be passed in. If it is not, then the default <code>__opts__</code> values for the node type (master or minion) will be used. Because this library is intended primarily for use by minions, the default node type is <code>minion</code>. However, this can be changed to <code>master</code> if necessary. </p>
<p>salt.utils.http.query(<br />
                   &#8216;http://example.com/post/url&#8217;,<br />
                   method = &#8216;POST&#8217;,<br />
                   data_file = &#8216;/srv/salt/somefile.jinja&#8217;,<br />
                   data_render = True,<br />
                   template_data = {&#8216;key1&#8217; : &#8216;value1&#8217;, &#8216;key2&#8217; : &#8216;value2&#8217;},<br />
                   opts = __opts__)<br />
    salt.utils.http.query(<br />
        &#8216;http://example.com/post/url&#8217;,<br />
        method = &#8216;POST&#8217;,<br />
        data_file = &#8216;/srv/salt/somefile.jinja&#8217;,<br />
        data_render = True,<br />
        template_data = {&#8216;key1&#8217; : &#8216;value1&#8217;, &#8216;key2&#8217; : &#8216;value2&#8217;},<br />
        node = &#8216;master&#8217;)</p>
<p> Headers may also be passed through, either as a <code>header_list</code>, a <code>header_dict</code>, or as a <code>header_file</code>. As with the <code>data_file</code>, the <code>header_file</code> may also be templated. Take note that because HTTP headers are normally syntactically-correct YAML, they will automatically be imported as an a Python dict. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow noopener" href="http://example.com/delete/url&#039;," target="_blank">http://example.com/delete/url',</a>
    method='POST',
    header_file='/srv/salt/headers.jinja',
    header_render=True,
    header_renderer='jinja',
    template_data={'key1': 'value1', 'key2': 'value2'}
)
</pre>
<p> Because much of the data that would be templated between headers and data may be the same, the <code>template_data</code> is the same for both. Correcting possible variable name collisions is up to the user. </p>
<p> The <code>query()</code> function supports basic HTTP authentication. A username and password may be passed in as <code>username</code> and <code>password</code>, respectively. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    username='larry',
    password=`5700g3543v4r`,
)
</pre>
<p> Cookies are also supported, using Python&#8217;s built-in <code>cookielib</code>. However, they are turned off by default. To turn cookies on, set <code>cookies</code> to True. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    cookies=True
)
</pre>
<p> By default cookies are stored in Salt&#8217;s cache directory, normally <code>/var/cache/salt</code>, as a file called <code>cookies.txt</code>. However, this location may be changed with the <code>cookie_jar</code> argument: </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    cookies=True,
    cookie_jar='/path/to/cookie_jar.txt'
)
</pre>
<p> By default, the format of the cookie jar is LWP (aka, lib-www-perl). This default was chosen because it is a human-readable text file. If desired, the format of the cookie jar can be set to Mozilla: </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    cookies=True,
    cookie_jar='/path/to/cookie_jar.txt',
    cookie_format='mozilla'
)
</pre>
<p> Because Salt commands are normally one-off commands that are piped together, this library cannot normally behave as a normal browser, with session cookies that persist across multiple HTTP requests. However, the session can be persisted in a separate cookie jar. The default filename for this file, inside Salt&#8217;s cache directory, is <code>cookies.session.p</code>. This can also be changed. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    persist_session=True,
    session_cookie_jar='/path/to/jar.p'
)
</pre>
<p> The format of this file is msgpack, which is consistent with much of the rest of Salt&#8217;s internal structure. Historically, the extension for this file is <code>.p</code>. There are no current plans to make this configurable.</p>
<h3>Return Data</h3>
<p> By default, <code>query()</code> will attempt to decode the return data. Because it was designed to be used with REST interfaces, it will attempt to decode the data received from the remote server. First it will check the <code>Content-type</code> header to try and find references to XML. If it does not find any, it will look for references to JSON. If it does not find any, it will fall back to plain text, which will not be decoded. </p>
<p> JSON data is translated into a dict using Python&#8217;s built-in <code>json</code> library. XML is translated using <code>salt.utils.xml_util</code>, which will use Python&#8217;s built-in XML libraries to attempt to convert the XML into a dict. In order to force either JSON or XML decoding, the <code>decode_type</code> may be set: </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    decode_type='xml'
)
</pre>
<p> Once translated, the return dict from <code>query()</code> will include a dict called <code>dict</code>. </p>
<p> If the data is not to be translated using one of these methods, decoding may be turned off. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    decode=False
)
</pre>
<p> If decoding is turned on, and references to JSON or XML cannot be found, then this module will default to plain text, and return the undecoded data as <code>text</code> (even if text is set to <code>False</code>; see below). </p>
<p> The <code>query()</code> function can return the HTTP status code, headers, and/or text as required. However, each must individually be turned on. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    status=True,
    headers=True,
    text=True
)
</pre>
<p> The return from these will be found in the return dict as <code>status</code>, <code>headers</code> and <code>text</code>, respectively.</p>
<h3>Writing Return Data to Files</h3>
<p> It is possible to write either the return data or headers to files, as soon as the response is received from the server, but specifying file locations via the <code>text_out</code> or <code>headers_out</code> arguments. <code>text</code> and <code>headers</code> do not need to be returned to the user in order to do this. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="http://example.com&#039;,">http://example.com',</a>
    text=False,
    headers=False,
    text_out='/path/to/url_download.txt',
    headers_out='/path/to/headers_download.txt',
)
</pre>
<h3>SSL Verification</h3>
<p> By default, this function will verify SSL certificates. However, for testing or debugging purposes, SSL verification can be turned off. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="https://example.com&#039;,">https://example.com',</a>
    verify_ssl=False,
)
</pre>
<h3>CA Bundles</h3>
<p> The <code>requests</code> library has its own method of detecting which CA (certficate authority) bundle file to use. Usually this is implemented by the packager for the specific operating system distribution that you are using. However, <code>urllib2</code> requires a little more work under the hood. By default, Salt will try to auto-detect the location of this file. However, if it is not in an expected location, or a different path needs to be specified, it may be done so using the <code>ca_bundle</code> variable. </p>
<pre>
salt.utils.http.query(
    '<a rel="nofollow" href="https://example.com&#039;,">https://example.com',</a>
    ca_bundle='/path/to/ca_bundle.pem',
)
</pre>
<h3>Updating CA Bundles</h3>
<p> The <code>update_ca_bundle()</code> function can be used to update the bundle file at a specified location. If the target location is not specified, then it will attempt to auto-detect the location of the bundle file. If the URL to download the bundle from does not exist, a bundle will be downloaded from the cURL website. </p>
<p> CAUTION: The <code>target</code> and the <code>source</code> should always be specified! Failure to specify the <code>target</code> may result in the file being written to the wrong location on the local system. Failure to specify the <code>source</code> may cause the upstream URL to receive excess unnecessary traffic, and may cause a file to be download which is hazardous or does not meet the needs of the user. </p>
<pre>
salt.utils.http.update_ca_bundle(
    target='/path/to/ca-bundle.crt',
    source='<a rel="nofollow noopener" href="https://example.com/path/to/ca-bundle.crt&#039;," target="_blank">https://example.com/path/to/ca-bundle.crt',</a>
    opts=__opts__,
)
</pre>
<p> The <code>opts</code> parameter should also always be specified. If it is, then the <code>target</code> and the <code>source</code> may be specified in the relevant configuration file (master or minion) as <code>ca_bundle</code> and <code>ca_bundle_url</code>, respectively. </p>
<pre>
ca_bundle: /path/to/ca-bundle.crt
ca_bundle_url: <a rel="nofollow noopener" href="https://example.com/path/to/ca-bundle.crt" target="_blank">https://example.com/path/to/ca-bundle.crt</a>
</pre>
<p> If Salt is unable to auto-detect the location of the CA bundle, it will raise an error. </p>
<p> The <code>update_ca_bundle()</code> function can also be passed a string or a list of strings which represent files on the local system, which should be appended (in the specified order) to the end of the CA bundle file. This is useful in environments where private certs need to be made available, and are not otherwise reasonable to add to the bundle file. </p>
<pre>
salt.utils.http.update_ca_bundle(
    opts=__opts__,
    merge_files=[
        '/etc/ssl/private_cert_1.pem',
        '/etc/ssl/private_cert_2.pem',
        '/etc/ssl/private_cert_3.pem',
    ]
)
</pre>
<h3>Test Mode</h3>
<p> This function may be run in test mode. This mode will perform all work up until the actual HTTP request. By default, instead of performing the request, an empty dict will be returned. Using this function with <code>TRACE</code> logging turned on will reveal the contents of the headers and POST data to be sent. </p>
<p> Rather than returning an empty dict, an alternate <code>test_url</code> may be passed in. If this is detected, then test mode will replace the <code>url</code> with the <code>test_url</code>, set <code>test</code> to <code>True</code> in the return data, and perform the rest of the requested operations as usual. This allows a custom, non-destructive URL to be used for testing when necessary.</p>
<h3>Execution Module</h3>
<p> The <code>http</code> execution module is a very thin wrapper around the <code>salt.utils.http</code> library. The <code>opts</code> can be passed through as well, but if they are not specified, the minion defaults will be used as necessary. </p>
<p> Because passing complete data structures from the command line can be tricky at best and dangerous (in terms of execution injection attacks) at worse, the <code>data_file</code>, and <code>header_file</code> are likely to see more use here. </p>
<p> All methods for the library are available in the execution module, as kwargs. </p>
<pre>
salt myminion http.query <a rel="nofollow noopener" href="http://example.com/restapi" target="_blank">http://example.com/restapi</a> method=POST \
    username='larry' password='5700g3543v4r' headers=True text=True \
    status=True decode_type=xml data_render=True \
    header_file=/tmp/headers.txt data_file=/tmp/data.txt \
    header_render=True cookies=True persist_session=True
</pre>
<h3>Runner Module</h3>
<p> Like the execution module, the <code>http</code> runner module is a very thin wrapper around the <code>salt.utils.http</code> library. The only significant difference is that because runners execute on the master instead of a minion, a target is not required, and default opts will be derived from the master config, rather than the minion config. </p>
<p> All methods for the library are available in the runner module, as kwargs. </p>
<pre>
salt-run http.query <a rel="nofollow noopener" href="http://example.com/restapi" target="_blank">http://example.com/restapi</a> method=POST \
    username='larry' password='5700g3543v4r' headers=True text=True \
    status=True decode_type=xml data_render=True \
    header_file=/tmp/headers.txt data_file=/tmp/data.txt \
    header_render=True cookies=True persist_session=True
</pre>
<h3>State Module</h3>
<p> The state module is a wrapper around the runner module, which applies stateful logic to a query. All kwargs as listed above are specified as usual in state files, but two more kwargs are available to apply stateful logic. A required parameter is <code>match</code>, which specifies a pattern to look for in the return text. By default, this will perform a string comparison of looking for the value of match in the return text. In Python terms this looks like: </p>
<pre>
if match in html_text:
    return True
</pre>
<p> If more complex pattern matching is required, a regular expression can be used by specifying a <code>match_type</code>. By default this is set to <code>string</code>, but it can be manually set to <code>pcre</code> instead. Please note that despite the name, this will use Python&#8217;s <code>re.search()</code> rather than <code>re.match()</code>. </p>
<p> Therefore, the following states are valid: </p>
<pre>
<a rel="nofollow noopener" href="http://example.com/restapi:" target="_blank">http://example.com/restapi:</a>
  http.query:
    - match: 'SUCCESS'
    - username: 'larry'
    - password: '5700g3543v4r'
    - data_render: True
    - header_file: /tmp/headers.txt
    - data_file: /tmp/data.txt
    - header_render: True
    - cookies: True
    - persist_session: True
<a rel="nofollow noopener" href="http://example.com/restapi:" target="_blank">http://example.com/restapi:</a>
  http.query:
    - match_type: pcre
    - match: '(?i)succe[ss|ed]'
    - username: 'larry'
    - password: '5700g3543v4r'
    - data_render: True
    - header_file: /tmp/headers.txt
    - data_file: /tmp/data.txt
    - header_render: True
    - cookies: True
    - persist_session: True
</pre>
<p> In addition to, or instead of a match pattern, the status code for a URL can be checked. This is done using the <code>status</code> argument: </p>
<pre>
<a rel="nofollow noopener" href="http://example.com/:" target="_blank">http://example.com/:</a>
  http.query:
    - status: '200'
</pre>
<p> If both are specified, both will be checked, but if only one is <code>True</code> and the other is <code>False</code>, then <code>False</code> will be returned. In this case, the comments in the return data will contain information for troubleshooting. </p>
<p> Because this is a monitoring state, it will return extra data to code that expects it. This data will always include <code>text</code> and <code>status</code>. Optionally, <code>headers</code> and <code>dict</code> may also be requested by setting the <code>headers</code> and <code>decode</code> arguments to True, respectively.</p>
<h3>LXC Management with Salt</h3>
<p> <code>NOTE:</code> This walkthrough assumes basic knowledge of Salt. To get up to speed, check out the <code>Salt Walkthrough</code>.</p>
<h3>Dependencies</h3>
<p> Manipulation of LXC containers in Salt requires the minion to have an LXC version of at least 1.0 (an alpha or beta release of LXC 1.0 is acceptable). The following distributions are known to have new enough versions of LXC packaged:</p>
<dl>
<dt>&bull;</p>
<dd> RHEL/CentOS 6 and later (via <i>EPEL</i>)</p>
<dt>&bull;</p>
<dd> Fedora (All non-EOL releases)</p>
<dt>&bull;</p>
<dd> Debian 8.0 (Jessie)</p>
<dt>&bull;</p>
<dd> Ubuntu 14.04 LTS and later (LXC templates are packaged separately as <code>lxc-templates</code>, it is recommended to also install this package)</p>
<dt>&bull;</p>
<dd> openSUSE 13.2 and later</dl>
<h3>Profiles</h3>
<p> Profiles allow for a sort of shorthand for commonly-used configurations to be defined in the minion config file, grains, pillar, or the master config file. The profile is retrieved by Salt using the <code>config.get</code> function, which looks in those locations, in that order. This allows for profiles to be defined centrally in the master config file, with several options for overriding them (if necessary) on groups of minions or individual minions. </p>
<p> There are two types of profiles:</p>
<dl>
<dt>&bull;</p>
<dd> One for defining the parameters used in container creation/clone.</p>
<dt>&bull;</p>
<dd> One for defining the container&#8217;s network interface(s) settings.</dl>
<h3>Container Profiles</h3>
<p> LXC container profiles are defined defined underneath the <code>lxc.container_profile</code> config option: </p>
<pre>
lxc.container_profile:
  centos:
    template: centos
    backing: lvm
    vgname: vg1
    lvname: lxclv
    size: 10G
  centos_big:
    template: centos
    backing: lvm
    vgname: vg1
    lvname: lxclv
    size: 20G
</pre>
<p> Profiles are retrieved using the <code>config.get</code> function, with the <code>recurse</code> merge strategy. This means that a profile can be defined at a lower level (for example, the master config file) and then parts of it can be overridden at a higher level (for example, in pillar data). Consider the following container profile data: </p>
<p> <code>In the Master config file:</code> </p>
<pre>
lxc.container_profile:
  centos:
    template: centos
    backing: lvm
    vgname: vg1
    lvname: lxclv
    size: 10G
</pre>
<p> <code>In the Pillar data</code> </p>
<pre>
lxc.container_profile:
  centos:
    size: 20G
</pre>
<p> Any minion with the above Pillar data would have the <code>size</code> parameter in the <code>centos</code> profile overridden to 20G, while those minions without the above Pillar data would have the 10G <code>size</code> value. This is another way of achieving the same result as the <code>centos_big</code> profile above, without having to define another whole profile that differs in just one value. </p>
<p> <code>NOTE:</code> In the 2014.7.x release cycle and earlier, container profiles are defined under <code>lxc.profile</code>. This parameter will still work in version 2015.5.0, but is deprecated and will be removed in a future release. Please note however that the profile merging feature described above will only work with profiles defined under <code>lxc.container_profile</code>, and only in versions 2015.5.0 and later. </p>
<p> Additionally, in version 2015.5.0 container profiles have been expanded to support passing template-specific CLI options to <code>lxc.create</code>. Below is a table describing the parameters which can be configured in container profiles: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Parameter </td>
<td> 2015.5.0 and Newer </td>
<td> 2014.7.x and Earlier
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>template</i><font SIZE="-2">1</font> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>options</i><font SIZE="-2">1</font> </td>
<td> Yes </td>
<td> No
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>image</i><font SIZE="-2">1</font> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>backing</i> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>snapshot</i><font SIZE="-2">2</font> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>lvname</i><font SIZE="-2">1</font> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>fstype</i><font SIZE="-2">1</font> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>size</i> </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt>1.</p>
<dd> Parameter is only supported for container creation, and will be ignored if the profile is used when cloning a container.</p>
<dt>2.</p>
<dd> Parameter is only supported for container cloning, and will be ignored if the profile is used when not cloning a container.</dl>
<h3>Network Profiles</h3>
<p> LXC network profiles are defined defined underneath the <code>lxc.network_profile</code> config option. By default, the module uses a DHCP based configuration and try to guess a bridge to get connectivity. </p>
<p> <code>WARNING:</code> on pre <code>2015.5.2</code>, you need to specify explicitly the network bridge </p>
<pre>
lxc.network_profile:
  centos:
    eth0:
      link: br0
      type: veth
      flags: up
  ubuntu:
    eth0:
      link: lxcbr0
      type: veth
      flags: up
</pre>
<p> As with container profiles, network profiles are retrieved using the <code>config.get</code> function, with the <code>recurse</code> merge strategy. Consider the following network profile data: </p>
<p> <code>In the Master config file:</code> </p>
<pre>
lxc.network_profile:
  centos:
    eth0:
      link: br0
      type: veth
      flags: up
</pre>
<p> <code>In the Pillar data</code> </p>
<pre>
lxc.network_profile:
  centos:
    eth0:
      link: lxcbr0
</pre>
<p> Any minion with the above Pillar data would use the <code>lxcbr0</code> interface as the bridge interface for any container configured using the <code>centos</code> network profile, while those minions without the above Pillar data would use the <code>br0</code> interface for the same. </p>
<p> <code>NOTE:</code> In the 2014.7.x release cycle and earlier, network profiles are defined under <code>lxc.nic</code>. This parameter will still work in version 2015.5.0, but is deprecated and will be removed in a future release. Please note however that the profile merging feature described above will only work with profiles defined under <code>lxc.network_profile</code>, and only in versions 2015.5.0 and later. </p>
<p> The following are parameters which can be configured in network profiles. These will directly correspond to a parameter in an LXC configuration file (see <code>man 5 lxc.container.conf</code>).</p>
<dl>
<dt>&bull;</p>
<dd> <code>type</code> &#8211; Corresponds to <code>lxc.network.type</code></p>
<dt>&bull;</p>
<dd> <code>link</code> &#8211; Corresponds to <code>lxc.network.link</code></p>
<dt>&bull;</p>
<dd> <code>flags</code> &#8211; Corresponds to <code>lxc.network.flags</code> </p>
<p> Interface-specific options (MAC address, IPv4/IPv6, etc.) must be passed on a container-by-container basis, for instance using the <code>nic_opts</code> argument to <code>lxc.create</code>: </p>
<p>salt myminion lxc.create container1 profile = centos network_profile = centos nic_opts = &#8216;{eth0: {ipv4: 10.0.0.20/24, gateway: 10.0.0.1}}&#8217;</p>
<p> <code>WARNING:</code> The <code>ipv4</code>, <code>ipv6</code>, <code>gateway</code>, and <code>link</code> (bridge) settings in network profiles / nic_opts will only work if the container doesnt redefine the network configuration (for example in <code>/etc/sysconfig/network-scripts/ifcfg-&lt;interface_name&gt;</code> on RHEL/CentOS, or <code>/etc/network/interfaces</code> on Debian/Ubuntu/etc.). Use these with caution. The container images installed using the <code>download</code> template, for instance, typically are configured for eth0 to use DHCP, which will conflict with static IP addresses set at the container level.</dl>
<h3>Old lxc support (&lt;1.0.7)</h3>
<p> With saltstack <code>2015.5.2</code> and above, normally the setting is autoselected, but before, you&#8217;ll need to teach your network profile to set <code>lxc.network.ipv4.gateway</code> to <code>auto</code> when using a classic ipv4 configuration. </p>
<p> Thus you&#8217;ll need </p>
<pre>
lxc.network_profile.foo:
  etho:
    link: lxcbr0
    ipv4.gateway: auto
</pre>
<h3>Tricky network setups Examples</h3>
<p> This example covers how to make a container with both an internal ip and a public routable ip, wired on two veth pairs. </p>
<p> The another interface which receives directly a public routable ip can&#8217;t be on the first interface that we reserve for private inter LXC networking. </p>
<pre>
lxc.network_profile.foo:
  eth0: {gateway: null, bridge: lxcbr0}
  eth1:
    # replace that by your main interface
    'link': 'br0'
    'mac': '00:16:5b:01:24:e1'
    'gateway': '2.20.9.14'
    'ipv4': '2.20.9.1'
</pre>
<h3>Creating a Container on the CLI</h3>
<h3>From a Template</h3>
<p> LXC is commonly distributed with several template scripts in /usr/share/lxc/templates. Some distros may package these separately in an <code>lxc-templates</code> package, so make sure to check if this is the case. </p>
<p> There are LXC template scripts for several different operating systems, but some of them are designed to use tools specific to a given distribution. For instance, the <code>ubuntu</code> template uses deb_bootstrap, the <code>centos</code> template uses yum, etc., making these templates impractical when a container from a different OS is desired. </p>
<p> The <code>lxc.create</code> function is used to create containers using a template script. To create a CentOS container named <code>container1</code> on a CentOS minion named <code>mycentosminion</code>, using the <code>centos</code> LXC template, one can simply run the following command: </p>
<pre>
salt mycentosminion lxc.create container1 template=centos
</pre>
<p> For these instances, there is a <code>download</code> template which retrieves minimal container images for several different operating systems. To use this template, it is necessary to provide an <code>options</code> parameter when creating the container, with three values:</p>
<dl>
<dt>1.</p>
<dd> <code>dist</code> &#8211; the Linux distribution (i.e. <code>ubuntu</code> or <code>centos</code>)</p>
<dt>2.</p>
<dd> <code>release</code> &#8211; the release name/version (i.e. <code>trusty</code> or <code>6</code>)</p>
<dt>3.</p>
<dd> <code>arch</code> &#8211; CPU architecture (i.e. <code>amd64</code> or <code>i386</code>) </p>
<p> The <code>lxc.images</code> function (new in version 2015.5.0) can be used to list the available images. Alternatively, the releases can be viewed on <i><a rel="nofollow noopener" href="http://images.linuxcontainers.org/images/" target="_blank">http://images.linuxcontainers.org/images/</a></i>. The images are organized in such a way that the <code>dist</code>, <code>release</code>, and <code>arch</code> can be determined using the following URL format: <code><a rel="nofollow noopener" href="http://images.linuxcontainers.org/images/dist/release/arch" target="_blank">http://images.linuxcontainers.org/images/dist/release/arch</a></code>. For example, <code><a rel="nofollow noopener" href="http://images.linuxcontainers.org/images/centos/6/amd64" target="_blank">http://images.linuxcontainers.org/images/centos/6/amd64</a></code> would correspond to a <code>dist</code> of <code>centos</code>, a <code>release</code> of <code>6</code>, and an <code>arch</code> of <code>amd64</code>. </p>
<p> Therefore, to use the <code>download</code> template to create a new 64-bit CentOS 6 container, the following command can be used: </p>
<pre>
salt myminion lxc.create container1 template=download options='{dist: centos, release: 6, arch: amd64}'
</pre>
<p> <code>NOTE:</code> These command-line options can be placed into a <i>container profile</i>, like so: </p>
<pre>
lxc.container_profile.cent6:
  template: download
  options:
    dist: centos
    release: 6
    arch: amd64
</pre>
<p> The <code>options</code> parameter is not supported in profiles for the 2014.7.x release cycle and earlier, so it would still need to be provided on the command-line.</dl>
<h3>Cloning an Existing Container</h3>
<p> To clone a container, use the <code>lxc.clone</code> function: </p>
<pre>
salt myminion lxc.clone container2 orig=container1
</pre>
<h3>Using a Container Image</h3>
<p> While cloning is a good way to create new containers from a common base container, the source container that is being cloned needs to already exist on the minion. This makes deploying a common container across minions difficult. For this reason, Salt&#8217;s <code>lxc.create</code> is capable of installing a container from a tar archive of another container&#8217;s rootfs. To create an image of a container named <code>cent6</code>, run the following command as root: </p>
<pre>
tar czf cent6.tar.gz -C /var/lib/lxc/cent6 rootfs
</pre>
<p> <code>NOTE:</code> Before doing this, it is recommended that the container is stopped. </p>
<p> The resulting tarball can then be placed alongside the files in the salt fileserver and referenced using a <code>salt://</code> URL. To create a container using an image, use the <code>image</code> parameter with <code>lxc.create</code>: </p>
<pre>
salt myminion lxc.create new-cent6 image=<a href="salt://path/to/cent6.tar.gz" rel="nofollow">salt://path/to/cent6.tar.gz</a>
</pre>
<p> <code>NOTE:</code> Making images of containers with LVM backing </p>
<p> For containers with LVM backing, the rootfs is not mounted, so it is necessary to mount it first before creating the tar archive. When a container is created using LVM backing, an empty <code>rootfs</code> dir is handily created within <code>/var/lib/lxc/container_name</code>, so this can be used as the mountpoint. The location of the logical volume for the container will be <code>/dev/vgname/lvname</code>, where <code>vgname</code> is the name of the volume group, and <code>lvname</code> is the name of the logical volume. Therefore, assuming a volume group of <code>vg1</code>, a logical volume of <code>lxc-cent6</code>, and a container name of <code>cent6</code>, the following commands can be used to create a tar archive of the rootfs: </p>
<pre>
mount /dev/vg1/lxc-cent6 /var/lib/lxc/cent6/rootfs
tar czf cent6.tar.gz -C /var/lib/lxc/cent6 rootfs
umount /var/lib/lxc/cent6/rootfs
</pre>
<p> <code>WARNING:</code> One caveat of using this method of container creation is that <code>/etc/hosts</code> is left unmodified. This could cause confusion for some distros if salt-minion is later installed on the container, as the functions that determine the hostname take <code>/etc/hosts</code> into account. </p>
<p> Additionally, when creating an rootfs image, be sure to remove <code>/etc/salt/minion_id</code> and make sure that <code>id</code> is not defined in <code>/etc/salt/minion</code>, as this will cause similar issues.</p>
<h3>Initializing a New Container as a Salt Minion</h3>
<p> The above examples illustrate a few ways to create containers on the CLI, but often it is desirable to also have the new container run as a Minion. To do this, the <code>lxc.init</code> function can be used. This function will do the following:</p>
<dl>
<dt>1.</p>
<dd> Create a new container</p>
<dt>2.</p>
<dd> Optionally set password and/or DNS</p>
<dt>3.</p>
<dd> Bootstrap the minion (using either <i>salt-bootstrap</i> or a custom command) </p>
<p> By default, the new container will be pointed at the same Salt Master as the host machine on which the container was created. It will then request to authenticate with the Master like any other bootstrapped Minion, at which point it can be accepted. </p>
<pre>
salt myminion lxc.init test1 profile=centos
salt-key -a test1
</pre>
<p> For even greater convenience, the <code>LXC runner</code> contains a runner function of the same name (<code>lxc.init</code>), which creates a keypair, seeds the new minion with it, and pre-accepts the key, allowing for the new Minion to be created and authorized in a single step: </p>
<pre>
salt-run lxc.init test1 host=myminion profile=centos
</pre>
</dl>
<h3>Running Commands Within a Container</h3>
<p> For containers which are not running their own Minion, commands can be run within the container in a manner similar to using (<code>cmd.run &lt;salt.modules.cmdmod.run</code>). The means of doing this have been changed significantly in version 2015.5.0 (though the deprecated behavior will still be supported for a few releases). Both the old and new usage are documented below.</p>
<h3>2015.5.0 and Newer</h3>
<p> New functions have been added to mimic the behavior of the functions in the <code>cmd</code> module. Below is a table with the <code>cmd</code> functions and their <code>lxc</code> module equivalents: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Description </td>
<td> <code>cmd</code> module </td>
<td> <code>lxc</code> module
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Run a command and get all output </td>
<td> <code>cmd.run</code> </td>
<td> <code>lxc.run</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Run a command and get just stdout </td>
<td> <code>cmd.run_stdout</code> </td>
<td> <code>lxc.run_stdout</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Run a command and get just stderr </td>
<td> <code>cmd.run_stderr</code> </td>
<td> <code>lxc.run_stderr</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Run a command and get just the retcode </td>
<td> <code>cmd.retcode</code> </td>
<td> <code>lxc.retcode</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Run a command and get all information </td>
<td> <code>cmd.run_all</code> </td>
<td> <code>lxc.run_all</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>2014.7.x and Earlier</h3>
<p> Earlier Salt releases use a single function (<code>lxc.run_cmd</code>) to run commands within containers. Whether stdout, stderr, etc. are returned depends on how the function is invoked. </p>
<p> To run a command and return the stdout: </p>
<pre>
salt myminion lxc.run_cmd web1 'tail /var/log/messages'
</pre>
<p> To run a command and return the stderr: </p>
<pre>
salt myminion lxc.run_cmd web1 'tail /var/log/messages' stdout=False stderr=True
</pre>
<p> To run a command and return the retcode: </p>
<pre>
salt myminion lxc.run_cmd web1 'tail /var/log/messages' stdout=False stderr=False
</pre>
<p> To run a command and return all information: </p>
<pre>
salt myminion lxc.run_cmd web1 'tail /var/log/messages' stdout=True stderr=True
</pre>
<h3>Container Management Using salt-cloud</h3>
<p> Salt cloud uses under the hood the salt runner and module to manage containers, Please look at this chapter</p>
<h3>Container Management Using States</h3>
<p> Several states are being renamed or otherwise modified in version 2015.5.0. The information in this tutorial refers to the new states. For 2014.7.x and earlier, please refer to the <code>documentation for the LXC states</code>.</p>
<h3>Ensuring a Container Is Present</h3>
<p> To ensure the existence of a named container, use the <code>lxc.present</code> state. Here are some examples: </p>
<pre>
# Using a template
web1:
  lxc.present:
    - template: download
    - options:
        dist: centos
        release: 6
        arch: amd64
# Cloning
web2:
  lxc.present:
    - clone_from: web-base
# Using a rootfs image
web3:
  lxc.present:
    - image: <a href="salt://path/to/cent6.tar.gz" rel="nofollow">salt://path/to/cent6.tar.gz</a>
# Using profiles
web4:
  lxc.present:
    - profile: centos_web
    - network_profile: centos
</pre>
<p> <code>WARNING:</code> The <code>lxc.present</code> state will not modify an existing container (in other words, it will not re-create the container). If an <code>lxc.present</code> state is run on an existing container, there will be no change and the state will return a <code>True</code> result. </p>
<p> The <code>lxc.present</code> state also includes an optional <code>running</code> parameter which can be used to ensure that a container is running/stopped. Note that there are standalone <code>lxc.running</code> and <code>lxc.stopped</code> states which can be used for this purpose.</p>
<h3>Ensuring a Container Does Not Exist</h3>
<p> To ensure that a named container is not present, use the <code>lxc.absent</code> state. For example: </p>
<pre>
web1:
  lxc.absent
</pre>
<h3>Ensuring a Container is Running/Stopped/Frozen</h3>
<p> Containers can be in one of three states:</p>
<dl>
<dt>&bull;</p>
<dd> <code>running</code> &#8211; Container is running and active</p>
<dt>&bull;</p>
<dd> <code>frozen</code> &#8211; Container is running, but all process are blocked and the container is essentially non-active until the container is &quot;unfrozen&quot;</p>
<dt>&bull;</p>
<dd> <code>stopped</code> &#8211; Container is not running </p>
<p> Salt has three states (<code>lxc.running</code>, <code>lxc.frozen</code>, and <code>lxc.stopped</code>) which can be used to ensure a container is in one of these states: </p>
<pre>
web1:
  lxc.running
# Restart the container if it was already running
web2:
  lxc.running:
    - restart: True
web3:
  lxc.stopped
# Explicitly kill all tasks in container instead of gracefully stopping
web4:
  lxc.stopped:
    - kill: True
web5:
  lxc.frozen
# If container is stopped, do not start it (in which case the state will fail)
web6:
  lxc.frozen:
    - start: False
</pre>
</dl>
<h3>Salt Virt</h3>
<h3>Salt as a Cloud Controller</h3>
<p> In Salt 0.14.0, an advanced cloud control system were introduced, allow private cloud vms to be managed directly with Salt. This system is generally referred to as <code>Salt Virt</code>. </p>
<p> The Salt Virt system already exists and is installed within Salt itself, this means that beside setting up Salt, no additional salt code needs to be deployed. </p>
<p> The main goal of Salt Virt is to facilitate a very fast and simple cloud. The cloud that can scale and fully featured. Salt Virt comes with the ability to set up and manage complex virtual machine networking, powerful image, and disk management, as well as virtual machine migration with and without shared storage. </p>
<p> This means that Salt Virt can be used to create a cloud from a blade center and a SAN, but can also create a cloud out of a swarm of Linux Desktops without a single shared storage system. Salt Virt can make clouds from truly commodity hardware, but can also stand up the power of specialized hardware as well.</p>
<h3>Setting up Hypervisors</h3>
<p> The first step to set up the hypervisors involves getting the correct software installed and setting up the hypervisor network interfaces.</p>
<h3>Installing Hypervisor Software</h3>
<p> Salt Virt is made to be hypervisor agnostic but currently the only fully implemented hypervisor is KVM via libvirt. </p>
<p> The required software for a hypervisor is libvirt and kvm. For advanced features install libguestfs or qemu-nbd. </p>
<p> <code>NOTE:</code> Libguestfs and qemu-nbd allow for virtual machine images to be mounted before startup and get pre-seeded with configurations and a salt minion </p>
<p> This sls will set up the needed software for a hypervisor, and run the routines to set up the libvirt pki keys. </p>
<p> <code>NOTE:</code> Package names and setup used is Red Hat specific, different package names will be required for different platforms </p>
<p>libvirt : pkg.installed : [] file.managed : -name : / etc / sysconfig / libvirtd &#8211; contents : &#8216;LIBVIRTD_ARGS=&#8221;&#8211;listen&#8221;&#8216; &#8211; require : -pkg : libvirt libvirt.keys : -require : -pkg : libvirt service.running : -name : libvirtd &#8211; require : -pkg : libvirt &#8211; network : br0 &#8211; libvirt : libvirt &#8211; watch : -file : libvirt libvirt &#8211; python : pkg.installed : [] libguestfs : pkg.installed : -pkgs : -libguestfs &#8211; libguestfs &#8211; tools</p>
<h3>Hypervisor Network Setup</h3>
<p> The hypervisors will need to be running a network bridge to serve up network devices for virtual machines, this formula will set up a standard bridge on a hypervisor connecting the bridge to eth0: </p>
<pre>
eth0:
  network.managed:
    - enabled: True
    - type: eth
    - bridge: br0
br0:
  network.managed:
    - enabled: True
    - type: bridge
    - proto: dhcp
    - require:
      - network: eth0
</pre>
<h3>Virtual Machine Network Setup</h3>
<p> Salt Virt comes with a system to model the network interfaces used by the deployed virtual machines; by default a single interface is created for the deployed virtual machine and is bridged to <code>br0</code>. To get going with the default networking setup, ensure that the bridge interface named <code>br0</code> exists on the hypervisor and is bridged to an active network device. </p>
<p> <code>NOTE:</code> To use more advanced networking in Salt Virt, read the <i>Salt Virt Networking</i> document: </p>
<p> <code>Salt Virt Networking</code></p>
<h3>Libvirt State</h3>
<p> One of the challenges of deploying a libvirt based cloud is the distribution of libvirt certificates. These certificates allow for virtual machine migration. Salt comes with a system used to auto deploy these certificates. Salt manages the signing authority key and generates keys for libvirt clients on the master, signs them with the certificate authority and uses pillar to distribute them. This is managed via the <code>libvirt</code> state. Simply execute this formula on the minion to ensure that the certificate is in place and up to date: </p>
<p> <code>NOTE:</code> The above formula includes the calls needed to set up libvirt keys. </p>
<pre>
libvirt_keys:
  libvirt.keys
</pre>
<h3>Getting Virtual Machine Images Ready</h3>
<p> Salt Virt, requires that virtual machine images be provided as these are not generated on the fly. Generating these virtual machine images differs greatly based on the underlying platform. </p>
<p> Virtual machine images can be manually created using KVM and running through the installer, but this process is not recommended since it is very manual and prone to errors. </p>
<p> Virtual Machine generation applications are available for many platforms:</p>
<dl>
<dt><code>vm-builder:</code></p>
<dd> <i><a rel="nofollow noopener" href="https://wiki.debian.org/VMBuilder" target="_blank">https://wiki.debian.org/VMBuilder</a></i> </p>
<p> <code>SEE ALSO:</code> <i>vmbuilder-formula</i> </p>
<p> Once virtual machine images are available, the easiest way to make them available to Salt Virt is to place them in the Salt file server. Just copy an image into <code>/srv/salt</code> and it can now be used by Salt Virt. </p>
<p> For purposes of this demo, the file name <code>centos.img</code> will be used.</dl>
<h3>Existing Virtual Machine Images</h3>
<p> Many existing Linux distributions distribute virtual machine images which can be used with Salt Virt. Please be advised that NONE OF THESE IMAGES ARE SUPPORTED BY SALTSTACK.</p>
<h3>CentOS</h3>
<p> These images have been prepared for OpenNebula but should work without issue with Salt Virt, only the raw qcow image file is needed: <i><a rel="nofollow noopener" href="http://wiki.centos.org/Cloud/OpenNebula" target="_blank">http://wiki.centos.org/Cloud/OpenNebula</a></i></p>
<h3>Fedora Linux</h3>
<p> Images for Fedora Linux can be found here: <i><a rel="nofollow noopener" href="http://fedoraproject.org/en/get-fedora#clouds" target="_blank">http://fedoraproject.org/en/get-fedora#clouds</a></i></p>
<h3>Ubuntu Linux</h3>
<p> Images for Ubuntu Linux can be found here: <i><a rel="nofollow noopener" href="http://cloud-images.ubuntu.com/" target="_blank">http://cloud-images.ubuntu.com/</a></i></p>
<h3>Using Salt Virt</h3>
<p> With hypervisors set up and virtual machine images ready, Salt can start issuing cloud commands. </p>
<p> Start by running a Salt Virt hypervisor info command: </p>
<pre>
salt-run virt.hyper_info
</pre>
<p> This will query what the running hypervisor stats are and display information for all configured hypervisors. This command will also validate that the hypervisors are properly configured. </p>
<p> Now that hypervisors are available a virtual machine can be provisioned. The <code>virt.init</code> routine will create a new virtual machine: </p>
<pre>
salt-run virt.init centos1 2 512 <a href="salt://centos.img" rel="nofollow noopener" target="_blank">salt://centos.img</a>
</pre>
<p> This command assumes that the CentOS virtual machine image is sitting in the root of the Salt fileserver. Salt Virt will now select a hypervisor to deploy the new virtual machine on and copy the virtual machine image down to the hypervisor. </p>
<p> Once the VM image has been copied down the new virtual machine will be seeded. Seeding the VMs involves setting pre-authenticated Salt keys on the new VM and if needed, will install the Salt Minion on the new VM before it is started. </p>
<p> <code>NOTE:</code> The biggest bottleneck in starting VMs is when the Salt Minion needs to be installed. Making sure that the source VM images already have Salt installed will GREATLY speed up virtual machine deployment. </p>
<p> Now that the new VM has been prepared, it can be seen via the <code>virt.query</code> command: </p>
<pre>
salt-run virt.query
</pre>
<p> This command will return data about all of the hypervisors and respective virtual machines. </p>
<p> Now that the new VM is booted it should have contacted the Salt Master, a <code>test.ping</code> will reveal if the new VM is running.</p>
<h3>Migrating Virtual Machines</h3>
<p> Salt Virt comes with full support for virtual machine migration, and using the libvirt state in the above formula makes migration possible. </p>
<p> A few things need to be available to support migration. Many operating systems turn on firewalls when originally set up, the firewall needs to be opened up to allow for libvirt and kvm to cross communicate and execution migration routines. On Red Hat based hypervisors in particular port 16514 needs to be opened on hypervisors: </p>
<pre>
iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 16514 -j ACCEPT
</pre>
<p> <code>NOTE:</code> More in-depth information regarding distribution specific firewall settings can read in: </p>
<p> <code>Opening the Firewall up for Salt</code> </p>
<p> Salt also needs an additional flag to be turned on as well. The <code>virt.tunnel</code> option needs to be turned on. This flag tells Salt to run migrations securely via the libvirt TLS tunnel and to use port 16514. Without <code>virt.tunnel</code> libvirt tries to bind to random ports when running migrations. To turn on <code>virt.tunnel</code> simple apply it to the master config file: </p>
<pre>
virt.tunnel: True
</pre>
<p> Once the master config has been updated, restart the master and send out a call to the minions to refresh the pillar to pick up on the change: </p>
<pre>
salt \* saltutil.refresh_modules
</pre>
<p> Now, migration routines can be run! To migrate a VM, simply run the Salt Virt migrate routine: </p>
<pre>
salt-run virt.migrate centos &lt;new hypervisor&gt;
</pre>
<h3>VNC Consoles</h3>
<p> Salt Virt also sets up VNC consoles by default, allowing for remote visual consoles to be oped up. The information from a <code>virt.query</code> routine will display the vnc console port for the specific vms: </p>
<pre>
centos
  CPU: 2
  Memory: 524288
  State: running
  Graphics: vnc - hyper6:5900
  Disk - vda:
    Size: 2.0G
    File: /srv/salt-images/ubuntu2/system.qcow2
    File Format: qcow2
  Nic - ac:de:48:98:08:77:
    Source: br0
    Type: bridge
</pre>
<p> The line <i>Graphics: vnc &#8211; hyper6:5900</i> holds the key. First the port named, in this case 5900, will need to be available in the hypervisor&#8217;s firewall. Once the port is open, then the console can be easily opened via vncviewer: </p>
<pre>
vncviewer hyper6:5900
</pre>
<p> By default there is no VNC security set up on these ports, which suggests that keeping them firewalled and mandating that SSH tunnels be used to access these VNC interfaces. Keep in mind that activity on a VNC interface that is accessed can be viewed by any other user that accesses that same VNC interface, and any other user logging in can also operate with the logged in user on the virtual machine.</p>
<h3>Conclusion</h3>
<p> Now with Salt Virt running, new hypervisors can be seamlessly added just by running the above states on new bare metal machines, and these machines will be instantly available to Salt Virt.</p>
<h3>Halite</h3>
<h3>Installing and Configuring Halite</h3>
<p> In this tutorial, we&#8217;ll walk through installing and setting up Halite. The current version of Halite is considered pre-alpha and is supported only in Salt <code>v2014.1.0</code> or greater. Additional information is available on GitHub: <i><a rel="nofollow noopener" href="https://github.com/saltstack/halite" target="_blank">https://github.com/saltstack/halite</a></i> </p>
<p> Before beginning this tutorial, ensure that the salt-master is installed. To install the salt-master, please review the installation documentation: <i><a rel="nofollow noopener" href="http://docs.saltstack.com/topics/installation/index.html" target="_blank">http://docs.saltstack.com/topics/installation/index.html</a></i> </p>
<p> <code>NOTE:</code> Halite only works with Salt versions greater than 2014.1.0.</p>
<h3>Installing Halite Via Package</h3>
<p> On CentOS, RHEL, or Fedora: </p>
<pre>
$ yum install python-halite
</pre>
<p> <code>NOTE:</code> By default python-halite only installs CherryPy. If you would like to use a different webserver please review the instructions below to install pip and your server of choice. The package does not modify the master configuration with <code>/etc/salt/master</code>.</p>
<h3>Installing Halite Using pip</h3>
<p> To begin the installation of Halite from PyPI, you&#8217;ll need to install pip. The Salt package, as well as the bootstrap, do not install pip by default. </p>
<p> On CentOS, RHEL, or Fedora: </p>
<pre>
$ yum install python-pip
</pre>
<p> On Debian: </p>
<pre>
$ apt-get install python-pip
</pre>
<p> Once you have pip installed, use it to install halite: </p>
<pre>
$ pip install -U halite
</pre>
<p> Depending on the webserver you want to run halite through, you&#8217;ll need to install that piece as well. On RHEL based distros, use one of the following: </p>
<pre>
$ pip install cherrypy
</pre>
<pre>
$ pip install paste
</pre>
<pre>
$ yum install python-devel
$ yum install gcc
$ pip install gevent
$ pip install pyopenssl
</pre>
<p> On Debian based distributions: </p>
<pre>
$ pip install CherryPy
</pre>
<pre>
$ pip install paste
</pre>
<pre>
$ apt-get install gcc
$ apt-get install python-dev
$ apt-get install libevent-dev
$ pip install gevent
$ pip install pyopenssl
</pre>
<h3>Configuring Halite Permissions</h3>
<p> Configuring Halite access permissions is easy. By default, you only need to ensure that the @runner group is configured. In the <code>/etc/salt/master</code> file, uncomment and modify the following lines: </p>
<pre>
external_auth:
  pam:
    testuser:
      - .*
      - '@runner'
</pre>
<p> <code>NOTE:</code> You cannot use the root user for pam login; it will fail to authenticate. </p>
<p> Halite uses the runner manage.present to get the status of minions, so runner permissions are required. For example: </p>
<pre>
external_auth:
  pam:
    mytestuser:
      - .*
      - '@runner'
      - '@wheel'
</pre>
<p> Currently Halite allows, but does not require, any wheel modules.</p>
<h3>Configuring Halite Settings</h3>
<p> Once you&#8217;ve configured the permissions for Halite, you&#8217;ll need to set up the Halite settings in the /etc/salt/master file. Halite supports CherryPy, Paste, and Gevent out of the box. </p>
<p> To configure cherrypy, add the following to the bottom of your /etc/salt/master file: </p>
<pre>
halite:
  level: 'debug'
  server: 'cherrypy'
  host: '0.0.0.0'
  port: '8080'
  cors: False
  tls: True
  certpath: '/etc/pki/tls/certs/localhost.crt'
  keypath: '/etc/pki/tls/certs/localhost.key'
  pempath: '/etc/pki/tls/certs/localhost.pem'
</pre>
<p> If you wish to use paste: </p>
<pre>
halite:
  level: 'debug'
  server: 'paste'
  host: '0.0.0.0'
  port: '8080'
  cors: False
  tls: True
  certpath: '/etc/pki/tls/certs/localhost.crt'
  keypath: '/etc/pki/tls/certs/localhost.key'
  pempath: '/etc/pki/tls/certs/localhost.pem'
</pre>
<p> To use gevent: </p>
<pre>
halite:
  level: 'debug'
  server: 'gevent'
  host: '0.0.0.0'
  port: '8080'
  cors: False
  tls: True
  certpath: '/etc/pki/tls/certs/localhost.crt'
  keypath: '/etc/pki/tls/certs/localhost.key'
  pempath: '/etc/pki/tls/certs/localhost.pem'
</pre>
<p> The &quot;cherrypy&quot; and &quot;gevent&quot; servers require the certpath and keypath files to run tls/ssl. The .crt file holds the public cert and the .key file holds the private key. Whereas the &quot;paste&quot; server requires a single .pem file that contains both the cert and key. This can be created simply by concatenating the .crt and .key files. </p>
<p> If you want to use a self-signed cert, you can create one using the Salt.tls module: </p>
<p> <code>NOTE:</code> The following command needs to be run on your salt master. </p>
<pre>
salt-call tls.create_self_signed_cert tls
</pre>
<p> Note that certs generated by the above command can be found under the <code>/etc/pki/tls/certs/</code> directory. When using self-signed certs, browsers will need approval before accepting the cert. If the web application page has been cached with a non-HTTPS version of the app, then the browser cache will have to be cleared before it will recognize and prompt to accept the self-signed certificate.</p>
<h3>Starting Halite</h3>
<p> Once you&#8217;ve configured the halite section of your /etc/salt/master, you can restart the salt-master service, and your halite instance will be available. Depending on your configuration, the instance will be available either at <i><a rel="nofollow noopener" href="https://localhost:8080/app" target="_blank">https://localhost:8080/app</a></i>, <i><a href="https://domain:8080/app" rel="nofollow">https://domain:8080/app</a></i>, or <i><a rel="nofollow" href="https://123.456.789.012:8080/app">https://123.456.789.012:8080/app</a></i> . </p>
<p> <code>NOTE:</code> halite requires an HTML 5 compliant browser. </p>
<p> All logs relating to halite are logged to the default /var/log/salt/master file.</p>
<h3>LXC</h3>
<h3>Using Salt at scale</h3>
<h3>Using Salt at scale</h3>
<p> The focus of this tutorial will be building a Salt infrastructure for handling large numbers of minions. This will include tuning, topology, and best practices. </p>
<p> For how to install the Salt Master please go here: <i>Installing saltstack</i> </p>
<p> <code>NOTE:</code> This tutorial is intended for large installations, although these same settings won&#8217;t hurt, it may not be worth the complexity to smaller installations. </p>
<p> When used with minions, the term &#8216;many&#8217; refers to at least a thousand and &#8216;a few&#8217; always means 500. </p>
<p> For simplicity reasons, this tutorial will default to the standard ports used by Salt.</p>
<h3>The Master</h3>
<p> The most common problems on the Salt Master are:</p>
<dl>
<dt>1.</p>
<dd> too many minions authing at once</p>
<dt>2.</p>
<dd> too many minions re-authing at once</p>
<dt>3.</p>
<dd> too many minions re-connecting at once</p>
<dt>4.</p>
<dd> too many minions returning at once</p>
<dt>5.</p>
<dd> too few resources (CPU/HDD) </p>
<p> The first three are all &quot;thundering herd&quot; problems. To mitigate these issues we must configure the minions to back-off appropriately when the Master is under heavy load. </p>
<p> The fourth is caused by masters with little hardware resources in combination with a possible bug in ZeroMQ. At least thats what it looks like till today (<i>Issue 118651</i>, <i>Issue 5948</i>, <i>Mail thread</i>) </p>
<p> To fully understand each problem, it is important to understand, how Salt works. </p>
<p> Very briefly, the Salt Master offers two services to the minions.</p>
<dt>&bull;</p>
<dd> a job publisher on port 4505</p>
<dt>&bull;</p>
<dd> an open port 4506 to receive the minions returns </p>
<p> All minions are always connected to the publisher on port 4505 and only connect to the open return port 4506 if necessary. On an idle Master, there will only be connections on port 4505.</dl>
<h3>Too many minions authing</h3>
<p> When the Minion service is first started up, it will connect to its Master&#8217;s publisher on port 4505. If too many minions are started at once, this can cause a &quot;thundering herd&quot;. This can be avoided by not starting too many minions at once. </p>
<p> The connection itself usually isn&#8217;t the culprit, the more likely cause of master-side issues is the authentication that the Minion must do with the Master. If the Master is too heavily loaded to handle the auth request it will time it out. The Minion will then wait <i>acceptance_wait_time</i> to retry. If <i>acceptance_wait_time_max</i> is set then the Minion will increase its wait time by the <i>acceptance_wait_time</i> each subsequent retry until reaching <i>acceptance_wait_time_max</i>.</p>
<h3>Too many minions re-authing</h3>
<p> This is most likely to happen in the testing phase of a Salt deployment, when all Minion keys have already been accepted, but the framework is being tested and parameters are frequently changed in the Salt Master&#8217;s configuration file(s). </p>
<p> The Salt Master generates a new AES key to encrypt its publications at certain events such as a Master restart or the removal of a Minion key. If you are encountering this problem of too many minions re-authing against the Master, you will need to recalibrate your setup to reduce the rate of events like a Master restart or Minion key removal (<code>salt-key -d</code>). </p>
<p> When the Master generates a new AES key, the minions aren&#8217;t notified of this but will discover it on the next pub job they receive. When the Minion receives such a job it will then re-auth with the Master. Since Salt does minion-side filtering this means that all the minions will re-auth on the next command published on the master&#8211; causing another &quot;thundering herd&quot;. This can be avoided by setting the </p>
<pre>
random_reauth_delay: 60
</pre>
<p> in the minions configuration file to a higher value and stagger the amount of re-auth attempts. Increasing this value will of course increase the time it takes until all minions are reachable via Salt commands.</p>
<h3>Too many minions re-connecting</h3>
<p> By default the zmq socket will re-connect every 100ms which for some larger installations may be too quick. This will control how quickly the TCP session is re-established, but has no bearing on the auth load. </p>
<p> To tune the minions sockets reconnect attempts, there are a few values in the sample configuration file (default values) </p>
<pre>
recon_default: 100ms
recon_max: 5000
recon_randomize: True
</pre>
<dl>
<dt>&bull;</p>
<dd> recon_default: the default value the socket should use, i.e. 100ms</p>
<dt>&bull;</p>
<dd> recon_max: the max value that the socket should use as a delay before trying to reconnect</p>
<dt>&bull;</p>
<dd> recon_randomize: enables randomization between recon_default and recon_max </p>
<p> To tune this values to an existing environment, a few decision have to be made.</p>
<dt>1.</p>
<dd> How long can one wait, before the minions should be online and reachable via Salt?</p>
<dt>2.</p>
<dd> How many reconnects can the Master handle without a syn flood? </p>
<p> These questions can not be answered generally. Their answers depend on the hardware and the administrators requirements. </p>
<p> Here is an example scenario with the goal, to have all minions reconnect within a 60 second time-frame on a Salt Master service restart. </p>
<pre>
recon_default: 1000
recon_max: 59000
recon_randomize: True
</pre>
<p> Each Minion will have a randomized reconnect value between &#8216;recon_default&#8217; and &#8216;recon_default + recon_max&#8217;, which in this example means between 1000ms and 60000ms (or between 1 and 60 seconds). The generated random-value will be doubled after each attempt to reconnect (ZeroMQ default behavior). </p>
<p> Lets say the generated random value is 11 seconds (or 11000ms). </p>
<pre>
reconnect 1: wait 11 seconds
reconnect 2: wait 22 seconds
reconnect 3: wait 33 seconds
reconnect 4: wait 44 seconds
reconnect 5: wait 55 seconds
reconnect 6: wait time is bigger than 60 seconds (recon_default + recon_max)
reconnect 7: wait 11 seconds
reconnect 8: wait 22 seconds
reconnect 9: wait 33 seconds
reconnect x: etc.
</pre>
<p> With a thousand minions this will mean </p>
<pre>
1000/60 = ~16
</pre>
<p> round about 16 connection attempts a second. These values should be altered to values that match your environment. Keep in mind though, that it may grow over time and that more minions might raise the problem again.</dl>
<h3>Too many minions returning at once</h3>
<p> This can also happen during the testing phase, if all minions are addressed at once with </p>
<pre>
$ salt * test.ping
</pre>
<p> it may cause thousands of minions trying to return their data to the Salt Master open port 4506. Also causing a flood of syn-flood if the Master can&#8217;t handle that many returns at once. </p>
<p> This can be easily avoided with Salt&#8217;s batch mode: </p>
<pre>
$ salt * test.ping -b 50
</pre>
<p> This will only address 50 minions at once while looping through all addressed minions.</p>
<h3>Too few resources</h3>
<p> The masters resources always have to match the environment. There is no way to give good advise without knowing the environment the Master is supposed to run in. But here are some general tuning tips for different situations:</p>
<h3>The Master is CPU bound</h3>
<p> Salt uses RSA-Key-Pairs on the masters and minions end. Both generate 4096 bit key-pairs on first start. While the key-size for the Master is currently not configurable, the minions keysize can be configured with different key-sizes. For example with a 2048 bit key: </p>
<pre>
keysize: 2048
</pre>
<p> With thousands of decryptions, the amount of time that can be saved on the masters end should not be neglected. See here for reference: <i>Pull Request 9235</i> how much influence the key-size can have. </p>
<p> Downsizing the Salt Master&#8217;s key is not that important, because the minions do not encrypt as many messages as the Master does.</p>
<h3>The Master is disk IO bound</h3>
<p> By default, the Master saves every Minion&#8217;s return for every job in its job-cache. The cache can then be used later, to lookup results for previous jobs. The default directory for this is: </p>
<pre>
cachedir: /var/cache/salt
</pre>
<p> and then in the <code>/proc</code> directory. </p>
<p> Each job return for every Minion is saved in a single file. Over time this directory can grow quite large, depending on the number of published jobs. The amount of files and directories will scale with the number of jobs published and the retention time defined by </p>
<pre>
keep_jobs: 24
</pre>
<pre>
250 jobs/day * 2000 minions returns = 500.000 files a day
</pre>
<p> If no job history is needed, the job cache can be disabled: </p>
<pre>
job_cache: False
</pre>
<p> If the job cache is necessary there are (currently) 2 options:</p>
<dl>
<dt>&bull;</p>
<dd> ext_job_cache: this will have the minions store their return data directly into a returner (not sent through the Master)</p>
<dt>&bull;</p>
<dd> master_job_cache (New in <i>2014.7.0</i>): this will make the Master store the job data using a returner (instead of the local job cache on disk).</dl>
<h2 id="TARGETING MINIONS"></h2>
<p> Targeting minions is specifying which minions should run a command or execute a state by matching against hostnames, or system information, or defined groups, or even combinations thereof. </p>
<p> For example the command <code>salt web1 apache.signal restart</code> to restart the Apache httpd server specifies the machine <code>web1</code> as the target and the command will only be run on that one minion. </p>
<p> Similarly when using States, the following top file specifies that only the <code>web1</code> minion should execute the contents of <code>webserver.sls</code>: </p>
<pre>
base:
  'web1':
    - webserver
</pre>
<p> There are many ways to target individual minions or groups of minions in Salt:</p>
<h3>Matching the <code>minion id</code></h3>
<p> Each minion needs a unique identifier. By default when a minion starts for the first time it chooses its FQDN as that identifier. The minion id can be overridden via the minion&#8217;s <code>id</code> configuration setting. </p>
<p> <code>TIP:</code> minion id and minion keys </p>
<p> The minion id is used to generate the minion&#8217;s public/private keys and if it ever changes the master must then accept the new key as though the minion was a new host.</p>
<h3>Globbing</h3>
<p> The default matching that Salt utilizes is <i>shell-style globbing</i> around the minion id. This also works for states in the top file. </p>
<p> <code>NOTE:</code> You must wrap <code>salt</code> calls that use globbing in single-quotes to prevent the shell from expanding the globs before Salt is invoked. </p>
<p> Match all minions: </p>
<pre>
salt '*' test.ping
</pre>
<p> Match all minions in the example.net domain or any of the example domains: </p>
<pre>
salt '*.example.net' test.ping
salt '*.example.*' test.ping
</pre>
<p> Match all the <code>webN</code> minions in the example.net domain (<code>web1.example.net</code>, <code>web2.example.net</code> â¦ <code>webN.example.net</code>): </p>
<pre>
salt 'web?.example.net' test.ping
</pre>
<p> Match the <code>web1</code> through <code>web5</code> minions: </p>
<pre>
salt 'web[1-5]' test.ping
</pre>
<p> Match the <code>web1</code> and <code>web3</code> minions: </p>
<pre>
salt 'web[1,3]' test.ping
</pre>
<p> Match the <code>web-x</code>, <code>web-y</code>, and <code>web-z</code> minions: </p>
<pre>
salt 'web-[x-z]' test.ping
</pre>
<p> <code>NOTE:</code> For additional targeting methods please review the <code>compound matchers</code> documentation.</p>
<h3>Regular Expressions</h3>
<p> Minions can be matched using Perl-compatible <i>regular expressions</i> (which is globbing on steroids and a ton of caffeine). </p>
<p> Match both <code>web1-prod</code> and <code>web1-devel</code> minions: </p>
<pre>
salt -E 'web1-(prod|devel)' test.ping
</pre>
<p> When using regular expressions in a State&#8217;s top file, you must specify the matcher as the first option. The following example executes the contents of <code>webserver.sls</code> on the above-mentioned minions. </p>
<pre>
base:
  'web1-(prod|devel)':
  - match: pcre
  - webserver
</pre>
<h3>Lists</h3>
<p> At the most basic level, you can specify a flat list of minion IDs: </p>
<pre>
salt -L 'web1,web2,web3' test.ping
</pre>
<h3>Grains</h3>
<p> Salt comes with an interface to derive information about the underlying system. This is called the grains interface, because it presents salt with grains of information. Grains are collected for the operating system, domain name, IP address, kernel, OS type, memory, and many other system properties. </p>
<p> The grains interface is made available to Salt modules and components so that the right salt minion commands are automatically available on the right systems. </p>
<p> Grain data is relatively static, though if system information changes (for example, if network settings are changed), or if a new value is assigned to a custom grain, grain data is refreshed. </p>
<p> <code>NOTE:</code> Grains resolve to lowercase letters. For example, <code>FOO</code>, and <code>foo</code> target the same grain. </p>
<p> <code>IMPORTANT:</code> See Is Targeting using Grain Data Secure? for important security information. </p>
<p> Match all CentOS minions: </p>
<pre>
salt -G 'os:CentOS' test.ping
</pre>
<p> Match all minions with 64-bit CPUs, and return number of CPU cores for each matching minion: </p>
<pre>
salt -G 'cpuarch:x86_64' grains.item num_cpus
</pre>
<p> Additionally, globs can be used in grain matches, and grains that are nested in a <i>dictionary</i> can be matched by adding a colon for each level that is traversed. For example, the following will match hosts that have a grain called <code>ec2_tags</code>, which itself is a <i>dict</i> with a key named <code>environment</code>, which has a value that contains the word <code>production</code>: </p>
<pre>
salt -G 'ec2_tags:environment:*production*'
</pre>
<h3>Listing Grains</h3>
<p> Available grains can be listed by using the &#8216;grains.ls&#8217; module: </p>
<pre>
salt '*' grains.ls
</pre>
<p> Grains data can be listed by using the &#8216;grains.items&#8217; module: </p>
<pre>
salt '*' grains.items
</pre>
<h3>Grains in the Minion Config</h3>
<p> Grains can also be statically assigned within the minion configuration file. Just add the option <code>grains</code> and pass options to it: </p>
<pre>
grains:
  roles:
    - webserver
    - memcache
  deployment: datacenter4
  cabinet: 13
  cab_u: 14-15
</pre>
<p> Then status data specific to your servers can be retrieved via Salt, or used inside of the State system for matching. It also makes targeting, in the case of the example above, simply based on specific data about your deployment.</p>
<h3>Grains in /etc/salt/grains</h3>
<p> If you do not want to place your custom static grains in the minion config file, you can also put them in <code>/etc/salt/grains</code> on the minion. They are configured in the same way as in the above example, only without a top-level <code>grains:</code> key: </p>
<pre>
roles:
  - webserver
  - memcache
deployment: datacenter4
cabinet: 13
cab_u: 14-15
</pre>
<h3>Matching Grains in the Top File</h3>
<p> With correctly configured grains on the Minion, the top file used in Pillar or during Highstate can be made very efficient. For example, consider the following configuration: </p>
<pre>
'node_type:web':
  - match: grain
  - webserver
'node_type:postgres':
  - match: grain
  - database
'node_type:redis':
  - match: grain
  - redis
'node_type:lb':
  - match: grain
  - lb
</pre>
<p> For this example to work, you would need to have defined the grain <code>node_type</code> for the minions you wish to match. This simple example is nice, but too much of the code is similar. To go one step further, Jinja templating can be used to simplify the top file. </p>
<p>{ % set node_type = salt[&#8216;grains.get&#8217;](&#8216;node_type&#8217;, &#8221;) % } {<br />
    % if node_type %<br />
}<br />
&#8216;node_type:&#123;&#123; self }}&#8217; : -match : grain &#8211; &#123;&#123;self}}<br />
{<br />
    % endif %<br />
}</p>
<p> Using Jinja templating, only one match entry needs to be defined. </p>
<p> <code>NOTE:</code> The example above uses the <code>grains.get</code> function to account for minions which do not have the <code>node_type</code> grain set.</p>
<h3>Writing Grains</h3>
<p> The grains interface is derived by executing all of the &quot;public&quot; functions found in the modules located in the grains package or the custom grains directory. The functions in the modules of the grains must return a Python <i>dict</i>, where the keys in the <i>dict</i> are the names of the grains and the values are the values. </p>
<p> Custom grains should be placed in a <code>_grains</code> directory located under the <code>file_roots</code> specified by the master config file. The default path would be <code>/srv/salt/_grains</code>. Custom grains will be distributed to the minions when <code>state.highstate</code> is run, or by executing the <code>saltutil.sync_grains</code> or <code>saltutil.sync_all</code> functions. </p>
<p> Grains are easy to write, and only need to return a dictionary. A common approach would be code something similar to the following: </p>
<p>#!/ usr / bin / env python<br />
def yourfunction()<br />
    :<br />
#initialize a grains dictionary<br />
      grains = {}<br />
#Some code for logic that sets grains like<br />
      grains[&#8216;yourcustomgrain&#8217;] = True grains[&#8216;anothergrain&#8217;] = &#8216;somevalue&#8217; return grains</p>
<p> Before adding a grain to Salt, consider what the grain is and remember that grains need to be static data. If the data is something that is likely to change, consider using <code>Pillar</code> instead. </p>
<p> <code>WARNING:</code> Custom grains will not be available in the top file until after the first highstate. To make custom grains available on a minion&#8217;s first highstate, it is recommended to use this example to ensure that the custom grains are synced when the minion starts.</p>
<h3>Precedence</h3>
<p> Core grains can be overridden by custom grains. As there are several ways of defining custom grains, there is an order of precedence which should be kept in mind when defining them. The order of evaluation is as follows:</p>
<dl>
<dt>1.</p>
<dd> Core grains.</p>
<dt>2.</p>
<dd> Custom grains in <code>/etc/salt/grains</code>.</p>
<dt>3.</p>
<dd> Custom grains in <code>/etc/salt/minion</code>.</p>
<dt>4.</p>
<dd> Custom grain modules in <code>_grains</code> directory, synced to minions. </p>
<p> Each successive evaluation overrides the previous ones, so any grains defined by custom grains modules synced to minions that have the same name as a core grain will override that core grain. Similarly, grains from <code>/etc/salt/minion</code> override both core grains and custom grain modules, and grains in <code>_grains</code> will override <i>any</i> grains of the same name.</dl>
<h3>Examples of Grains</h3>
<p> The core module in the grains package is where the main grains are loaded by the Salt minion and provides the principal example of how to write grains: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt/blob/develop/salt/grains/core.py" target="_blank">https://github.com/saltstack/salt/blob/develop/salt/grains/core.py</a></i></p>
<h3>Syncing Grains</h3>
<p> Syncing grains can be done a number of ways, they are automatically synced when <code>state.highstate</code> is called, or (as noted above) the grains can be manually synced and reloaded by calling the <code>saltutil.sync_grains</code> or <code>saltutil.sync_all</code> functions.</p>
<h3>Targeting with Pillar</h3>
<p> Pillar data can be used when targeting minions. This allows for ultimate control and flexibility when targeting minions. </p>
<pre>
salt -I 'somekey:specialvalue' test.ping
</pre>
<p> Like with Grains, it is possible to use globbing as well as match nested values in Pillar, by adding colons for each level that is being traversed. The below example would match minions with a pillar named <code>foo</code>, which is a dict containing a key <code>bar</code>, with a value beginning with <code>baz</code>: </p>
<pre>
salt -I 'foo:bar:baz*' test.ping
</pre>
<h3>Subnet/IP Address Matching</h3>
<p> Minions can easily be matched based on IP address, or by subnet (using <i>CIDR</i> notation). </p>
<pre>
salt -S 192.168.40.20 test.ping
salt -S 10.0.0.0/24 test.ping
</pre>
<p> <code>NOTE:</code> Only IPv4 matching is supported at this time.</p>
<h3>Compound matchers</h3>
<p> Compound matchers allow very granular minion targeting using any of Salt&#8217;s matchers. The default matcher is a <i>glob</i> match, just as with CLI and top file matching. To match using anything other than a glob, prefix the match string with the appropriate letter from the table below, followed by an <code>@</code> sign. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Letter </td>
<td> Match Type </td>
<td> Example
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> G </td>
<td> Grains glob </td>
<td> <code>G@os:Ubuntu</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E </td>
<td> PCRE Minion ID </td>
<td> <code>E@web\d+\.(dev|qa|prod)\.loc</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> P </td>
<td> Grains PCRE </td>
<td> <code>P@os:(RedHat|Fedora|CentOS)</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> L </td>
<td> List of minions </td>
<td> <code>L@minion1.example.com,minion3.domain.com or bl*.domain.com</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> I </td>
<td> Pillar glob </td>
<td> <code>I@pdata:foobar</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> S </td>
<td> Subnet/IP address </td>
<td> <code>S@192.168.1.0/24</code> or <code>S@192.168.1.100</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> R </td>
<td> Range cluster </td>
<td> <code>R@%foo.bar</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Matchers can be joined using boolean <code>and</code>, <code>or</code>, and <code>not</code> operators. </p>
<p> For example, the following string matches all Debian minions with a hostname that begins with <code>webserv</code>, as well as any minions that have a hostname which matches the <i>regular expression</i> <code>web-dc1-srv.*</code>: </p>
<pre>
salt -C 'webserv* and G@os:Debian or E@web-dc1-srv.*' test.ping
</pre>
<p> That same example expressed in a top file looks like the following: </p>
<pre>
base:
  'webserv* and G@os:Debian or E@web-dc1-srv.*':
    - match: compound
    - webserver
</pre>
<p> Note that a leading <code>not</code> is not supported in compound matches. Instead, something like the following must be done: </p>
<pre>
salt -C '* and not G@kernel:Darwin' test.ping
</pre>
<p> Excluding a minion based on its ID is also possible: </p>
<pre>
salt -C '* and not web-dc1-srv' test.ping
</pre>
<h3>Precedence Matching</h3>
<p> Matches can be grouped together with parentheses to explicitly declare precedence amongst groups. </p>
<pre>
salt -C '( ms-1 or G@id:ms-3 ) and G@id:ms-3' test.ping
</pre>
<p> <code>NOTE:</code> Be certain to note that spaces are required between the parentheses and targets. Failing to obey this rule may result in incorrect targeting!</p>
<h3>Node groups</h3>
<p> Nodegroups are declared using a compound target specification. The compound target documentation can be found <code>here</code>. </p>
<p> The <code>nodegroups</code> master config file parameter is used to define nodegroups. Here&#8217;s an example nodegroup configuration within <code>/etc/salt/master</code>: </p>
<pre>
nodegroups:
  group1: 'L@foo.domain.com,bar.domain.com,baz.domain.com or bl*.domain.com'
  group2: 'G@os:Debian and foo.domain.com'
  group3: 'G@os:Debian and N@group1'
</pre>
<p> <code>NOTE:</code> The <code>L</code> within group1 is matching a list of minions, while the <code>G</code> in group2 is matching specific grains. See the <code>compound matchers</code> documentation for more details. </p>
<p> <code>NOTE:</code> Nodgroups can reference other nodegroups as seen in <code>group3</code>. Ensure that you do not have circular references. Circular references will be detected and cause partial expansion with a logged error message. </p>
<p> To match a nodegroup on the CLI, use the <code>-N</code> command-line option: </p>
<pre>
salt -N group1 test.ping
</pre>
<p> To match a nodegroup in your top file, make sure to put <code>&#8211; match: nodegroup</code> on the line directly following the nodegroup name. </p>
<pre>
base:
  group1:
    - match: nodegroup
    - webserver
</pre>
<p> <code>NOTE:</code> When adding or modifying nodegroups to a master configuration file, the master must be restarted for those changes to be fully recognized. </p>
<p> A limited amount of functionality, such as targeting with -N from the command-line may be available without a restart.</p>
<h3>Batch Size</h3>
<p> The <code>-b</code> (or <code>&#8211;batch-size</code>) option allows commands to be executed on only a specified number of minions at a time. Both percentages and finite numbers are supported. </p>
<pre>
salt '*' -b 10 test.ping
salt -G 'os:RedHat' --batch-size 25% apache.signal restart
</pre>
<p> This will only run test.ping on 10 of the targeted minions at a time and then restart apache on 25% of the minions matching <code>os:RedHat</code> at a time and work through them all until the task is complete. This makes jobs like rolling web server restarts behind a load balancer or doing maintenance on BSD firewalls using carp much easier with salt. </p>
<p> The batch system maintains a window of running minions, so, if there are a total of 150 minions targeted and the batch size is 10, then the command is sent to 10 minions, when one minion returns then the command is sent to one additional minion, so that the job is constantly running on 10 minions.</p>
<h3>SECO Range</h3>
<p> SECO range is a cluster-based metadata store developed and maintained by Yahoo! </p>
<p> The Range project is hosted here: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/ytoolshed/range" target="_blank">https://github.com/ytoolshed/range</a></i> </p>
<p> Learn more about range here: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/ytoolshed/range/wiki/" target="_blank">https://github.com/ytoolshed/range/wiki/</a></i></p>
<h3>Prerequisites</h3>
<p> To utilize range support in Salt, a range server is required. Setting up a range server is outside the scope of this document. Apache modules are included in the range distribution. </p>
<p> With a working range server, cluster files must be defined. These files are written in YAML and define hosts contained inside a cluster. Full documentation on writing YAML range files is here: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/ytoolshed/range/wiki/%22yamlfile%22-module-file-spec" target="_blank">https://github.com/ytoolshed/range/wiki/%22yamlfile%22-module-file-spec</a></i> </p>
<p> Additionally, the Python seco range libraries must be installed on the salt master. One can verify that they have been installed correctly via the following command: </p>
<pre>
python -c 'import seco.range'
</pre>
<p> If no errors are returned, range is installed successfully on the salt master.</p>
<h3>Preparing Salt</h3>
<p> Range support must be enabled on the salt master by setting the hostname and port of the range server inside the master configuration file: </p>
<pre>
range_server: my.range.server.com:80
</pre>
<p> Following this, the master must be restarted for the change to have an effect.</p>
<h3>Targeting with Range</h3>
<p> Once a cluster has been defined, it can be targeted with a salt command by using the <code>-R</code> or <code>&#8211;range</code> flags. </p>
<p> For example, given the following range YAML file being served from a range server: </p>
<pre>
$ cat /etc/range/test.yaml
CLUSTER: host1..100.test.com
APPS:
  - frontend
  - backend
  - mysql
</pre>
<p> One might target host1 through host100 in the test.com domain with Salt as follows: </p>
<pre>
salt --range %test:CLUSTER test.ping
</pre>
<p> The following salt command would target three hosts: <code>frontend</code>, <code>backend</code>, and <code>mysql</code>: </p>
<pre>
salt --range %test:APPS test.ping
</pre>
<h2 id="STORING STATIC DATA IN THE PILLAR"></h2>
<p> Pillar is an interface for Salt designed to offer global values that can be distributed to all minions. Pillar data is managed in a similar way as the Salt State Tree. </p>
<p> Pillar was added to Salt in version 0.9.8 </p>
<p> <code>NOTE:</code> Storing sensitive data </p>
<p> Unlike state tree, pillar data is only available for the targeted minion specified by the matcher type. This makes it useful for storing sensitive data specific to a particular minion.</p>
<h3>Declaring the Master Pillar</h3>
<p> The Salt Master server maintains a pillar_roots setup that matches the structure of the file_roots used in the Salt file server. Like the Salt file server the <code>pillar_roots</code> option in the master config is based on environments mapping to directories. The pillar data is then mapped to minions based on matchers in a top file which is laid out in the same way as the state top file. Salt pillars can use the same matcher types as the standard top file. </p>
<p> The configuration for the <code>pillar_roots</code> in the master config file is identical in behavior and function as <code>file_roots</code>: </p>
<pre>
pillar_roots:
  base:
    - /srv/pillar
</pre>
<p> This example configuration declares that the base environment will be located in the <code>/srv/pillar</code> directory. It must not be in a subdirectory of the state tree. </p>
<p> The top file used matches the name of the top file used for States, and has the same structure: </p>
<p> <code>/srv/pillar/top.sls</code> </p>
<pre>
base:
  '*':
    - packages
</pre>
<p> In the above top file, it is declared that in the <code>base</code> environment, the glob matching all minions will have the pillar data found in the <code>packages</code> pillar available to it. Assuming the <code>pillar_roots</code> value of <code>/srv/pillar</code> taken from above, the <code>packages</code> pillar would be located at <code>/srv/pillar/packages.sls</code>. </p>
<p> Another example shows how to use other standard top matching types to deliver specific salt pillar data to minions with different properties. </p>
<p> Here is an example using the <code>grains</code> matcher to target pillars to minions by their <code>os</code> grain: </p>
<pre>
dev:
  'os:Debian':
    - match: grain
    - servers
</pre>
<p> <code>/srv/pillar/packages.sls</code> </p>
<p>{<br />
    % if grains[&#8216;os&#8217;] == &#8216;RedHat&#8217; %<br />
}<br />
apache : httpd<br />
             git : git{ % elif grains[&#8216;os&#8217;] == &#8216;Debian&#8217; % } apache : apache2<br />
                                                                         git : git &#8211;<br />
                                                                               core{ % endif % } company : Foo Industries</p>
<p> <code>IMPORTANT:</code> See Is Targeting using Grain Data Secure? for important security information. </p>
<p> The above pillar sets two key/value pairs. If a minion is running RedHat, then the <code>apache</code> key is set to <code>httpd</code> and the <code>git</code> key is set to the value of <code>git</code>. If the minion is running Debian, those values are changed to <code>apache2</code> and <code>git-core</code> respctively. All minions that have this pillar targeting to them via a top file will have the key of <code>company</code> with a value of <code>Foo Industries</code>. </p>
<p> Consequently this data can be used from within modules, renderers, State SLS files, and more via the shared pillar <i>dict</i>: </p>
<p>apache : pkg.installed : -name:<br />
{<br />
    {<br />
        pillar[&#8216;apache&#8217;]<br />
    }<br />
}</p>
<p>git : pkg.installed : -name:<br />
{<br />
    {<br />
        pillar[&#8216;git&#8217;]<br />
    }<br />
}</p>
<p> Finally, the above states can utilize the values provided to them via Pillar. All pillar values targeted to a minion are available via the &#8216;pillar&#8217; dictionary. As seen in the above example, Jinja substitution can then be utilized to access the keys and values in the Pillar dictionary. </p>
<p> Note that you cannot just list key/value-information in <code>top.sls</code>. Instead, target a minion to a pillar file and then list the keys and values in the pillar. Here is an example top file that illustrates this point: </p>
<pre>
base:
  '*':
     - common_pillar
</pre>
<p> And the actual pillar file at &#8216;/srv/pillar/common_pillar.sls&#8217;: </p>
<pre>
foo: bar
boo: baz
</pre>
<h3>Pillar namespace flattened</h3>
<p> The separate pillar files all share the same namespace. Given a <code>top.sls</code> of: </p>
<pre>
base:
  '*':
    - packages
    - services
</pre>
<p> a <code>packages.sls</code> file of: </p>
<pre>
bind: bind9
</pre>
<p> and a <code>services.sls</code> file of: </p>
<pre>
bind: named
</pre>
<p> Then a request for the <code>bind</code> pillar will only return <code>named</code>; the <code>bind9</code> value is not available. It is better to structure your pillar files with more hierarchy. For example your <code>package.sls</code> file could look like: </p>
<pre>
packages:
  bind: bind9
</pre>
<h3>Pillar Namespace Merges</h3>
<p> With some care, the pillar namespace can merge content from multiple pillar files under a single key, so long as conflicts are avoided as described above. </p>
<p> For example, if the above example were modified as follows, the values are merged below a single key: </p>
<pre>
base:
  '*':
    - packages
    - services
</pre>
<p> And a <code>packages.sls</code> file like: </p>
<pre>
bind:
  package-name: bind9
  version: 9.9.5
</pre>
<p> And a <code>services.sls</code> file like: </p>
<pre>
bind:
  port: 53
  listen-on: any
</pre>
<p> The resulting pillar will be as follows: </p>
<p>$ salt &#8211; call pillar.get bind local : &#8212; &#8212; &#8212; &#8212; &#8211;listen &#8211; on : any package &#8211; name : bind9 port : 53 version : 9.9.5</p>
<p> <code>NOTE:</code> Remember: conflicting keys will be overwritten in a non-deterministic manner!</p>
<h3>Including Other Pillars</h3>
<p> New in version 0.16.0. </p>
<p> Pillar SLS files may include other pillar files, similar to State files. Two syntaxes are available for this purpose. The simple form simply includes the additional pillar as if it were part of the same file: </p>
<pre>
include:
  - users
</pre>
<p> The full include form allows two additional options &#8212; passing default values to the templating engine for the included pillar file as well as an optional key under which to nest the results of the included pillar: </p>
<pre>
include:
  - users:
      defaults:
          sudo: ['bob', 'paul']
      key: users
</pre>
<p> With this form, the included file (users.sls) will be nested within the &#8216;users&#8217; key of the compiled pillar. Additionally, the &#8216;sudo&#8217; value will be available as a template variable to users.sls.</p>
<h3>Viewing Minion Pillar</h3>
<p> Once the pillar is set up the data can be viewed on the minion via the <code>pillar</code> module, the pillar module comes with functions, <code>pillar.items</code> and <code>pillar.raw</code>. <code>pillar.items</code> will return a freshly reloaded pillar and <code>pillar.raw</code> will return the current pillar without a refresh: </p>
<pre>
salt '*' pillar.items
</pre>
<p> <code>NOTE:</code> Prior to version 0.16.2, this function is named <code>pillar.data</code>. This function name is still supported for backwards compatibility.</p>
<h3>Pillar get Function</h3>
<p> New in version 0.14.0. </p>
<p> The <code>pillar.get</code> function works much in the same way as the <code>get</code> method in a python dict, but with an enhancement: nested dict components can be extracted using a <i>:</i> delimiter. </p>
<p> If a structure like this is in pillar: </p>
<pre>
foo:
  bar:
    baz: qux
</pre>
<p> Extracting it from the raw pillar in an sls formula or file template is done this way: </p>
<p>{<br />
    {<br />
        pillar[&#8216;foo&#8217;][&#8216;bar&#8217;][&#8216;baz&#8217;]<br />
    }<br />
}</p>
<p> Now, with the new <code>pillar.get</code> function the data can be safely gathered and a default can be set, allowing the template to fall back if the value is not available: </p>
<p>{<br />
    {<br />
        salt[&#8216;pillar.get&#8217;](&#8216;foo:bar:baz&#8217;, &#8216;qux&#8217;)<br />
    }<br />
}</p>
<p> This makes handling nested structures much easier. </p>
<p> <code>NOTE:</code> <code>pillar.get()</code> vs <code>salt[&#8216;pillar.get&#8217;]()</code> </p>
<p> It should be noted that within templating, the <code>pillar</code> variable is just a dictionary. This means that calling <code>pillar.get()</code> inside of a template will just use the default dictionary <code>.get()</code> function which does not include the extra <code>:</code> delimiter functionality. It must be called using the above syntax (<code>salt[&#8216;pillar.get&#8217;](&#8216;foo:bar:baz&#8217;, &#8216;qux&#8217;)</code>) to get the salt function, instead of the default dictionary behavior.</p>
<h3>Refreshing Pillar Data</h3>
<p> When pillar data is changed on the master the minions need to refresh the data locally. This is done with the <code>saltutil.refresh_pillar</code> function. </p>
<pre>
salt '*' saltutil.refresh_pillar
</pre>
<p> This function triggers the minion to asynchronously refresh the pillar and will always return <code>None</code>.</p>
<h3>Set Pillar Data at the Command Line</h3>
<p> Pillar data can be set at the command line like the following example: </p>
<pre>
salt '*' state.highstate pillar='{&quot;cheese&quot;: &quot;spam&quot;}'
</pre>
<p> This will create a dict with a key of &#8216;cheese&#8217; and a value of &#8216;spam&#8217;. A list can be created like this: </p>
<pre>
salt '*' state.highstate pillar='[&quot;cheese&quot;, &quot;milk&quot;, &quot;bread&quot;]'
</pre>
<h3>Master Config In Pillar</h3>
<p> For convenience the data stored in the master configuration file can be made available in all minion&#8217;s pillars. This makes global configuration of services and systems very easy but may not be desired if sensitive data is stored in the master configuration. This option is disabled by default. </p>
<p> To enable the master config from being added to the pillar set <code>pillar_opts</code> to <code>True</code>: </p>
<pre>
pillar_opts: True
</pre>
<h3>Master Provided Pillar Error</h3>
<p> By default if there is an error rendering a pillar, the detailed error is hidden and replaced with: </p>
<pre>
Rendering SLS 'my.sls' failed. Please see master log for details.
</pre>
<p> The error is protected because it&#8217;s possible to contain templating data which would give that minion information it shouldn&#8217;t know, like a password! </p>
<p> To have the master provide the detailed error that could potentially carry protected data set <code>pillar_safe_render_error</code> to <code>False</code>: </p>
<pre>
pillar_safe_render_error: True
</pre>
<h2 id="REACTOR SYSTEM"></h2>
<p> Salt version 0.11.0 introduced the reactor system. The premise behind the reactor system is that with Salt&#8217;s events and the ability to execute commands, a logic engine could be put in place to allow events to trigger actions, or more accurately, reactions. </p>
<p> This system binds sls files to event tags on the master. These sls files then define reactions. This means that the reactor system has two parts. First, the reactor option needs to be set in the master configuration file. The reactor option allows for event tags to be associated with sls reaction files. Second, these reaction files use highdata (like the state system) to define reactions to be executed.</p>
<h3>Event System</h3>
<p> A basic understanding of the event system is required to understand reactors. The event system is a local ZeroMQ PUB interface which fires salt events. This event bus is an open system used for sending information notifying Salt and other systems about operations. </p>
<p> The event system fires events with a very specific criteria. Every event has a <code>tag</code>. Event tags allow for fast top level filtering of events. In addition to the tag, each event has a data structure. This data structure is a dict, which contains information about the event.</p>
<h3>Mapping Events to Reactor SLS Files</h3>
<p> Reactor SLS files and event tags are associated in the master config file. By default this is /etc/salt/master, or /etc/salt/master.d/reactor.conf. </p>
<p> New in version 2014.7.0: Added Reactor support for <code>salt://</code> file paths. </p>
<p> In the master config section &#8216;reactor:&#8217; is a list of event tags to be matched and each event tag has a list of reactor SLS files to be run. </p>
<pre>
reactor:                            # Master config section &quot;reactor&quot;
  - 'salt/minion/*/start':          # Match tag &quot;salt/minion/*/start&quot;
    - /srv/reactor/start.sls        # Things to do when a minion starts
    - /srv/reactor/monitor.sls      # Other things to do
  - 'salt/cloud/*/destroyed':       # Globs can be used to matching tags
    - /srv/reactor/destroy/*.sls    # Globs can be used to match file names
  - 'myco/custom/event/tag':        # React to custom event tags
    - <a href="salt://reactor/mycustom.sls" rel="nofollow">salt://reactor/mycustom.sls</a>   # Put reactor files under file_roots
</pre>
<p> Reactor sls files are similar to state and pillar sls files. They are by default yaml + Jinja templates and are passed familiar context variables. </p>
<p> They differ because of the addition of the <code>tag</code> and <code>data</code> variables.</p>
<dl>
<dt>&bull;</p>
<dd> The <code>tag</code> variable is just the tag in the fired event.</p>
<dt>&bull;</p>
<dd> The <code>data</code> variable is the event&#8217;s data dict. </p>
<p> Here is a simple reactor sls: </p>
<p>{<br />
    % if data[&#8216;id&#8217;] == &#8216;mysql1&#8217; %<br />
}<br />
highstate_run : local.state.highstate : -tgt : mysql1<br />
{<br />
    % endif %<br />
}</p>
<p> This simple reactor file uses Jinja to further refine the reaction to be made. If the <code>id</code> in the event data is <code>mysql1</code> (in other words, if the name of the minion is <code>mysql1</code>) then the following reaction is defined. The same data structure and compiler used for the state system is used for the reactor system. The only difference is that the data is matched up to the salt command API and the runner system. In this example, a command is published to the <code>mysql1</code> minion with a function of <code>state.highstate</code>. Similarly, a runner can be called: </p>
<p>{<br />
    % if data[&#8216;data&#8217;][&#8216;overstate&#8217;] == &#8216;refresh&#8217; %<br />
}<br />
overstate_run : runner.state.over<br />
{<br />
    % endif %<br />
}</p>
<p> This example will execute the state.overstate runner and initiate an overstate execution.</dl>
<h3>Fire an event</h3>
<p> To fire an event from a minion call <code>event.send</code> </p>
<pre>
salt-call event.send 'foo' '{overstate: refresh}'
</pre>
<p> After this is called, any reactor sls files matching event tag <code>foo</code> will execute with <code>&#123;&#123; data[&#8216;data&#8217;][&#8216;overstate&#8217;] }}</code> equal to <code>&#8216;refresh&#8217;</code>. </p>
<p> See <code>salt.modules.event</code> for more information.</p>
<h3>Knowing what event is being fired</h3>
<p> The best way to see exactly what events are fired and what data is available in each event is to use the <code>state.event runner</code>. </p>
<p> <code>SEE ALSO:</code> Common Salt Events </p>
<p> Example usage: </p>
<pre>
salt-run state.event pretty=True
</pre>
<p> Example output: </p>
<p>salt / job / 20150213001905721678 / new {<br />
    &#8220;_stamp&#8221; : &#8220;2015-02-13T00:19:05.724583&#8221;,<br />
    &#8220;arg&#8221; : [],<br />
    &#8220;fun&#8221; : &#8220;test.ping&#8221;,<br />
    &#8220;jid&#8221; : &#8220;20150213001905721678&#8221;,<br />
    &#8220;minions&#8221; : [&#8220;jerry&#8221;],<br />
    &#8220;tgt&#8221; : &#8220;*&#8221;,<br />
    &#8220;tgt_type&#8221; : &#8220;glob&#8221;,<br />
    &#8220;user&#8221; : &#8220;root&#8221;<br />
} salt /<br />
    job / 20150213001910749506 / ret / jerry<br />
{<br />
    &#8220;_stamp&#8221; : &#8220;2015-02-13T00:19:11.136730&#8221;,<br />
               &#8220;cmd&#8221; : &#8220;_return&#8221;,<br />
                       &#8220;fun&#8221; : &#8220;saltutil.find_job&#8221;,<br />
                               &#8220;fun_args&#8221; : [&#8220;20150213001905721678&#8221;],<br />
                                            &#8220;id&#8221; : &#8220;jerry&#8221;,<br />
                                                   &#8220;jid&#8221; : &#8220;20150213001910749506&#8221;,<br />
                                                           &#8220;retcode&#8221; : 0,<br />
                                                           &#8220;return&#8221; : {},<br />
                                                                      &#8220;success&#8221; : true<br />
}</p>
<h3>Debugging the Reactor</h3>
<p> The best window into the Reactor is to run the master in the foreground with debug logging enabled. The output will include when the master sees the event, what the master does in response to that event, and it will also include the rendered SLS file (or any errors generated while rendering the SLS file).</p>
<dl>
<dt>1.</p>
<dd> Stop the master.</p>
<dt>2.</p>
<dd> Start the master manually: </p>
<pre>
salt-master -l debug
</pre>
<dt>3.</p>
<dd> Look for log entries in the form: </p>
<p>[DEBUG   ] Gathering reactors for tag foo/bar<br />
[DEBUG   ] Compiling reactions for tag foo/bar<br />
[DEBUG   ] Rendered data from file: /path/to/the/reactor_file.sls:<br />
&lt;&#8230; Rendered output appears here. &#8230;&gt;</p>
<p> The rendered output is the result of the Jinja parsing and is a good way to view the result of referencing Jinja variables. If the result is empty then Jinja produced an empty result and the Reactor will ignore it.</dl>
<h3>Understanding the Structure of Reactor Formulas</h3>
<p> <code>I.e., when to use `arg` and `kwarg` and when to specify the function arguments directly.</code> </p>
<p> While the reactor system uses the same basic data structure as the state system, the functions that will be called using that data structure are different functions than are called via Salt&#8217;s state system. The Reactor can call Runner modules using the <i>runner</i> prefix, Wheel modules using the <i>wheel</i> prefix, and can also cause minions to run Execution modules using the <i>local</i> prefix. </p>
<p> Changed in version 2014.7.0: The <code>cmd</code> prefix was renamed to <code>local</code> for consistency with other parts of Salt. A backward-compatible alias was added for <code>cmd</code>. </p>
<p> The Reactor runs on the master and calls functions that exist on the master. In the case of Runner and Wheel functions the Reactor can just call those functions directly since they exist on the master and are run on the master. </p>
<p> In the case of functions that exist on minions and are run on minions, the Reactor still needs to call a function on the master in order to send the necessary data to the minion so the minion can execute that function. </p>
<p> The Reactor calls functions exposed in Salt&#8217;s Python API documentation. and thus the structure of Reactor files very transparently reflects the function signatures of those functions.</p>
<h3>Calling Execution modules on Minions</h3>
<p> The Reactor sends commands down to minions in the exact same way Salt&#8217;s CLI interface does. It calls a function locally on the master that sends the name of the function as well as a list of any arguments and a dictionary of any keyword arguments that the minion should use to execute that function. </p>
<p> Specifically, the Reactor calls the async version of <code>this function</code>. You can see that function has &#8216;arg&#8217; and &#8216;kwarg&#8217; parameters which are both values that are sent down to the minion. </p>
<p> Executing remote commands maps to the <code>LocalClient</code> interface which is used by the <code>salt</code> command. This interface more specifically maps to the <code>cmd_async</code> method inside of the <code>LocalClient</code> class. This means that the arguments passed are being passed to the <code>cmd_async</code> method, not the remote method. A field starts with <code>local</code> to use the <code>LocalClient</code> subsystem. The result is, to execute a remote command, a reactor formula would look like this: </p>
<pre>
clean_tmp:
  local.cmd.run:
    - tgt: '*'
    - arg:
      - rm -rf /tmp/*
</pre>
<p> The <code>arg</code> option takes a list of arguments as they would be presented on the command line, so the above declaration is the same as running this salt command: </p>
<pre>
salt '*' cmd.run 'rm -rf /tmp/*'
</pre>
<p> Use the <code>expr_form</code> argument to specify a matcher: </p>
<pre>
clean_tmp:
  local.cmd.run:
    - tgt: 'os:Ubuntu'
    - expr_form: grain
    - arg:
      - rm -rf /tmp/*
clean_tmp:
  local.cmd.run:
    - tgt: 'G@roles:hbase_master'
    - expr_form: compound
    - arg:
      - rm -rf /tmp/*
</pre>
<p> Any other parameters in the <code>LocalClient().cmd()</code> method can be specified as well.</p>
<h3>Calling Runner modules and Wheel modules</h3>
<p> Calling Runner modules and Wheel modules from the Reactor uses a more direct syntax since the function is being executed locally instead of sending a command to a remote system to be executed there. There are no &#8216;arg&#8217; or &#8216;kwarg&#8217; parameters (unless the Runner function or Wheel function accepts a parameter with either of those names.) </p>
<p> For example: </p>
<pre>
clear_the_grains_cache_for_all_minions:
  runner.cache.clear_grains
</pre>
<p> If <code>the runner takes arguments</code> then they can be specified as well: </p>
<pre>
spin_up_more_web_machines:
  runner.cloud.profile:
    - prof: centos_6
    - instances:
      - web11       # These VM names would be generated via Jinja in a
      - web12       # real-world example.
</pre>
<h3>Passing event data to Minions or Orchestrate as Pillar</h3>
<p> An interesting trick to pass data from the Reactor script to <code>state.highstate</code> or <code>state.sls</code> is to pass it as inline Pillar data since both functions take a keyword argument named <code>pillar</code>. </p>
<p> The following example uses Salt&#8217;s Reactor to listen for the event that is fired when the key for a new minion is accepted on the master using <code>salt-key</code>. </p>
<p> <code>/etc/salt/master.d/reactor.conf</code>: </p>
<pre>
reactor:
  - 'salt/key':
    - /srv/salt/haproxy/react_new_minion.sls
</pre>
<p> The Reactor then fires a <code>state.sls</code> command targeted to the HAProxy servers and passes the ID of the new minion from the event to the state file via inline Pillar. </p>
<p> <code>/srv/salt/haproxy/react_new_minion.sls</code>: </p>
<p>{<br />
    % if data[&#8216;act&#8217;] == &#8216;accept&#8217; and data[&#8216;id&#8217;].startswith(&#8216;web&#8217;) %<br />
}<br />
add_new_minion_to_pool : local.state.sls : -tgt : &#8216;haproxy*&#8217; &#8211; arg : -haproxy.refresh_pool &#8211; kwarg : pillar : new_minion : &#123;&#123;data[&#8216;id&#8217;]}}<br />
{<br />
    % endif %<br />
}</p>
<p> The above command is equivalent to the following command at the CLI: </p>
<pre>
salt 'haproxy*' state.sls haproxy.refresh_pool 'pillar={new_minion: minionid}'
</pre>
<p> This works with Orchestrate files as well: </p>
<pre>
call_some_orchestrate_file:
  runner.state.orchestrate:
    - mods: some_orchestrate_file
    - pillar:
        stuff: things
</pre>
<p> Which is equivalent to the following command at the CLI: </p>
<pre>
salt-run state.orchestrate some_orchestrate_file pillar='{stuff: things}'
</pre>
<p> Finally, that data is available in the state file using the normal Pillar lookup syntax. The following example is grabbing web server names and IP addresses from Salt Mine. If this state is invoked from the Reactor then the custom Pillar value from above will be available and the new minion will be added to the pool but with the <code>disabled</code> flag so that HAProxy won&#8217;t yet direct traffic to it. </p>
<p> <code>/srv/salt/haproxy/refresh_pool.sls</code>: </p>
<p>{ % set new_minion = salt[&#8216;pillar.get&#8217;](&#8216;new_minion&#8217;) % } listen web * : 80 balance source<br />
{% for server,ip in salt[&#8216;mine.get&#8217;](&#8216;web*&#8217;, &#8216;network.interfaces&#8217;, [&#8216;eth0&#8217;]).items() %<br />
}<br />
{<br />
    % if server == new_minion %<br />
}<br />
server&#123;&#123;server}} &#123;&#123;ip}} : 80 disabled{ % else % } server&#123;&#123;server}} &#123;&#123;ip}} : 80 check{ % endif % }<br />
{<br />
    % endfor %<br />
}</p>
<h3>A Complete Example</h3>
<p> In this example, we&#8217;re going to assume that we have a group of servers that will come online at random and need to have keys automatically accepted. We&#8217;ll also add that we don&#8217;t want all servers being automatically accepted. For this example, we&#8217;ll assume that all hosts that have an id that starts with &#8216;ink&#8217; will be automatically accepted and have state.highstate executed. On top of this, we&#8217;re going to add that a host coming up that was replaced (meaning a new key) will also be accepted. </p>
<p> Our master configuration will be rather simple. All minions that attempte to authenticate will match the <code>tag</code> of <code>salt/auth</code>. When it comes to the minion key being accepted, we get a more refined <code>tag</code> that includes the minion id, which we can use for matching. </p>
<p> <code>/etc/salt/master.d/reactor.conf</code>: </p>
<pre>
reactor:
  - 'salt/auth':
    - /srv/reactor/auth-pending.sls
  - 'salt/minion/ink*/start':
    - /srv/reactor/auth-complete.sls
</pre>
<p> In this sls file, we say that if the key was rejected we will delete the key on the master and then also tell the master to ssh in to the minion and tell it to restart the minion, since a minion process will die if the key is rejected. </p>
<p> We also say that if the key is pending and the id starts with ink we will accept the key. A minion that is waiting on a pending key will retry authentication every ten seconds by default. </p>
<p> <code>/srv/reactor/auth-pending.sls</code>: </p>
<p>{#Ink server faild to authenticate&#8211; remove accepted key #} {<br />
    % if not data[&#8216;result&#8217;] and data[&#8216;id&#8217;].startswith(&#8216;ink&#8217;) %<br />
}<br />
minion_remove : wheel.key.delete : -match:<br />
{<br />
    {<br />
        data[&#8216;id&#8217;]<br />
    }<br />
}<br />
minion_rejoin : local.cmd.run : -tgt : salt &#8211; master.domain.tld &#8211; arg : -ssh &#8211; o UserKnownHostsFile = / dev / null &#8211; o StrictHostKeyChecking = no &#8220;&#123;&#123; data[&#8216;id&#8217;] }}&#8221; &#8216;sleep 10 &amp;&amp; /etc/init.d/salt-minion restart&#8217; { % endif % } {#Ink server is sending new key&#8211; accept this key #}<br />
{<br />
    % if &#8216;act&#8217; in data and data[&#8216;act&#8217;] == &#8216;pend&#8217; and data[&#8216;id&#8217;].startswith(&#8216;ink&#8217;) %<br />
}<br />
minion_add : wheel.key.accept : -match : &#123;&#123;data[&#8216;id&#8217;]}}<br />
{<br />
    % endif %<br />
}</p>
<p> No if statements are needed here because we already limited this action to just Ink servers in the master configuration. </p>
<p> <code>/srv/reactor/auth-complete.sls</code>: </p>
<p>{#When an Ink server connects, run state.highstate.#} highstate_run : local.state.highstate : -tgt : &#123;&#123;data[&#8216;id&#8217;]}} &#8211; ret : smtp</p>
<p> The above will also return the highstate result data using the <i>smtp_return</i> returner (use virtualname like when using from the command line with <i>&#8211;return</i>). The returner needs to be configured on the minion for this to work. See <code>salt.returners.smtp_return</code> documentation for that.</p>
<h3>Syncing Custom Types on Minion Start</h3>
<p> Salt will sync all custom types (by running a <code>saltutil.sync_all</code>) on every highstate. However, there is a chicken-and-egg issue where, on the initial highstate, a minion will not yet have these custom types synced when the top file is first compiled. This can be worked around with a simple reactor which watches for <code>minion_start</code> events, which each minion fires when it first starts up and connects to the master. </p>
<p> On the master, create <code>/srv/reactor/sync_grains.sls</code> with the following contents: </p>
<p>sync_grains : local.saltutil.sync_grains : -tgt:<br />
{<br />
    {<br />
        data[&#8216;id&#8217;]<br />
    }<br />
}</p>
<p> And in the master config file, add the following reactor configuration: </p>
<pre>
reactor:
  - 'minion_start':
    - /srv/reactor/sync_grains.sls
</pre>
<p> This will cause the master to instruct each minion to sync its custom grains when it starts, making these grains available when the initial highstate is executed. </p>
<p> Other types can be synced by replacing <code>local.saltutil.sync_grains</code> with <code>local.saltutil.sync_modules</code>, <code>local.saltutil.sync_all</code>, or whatever else suits the intended use case.</p>
<h2 id="THE SALT MINE"></h2>
<p> The Salt Mine is used to collect arbitrary data from Minions and store it on the Master. This data is then made available to all Minions via the <code>salt.modules.mine</code> module. </p>
<p> Mine data is gathered on the Minion and sent back to the Master where only the most recent data is maintained (if long term data is required use returners or the external job cache).</p>
<h3>Mine vs Grains</h3>
<p> Mine data is designed to be much more up-to-date than grain data. Grains are refreshed on a very limited basis and are largely static data. Mines are designed to replace slow peer publishing calls when Minions need data from other Minions. Rather than having a Minion reach out to all the other Minions for a piece of data, the Salt Mine, running on the Master, can collect it from all the Minions every mine-interval, resulting in almost fresh data at any given time, with much less overhead.</p>
<h3>Mine Functions</h3>
<p> To enable the Salt Mine the <code>mine_functions</code> option needs to be applied to a Minion. This option can be applied via the Minion&#8217;s configuration file, or the Minion&#8217;s Pillar. The <code>mine_functions</code> option dictates what functions are being executed and allows for arguments to be passed in. If no arguments are passed, an empty list must be added: </p>
<pre>
mine_functions:
  test.ping: []
  network.ip_addrs:
    interface: eth0
    cidr: '10.0.0.0/8'
</pre>
<h3>Mine Functions Aliases</h3>
<p> Function aliases can be used to provide usage intentions or to allow multiple calls of the same function with different arguments. </p>
<p> New in version 2014.7.0. </p>
<p>mine_functions : network.ip_addrs : [eth0] networkplus.internal_ip_addrs : [] internal_ip_addrs : mine_function : network.ip_addrs<br />
                                                                                                                      cidr : 192.168.0.0 /<br />
    16 loopback_ip_addrs : mine_function : network.ip_addrs<br />
                                               lo : True</p>
<h3>Mine Interval</h3>
<p> The Salt Mine functions are executed when the Minion starts and at a given interval by the scheduler. The default interval is every 60 minutes and can be adjusted for the Minion via the <code>mine_interval</code> option: </p>
<pre>
mine_interval: 60
</pre>
<h3>Mine in Salt-SSH</h3>
<p> As of the 2015.5.0 release of salt, salt-ssh supports <code>mine.get</code>. </p>
<p> Because the Minions cannot provide their own <code>mine_functions</code> configuration, we retrieve the args for specified mine functions in one of three places, searched in the following order:</p>
<dl>
<dt>1.</p>
<dd> Roster data</p>
<dt>2.</p>
<dd> Pillar</p>
<dt>3.</p>
<dd> Master config </p>
<p> The <code>mine_functions</code> are formatted exactly the same as in normal salt, just stored in a different location. Here is an example of a flat roster containing <code>mine_functions</code>: </p>
<pre>
test:
  host: 104.237.131.248
  user: root
  mine_functions:
    cmd.run: ['echo &quot;hello!&quot;']
    network.ip_addrs:
      interface: eth0
</pre>
<p> <code>NOTE:</code> Because of the differences in the architecture of salt-ssh, <code>mine.get</code> calls are somewhat inefficient. Salt must make a new salt-ssh call to each of the Minions in question to retrieve the requested data, much like a publish call. However, unlike publish, it must run the requested function as a wrapper function, so we can retrieve the function args from the pillar of the Minion in question. This results in a non-trivial delay in retrieving the requested data.</dl>
<h3>Example</h3>
<p> One way to use data from Salt Mine is in a State. The values can be retrieved via Jinja and used in the SLS file. The following example is a partial HAProxy configuration file and pulls IP addresses from all Minions with the &quot;web&quot; grain to add them to the pool of load balanced servers. </p>
<p> <code>/srv/pillar/top.sls</code>: </p>
<pre>
base:
  'G@roles:web':
    - web
</pre>
<p> <code>/srv/pillar/web.sls</code>: </p>
<pre>
mine_functions:
  network.ip_addrs: [eth0]
</pre>
<p> <code>/etc/salt/minion.d/mine.conf</code>: </p>
<pre>
mine_interval: 5
</pre>
<p> <code>/srv/salt/haproxy.sls</code>: </p>
<pre>
haproxy_config:
  file.managed:
    - name: /etc/haproxy/config
    - source: <a href="salt://haproxy_config" rel="nofollow">salt://haproxy_config</a>
    - template: jinja
</pre>
<p> <code>/srv/salt/haproxy_config</code>: </p>
<p>&lt;&#8230;file contents snipped&#8230;&gt;<br />
{% for server, addrs in salt[&#8216;mine.get&#8217;](&#8216;roles:web&#8217;, &#8216;network.ip_addrs&#8217;, expr_form=&#8217;pillar&#8217;).items() %}<br />
server &#123;&#123; server }} &#123;&#123; addrs[0] }}:80 check<br />
{% endfor %}<br />
&lt;&#8230;file contents snipped&#8230;&gt;</p>
<h2 id="EXTERNAL AUTHENTICATION SYSTEM"></h2>
<p> Salt&#8217;s External Authentication System (eAuth) allows for Salt to pass through command authorization to any external authentication system, such as PAM or LDAP.</p>
<h3>Access Control System</h3>
<p> The external authentication system allows for specific users to be granted access to execute specific functions on specific minions. Access is configured in the master configuration file and uses the access control system: </p>
<pre>
external_auth:
  pam:
    thatch:
      - 'web*':
        - test.*
        - network.*
    steve:
      - .*
</pre>
<p> The above configuration allows the user <code>thatch</code> to execute functions in the test and network modules on the minions that match the web* target. User <code>steve</code> is given unrestricted access to minion commands. </p>
<p> Salt respects the current PAM configuration in place, and uses the &#8216;login&#8217; service to authenticate. </p>
<p> <code>NOTE:</code> The PAM module does not allow authenticating as <code>root</code>. </p>
<p> To allow access to wheel modules or runner modules the following <code>@</code> syntax must be used: </p>
<pre>
external_auth:
  pam:
    thatch:
      - '@wheel'   # to allow access to all wheel modules
      - '@runner'  # to allow access to all runner modules
      - '@jobs'    # to allow access to the jobs runner and/or wheel module
</pre>
<p> <code>NOTE:</code> The runner/wheel markup is different, since there are no minions to scope the acl to. </p>
<p> <code>NOTE:</code> Globs will not match wheel or runners! They must be explicitly allowed with @wheel or @runner. </p>
<p> The external authentication system can then be used from the command-line by any user on the same system as the master with the <code>-a</code> option: </p>
<pre>
$ salt -a pam web\* test.ping
</pre>
<p> The system will ask the user for the credentials required by the authentication system and then publish the command. </p>
<p> To apply permissions to a group of users in an external authentication system, append a <code>%</code> to the ID: </p>
<pre>
external_auth:
  pam:
    admins%:
      - '*':
        - 'pkg.*'
</pre>
<p> <code>WARNING:</code> All users that have external authentication privileges are allowed to run <code>saltutil.findjob</code>. Be aware that this could inadvertently expose some data such as minion IDs.</p>
<h3>Tokens</h3>
<p> With external authentication alone, the authentication credentials will be required with every call to Salt. This can be alleviated with Salt tokens. </p>
<p> Tokens are short term authorizations and can be easily created by just adding a <code>-T</code> option when authenticating: </p>
<pre>
$ salt -T -a pam web\* test.ping
</pre>
<p> Now a token will be created that has a expiration of 12 hours (by default). This token is stored in a file named <code>.salt_token</code> in the active user&#8217;s home directory. </p>
<p> Once the token is created, it is sent with all subsequent communications. User authentication does not need to be entered again until the token expires. </p>
<p> Token expiration time can be set in the Salt master config file.</p>
<h3>LDAP and Active Directory</h3>
<p> Salt supports both user and group authentication for LDAP (and Active Directory accessed via its LDAP interface)</p>
<h3>OpenLDAP and similar systems</h3>
<p> LDAP configuration happens in the Salt master configuration file. </p>
<p> Server configuration values and their defaults: </p>
<p>#Server to auth against<br />
auth.ldap.server : localhost<br />
#Port to connect via<br />
                       auth.ldap.port : 389<br />
#Use TLS when connecting<br />
                   auth.ldap.tls : False<br />
#LDAP scope level, almost always 2<br />
                                       auth.ldap.scope : 2<br />
#Server specified in URI format<br />
                                   auth.ldap.uri : &#8221; #Overrides.ldap.server,<br />
    .ldap.port, .ldap.tls above<br />
#Verify server&#8217;s TLS certificate<br />
                    auth.ldap.no_verify : False<br />
#Bind to LDAP anonymously to determine group membership<br />
#Active Directory does not allow anonymous binds without special configuration<br />
                                              auth.ldap.anonymous : False<br />
#FOR TESTING ONLY, this is a VERY insecure setting.<br />
#If this is True, the LDAP bind password will be ignored and<br />
#access will be determined by group membership alone with<br />
#the group memberships being retrieved via anonymous bind<br />
                                                                        auth.ldap.auth_by_group_membership_only : False<br />
#Require authenticating user to be part of this Organizational Unit<br />
#This can be blank if your LDAP schema does not use this kind of OU<br />
                                                                                                                      auth.ldap.groupou : &#8216;Groups&#8217;<br />
#Object Class for groups.An LDAP search will be done to find all groups of this<br />
#class to which the authenticating user belongs.<br />
                                                                                                                                          auth.ldap.groupclass : &#8216;posixGroup&#8217;<br />
#Unique ID attribute name for the user<br />
                                                                                                                                                                 auth.ldap.accountattributename : &#8216;memberUid&#8217;<br />
#These are only for Active Directory<br />
                                                                                                                                                                                                  auth.ldap.activedirectory : False auth.ldap.persontype : &#8216;person&#8217;</p>
<p> There are two phases to LDAP authentication. First, Salt authenticates to search for a users&#8217;s Distinguished Name and group membership. The user it authenticates as in this phase is often a special LDAP system user with read-only access to the LDAP directory. After Salt searches the directory to determine the actual user&#8217;s DN and groups, it re-authenticates as the user running the Salt commands. </p>
<p> If you are already aware of the structure of your DNs and permissions in your LDAP store are set such that users can look up their own group memberships, then the first and second users can be the same. To tell Salt this is the case, omit the <code>auth.ldap.bindpw</code> parameter. You can template the binddn like this: </p>
<p>auth.ldap.basedn : dc = saltstack, dc = com auth.ldap.binddn : uid = &#123;&#123;username}}, cn = users, cn = accounts, dc = saltstack, dc = com</p>
<p> Salt will use the password entered on the salt command line in place of the bindpw. </p>
<p> To use two separate users, specify the LDAP lookup user in the binddn directive, and include a bindpw like so </p>
<pre>
auth.ldap.binddn: uid=ldaplookup,cn=sysaccounts,cn=etc,dc=saltstack,dc=com
auth.ldap.bindpw: mypassword
</pre>
<p> As mentioned before, Salt uses a filter to find the DN associated with a user. Salt substitutes the <code>&#123;&#123; username }}</code> value for the username when querying LDAP </p>
<p>auth.ldap.filter : uid = &#123;&#123;username}}</p>
<p> For OpenLDAP, to determine group membership, one can specify an OU that contains group data. This is prepended to the basedn to create a search path. Then the results are filtered against <code>auth.ldap.groupclass</code>, default <code>posixGroup</code>, and the account&#8217;s &#8216;name&#8217; attribute, <code>memberUid</code> by default. </p>
<pre>
auth.ldap.groupou: Groups
</pre>
<h3>Active Directory</h3>
<p> Active Directory handles group membership differently, and does not utilize the <code>groupou</code> configuration variable. AD needs the following options in the master config: </p>
<p>auth.ldap.activedirectory : True<br />
                                auth.ldap.filter : sAMAccountName = &#123;&#123;username}} auth.ldap.accountattributename : sAMAccountName<br />
                                                                                                                      auth.ldap.groupclass : group<br />
                                                                                                                                                 auth.ldap.persontype : person</p>
<p> To determine group membership in AD, the username and password that is entered when LDAP is requested as the eAuth mechanism on the command line is used to bind to AD&#8217;s LDAP interface. If this fails, then it doesn&#8217;t matter what groups the user belongs to, he or she is denied access. Next, the distinguishedName of the user is looked up with the following LDAP search: </p>
<p>(&amp;(&lt; value of auth.ldap.accountattributename &gt;= &#123;&#123;username}})(objectClass = &lt;value of auth.ldap.persontype&gt;))</p>
<p> This should return a distinguishedName that we can use to filter for group membership. Then the following LDAP query is executed: </p>
<pre>
(&amp;(member=&lt;distinguishedName from search above&gt;)
  (objectClass=&lt;value of auth.ldap.groupclass&gt;)
)
</pre>
<pre>
external_auth:
  ldap:
    test_ldap_user:
      - '*':
        - test.ping
</pre>
<p> To configure an LDAP group, append a <code>%</code> to the ID: </p>
<pre>
external_auth:
  ldap:
    test_ldap_group%:
      - '*':
        - test.echo
</pre>
<h2 id="ACCESS CONTROL SYSTEM"></h2>
<p> New in version 0.10.4. </p>
<p> Salt maintains a standard system used to open granular control to non administrative users to execute Salt commands. The access control system has been applied to all systems used to configure access to non administrative control interfaces in Salt.These interfaces include, the <code>peer</code> system, the <code>external auth</code> system and the <code>client acl</code> system. </p>
<p> The access control system mandated a standard configuration syntax used in all of the three aforementioned systems. While this adds functionality to the configuration in 0.10.4, it does not negate the old configuration. </p>
<p> Now specific functions can be opened up to specific minions from specific users in the case of external auth and client ACLs, and for specific minions in the case of the peer system. </p>
<p> The access controls are manifested using matchers in these configurations: </p>
<pre>
client_acl:
  fred:
    - web\*:
      - pkg.list_pkgs
      - test.*
      - apache.*
</pre>
<p> In the above example, fred is able to send commands only to minions which match the specified glob target. This can be expanded to include other functions for other minions based on standard targets. </p>
<pre>
external_auth:
  pam:
    dave:
      - test.ping
      - mongo\*:
        - network.*
      - log\*:
        - network.*
        - pkg.*
      - 'G@os:RedHat':
        - kmod.*
    steve:
      - .*
</pre>
<p> The above allows for all minions to be hit by test.ping by dave, and adds a few functions that dave can execute on other minions. It also allows steve unrestricted access to salt commands.</p>
<h2 id="JOB MANAGEMENT"></h2>
<p> New in version 0.9.7. </p>
<p> Since Salt executes jobs running on many systems, Salt needs to be able to manage jobs running on many systems.</p>
<h3>The Minion proc System</h3>
<p> Salt Minions maintain a <i>proc</i> directory in the Salt <code>cachedir</code>. The <i>proc</i> directory maintains files named after the executed job ID. These files contain the information about the current running jobs on the minion and allow for jobs to be looked up. This is located in the <i>proc</i> directory under the cachedir, with a default configuration it is under <code>/var/cache/salt/proc</code>.</p>
<h3>Functions in the saltutil Module</h3>
<p> Salt 0.9.7 introduced a few new functions to the <code>saltutil</code> module for managing jobs. These functions are:</p>
<dl>
<dt>1.</p>
<dd> <code>running</code> Returns the data of all running jobs that are found in the <i>proc</i> directory.</p>
<dt>2.</p>
<dd> <code>find_job</code> Returns specific data about a certain job based on job id.</p>
<dt>3.</p>
<dd> <code>signal_job</code> Allows for a given jid to be sent a signal.</p>
<dt>4.</p>
<dd> <code>term_job</code> Sends a termination signal (SIGTERM, 15) to the process controlling the specified job.</p>
<dt>5.</p>
<dd> <code>kill_job</code> Sends a kill signal (SIGKILL, 9) to the process controlling the specified job. </p>
<p> These functions make up the core of the back end used to manage jobs at the minion level.</dl>
<h3>The jobs Runner</h3>
<p> A convenience runner front end and reporting system has been added as well. The jobs runner contains functions to make viewing data easier and cleaner. </p>
<p> The jobs runner contains a number of functions&#8230;</p>
<h3>active</h3>
<p> The active function runs saltutil.running on all minions and formats the return data about all running jobs in a much more usable and compact format. The active function will also compare jobs that have returned and jobs that are still running, making it easier to see what systems have completed a job and what systems are still being waited on. </p>
<pre>
# salt-run jobs.active
</pre>
<h3>lookup_jid</h3>
<p> When jobs are executed the return data is sent back to the master and cached. By default it is cached for 24 hours, but this can be configured via the <code>keep_jobs</code> option in the master configuration. Using the lookup_jid runner will display the same return data that the initial job invocation with the salt command would display. </p>
<pre>
# salt-run jobs.lookup_jid &lt;job id number&gt;
</pre>
<h3>list_jobs</h3>
<p> Before finding a historic job, it may be required to find the job id. list_jobs will parse the cached execution data and display all of the job data for jobs that have already, or partially returned. </p>
<pre>
# salt-run jobs.list_jobs
</pre>
<h3>Scheduling Jobs</h3>
<p> In Salt versions greater than 0.12.0, the scheduling system allows incremental executions on minions or the master. The schedule system exposes the execution of any execution function on minions or any runner on the master. </p>
<p> Scheduling is enabled via the <code>schedule</code> option on either the master or minion config files, or via a minion&#8217;s pillar data. Schedules that are impletemented via pillar data, only need to refresh the minion&#8217;s pillar data, for example by using <code>saltutil.refresh_pillar</code>. Schedules implemented in the master or minion config have to restart the application in order for the schedule to be implemented. </p>
<p> <code>NOTE:</code> The scheduler executes different functions on the master and minions. When running on the master the functions reference runner functions, when running on the minion the functions specify execution functions. </p>
<p> A scheduled run has no output on the minion unless the config is set to info level or higher. Refer to <code>minion logging settings</code>. </p>
<p> Specify <code>maxrunning</code> to ensure that there are no more than N copies of a particular routine running. Use this for jobs that may be long-running and could step on each other or otherwise double execute. The default for <code>maxrunning</code> is 1. </p>
<p> States are executed on the minion, as all states are. You can pass positional arguments and provide a yaml dict of named arguments. </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
    splay: 15
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) splaying the time between 0 and 15 seconds </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
    splay:
      start: 10
      end: 15
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) splaying the time between 10 and 15 seconds </p>
<p> New in version 2014.7.0. </p>
<p> Frequency of jobs can also be specified using date strings supported by the python dateutil library. This requires python-dateutil to be installed on the minion. </p>
<pre>
schedule:
  job1:
    function: state.sls
    args:
      - httpd
    kwargs:
      test: True
    when: 5:00pm
</pre>
<p> This will schedule the command: state.sls httpd test=True at 5:00pm minion localtime. </p>
<pre>
schedule:
  job1:
    function: state.sls
    args:
      - httpd
    kwargs:
      test: True
    when:
        - Monday 5:00pm
        - Tuesday 3:00pm
        - Wednesday 5:00pm
        - Thursday 3:00pm
        - Friday 5:00pm
</pre>
<p> This will schedule the command: state.sls httpd test=True at 5pm on Monday, Wednesday, and Friday, and 3pm on Tuesday and Thursday. </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
    range:
        start: 8:00am
        end: 5:00pm
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) between the hours of 8am and 5pm. The range parameter must be a dictionary with the date strings using the dateutil format. This requires python-dateutil to be installed on the minion. </p>
<p> New in version 2014.7.0. </p>
<p> The scheduler also supports ensuring that there are no more than N copies of a particular routine running. Use this for jobs that may be long-running and could step on each other or pile up in case of infrastructure outage. </p>
<p> The default for maxrunning is 1. </p>
<pre>
schedule:
  long_running_job:
      function: big_file_transfer
      jid_include: True
</pre>
<h3>States</h3>
<pre>
schedule:
  log-loadavg:
    function: cmd.run
    seconds: 3660
    args:
      - 'logger -t salt &lt; /proc/loadavg'
    kwargs:
      stateful: False
      shell: \bin\sh
</pre>
<h3>Highstates</h3>
<p> To set up a highstate to run on a minion every 60 minutes set this in the minion config or pillar: </p>
<pre>
schedule:
  highstate:
    function: state.highstate
    minutes: 60
</pre>
<p> Time intervals can be specified as seconds, minutes, hours, or days.</p>
<h3>Runners</h3>
<p> Runner executions can also be specified on the master within the master configuration file: </p>
<pre>
schedule:
  run_my_orch:
    function: state.orchestrate
    hours: 6
    splay: 600
    args:
      - orchestration.my_orch
</pre>
<p> The above configuration is analogous to running <code>salt-run state.orch orchestration.my_orch</code> every 6 hours.</p>
<h3>Scheduler With Returner</h3>
<p> The scheduler is also useful for tasks like gathering monitoring data about a minion, this schedule option will gather status data and send it to a MySQL returner database: </p>
<pre>
schedule:
  uptime:
    function: status.uptime
    seconds: 60
    returner: mysql
  meminfo:
    function: status.meminfo
    minutes: 5
    returner: mysql
</pre>
<p> Since specifying the returner repeatedly can be tiresome, the <code>schedule_returner</code> option is available to specify one or a list of global returners to be used by the minions when scheduling. In Salt versions greater than 0.12.0, the scheduling system allows incremental executions on minions or the master. The schedule system exposes the execution of any execution function on minions or any runner on the master. </p>
<p> Scheduling is enabled via the <code>schedule</code> option on either the master or minion config files, or via a minion&#8217;s pillar data. Schedules that are impletemented via pillar data, only need to refresh the minion&#8217;s pillar data, for example by using <code>saltutil.refresh_pillar</code>. Schedules implemented in the master or minion config have to restart the application in order for the schedule to be implemented. </p>
<p> <code>NOTE:</code> The scheduler executes different functions on the master and minions. When running on the master the functions reference runner functions, when running on the minion the functions specify execution functions. </p>
<p> A scheduled run has no output on the minion unless the config is set to info level or higher. Refer to <code>minion logging settings</code>. </p>
<p> Specify <code>maxrunning</code> to ensure that there are no more than N copies of a particular routine running. Use this for jobs that may be long-running and could step on each other or otherwise double execute. The default for <code>maxrunning</code> is 1. </p>
<p> States are executed on the minion, as all states are. You can pass positional arguments and provide a yaml dict of named arguments. </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
    splay: 15
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) splaying the time between 0 and 15 seconds </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
    splay:
      start: 10
      end: 15
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) splaying the time between 10 and 15 seconds </p>
<p> New in version 2014.7.0. </p>
<p> Frequency of jobs can also be specified using date strings supported by the python dateutil library. This requires python-dateutil to be installed on the minion. </p>
<pre>
schedule:
  job1:
    function: state.sls
    args:
      - httpd
    kwargs:
      test: True
    when: 5:00pm
</pre>
<p> This will schedule the command: state.sls httpd test=True at 5:00pm minion localtime. </p>
<pre>
schedule:
  job1:
    function: state.sls
    args:
      - httpd
    kwargs:
      test: True
    when:
        - Monday 5:00pm
        - Tuesday 3:00pm
        - Wednesday 5:00pm
        - Thursday 3:00pm
        - Friday 5:00pm
</pre>
<p> This will schedule the command: state.sls httpd test=True at 5pm on Monday, Wednesday, and Friday, and 3pm on Tuesday and Thursday. </p>
<pre>
schedule:
  job1:
    function: state.sls
    seconds: 3600
    args:
      - httpd
    kwargs:
      test: True
    range:
        start: 8:00am
        end: 5:00pm
</pre>
<p> This will schedule the command: state.sls httpd test=True every 3600 seconds (every hour) between the hours of 8am and 5pm. The range parameter must be a dictionary with the date strings using the dateutil format. This requires python-dateutil to be installed on the minion. </p>
<p> New in version 2014.7.0. </p>
<p> The scheduler also supports ensuring that there are no more than N copies of a particular routine running. Use this for jobs that may be long-running and could step on each other or pile up in case of infrastructure outage. </p>
<p> The default for maxrunning is 1. </p>
<pre>
schedule:
  long_running_job:
      function: big_file_transfer
      jid_include: True
</pre>
<h3>States</h3>
<pre>
schedule:
  log-loadavg:
    function: cmd.run
    seconds: 3660
    args:
      - 'logger -t salt &lt; /proc/loadavg'
    kwargs:
      stateful: False
      shell: \bin\sh
</pre>
<h3>Highstates</h3>
<p> To set up a highstate to run on a minion every 60 minutes set this in the minion config or pillar: </p>
<pre>
schedule:
  highstate:
    function: state.highstate
    minutes: 60
</pre>
<p> Time intervals can be specified as seconds, minutes, hours, or days.</p>
<h3>Runners</h3>
<p> Runner executions can also be specified on the master within the master configuration file: </p>
<pre>
schedule:
  run_my_orch:
    function: state.orchestrate
    hours: 6
    splay: 600
    args:
      - orchestration.my_orch
</pre>
<p> The above configuration is analogous to running <code>salt-run state.orch orchestration.my_orch</code> every 6 hours.</p>
<h3>Scheduler With Returner</h3>
<p> The scheduler is also useful for tasks like gathering monitoring data about a minion, this schedule option will gather status data and send it to a MySQL returner database: </p>
<pre>
schedule:
  uptime:
    function: status.uptime
    seconds: 60
    returner: mysql
  meminfo:
    function: status.meminfo
    minutes: 5
    returner: mysql
</pre>
<p> Since specifying the returner repeatedly can be tiresome, the <code>schedule_returner</code> option is available to specify one or a list of global returners to be used by the minions when scheduling.</p>
<h2 id="MANAGING THE JOB CACHE"></h2>
<p> The Salt Master maintains a job cache of all job executions which can be queried via the jobs runner. This job cache is called the Default Job Cache.</p>
<h3>Default Job Cache</h3>
<p> A number of options are available when configuring the job cache. The default caching system uses local storage on the Salt Master and can be found in the job cache directory (on Linux systems this is typically <code>/var/cache/salt/master/jobs</code>). The default caching system is suitable for most deployments as it does not typically require any further configuration or management. </p>
<p> The default job cache is a temporary cache and jobs will be stored for 24 hours. If the default cache needs to store jobs for a different period the time can be easily adjusted by changing the <i>keep_jobs</i> parameter in the Salt Master configuration file. The value passed in is measured via hours: </p>
<pre>
keep_jobs: 24
</pre>
<h3>Additional Job Cache Options</h3>
<p> Many deployments may wish to use an external database to maintain a long term register of executed jobs. Salt comes with two main mechanisms to do this, the master job cache and the external job cache. </p>
<p> See Storing Job Results in an External System.</p>
<h2 id="STORING JOB RESULTS IN AN EXTERNAL SYSTEM"></h2>
<p> After a job executes, job results are returned to the Salt Master by each Salt Minion. These results are stored in the Default Job Cache. </p>
<p> In addition to the Default Job Cache, Salt provides two additional mechanisms to send job results to other systems (databases, local syslog, and others):</p>
<dl>
<dt>&bull;</p>
<dd> External Job Cache</p>
<dt>&bull;</p>
<dd> Master Job Cache </p>
<p> The major difference between these two mechanism is from where results are returned (from the Salt Master or Salt Minion).</dl>
<h3>External Job Cache &#8211; Minion-Side Returner</h3>
<p> When an External Job Cache is configured, data is returned to the Default Job Cache on the Salt Master like usual, and then results are also sent to an External Job Cache using a Salt returner module running on the Salt Minion. [image]</p>
<dl>
<dt>&bull;</p>
<dd> Advantages: Data is stored without placing additional load on the Salt Master.</p>
<dt>&bull;</p>
<dd> Disadvantages: Each Salt Minion connects to the external job cache, which can result in a large number of connections. Also requires additional configuration to get returner module settings on all Salt Minions.</dl>
<h3>Master Job Cache &#8211; Master-Side Returner</h3>
<p> New in version 2014.7.0. </p>
<p> Instead of configuring an External Job Cache on each Salt Minion, you can configure the Master Job Cache to send job results from the Salt Master instead. In this configuration, Salt Minions send data to the Default Job Cache as usual, and then the Salt Master sends the data to the external system using a Salt returner module running on the Salt Master. [image]</p>
<dl>
<dt>&bull;</p>
<dd> Advantages: A single connection is required to the external system. This is preferred for databases and similar systems.</p>
<dt>&bull;</p>
<dd> Disadvantages: Places additional load on your Salt Master.</dl>
<h3>Configure an External or Master Job Cache</h3>
<h3>Step 1: Understand Salt Returners</h3>
<p> Before you configure a job cache, it is essential to understand Salt returner modules (&quot;returners&quot;). Returners are pluggable Salt Modules that take the data returned by jobs, and then perform any necessary steps to send the data to an external system. For example, a returner might establish a connection, authenticate, and then format and transfer data. </p>
<p> The Salt Returner system provides the core functionality used by the External and Master Job Cache systems, and the same returners are used by both systems. </p>
<p> Salt currently provides many different returners that let you connect to a wide variety of systems. A complete list is available at all Salt returners. Each returner is configured differently, so make sure you read and follow the instructions linked from that page. </p>
<p> For example, the MySQL returner requires:</p>
<dl>
<dt>&bull;</p>
<dd> A database created using provided schema (structure is available at <code>MySQL returner</code>)</p>
<dt>&bull;</p>
<dd> A user created with with privileges to the database</p>
<dt>&bull;</p>
<dd> Optional SSL configuration </p>
<p> A simpler returner, such as Slack or HipChat, requires:</p>
<dt>&bull;</p>
<dd> An API key/version</p>
<dt>&bull;</p>
<dd> The target channel/room</p>
<dt>&bull;</p>
<dd> The username that should be used to send the message</dl>
<h3>Step 2: Configure the Returner</h3>
<p> After you understand the configuration and have the external system ready, add the returner configuration settings to the Salt Minion configuration file for the External Job Cache, or to the Salt Master configuration file for the Master Job Cache. </p>
<p> For example, MySQL requires: </p>
<pre>
mysql.host: 'salt'
mysql.user: 'salt'
mysql.pass: 'salt'
mysql.db: 'salt'
mysql.port: 3306
</pre>
<p> Slack requires: </p>
<pre>
slack.channel: 'channel'
slack.api_key: 'key'
slack.from_name: 'name'
</pre>
<p> After you have configured the returner and added settings to the configuration file, you can enable the External or Master Job Cache.</p>
<h3>Step 3: Enable the External or Master Job Cache</h3>
<p> Configuration is a single line that specifies an already-configured returner to use to send all job data to an external system.</p>
<h3>External Job Cache</h3>
<p> To enable a returner as the External Job Cache (Minion-side), add the following line to the Salt Master configuration file: </p>
<pre>
ext_job_cache: &lt;returner&gt;
</pre>
<p> For example: </p>
<pre>
ext_job_cache: mysql
</pre>
<p> <code>NOTE:</code> When configuring an External Job Cache (Minion-side), the returner settings are added to the Minion configuration file, but the External Job Cache setting is configured in the Master configuration file.</p>
<h3>Master Job Cache</h3>
<p> To enable a returner as a Master Job Cache (Master-side), add the following line to the Salt Master configuration file: </p>
<pre>
master_job_cache: &lt;returner&gt;
</pre>
<p> For example: </p>
<pre>
master_job_cache: mysql
</pre>
<p> Verify that the returner configuration settings are in the Master configuration file, and be sure to restart the salt-master service after you make configuration changes. (<code>service salt-master restart</code>).</p>
<h2 id="STORING DATA IN OTHER DATABASES"></h2>
<p> The SDB interface is designed to store and retrieve data that, unlike pillars and grains, is not necessarily minion-specific. The initial design goal was to allow passwords to be stored in a secure database, such as one managed by the keyring package, rather than as plain-text files. However, as a generic database interface, it could conceptually be used for a number of other purposes. </p>
<p> SDB was added to Salt in version 2014.7.0. SDB is currently experimental, and should probably not be used in production.</p>
<h3>SDB Configuration</h3>
<p> In order to use the SDB interface, a configuration profile must be set up in either the master or minion configuration file. The configuration stanza includes the name/ID that the profile will be referred to as, a <code>driver</code> setting, and any other arguments that are necessary for the SDB module that will be used. For instance, a profile called <code>mykeyring</code>, which uses the <code>system</code> service in the <code>keyring</code> module would look like: </p>
<pre>
mykeyring:
  driver: keyring
  service: system
</pre>
<p> It is recommended to keep the name of the profile simple, as it is used in the SDB URI as well.</p>
<h3>SDB URIs</h3>
<p> SDB is designed to make small database queries (hence the name, SDB) using a compact URL. This allows users to reference a database value quickly inside a number of Salt configuration areas, without a lot of overhead. The basic format of an SDB URI is: </p>
<pre>
sdb://&lt;profile&gt;/&lt;args&gt;
</pre>
<p> The profile refers to the configuration profile defined in either the master or the minion configuration file. The args are specific to the module referred to in the profile, but will typically only need to refer to the key of a key/value pair inside the database. This is because the profile itself should define as many other parameters as possible. </p>
<p> For example, a profile might be set up to reference credentials for a specific OpenStack account. The profile might look like: </p>
<pre>
kevinopenstack:
  driver: keyring
  service: salt.cloud.openstack.kevin
</pre>
<p> And the URI used to reference the password might look like: </p>
<pre>
<a href="sdb://kevinopenstack/password" rel="nofollow">sdb://kevinopenstack/password</a>
</pre>
<h3>Writing SDB Modules</h3>
<p> There is currently one function that MUST exist in any SDB module (<code>get()</code>) and one that MAY exist (<code>set_()</code>). If using a (<code>set_()</code>) function, a <code>__func_alias__</code> dictionary MUST be declared in the module as well: </p>
<pre>
__func_alias__ = {
    'set_': 'set',
}
</pre>
<p> This is because <code>set</code> is a Python built-in, and therefore functions should not be created which are called <code>set()</code>. The <code>__func_alias__</code> functionality is provided via Salt&#8217;s loader interfaces, and allows legally-named functions to be referred to using names that would otherwise be unwise to use. </p>
<p> The <code>get()</code> function is required, as it will be called via functions in other areas of the code which make use of the <code>sdb://</code> URI. For example, the <code>config.get</code> function in the <code>config</code> execution module uses this function. </p>
<p> The <code>set_()</code> function may be provided, but is not required, as some sources may be read-only, or may be otherwise unwise to access via a URI (for instance, because of SQL injection attacks). </p>
<p> A simple example of an SDB module is <code>salt/sdb/keyring_db.py</code>, as it provides basic examples of most, if not all, of the types of functionality that are available not only for SDB modules, but for Salt modules in general.</p>
<h2 id="SALT EVENT SYSTEM"></h2>
<p> The Salt Event System is used to fire off events enabling third party applications or external processes to react to behavior within Salt. </p>
<p> The event system is comprised of a two primary components:</p>
<dl>
<dt>&bull;</p>
<dd> The event sockets which publishes events.</p>
<dt>&bull;</p>
<dd> The event library which can listen to events and send events into the salt system.</dl>
<h3>Event types</h3>
<h3>Salt Master Events</h3>
<p> These events are fired on the Salt Master event bus. This list is <code>not</code> comprehensive.</p>
<h3>Authentication events</h3>
<dl>
<dt><code>salt/auth</code></p>
<dd> Fired when a minion performs an authentication check with the master.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>id</code> &#8212; The minion ID.</p>
<dt>&bull;</p>
<dd> <code>act</code> &#8212; The current status of the minion key: <code>accept</code>, <code>pend</code>, <code>reject</code>.</p>
<dt>&bull;</p>
<dd> <code>pub</code> &#8212; The minion public key. </p>
<p> <code>NOTE:</code> Minions fire auth events on fairly regular basis for a number of reasons. Writing reactors to respond to events through the auth cycle can lead to infinite reactor event loops (minion tries to auth, reactor responds by doing something that generates another auth event, minion sends auth event, etc.). Consider reacting to <code>salt/key</code> or <code>salt/minion/&lt;MID&gt;/start</code> or firing a custom event tag instead.</dl>
<h3>Start events</h3>
<dl>
<dt><code>salt/minion/&lt;MID&gt;/start</code></p>
<dd> Fired every time a minion connects to the Salt master.</p>
<dt><code>Variables</code></p>
<dd> <code>id</code> &#8212; The minion ID.</dl>
<h3>Key events</h3>
<dl>
<dt><code>salt/key</code></p>
<dd> Fired when accepting and rejecting minions keys on the Salt master.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>id</code> &#8212; The minion ID.</p>
<dt>&bull;</p>
<dd> <code>act</code> &#8212; The new status of the minion key: <code>accept</code>, <code>pend</code>, <code>reject</code>. </p>
<p> <code>WARNING:</code> If a master is in <code>auto_accept mode</code>, <code>salt/key</code> events will not be fired when the keys are accepted. In addition, pre-seeding keys (like happens through Salt-Cloud) will not cause firing of these events.</dl>
<h3>Job events</h3>
<dl>
<dt><code>salt/job/&lt;JID&gt;/new</code></p>
<dd> Fired as a new job is sent out to minions.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>jid</code> &#8212; The job ID.</p>
<dt>&bull;</p>
<dd> <code>tgt</code> &#8212; The target of the job: <code>*</code>, a minion ID, <code>G@os_family:RedHat</code>, etc.</p>
<dt>&bull;</p>
<dd> <code>tgt_type</code> &#8212; The type of targeting used: <code>glob</code>, <code>grain</code>, <code>compound</code>, etc.</p>
<dt>&bull;</p>
<dd> <code>fun</code> &#8212; The function to run on minions: <code>test.ping</code>, <code>network.interfaces</code>, etc.</p>
<dt>&bull;</p>
<dd> <code>arg</code> &#8212; A list of arguments to pass to the function that will be called.</p>
<dt>&bull;</p>
<dd> <code>minions</code> &#8212; A list of minion IDs that Salt expects will return data for this job.</p>
<dt>&bull;</p>
<dd> <code>user</code> &#8212; The name of the user that ran the command as defined in Salt&#8217;s Client ACL or external auth.</p>
<dt><code>salt/job/&lt;JID&gt;/ret/&lt;MID&gt;</code></p>
<dd> Fired each time a minion returns data for a job.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>id</code> &#8212; The minion ID.</p>
<dt>&bull;</p>
<dd> <code>jid</code> &#8212; The job ID.</p>
<dt>&bull;</p>
<dd> <code>retcode</code> &#8212; The return code for the job.</p>
<dt>&bull;</p>
<dd> <code>fun</code> &#8212; The function the minion ran. E.g., <code>test.ping</code>.</p>
<dt>&bull;</p>
<dd> <code>return</code> &#8212; The data returned from the execution module.</p>
<dt><code>salt/job/&lt;JID&gt;/prog/&lt;MID&gt;/&lt;RUN NUM&gt;</code></p>
<dd> Fired each time a each function in a state run completes execution. Must be enabled using the <code>state_events</code> option.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>data</code> &#8212; The data returned from the state module function.</p>
<dt>&bull;</p>
<dd> <code>id</code> &#8212; The minion ID.</p>
<dt>&bull;</p>
<dd> <code>jid</code> &#8212; The job ID.</dl>
<h3>Presence events</h3>
<dl>
<dt><code>salt/presence/present</code></p>
<dd> Events fired on a regular interval about currently connected, newly connected, or recently disconnected minions. Requires the <code>presence_events</code> setting to be enabled.</p>
<dt><code>Variables</code></p>
<dd> <code>present</code> &#8212; A list of minions that are currently connected to the Salt master.</p>
<dt><code>salt/presence/change</code></p>
<dd> Fired when the Presence system detects new minions connect or disconnect.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>new</code> &#8212; A list of minions that have connected since the last presence event.</p>
<dt>&bull;</p>
<dd> <code>lost</code> &#8212; A list of minions that have disconnected since the last presence event.</dl>
<h3>Cloud Events</h3>
<p> Unlike other Master events, <code>salt-cloud</code> events are not fired on behalf of a Salt Minion. Instead, <code>salt-cloud</code> events are fired on behalf of a VM. This is because the minion-to-be may not yet exist to fire events to or also may have been destroyed. </p>
<p> This behavior is reflected by the <code>name</code> variable in the event data for <code>salt-cloud</code> events as compared to the <code>id</code> variable for Salt Minion-triggered events.</p>
<dl>
<dt><code>salt/cloud/&lt;VM NAME&gt;/creating</code></p>
<dd> Fired when salt-cloud starts the VM creation process.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the name of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>provider</code> &#8212; the cloud provider of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>profile</code> &#8212; the cloud profile for the VM being created.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/deploying</code></p>
<dd> Fired when the VM is available and salt-cloud begins deploying Salt to the new VM.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the name of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>kwargs</code> &#8212; options available as the deploy script is invoked: <code>conf_file</code>, <code>deploy_command</code>, <code>display_ssh_output</code>, <code>host</code>, <code>keep_tmp</code>, <code>key_filename</code>, <code>make_minion</code>, <code>minion_conf</code>, <code>name</code>, <code>parallel</code>, <code>preseed_minion_keys</code>, <code>script</code>, <code>script_args</code>, <code>script_env</code>, <code>sock_dir</code>, <code>start_action</code>, <code>sudo</code>, <code>tmp_dir</code>, <code>tty</code>, <code>username</code></p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/requesting</code></p>
<dd> Fired when salt-cloud sends the request to create a new VM.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>location</code> &#8212; the location of the VM being requested.</p>
<dt>&bull;</p>
<dd> <code>kwargs</code> &#8212; options available as the VM is being requested: <code>Action</code>, <code>ImageId</code>, <code>InstanceType</code>, <code>KeyName</code>, <code>MaxCount</code>, <code>MinCount</code>, <code>SecurityGroup.1</code></p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/querying</code></p>
<dd> Fired when salt-cloud queries data for a new instance.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>instance_id</code> &#8212; the ID of the new VM.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/tagging</code></p>
<dd> Fired when salt-cloud tags a new instance.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>tags</code> &#8212; tags being set on the new instance.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/waiting_for_ssh</code></p>
<dd> Fired while the salt-cloud deploy process is waiting for ssh to become available on the new instance.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>ip_address</code> &#8212; IP address of the new instance.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/deploy_script</code></p>
<dd> Fired once the deploy script is finished.</p>
<dt><code>Variables</code></p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/created</code></p>
<dd> Fired once the new instance has been fully created.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the name of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>instance_id</code> &#8212; the ID of the new instance.</p>
<dt>&bull;</p>
<dd> <code>provider</code> &#8212; the cloud provider of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>profile</code> &#8212; the cloud profile for the VM being created.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/destroying</code></p>
<dd> Fired when salt-cloud requests the destruction of an instance.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the name of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>instance_id</code> &#8212; the ID of the new instance.</p>
<dt><code>salt/cloud/&lt;VM NAME&gt;/destroyed</code></p>
<dd> Fired when an instance has been destroyed.</p>
<dt><code>Variables</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the name of the VM being created.</p>
<dt>&bull;</p>
<dd> <code>event</code> &#8212; description of the event.</p>
<dt>&bull;</p>
<dd> <code>instance_id</code> &#8212; the ID of the new instance.</dl>
<h3>Listening for Events</h3>
<p> Salt&#8217;s Event Bus is used heavily within Salt and it is also written to integrate heavily with existing tooling and scripts. There is a variety of ways to consume it.</p>
<h3>From the CLI</h3>
<p> The quickest way to watch the event bus is by calling the <code>state.event runner</code>: </p>
<pre>
salt-run state.event pretty=True
</pre>
<p> That runner is designed to interact with the event bus from external tools and shell scripts. See the documentation for more examples.</p>
<h3>Remotely via the REST API</h3>
<p> Salt&#8217;s event bus can be consumed <code>salt.netapi.rest_cherrypy.app.Events</code> as an HTTP stream from external tools or services. </p>
<pre>
curl -SsNk <a rel="nofollow noopener" href="https://salt-api.example.com:8000/events?token=05A3" target="_blank">https://salt-api.example.com:8000/events?token=05A3</a>
</pre>
<h3>From Python</h3>
<p> Python scripts can access the event bus only as the same system user that Salt is running as. </p>
<p> The event system is accessed via the event library and can only be accessed by the same system user that Salt is running as. To listen to events a SaltEvent object needs to be created and then the get_event function needs to be run. The SaltEvent object needs to know the location that the Salt Unix sockets are kept. In the configuration this is the <code>sock_dir</code> option. The <code>sock_dir</code> option defaults to &quot;/var/run/salt/master&quot; on most systems. </p>
<p> The following code will check for a single event: </p>
<p>import salt.config import salt.utils.event opts = salt.config.client_config(&#8216;/etc/salt/master&#8217;)<br />
                                                                                event = salt.utils.event.get_event(<br />
                                                                                    &#8216;master&#8217;,<br />
                                                                                    sock_dir = opts[&#8216;sock_dir&#8217;],<br />
                                                                                                    transport = opts[&#8216;transport&#8217;],<br />
                                                                                                                     opts = opts)<br />
                                                                                                                         data = event.get_event()</p>
<p> Events will also use a &quot;tag&quot;. Tags allow for events to be filtered by prefix. By default all events will be returned. If only authentication events are desired, then pass the tag &quot;salt/auth&quot;. </p>
<p> The <code>get_event</code> method has a default poll time assigned of 5 seconds. To change this time set the &quot;wait&quot; option. </p>
<p> The following example will only listen for auth events and will wait for 10 seconds instead of the default 5. </p>
<pre>
data = event.get_event(wait=10, tag='salt/auth')
</pre>
<p> To retrieve the tag as well as the event data, pass <code>full=True</code>: </p>
<p>evdata = event.get_event(wait = 10, tag = &#8216;salt/job&#8217;, full = True)<br />
             tag,<br />
    data = evdata[&#8216;tag&#8217;], evdata[&#8216;data&#8217;]</p>
<p> Instead of looking for a single event, the <code>iter_events</code> method can be used to make a generator which will continually yield salt events. </p>
<p> The iter_events method also accepts a tag but not a wait time: </p>
<pre>
for data in event.iter_events(tag='salt/auth'):
    print(data)
</pre>
<p> And finally event tags can be globbed, such as they can be in the Reactor, using the fnmatch library. </p>
<p>import fnmatch import salt.config import salt.utils.event opts = salt.config.client_config(&#8216;/etc/salt/master&#8217;)<br />
                                                                                               sevent = salt.utils.event.get_event(<br />
                                                                                                   &#8216;master&#8217;,<br />
                                                                                                   sock_dir = opts[&#8216;sock_dir&#8217;],<br />
                                                                                                                   transport = opts[&#8216;transport&#8217;],<br />
                                                                                                                                    opts = opts) while True:ret = sevent.get_event(full = True) if ret is None: continue if fnmatch.fnmatch(ret[&#8216;tag&#8217;], &#8216;salt/job/*/ret/*&#8217;) :do_something_with_job_return(ret[&#8216;data&#8217;])</p>
<h3>Firing Events</h3>
<p> It is possible to fire events on either the minion&#8217;s local bus or to fire events intended for the master. </p>
<p> To fire a local event from the minion on the command line call the <code>event.fire</code> execution function: </p>
<pre>
salt-call event.fire '{&quot;data&quot;: &quot;message to be sent in the event&quot;}' 'tag'
</pre>
<p> To fire an event to be sent up to the master from the minion call the <code>event.send</code> execution function. Remember YAML can be used at the CLI in function arguments: </p>
<pre>
salt-call event.send 'myco/mytag/success' '{success: True, message: &quot;It works!&quot;}'
</pre>
<p> If a process is listening on the minion, it may be useful for a user on the master to fire an event to it: </p>
<pre>
# Job on minion
import salt.utils.event
event = salt.utils.event.MinionEvent(**__opts__)
for evdata in event.iter_events(tag='customtag/'):
    return evdata # do your processing here...
</pre>
<pre>
salt minionname event.fire '{&quot;data&quot;: &quot;message for the minion&quot;}' 'customtag/african/unladen'
</pre>
<h3>Firing Events from Python</h3>
<h3>From Salt execution modules</h3>
<p> Events can be very useful when writing execution modules, in order to inform various processes on the master when a certain task has taken place. This is easily done using the normal cross-calling syntax: </p>
<p>#/ srv / salt / _modules / my_custom_module.py<br />
def do_something()<br />
    :<br />
    &#8221;&#8217; Do something and fire an event to the master when finished<br />
      CLI Example::<br />
          salt &#8216;*&#8217; my_custom_module : do_something<br />
    &#8221;&#8217;<br />
#do something !<br />
                                      __salt__[&#8216;event.send&#8217;](&#8216;myco/my_custom_module/finished&#8217;, {<br />
                                          &#8216;finished&#8217; : True,<br />
                                          &#8216;message&#8217; : &#8220;The something is finished!&#8221;,<br />
                                      })</p>
<h3>From Custom Python Scripts</h3>
<p> Firing events from custom Python code is quite simple and mirrors how it is done at the CLI: </p>
<p>import salt.client caller = salt.client.Caller()<br />
                                                   caller.sminion.functions[&#8216;event.send&#8217;](<br />
                                                       &#8216;myco/myevent/success&#8217;,<br />
                                                       {<br />
                                                           &#8216;success&#8217; :True,<br />
                                                           &#8216;message&#8217; : &#8220;It works!&#8221;, })</p>
<h2 id="BEACONS"></h2>
<p> The beacon system allows the minion to hook into a variety of system processes and continually monitor these processes. When monitored activity occurs in a system process, an event is sent on the Salt event bus that can be used to trigger a reactor. </p>
<p> Salt beacons can currently monitor and send Salt events for many system activities, including:</p>
<dl>
<dt>&bull;</p>
<dd> file system changes</p>
<dt>&bull;</p>
<dd> system load</p>
<dt>&bull;</p>
<dd> service status</p>
<dt>&bull;</p>
<dd> shell activity, such as user login</p>
<dt>&bull;</p>
<dd> network and disk usage </p>
<p> See beacon modules for a current list. </p>
<p> <code>NOTE:</code> Salt beacons are an event generation mechanism. Beacons leverage the Salt reactor system to make changes when beacon events occur.</dl>
<h3>Configuring Beacons</h3>
<p> Salt beacons do not require any changes to the system process that is being monitored, everything is configured using Salt. </p>
<p> Beacons are typically enabled by placing a <code>beacons:</code> top level block in the minion configuration file: </p>
<p>beacons : inotify : / etc / httpd / conf.d : {} / opt:<br />
{<br />
}</p>
<p> The beacon system, like many others in Salt, can also be configured via the minion pillar, grains, or local config file.</p>
<h3>Beacon Monitoring Interval</h3>
<p> Beacons monitor on a 1-second interval by default. To set a different interval, provide an <code>interval</code> argument to a beacon. The following beacons run on 5- and 10-second intervals: </p>
<p>beacons : inotify : / etc / httpd / conf.d : {} / opt:<br />
{<br />
}<br />
interval : 5 load : -1m : -0.0 &#8211; 2.0 &#8211; 5m : -0.0 &#8211; 1.5 &#8211; 15m : -0.1 &#8211; 1.0 &#8211; interval : 10</p>
<h3>Beacon Example</h3>
<p> This example demonstrates configuring the <code>inotify</code> beacon to monitor a file for changes, and then create a backup each time a change is detected. </p>
<p> <code>NOTE:</code> The inotify beacon requires Pyinotify on the minion, install it using <code>salt myminion pkg.install python-inotify</code>. </p>
<p> First, on the Salt minion, add the following beacon configuration to <code>/ect/salt/minion</code>: </p>
<pre>
beacons:
  inotify:
    home/user/importantfile:
      mask:
        - modify
</pre>
<p> Replace <code>user</code> in the previous example with the name of your user account, and then save the configuration file and restart the minion service. </p>
<p> Next, create a file in your home directory named <code>importantfile</code> and add some simple content. The beacon is now set up to monitor this file for modifications.</p>
<h3>View Events on the Master</h3>
<p> On your Salt master, start the event runner using the following command: </p>
<pre>
salt-run state.event pretty=true
</pre>
<p> This runner displays events as they are received on the Salt event bus. To test the beacon you set up in the previous section, make and save a modification to the <code>importantfile</code> you created. You&#8217;ll see an event similar to the following on the event bus: </p>
<p>salt / beacon / minion1 / inotify / home / user / importantfile<br />
{<br />
    &#8220;_stamp&#8221; : &#8220;2015-09-09T15:59:37.972753&#8221;,<br />
               &#8220;data&#8221; : {<br />
                   &#8220;change&#8221; : &#8220;IN_IGNORED&#8221;,<br />
                   &#8220;id&#8221; : &#8220;minion1&#8221;,<br />
                   &#8220;path&#8221; : &#8220;/home/user/importantfile&#8221;<br />
               },<br />
                        &#8220;tag&#8221; : &#8220;salt/beacon/minion1/inotify/home/user/importantfile&#8221;<br />
}</p>
<p> This indicates that the event is being captured and sent correctly. Now you can create a reactor to take action when this event occurs.</p>
<h3>Create a Reactor</h3>
<p> On your Salt master, create a file named <code>srv/reactor/backup.sls</code>. If the <code>reactor</code> directory doesn&#8217;t exist, create it. Add the following to <code>backup.sls</code>: </p>
<p>backup file : cmd.file.copy : -tgt : &#123;&#123;data[&#8216;data&#8217;][&#8216;id&#8217;]}} &#8211; arg : -&#123;&#123;data[&#8216;data&#8217;][&#8216;path&#8217;]}} &#8211; &#123;&#123;data[&#8216;data&#8217;][&#8216;path&#8217;]}}.bak</p>
<p> Next, add the code to trigger the reactor to <code>ect/salt/master</code>: </p>
<pre>
reactor:
  - salt/beacon/*/inotify/*/importantfile:
    - /srv/reactor/backup.sls
</pre>
<p> This reactor creates a backup each time a file named <code>importantfile</code> is modified on a minion that has the <code>inotify</code> beacon configured as previously shown. </p>
<p> <code>NOTE:</code> You can have only one top level <code>reactor</code> section, so if one already exists, add this code to the existing section. See Understanding the Structure of Reactor Formulas to learn more about reactor SLS syntax.</p>
<h3>Start the Salt Master in Debug Mode</h3>
<p> To help with troubleshooting, start the Salt master in debug mode: </p>
<pre>
service salt-master stop
salt-master -l debug
</pre>
<p> When debug logging is enabled, event and reactor data are displayed so you can discover syntax and other issues.</p>
<h3>Trigger the Reactor</h3>
<p> On your minion, make and save another change to <code>importantfile</code>. On the Salt master, you&#8217;ll see debug messages that indicate the event was received and the <code>file.copy</code> job was sent. When you list the directory on the minion, you&#8217;ll now see <code>importantfile.bak</code>. </p>
<p> All beacons are configured using a similar process of enabling the beacon, writing a reactor SLS, and mapping a beacon event to the reactor SLS.</p>
<h3>Writing Beacon Plugins</h3>
<p> Beacon plugins use the standard Salt loader system, meaning that many of the constructs from other plugin systems holds true, such as the <code>__virtual__</code> function. </p>
<p> The important function in the Beacon Plugin is the <code>beacon</code> function. When the beacon is configured to run, this function will be executed repeatedly by the minion. The <code>beacon</code> function therefore cannot block and should be as lightweight as possible. The <code>beacon</code> also must return a list of dicts, each dict in the list will be translated into an event on the master. </p>
<p> Please see the <code>inotify</code> beacon as an example.</p>
<h2 id="RUNNING CUSTOM MASTER PROCESSES"></h2>
<p> In addition to the processes that the Salt Master automatically spawns, it is possible to configure it to start additional custom processes. </p>
<p> This is useful if a dedicated process is needed that should run throughout the life of the Salt Master. For periodic independent tasks, a <code>scheduled runner</code> may be more appropriate. </p>
<p> Processes started in this way will be restarted if they die and will be killed when the Salt Master is shut down.</p>
<h3>Example Configuration</h3>
<p> Processes are declared in the master config file with the <i>ext_processes</i> option. Processes will be started in the order they are declared. </p>
<pre>
ext_processes:
  - mymodule.TestProcess
  - mymodule.AnotherProcess
</pre>
<h3>Example Process Class</h3>
<p>#Import python libs<br />
import time import logging from multiprocessing import Process<br />
#Import Salt libs<br />
    from salt.utils.event import SaltEvent log = logging.getLogger(__name__) class TestProcess(Process) :def __init__(self, opts) :Process.__init__(self)<br />
                                                                                                                                                        self.opts = opts def run(self) :self.event = SaltEvent(&#8216;master&#8217;, self.opts[&#8216;sock_dir&#8217;])<br />
                                                                                                                                                                                                                             i = 0 while True:self.event.fire_event({&#8216;iteration&#8217; :i }, &#8216;ext_processes/test{0}&#8217;)<br />
                                                                                                                                                                                                                                                                                           time.sleep(60)</p>
<h2 id="HIGH AVAILABILITY FEATURES IN SALT"></h2>
<p> Salt supports several features for high availability and fault tolerance. Brief documentation for these features is listed alongside their configuration parameters in Configuration file examples.</p>
<h3>Multimaster</h3>
<p> Salt minions can connect to multiple masters at one time by configuring the <i>master</i> configuration paramter as a YAML list of all the available masters. By default, all masters are &quot;hot&quot;, meaning that any master can direct commands to the Salt infrastructure. </p>
<p> In a multimaster configuration, each master must have the same cryptographic keys, and minion keys must be accepted on all masters separately. The contents of file_roots and pillar_roots need to be kept in sync with processes external to Salt as well </p>
<p> A tutorial on setting up multimaster with &quot;hot&quot; masters is here: </p>
<p> <code>Multimaster Tutorial</code></p>
<h3>Multimaster with Failover</h3>
<p> Changing the <code>master_type</code> parameter from <code>str</code> to <code>failover</code> will cause minions to connect to the first responding master in the list of masters. Every <code>master_alive_check</code> seconds the minions will check to make sure the current master is still responding. If the master does not respond, the minion will attempt to connect to the next master in the list. If the minion runs out of masters, the list will be recycled in case dead masters have been restored. Note that <code>master_alive_check</code> must be present in the minion configuration, or else the recurring job to check master status will not get scheduled. </p>
<p> Failover can be combined with PKI-style encrypted keys, but PKI is NOT REQUIRED to use failover. </p>
<p> Multimaster with PKI and Failover is discussed in <code>this tutorial</code> </p>
<p> <code>master_type: failover</code> can be combined with <code>master_shuffle: True</code> to spread minion connections across all masters (one master per minion, not each minion connecting to all masters). Adding Salt Syndics into the mix makes it possible to create a load-balanced Salt infrastructure. If a master fails, minions will notice and select another master from the available list.</p>
<h3>Syndic</h3>
<p> Salt&#8217;s Syndic feature is a way to create differing infrastructure topologies. It is not strictly an HA feature, but can be treated as such. </p>
<p> With the syndic, a Salt infrastructure can be partitioned in such a way that certain masters control certain segments of the infrastructure, and &quot;Master of Masters&quot; nodes can control multiple segments underneath them. </p>
<p> Syndics are covered in depth in <code>Salt Syndic</code>.</p>
<h3>Syndic with Multimaster</h3>
<p> New in version 2015.5.0. </p>
<p> Syndic with Multimaster lets you connect a syndic to multiple masters to provide an additional layer of redundancy in a syndic configuration. </p>
<p> Syndics are covered in depth in <code>Salt Syndic</code>.</p>
<h2 id="SALT SYNDIC"></h2>
<p> The most basic or typical Salt topology consists of a single Master node controlling a group of Minion nodes. An intermediate node type, called Syndic, when used offers greater structural flexibility and scalability in the construction of Salt topologies than topologies constructed only out of Master and Minion node types. </p>
<p> A Syndic node can be thought of as a special passthrough Minion node. A Syndic node consists of a <code>salt-syndic</code> daemon and a <code>salt-master</code> daemon running on the same system. The <code>salt-master</code> daemon running on the Syndic node controls a group of lower level Minion nodes and the <code>salt-syndic</code> daemon connects higher level Master node, sometimes called a Master of Masters. </p>
<p> The <code>salt-syndic</code> daemon relays publications and events between the Master node and the local <code>salt-master</code> daemon. This gives the Master node control over the Minion nodes attached to the <code>salt-master</code> daemon running on the Syndic node.</p>
<h3>Configuring the Syndic</h3>
<p> To setup a Salt Syndic you need to tell the Syndic node and its Master node about each other. If your Master node is located at <code>10.10.0.1</code>, then your configurations would be: </p>
<p> On the Syndic node: </p>
<pre>
# /etc/salt/master
syndic_master: 10.10.0.1  # may be either an IP address or a hostname
</pre>
<pre>
# /etc/salt/minion
# id is shared by the salt-syndic daemon and a possible salt-minion daemon
# on the Syndic node
id: my_syndic
</pre>
<p> On the Master node: </p>
<pre>
# /etc/salt/master
order_masters: True
</pre>
<p> The <code>syndic_master</code> option tells the Syndic node where to find the Master node in the same way that the <code>master</code> option tells a Minion node where to find a Master node. </p>
<p> The <code>id</code> option is used by the <code>salt-syndic</code> daemon to identify with the Master node and if unset will default to the hostname or IP address of the Syndic just as with a Minion. </p>
<p> The <code>order_masters</code> option configures the Master node to send extra information with its publications that is needed by Syndic nodes connected directly to it. </p>
<p> <code>NOTE:</code> Each Syndic must provide its own <code>file_roots</code> directory. Files will not be automatically transferred from the Master node.</p>
<h3>Configuring the Syndic with Multimaster</h3>
<p> New in version 2015.5.0. </p>
<p> Syndic with Multimaster lets you connect a syndic to multiple masters to provide an additional layer of redundancy in a syndic configuration. </p>
<p> Higher level masters should first be configured in a multimaster configuration. See <code>Multimaster Tutorial</code>. </p>
<p> On the syndic, the <code>syndic_master</code> option is populated with a list of the higher level masters. </p>
<p> Since each syndic is connected to each master, jobs sent from any master are forwarded to minions that are connected to each syndic. If the <code>master_id</code> value is set in the master config on the higher level masters, job results are returned to the master that originated the request in a best effort fashion. Events/jobs without a <code>master_id</code> are returned to any available master.</p>
<h3>Running the Syndic</h3>
<p> The <code>salt-syndic</code> daemon is a separate process that needs to be started in addition to the <code>salt-master</code> daemon running on the Syndic node. Starting the <code>salt-syndic</code> daemon is the same as starting the other Salt daemons. </p>
<p> The Master node in many ways sees the Syndic as an ordinary Minion node. In particular, the Master will need to accept the Syndic&#8217;s Minion key as it would for any other Minion. </p>
<p> On the Syndic node: </p>
<pre>
# salt-syndic
or
# service salt-syndic start
</pre>
<p> On the Master node: </p>
<pre>
# salt-key -a my_syndic
</pre>
<p> The Master node will now be able to control the Minion nodes connected to the Syndic. Only the Syndic key will be listed in the Master node&#8217;s key registry but this also means that key activity between the Syndic&#8217;s Minions and the Syndic does not encumber the Master node. In this way, the Syndic&#8217;s key on the Master node can be thought of as a placeholder for the keys of all the Minion and Syndic nodes beneath it, giving the Master node a clear, high level structural view on the Salt cluster. </p>
<p> On the Master node: </p>
<pre>
# salt-key -L
Accepted Keys:
my_syndic
Denied Keys:
Unaccepted Keys:
Rejected Keys:
# salt '*' test.ping
minion_1:
    True
minion_2:
    True
minion_4:
    True
minion_3:
    True
</pre>
<h3>Topology</h3>
<p> A Master node (a node which is itself not a Syndic to another higher level Master node) must run a <code>salt-master</code> daemon and optionally a <code>salt-minion</code> daemon. </p>
<p> A Syndic node must run <code>salt-syndic</code> and <code>salt-master</code> daemons and optionally a <code>salt-minion</code> daemon. </p>
<p> A Minion node must run a <code>salt-minion</code> daemon. </p>
<p> When a <code>salt-master</code> daemon issues a command, it will be received by the Syndic and Minion nodes directly connected to it. A Minion node will process the command in the way it ordinarily would. On a Syndic node, the <code>salt-syndic</code> daemon will relay the command to the <code>salt-master</code> daemon running on the Syndic node, which then propagates the command to to the Minions and Syndics connected to it. </p>
<p> When events and job return data are generated by <code>salt-minion</code> daemons, they are aggregated by the <code>salt-master</code> daemon they are connected to, which <code>salt-master</code> daemon then relays the data back through its <code>salt-syndic</code> daemon until the data reaches the Master or Syndic node that issued the command.</p>
<h3>Syndic wait</h3>
<p> <code>NOTE:</code> To reduce the amount of time the CLI waits for Minions to respond, install a Minion on the Syndic or tune the value of the <code>syndic_wait</code> configuration. </p>
<p> While it is possible to run a Syndic without a Minion installed on the same system, it is recommended, for a faster CLI response time, to do so. Without a Minion installed on the Syndic node, the timeout value of <code>syndic_wait</code> increases significantly &#8211; about three-fold. With a Minion installed on the Syndic, the CLI timeout resides at the value defined in <code>syndic_wait</code>. </p>
<p> <code>NOTE:</code> If you have a very large infrastructure or many layers of Syndics, you may find that the CLI doesn&#8217;t wait long enough for the Syndics to return their events. If you think this is the case, you can set the <code>syndic_wait</code> value in the Master configs on the Master or Syndic nodes from which commands are executed. The default value is <code>5</code>, and should work for the majority of deployments. </p>
<p> In order for a Master or Syndic node to return information from Minions that are below their Syndics, the CLI requires a short wait time in order to allow the Syndics to gather responses from their Minions. This value is defined in the <code>syndic_wait</code> config option and has a default of five seconds.</p>
<h3>Syndic config options</h3>
<p> These are the options that can be used to configure a Syndic node. Note that other than <code>id</code>, Syndic config options are placed in the Master config on the Syndic node.</p>
<dl>
<dt>&bull;</p>
<dd> <code>id</code>: Syndic id (shared by the <code>salt-syndic</code> daemon with a potential <code>salt-minion</code> daemon on the same system)</p>
<dt>&bull;</p>
<dd> <code>syndic_master</code>: Master node IP address or hostname</p>
<dt>&bull;</p>
<dd> <code>syndic_master_port</code>: Master node ret_port</p>
<dt>&bull;</p>
<dd> <code>syndic_log_file</code>: path to the logfile (absolute or not)</p>
<dt>&bull;</p>
<dd> <code>syndic_pidfile</code>: path to the pidfile (absolute or not)</p>
<dt>&bull;</p>
<dd> <code>syndic_wait</code>: time in seconds to wait on returns from this syndic</dl>
<h2 id="SALT PROXY MINION DOCUMENTATION"></h2>
<p> Proxy minions are a developing Salt feature that enables controlling devices that, for whatever reason, cannot run a standard salt-minion. Examples include network gear that has an API but runs a proprietary OS, devices with limited CPU or memory, or devices that could run a minion, but for security reasons, will not. </p>
<p> <i>Proxy minions are not an &quot;out of the box&quot; feature</i>. Because there are an infinite number of controllable devices, you will most likely have to write the interface yourself. Fortunately, this is only as difficult as the actual interface to the proxied device. Devices that have an existing Python module (PyUSB for example) would be relatively simple to interface. Code to control a device that has an HTML REST-based interface should be easy. Code to control your typical housecat would be excellent source material for a PhD thesis. </p>
<p> Salt proxy-minions provide the &#8216;plumbing&#8217; that allows device enumeration and discovery, control, status, remote execution, and state management.</p>
<h3>Getting Started</h3>
<p> The following diagram may be helpful in understanding the structure of a Salt installation that includes proxy-minions: [image] </p>
<p> The key thing to remember is the left-most section of the diagram. Salt&#8217;s nature is to have a minion connect to a master, then the master may control the minion. However, for proxy minions, the target device cannot run a minion, and thus must rely on a separate minion to fire up the proxy-minion and make the initial and persistent connection. </p>
<p> After the proxy minion is started and initiates its connection to the &#8216;dumb&#8217; device, it connects back to the salt-master and ceases to be affiliated in any way with the minion that started it. </p>
<p> To create support for a proxied device one needs to create four things:</p>
<dl>
<dt>1.</p>
<dd> The <i>proxy_connection_module</i> (located in salt/proxy).</p>
<dt>2.</p>
<dd> The <i>grains support code</i> (located in salt/grains).</p>
<dt>3.</p>
<dd> Salt modules specific to the controlled device.</p>
<dt>4.</p>
<dd> Salt states specific to the controlled device.</dl>
<h3>Configuration parameters on the master</h3>
<p> Proxy minions require no configuration parameters in /etc/salt/master. </p>
<p> Salt&#8217;s Pillar system is ideally suited for configuring proxy-minions. Proxies can either be designated via a pillar file in pillar_roots, or through an external pillar. External pillars afford the opportunity for interfacing with a configuration management system, database, or other knowledgeable system that that may already contain all the details of proxy targets. To use static files in pillar_roots, pattern your files after the following examples, which are based on the diagram above: </p>
<p> <code>/srv/pillar/top.sls</code> </p>
<pre>
base:
  minioncontroller1:
    - networkswitches
  minioncontroller2:
    - reallydumbdevices
  minioncontroller3:
    - smsgateway
</pre>
<p> <code>/srv/pillar/networkswitches.sls</code> </p>
<pre>
proxy:
  dumbdevice1:
    proxytype: networkswitch
    host: 172.23.23.5
    username: root
    passwd: letmein
  dumbdevice2:
    proxytype: networkswitch
    host: 172.23.23.6
    username: root
    passwd: letmein
  dumbdevice3:
    proxytype: networkswitch
    host: 172.23.23.7
    username: root
    passwd: letmein
</pre>
<p> <code>/srv/pillar/reallydumbdevices.sls</code> </p>
<pre>
proxy:
  dumbdevice4:
    proxytype: i2c_lightshow
    i2c_address: 1
  dumbdevice5:
    proxytype: i2c_lightshow
    i2c_address: 2
  dumbdevice6:
    proxytype: 433mhz_wireless
</pre>
<p> <code>/srv/pillar/smsgateway.sls</code> </p>
<pre>
proxy:
  minioncontroller3:
    dumbdevice7:
      proxytype: sms_serial
      deventry: /dev/tty04
</pre>
<p> Note the contents of each minioncontroller key may differ widely based on the type of device that the proxy-minion is managing. </p>
<p> In the above example</p>
<dl>
<dt>&bull;</p>
<dd> dumbdevices 1, 2, and 3 are network switches that have a management interface available at a particular IP address.</p>
<dt>&bull;</p>
<dd> dumbdevices 4 and 5 are very low-level devices controlled over an i2c bus. In this case the devices are physically connected to machine &#8216;minioncontroller2&#8217;, and are addressable on the i2c bus at their respective i2c addresses.</p>
<dt>&bull;</p>
<dd> dumbdevice6 is a 433 MHz wireless transmitter, also physically connected to minioncontroller2</p>
<dt>&bull;</p>
<dd> dumbdevice7 is an SMS gateway connected to machine minioncontroller3 via a serial port. </p>
<p> Because of the way pillar works, each of the salt-minions that fork off the proxy minions will only see the keys specific to the proxies it will be handling. In other words, from the above example, only minioncontroller1 will see the connection information for dumbdevices 1, 2, and 3. Minioncontroller2 will see configuration data for dumbdevices 4, 5, and 6, and minioncontroller3 will be privy to dumbdevice7. </p>
<p> Also, in general, proxy-minions are lightweight, so the machines that run them could conceivably control a large number of devices. The example above is just to illustrate that it is possible for the proxy services to be spread across many machines if necessary, or intentionally run on machines that need to control devices because of some physical interface (e.g. i2c and serial above). Another reason to divide proxy services might be security. In more secure environments only certain machines may have a network path to certain devices. </p>
<p> Now our salt-minions know if they are supposed to spawn a proxy-minion process to control a particular device. That proxy-minion process will initiate a connection back to the master to enable control.</dl>
<h3>Proxymodules</h3>
<p> A proxy module encapsulates all the code necessary to interface with a device. Proxymodules are located inside the salt.proxy module. At a minimum a proxymodule object must implement the following functions: </p>
<p> <code>__virtual__()</code>: This function performs the same duty that it does for other types of Salt modules. Logic goes here to determine if the module can be loaded, checking for the presence of Python modules on which the proxy deepends. Returning <code>False</code> will prevent the module from loading. </p>
<p> <code>init(opts)</code>: Perform any initialization that the device needs. This is a good place to bring up a persistent connection to a device, or authenticate to create a persistent authorization token. </p>
<p> <code>id(opts)</code>: Returns a unique, unchanging id for the controlled device. This is the &quot;name&quot; of the device, and is used by the salt-master for targeting and key authentication. </p>
<p> <code>shutdown()</code>: Code to cleanly shut down or close a connection to a controlled device goes here. This function must exist, but can contain only the keyword <code>pass</code> if there is no shutdown logic required. </p>
<p> <code>ping()</code>: While not required, it is highly recommended that this function also be defined in the proxymodule. The code for <code>ping</code> should contact the controlled device and make sure it is really available. </p>
<p> Here is an example proxymodule used to interface to a <i>very</i> simple REST server. Code for the server is in the <i>salt-contrib GitHub repository</i> </p>
<p> This proxymodule enables &quot;service&quot; enumration, starting, stopping, restarting, and status; &quot;package&quot; installation, and a ping. </p>
<p>#- * &#8211; coding : utf &#8211; 8 &#8211; * &#8211;<br />
&#8221;&#8217;<br />
This is a simple proxy-minion designed to connect to and communicate with<br />
the bottle-based web service contained in<br />
https://github.com/saltstack/salt-contrib/proxyminion_rest_example<br />
&#8221;&#8217;<br />
from __future__ import absolute_import<br />
#Import python libs<br />
import logging<br />
import salt.utils.http<br />
HAS_REST_EXAMPLE = True<br />
#This must be present or the Salt loader won&#8217;t load this module<br />
__proxyenabled__ = [&#8216;rest_sample&#8217;]<br />
#Variables are scoped to this module so we can have persistent data<br />
#across calls to fns in here.<br />
GRAINS_CACHE = {}<br />
DETAILS = {}<br />
#Want logging !<br />
log = logging.getLogger(__file__)<br />
#This does nothing, it&#8217;s here just as an example and to provide a log<br />
#entry when the module is loaded.<br />
def __virtual__():<br />
    &#8221;&#8217;<br />
    Only return if all the modules are available<br />
    &#8221;&#8217;<br />
    log.debug(&#8216;rest_sample proxy __virtual__() called&#8230;&#8217;)<br />
    return True<br />
#Every proxy module needs an &#8216;init&#8217;, though you can<br />
#just put a &#8216;pass&#8217; here if it doesn&#8217;t need to do anything.<br />
def init(opts):<br />
    log.debug(&#8216;rest_sample proxy init() called&#8230;&#8217;)<br />
#Save the REST URL<br />
    DETAILS[&#8216;url&#8217;] = opts[&#8216;proxy&#8217;][&#8216;url&#8217;]<br />
#Make sure the REST URL ends with a &#8216;/&#8217;<br />
    if not DETAILS[&#8216;url&#8217;].endswith(&#8216;/&#8217;):<br />
        DETAILS[&#8216;url&#8217;] += &#8216;/&#8217;<br />
def id(opts):<br />
    &#8221;&#8217;<br />
    Return a unique ID for this proxy minion.  This ID MUST NOT CHANGE.<br />
    If it changes while the proxy is running the salt-master will get<br />
    really confused and may stop talking to this minion<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(opts[&#8216;proxy&#8217;][&#8216;url&#8217;]+&#8217;id&#8217;, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;][&#8216;id&#8217;].encode(&#8216;ascii&#8217;, &#8216;ignore&#8217;)<br />
def grains():<br />
    &#8221;&#8217;<br />
    Get the grains from the proxied device<br />
    &#8221;&#8217;<br />
    if not GRAINS_CACHE:<br />
        r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;info&#8217;, decode_type=&#8217;json&#8217;, decode=True)<br />
        GRAINS_CACHE = r[&#8216;dict&#8217;]<br />
    return GRAINS_CACHE<br />
def grains_refresh():<br />
    &#8221;&#8217;<br />
    Refresh the grains from the proxied device<br />
    &#8221;&#8217;<br />
    GRAINS_CACHE = {}<br />
    return grains()<br />
def service_start(name):<br />
    &#8221;&#8217;<br />
    Start a &#8220;service&#8221; on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;service/start/&#8217;+name, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def service_stop(name):<br />
    &#8221;&#8217;<br />
    Stop a &#8220;service&#8221; on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;service/stop/&#8217;+name, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def service_restart(name):<br />
    &#8221;&#8217;<br />
    Restart a &#8220;service&#8221; on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;service/restart/&#8217;+name, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def service_list():<br />
    &#8221;&#8217;<br />
    List &#8220;services&#8221; on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;service/list&#8217;, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def service_status(name):<br />
    &#8221;&#8217;<br />
    Check if a service is running on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;service/status/&#8217;+name, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def package_list():<br />
    &#8221;&#8217;<br />
    List &#8220;packages&#8221; installed on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;package/list&#8217;, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def package_install(name, **kwargs):<br />
    &#8221;&#8217;<br />
    Install a &#8220;package&#8221; on the REST server<br />
    &#8221;&#8217;<br />
    cmd = DETAILS[&#8216;url&#8217;]+&#8217;package/install/&#8217;+name<br />
    if &#8216;version&#8217; in kwargs:<br />
        cmd += &#8216;/&#8217;+kwargs[&#8216;version&#8217;]<br />
    else:<br />
        cmd += &#8216;/1.0&#8242;<br />
    r = salt.utils.http.query(cmd, decode_type=&#8217;json&#8217;, decode=True)<br />
def package_remove(name):<br />
    &#8221;&#8217;<br />
    Remove a &#8220;package&#8221; on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;package/remove/&#8217;+name, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def package_status(name):<br />
    &#8221;&#8217;<br />
    Check the installation status of a package on the REST server<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;package/status/&#8217;+name, decode_type=&#8217;json&#8217;, decode=True)<br />
    return r[&#8216;dict&#8217;]<br />
def ping():<br />
    &#8221;&#8217;<br />
    Is the REST server up?<br />
    &#8221;&#8217;<br />
    r = salt.utils.http.query(DETAILS[&#8216;url&#8217;]+&#8217;ping&#8217;, decode_type=&#8217;json&#8217;, decode=True)<br />
try:<br />
return r[&#8216;dict&#8217;].get(&#8216;ret&#8217;, False)<br />
           except Exception : return False<br />
                                  def<br />
                                  shutdown(opts)<br />
    :<br />
    &#8221;&#8217; For this proxy shutdown is a no &#8211;<br />
       op<br />
    &#8221;&#8217; log.debug(&#8216;rest_sample proxy shutdown() called&#8230;&#8217;)<br />
           pass</p>
<p> Grains are data about minions. Most proxied devices will have a paltry amount of data as compared to a typical Linux server. By default, a proxy minion will have no grains set at all. Salt core code requires values for <code>kernel</code>, <code>os</code>, and <code>os_family</code>. To add them (and others) to your proxy minion for a particular device, create a file in salt/grains named [proxytype].py and place inside it the different functions that need to be run to collect the data you are interested in. Here&#8217;s an example:</p>
<h3>The __proxyenabled__ directive</h3>
<p> Salt execution moduless, by, and large, cannot &quot;automatically&quot; work with proxied devices. Execution modules like <code>pkg</code> or <code>sqlite3</code> have no meaning on a network switch or a housecat. For an execution module to be available to a proxy-minion, the <code>__proxyenabled__</code> variable must be defined in the module as an array containing the names of all the proxytypes that this module can support. The array can contain the special value <code>*</code> to indicate that the module supports all proxies. </p>
<p> If no <code>__proxyenabled__</code> variable is defined, then by default, the execution module is unavailable to any proxy. </p>
<p> Here is an excerpt from a module that was modified to support proxy-minions: </p>
<p>__proxyenabled__ = [&#8216;*&#8217;]<br />
                       [&#8230;] def<br />
                       ping()<br />
    : if &#8216;proxymodule&#8217; in __opts__ : if &#8216;ping&#8217; in __opts__[&#8216;proxyobject&#8217;].__attr__()<br />
    : return __opts[&#8216;proxyobject&#8217;].ping() else : return False else : return True</p>
<p> And then in salt.proxy.rest_sample.py we find </p>
<p>def ping()<br />
    :<br />
    &#8221;&#8217; Is the REST server up ?<br />
    &#8221;&#8217; r = salt.utils.http.query(DETAILS[&#8216;url&#8217;] + &#8216;ping&#8217;, decode_type = &#8216;json&#8217;, decode = True)<br />
try:<br />
return r[&#8216;dict&#8217;].get(&#8216;ret&#8217;, False)<br />
    except Exception : return False</p>
<h2 id="THE RAET TRANSPORT"></h2>
<p> <code>NOTE:</code> The RAET transport is in very early development, it is functional but no promises are yet made as to its reliability or security. As for reliability and security, the encryption used has been audited and our tests show that raet is reliable. With this said we are still conducting more security audits and pushing the reliability. This document outlines the encryption used in RAET </p>
<p> New in version 2014.7.0. </p>
<p> The Reliable Asynchronous Event Transport, or RAET, is an alternative transport medium developed specifically with Salt in mind. It has been developed to allow queuing to happen up on the application layer and comes with socket layer encryption. It also abstracts a great deal of control over the socket layer and makes it easy to bubble up errors and exceptions. </p>
<p> RAET also offers very powerful message routing capabilities, allowing for messages to be routed between processes on a single machine all the way up to processes on multiple machines. Messages can also be restricted, allowing processes to be sent messages of specific types from specific sources allowing for trust to be established.</p>
<h3>Using RAET in Salt</h3>
<p> Using RAET in Salt is easy, the main difference is that the core dependencies change, instead of needing pycrypto, M2Crypto, ZeroMQ, and PYZMQ, the packages libsodium, libnacl, ioflo, and raet are required. Encryption is handled very cleanly by libnacl, while the queueing and flow control is handled by ioflo. Distribution packages are forthcoming, but libsodium can be easily installed from source, or many distributions do ship packages for it. The libnacl and ioflo packages can be easily installed from pypi, distribution packages are in the works. </p>
<p> Once the new deps are installed the 2014.7 release or higher of Salt needs to be installed. </p>
<p> Once installed, modify the configuration files for the minion and master to set the transport to raet: </p>
<p> <code>/etc/salt/master</code>: </p>
<pre>
transport: raet
</pre>
<p> <code>/etc/salt/minion</code>: </p>
<pre>
transport: raet
</pre>
<p> Now start salt as it would normally be started, the minion will connect to the master and share long term keys, which can then in turn be managed via salt-key. Remote execution and salt states will function in the same way as with Salt over ZeroMQ.</p>
<h3>Limitations</h3>
<p> The 2014.7 release of RAET is not complete! The Syndic and Multi Master have not been completed yet and these are slated for completion in the 2015.5.0 release. </p>
<p> Also, Salt-Raet allows for more control over the client but these hooks have not been implemented yet, thereforre the client still uses the same system as the ZeroMQ client. This means that the extra reliability that RAET exposes has not yet been implemented in the CLI client.</p>
<h3>Why?</h3>
<h3>Customer and User Request</h3>
<p> Why make an alternative transport for Salt? There are many reasons, but the primary motivation came from customer requests, many large companies came with requests to run Salt over an alternative transport, the reasoning was varied, from performance and scaling improvements to licensing concerns. These customers have partnered with SaltStack to make RAET a reality.</p>
<h3>More Capabilities</h3>
<p> RAET has been designed to allow salt to have greater communication capabilities. It has been designed to allow for development into features which out ZeroMQ topologies can&#8217;t match. </p>
<p> Many of the proposed features are still under development and will be announced as they enter proof of concept phases, but these features include <i>salt-fuse</i> &#8211; a filesystem over salt, <i>salt-vt</i> &#8211; a parallel api driven shell over the salt transport and many others.</p>
<h3>RAET Reliability</h3>
<p> RAET is reliable, hence the name (Reliable Asynchronous Event Transport). </p>
<p> The concern posed by some over RAET reliability is based on the fact that RAET uses UDP instead of TCP and UDP does not have built in reliability. </p>
<p> RAET itself implements the needed reliability layers that are not natively present in UDP, this allows RAET to dynamically optimize packet delivery in a way that keeps it both reliable and asynchronous.</p>
<h3>RAET and ZeroMQ</h3>
<p> When using RAET, ZeroMQ is not required. RAET is a complete networking replacement. It is noteworthy that RAET is not a ZeroMQ replacement in a general sense, the ZeroMQ constructs are not reproduced in RAET, but they are instead implemented in such a way that is specific to Salt&#8217;s needs. </p>
<p> RAET is primarily an async communication layer over truly async connections, defaulting to UDP. ZeroMQ is over TCP and abstracts async constructs within the socket layer. </p>
<p> Salt is not dropping ZeroMQ support and has no immediate plans to do so.</p>
<h3>Encryption</h3>
<p> RAET uses Dan Bernstein&#8217;s NACL encryption libraries and CurveCP handshake. The libnacl python binding binds to both libsodium and tweetnacl to execute the underlying cryptography. This allows us to completely rely on an externally developed cryptography system. </p>
<p> For more information on libsodium and CurveCP please see: <i><a rel="nofollow noopener" href="http://doc.libsodium.org/" target="_blank">http://doc.libsodium.org/</a></i> <i><a rel="nofollow noopener" href="http://curvecp.org/" target="_blank">http://curvecp.org/</a></i></p>
<h3>Programming Intro</h3>
<p> Raet Programming Introduction</p>
<h2 id="WINDOWS SOFTWARE REPOSITORY"></h2>
<p> The Salt Windows Software Repository provides a package manager and software repository similar to what is provided by yum and apt on Linux. </p>
<p> It permits the installation of software using the installers on remote windows machines. In many senses, the operation is similar to that of the other package managers salt is aware of:</p>
<dl>
<dt>&bull;</p>
<dd> the <code>pkg.installed</code> and similar states work on Windows.</p>
<dt>&bull;</p>
<dd> the <code>pkg.install</code> and similar module functions work on Windows.</p>
<dt>&bull;</p>
<dd> each windows machine needs to have <code>pkg.refresh_db</code> executed against it to pick up the latest version of the package database. </p>
<p> High level differences to yum and apt are:</p>
<dt>&bull;</p>
<dd> The repository metadata (sls files) is hosted through either salt or git.</p>
<dt>&bull;</p>
<dd> Packages can be downloaded from within the salt repository, a git repository or from http(s) or ftp urls.</p>
<dt>&bull;</p>
<dd> No dependencies are managed. Dependencies between packages needs to be managed manually.</dl>
<h3>Operation</h3>
<p> The install state/module function of the windows package manager works roughly as follows:</p>
<dl>
<dt>1.</p>
<dd> Execute <code>pkg.list_pkgs</code> and store the result</p>
<dt>2.</p>
<dd> Check if any action needs to be taken. (i.e. compare required package and version against <code>pkg.list_pkgs</code> results)</p>
<dt>3.</p>
<dd> If so, run the installer command.</p>
<dt>4.</p>
<dd> Execute <code>pkg.list_pkgs</code> and compare to the result stored from before installation.</p>
<dt>5.</p>
<dd> Success/Failure/Changes will be reported based on the differences between the original and final <code>pkg.list_pkgs</code> results. </p>
<p> If there are any problems in using the package manager it is likely to be due to the data in your sls files not matching the difference between the pre and post <code>pkg.list_pkgs</code> results.</dl>
<h3>Usage</h3>
<p> By default, the Windows software repository is found at <code>/srv/salt/win/repo</code> This can be changed in the master config file (default location is <code>/etc/salt/master</code>) by modifying the <code>win_repo</code> variable. Each piece of software should have its own directory which contains the installers and a package definition file. This package definition file is a YAML file named <code>init.sls</code>. </p>
<p> The package definition file should look similar to this example for Firefox: <code>/srv/salt/win/repo/firefox/init.sls</code> </p>
<pre>
Firefox:
  '17.0.1':
    installer: '<a href="salt://win/repo/firefox/English/Firefox" rel="nofollow">salt://win/repo/firefox/English/Firefox</a> Setup 17.0.1.exe'
    full_name: Mozilla Firefox 17.0.1 (x86 en-US)
    locale: en_US
    reboot: False
    install_flags: '-ms'
    uninstaller: '%ProgramFiles(x86)%/Mozilla Firefox/uninstall/helper.exe'
    uninstall_flags: '/S'
  '16.0.2':
    installer: '<a href="salt://win/repo/firefox/English/Firefox" rel="nofollow">salt://win/repo/firefox/English/Firefox</a> Setup 16.0.2.exe'
    full_name: Mozilla Firefox 16.0.2 (x86 en-US)
    locale: en_US
    reboot: False
    install_flags: '-ms'
    uninstaller: '%ProgramFiles(x86)%/Mozilla Firefox/uninstall/helper.exe'
    uninstall_flags: '/S'
  '15.0.1':
    installer: '<a href="salt://win/repo/firefox/English/Firefox" rel="nofollow">salt://win/repo/firefox/English/Firefox</a> Setup 15.0.1.exe'
    full_name: Mozilla Firefox 15.0.1 (x86 en-US)
    locale: en_US
    reboot: False
    install_flags: '-ms'
    uninstaller: '%ProgramFiles(x86)%/Mozilla Firefox/uninstall/helper.exe'
    uninstall_flags: '/S'
</pre>
<p> More examples can be found here: <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-winrepo" target="_blank">https://github.com/saltstack/salt-winrepo</a></i> </p>
<p> The version number and <code>full_name</code> need to match the output from <code>pkg.list_pkgs</code> so that the status can be verified when running highstate. Note: It is still possible to successfully install packages using <code>pkg.install</code> even if they don&#8217;t match which can make this hard to troubleshoot. </p>
<p>salt &#8216;test-2008&#8217; pkg.list_pkgs<br />
        test &#8211;<br />
    2008 &#8212; &#8212; &#8212; &#8212; &#8211;7 &#8211; Zip 9.20(x64 edition) : 9.20.00.0 Microsoft.NET Framework 4 Client Profile : 4.0.30319,<br />
    4.0.30319 Microsoft.NET Framework 4 Extended : 4.0.30319, 4.0.30319 Microsoft Visual C++ 2008 Redistributable &#8211; x64 9.0.21022 : 9.0.21022 Mozilla Firefox 17.0.1(x86 en &#8211; US) : 17.0.1 Mozilla Maintenance Service : 17.0.1 NSClient++(x64) : 0.3.8.76 Notepad++ : 6.4.2 Salt Minion 0.16.0 : 0.16.0</p>
<p> If any of these preinstalled packages already exist in winrepo the full_name will be automatically renamed to their package name during the next update (running highstate or installing another package). </p>
<p>test &#8211; 2008 : &#8212; &#8212; &#8212; &#8212; &#8211;7zip : 9.20.00.0 Microsoft.NET Framework 4 Client Profile : 4.0.30319, 4.0.30319 Microsoft.NET Framework 4 Extended : 4.0.30319, 4.0.30319 Microsoft Visual C++ 2008 Redistributable &#8211; x64 9.0.21022 : 9.0.21022 Mozilla Maintenance Service : 17.0.1 Notepad++ : 6.4.2 Salt Minion 0.16.0 : 0.16.0 firefox : 17.0.1 nsclient : 0.3.9.328</p>
<p> Add <code>msiexec: True</code> if using an MSI installer requiring the use of <code>msiexec /i</code> to install and <code>msiexec /x</code> to uninstall. </p>
<p> The <code>install_flags</code> and <code>uninstall_flags</code> are flags passed to the software installer to cause it to perform a silent install. These can often be found by adding <code>/?</code> or <code>/h</code> when running the installer from the command line. A great resource for finding these silent install flags can be found on the WPKG project&#8217;s <i>wiki</i>: </p>
<pre>
7zip:
  9.20.00.0:
    installer: <a href="salt://win/repo/7zip/7z920-x64.msi" rel="nofollow">salt://win/repo/7zip/7z920-x64.msi</a>
    full_name: 7-Zip 9.20 (x64 edition)
    reboot: False
    install_flags: '/qn /norestart'
    msiexec: True
    uninstaller: '{23170F69-40C1-2702-0920-000001000000}'
    uninstall_flags: '/qn /norestart'
</pre>
<p> Alternatively the <code>uninstaller</code> can also simply repeat the URL of the msi file. </p>
<pre>
7zip:
  9.20.00.0:
    installer: <a href="salt://win/repo/7zip/7z920-x64.msi" rel="nofollow">salt://win/repo/7zip/7z920-x64.msi</a>
    full_name: 7-Zip 9.20 (x64 edition)
    reboot: False
    install_flags: '/qn /norestart'
    msiexec: True
    uninstaller: <a href="salt://win/repo/7zip/7z920-x64.msi" rel="nofollow">salt://win/repo/7zip/7z920-x64.msi</a>
    uninstall_flags: '/qn /norestart'
</pre>
<h3>Generate Repo Cache File</h3>
<p> Once the sls file has been created, generate the repository cache file with the winrepo runner: </p>
<pre>
salt-run winrepo.genrepo
</pre>
<p> Then update the repository cache file on your minions, exactly how it&#8217;s done for the Linux package managers: </p>
<pre>
salt '*' pkg.refresh_db
</pre>
<h3>Install Windows Software</h3>
<p> Now you can query the available version of Firefox using the Salt pkg module. </p>
<p>salt &#8216;*&#8217; pkg.available_version Firefox<br />
{<br />
    &#8216;Firefox&#8217;:<br />
    {<br />
        &#8216;15.0.1&#8217; : &#8216;Mozilla Firefox 15.0.1 (x86 en-US)&#8217;,<br />
                   &#8216;16.0.2&#8217; : &#8216;Mozilla Firefox 16.0.2 (x86 en-US)&#8217;,<br />
                              &#8216;17.0.1&#8217; : &#8216;Mozilla Firefox 17.0.1 (x86 en-US)&#8217;<br />
    }<br />
}</p>
<p> As you can see, there are three versions of Firefox available for installation. You can refer a software package by its <code>name</code> or its <code>full_name</code> surround by single quotes. </p>
<pre>
salt '*' pkg.install 'Firefox'
</pre>
<p> The above line will install the latest version of Firefox. </p>
<pre>
salt '*' pkg.install 'Firefox' version=16.0.2
</pre>
<p> The above line will install version 16.0.2 of Firefox. </p>
<p> If a different version of the package is already installed it will be replaced with the version in winrepo (only if the package itself supports live updating). </p>
<p> You can also specify the full name: </p>
<pre>
salt '*' pkg.install 'Mozilla Firefox 17.0.1 (x86 en-US)'
</pre>
<h3>Uninstall Windows Software</h3>
<p> Uninstall software using the pkg module: </p>
<pre>
salt '*' pkg.remove 'Firefox'
salt '*' pkg.purge 'Firefox'
</pre>
<p> <code>pkg.purge</code> just executes <code>pkg.remove</code> on Windows. At some point in the future <code>pkg.purge</code> may direct the installer to remove all configs and settings for software packages that support that option.</p>
<h3>Standalone Minion Salt Windows Repo Module</h3>
<p> In order to facilitate managing a Salt Windows software repo with Salt on a Standalone Minion on Windows, a new module named winrepo has been added to Salt. winrepo matches what is available in the salt runner and allows you to manage the Windows software repo contents. Example: <code>salt &#8216;*&#8217; winrepo.genrepo</code></p>
<h3>Git Hosted Repo</h3>
<p> Windows software package definitions can also be hosted in one or more git repositories. The default repo is one hosted on Github.com by SaltStack,Inc., which includes package definitions for open source software. This repo points to the HTTP or ftp locations of the installer files. Anyone is welcome to send a pull request to this repo to add new package definitions. Browse the repo here: <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-winrepo" target="_blank">https://github.com/saltstack/salt-winrepo</a></i> . </p>
<p> Configure which git repos the master can search for package definitions by modifying or extending the <code>win_gitrepos</code> configuration option list in the master config. </p>
<p> Checkout each git repo in <code>win_gitrepos</code>, compile your package repository cache and then refresh each minion&#8217;s package cache: </p>
<pre>
salt-run winrepo.update_git_repos
salt-run winrepo.genrepo
salt '*' pkg.refresh_db
</pre>
<h3>Troubleshooting</h3>
<h3>Incorrect name/version</h3>
<p> If the package seems to install properly, but salt reports a failure then it is likely you have a version or <code>full_name</code> mismatch. </p>
<p> Check the exact <code>full_name</code> and version used by the package. Use <code>pkg.list_pkgs</code> to check that the names and version exactly match what is installed.</p>
<h3>Changes to sls files not being picked up</h3>
<p> Ensure you have (re)generated the repository cache file and then updated the repository cache on the relevant minions: </p>
<pre>
salt-run winrepo.genrepo
salt 'MINION' pkg.refresh_db
</pre>
<h3>Packages management under Windows 2003</h3>
<p> On windows server 2003, you need to install optional windows component &quot;wmi windows installer provider&quot; to have full list of installed packages. If you don&#8217;t have this, salt-minion can&#8217;t report some installed software.</p>
<h2 id="WINDOWS-SPECIFIC BEHAVIOUR"></h2>
<p> Salt is capable of managing Windows systems, however due to various differences between the operating systems, there are some things you need to keep in mind. </p>
<p> This document will contain any quirks that apply across Salt or generally across multiple module functions. Any Windows-specific behavior for particular module functions will be documented in the module function documentation. Therefore this document should be read in conjunction with the module function documentation.</p>
<h3>Group parameter for files</h3>
<p> Salt was originally written for managing Unix-based systems, and therefore the file module functions were designed around that security model. Rather than trying to shoehorn that model on to Windows, Salt ignores these parameters and makes non-applicable module functions unavailable instead. </p>
<p> One of the commonly ignored parameters is the <code>group</code> parameter for managing files. Under Windows, while files do have a &#8216;primary group&#8217; property, this is rarely used. It generally has no bearing on permissions unless intentionally configured and is most commonly used to provide Unix compatibility (e.g. Services For Unix, NFS services). </p>
<p> Because of this, any file module functions that typically require a group, do not under Windows. Attempts to directly use file module functions that operate on the group (e.g. <code>file.chgrp</code>) will return a pseudo-value and cause a log message to appear. No group parameters will be acted on. </p>
<p> If you do want to access and change the &#8216;primary group&#8217; property and understand the implications, use the <code>file.get_pgid</code> or <code>file.get_pgroup</code> functions or the <code>pgroup</code> parameter on the <code>file.chown</code> module function.</p>
<h3>Dealing with case-insensitive but case-preserving names</h3>
<p> Windows is case-insensitive, but however preserves the case of names and it is this preserved form that is returned from system functions. This causes some issues with Salt because it assumes case-sensitive names. These issues generally occur in the state functions and can cause bizarre looking errors. </p>
<p> To avoid such issues, always pretend Windows is case-sensitive and use the right case for names, e.g. specify <code>user=Administrator</code> instead of <code>user=administrator</code>. </p>
<p> Follow <i>issue 11801</i> for any changes to this behavior.</p>
<h3>Dealing with various username forms</h3>
<p> Salt does not understand the various forms that Windows usernames can come in, e.g. username, mydomain\username, <i>username [at] mydomain.tld</i> can all refer to the same user. In fact, Salt generally only considers the raw username value, i.e. the username without the domain or host information. </p>
<p> Using these alternative forms will likely confuse Salt and cause odd errors to happen. Use only the raw username value in the correct case to avoid problems. </p>
<p> Follow <i>issue 11801</i> for any changes to this behavior.</p>
<h3>Specifying the None group</h3>
<p> Each Windows system has built-in _None_ group. This is the default &#8216;primary group&#8217; for files for users not on a domain environment. </p>
<p> Unfortunately, the word _None_ has special meaning in Python &#8211; it is a special value indicating &#8216;nothing&#8217;, similar to <code>null</code> or <code>nil</code> in other languages. </p>
<p> To specify the None group, it must be specified in quotes, e.g. <code>./salt &#8216;*&#8217; file.chpgrp C:\path\to\file &quot;&#8217;None&#8217;&quot;</code>.</p>
<h3>Symbolic link loops</h3>
<p> Under Windows, if any symbolic link loops are detected or if there are too many levels of symlinks (defaults to 64), an error is always raised. </p>
<p> For some functions, this behavior is different to the behavior on Unix platforms. In general, avoid symlink loops on either platform.</p>
<h3>Modifying security properties (ACLs) on files</h3>
<p> There is no support in Salt for modifying ACLs, and therefore no support for changing file permissions, besides modifying the owner/user.</p>
<h2 id="SALT CLOUD"></h2>
<h3>Getting Started</h3>
<p> Salt Cloud is built-in to Salt and is configured on and executed from your Salt Master.</p>
<h3>Define a Profile</h3>
<p> The first step is to add the credentials for your cloud provider. Credentials and provider settings are stored in provider configuration files. Provider configurations contain the details needed to connect, and any global options that you want set on your cloud minions (such as the location of your Salt Master). </p>
<p> On your Salt Master, browse to <code>/etc/salt/cloud.providers.d/</code> and create a file called <code>&lt;provider&gt;.provider.conf</code>, replacing <code>&lt;provider&gt;</code> with <code>ec2</code>, <code>softlayer</code>, and so on. The name helps you identify the contents, and is not important as long as the file ends in <code>.conf</code>. </p>
<p> Next, browse to the <i>Provider specifics</i> and add any required settings for your provider to this file. Here is an example for Amazon EC2: </p>
<pre>
my-ec2:
  provider: ec2
  # Set the EC2 access credentials (see below)
  #
  id: 'HJGRYCILJLKJYG'
  key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
  # Make sure this key is owned by root with permissions 0400.
  #
  private_key: /etc/salt/my_test_key.pem
  keyname: my_test_key
  securitygroup: default
  # Optional: Set up the location of the Salt Master
  #
  minion:
    master: saltmaster.example.com
</pre>
<p> The required configuration varies between providers so make sure you read the provider specifics.</p>
<h3>List Cloud Provider Options</h3>
<p> You can now query the cloud provider you configured for available locations, images, and sizes. This information is used when you set up VM profiles. </p>
<pre>
salt-cloud --list-locations &lt;provider_name&gt;  # my-ec2 in the previous example
salt-cloud --list-images &lt;provider_name&gt;
salt-cloud --list-sizes &lt;provider_name&gt;
</pre>
<p> Replace <code>&lt;provider_name&gt;</code> with the name of the provider configuration you defined.</p>
<h3>Create VM Profiles</h3>
<p> On your Salt Master, browse to <code>/etc/salt/cloud.profiles.d/</code> and create a file called <code>&lt;provider&gt;.profiles.conf</code>, replacing <code>&lt;provider&gt;</code> with <code>ec2</code>, <code>softlayer</code>, and so on. The file must end in <code>.conf</code>. </p>
<p> You can now add any custom profiles you&#8217;d like to define to this file. Here are a few examples: </p>
<pre>
micro_ec2:
  provider: my-ec2
  image: ami-d514f291
  size: t1.micro
medium_ec2:
  provider: my-ec2
  image: ami-d514f291
  size: m3.medium
large_ec2:
  provider: my-ec2
  image: ami-d514f291
  size: m3.large
</pre>
<p> Notice that the <code>provider</code> in our profile matches the provider name that we defined? That is how Salt Cloud knows how to connect to create a VM with these attributes.</p>
<h3>Create VMs</h3>
<p> VMs are created by calling <code>salt-cloud</code> with the following options: </p>
<pre>
salt-cloud -p &lt;profile&gt; &lt;name1&gt; &lt;name2&gt; ...
</pre>
<p> For example: </p>
<pre>
salt-cloud -p micro_ec2 minion1 minion2
</pre>
<h3>Destroy VMs</h3>
<p> Add a <code>-d</code> and the minion name you provided to destroy: </p>
<pre>
salt-cloud -d minion1 minion2
</pre>
<h3>Query VMs</h3>
<p> You can view details about the VMs you&#8217;ve created using <code>&#8211;query</code>: </p>
<pre>
salt-cloud --query
</pre>
<h3>Using Salt Cloud</h3>
<h3><code>salt-cloud</code></h3>
<p> Provision virtual machines in the cloud with Salt</p>
<h3>Synopsis</h3>
<pre>
salt-cloud -m /etc/salt/cloud.map
salt-cloud -m /etc/salt/cloud.map NAME
salt-cloud -m /etc/salt/cloud.map NAME1 NAME2
salt-cloud -p PROFILE NAME
salt-cloud -p PROFILE NAME1 NAME2 NAME3 NAME4 NAME5 NAME6
</pre>
<h3>Description</h3>
<p> Salt Cloud is the system used to provision virtual machines on various public clouds via a cleanly controlled profile and mapping system.</p>
<h3>Options</h3>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version of Salt that is running.</p>
<dt><code>&#8211;versions-report</code></p>
<dd> Show program&#8217;s dependencies and version number, and then exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></p>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</dl>
<h3>Execution Options</h3>
<dl>
<dt><code>-L LOCATION, &#8211;location=LOCATION</code></p>
<dd> Specify which region to connect to.</p>
<dt><code>-a ACTION, &#8211;action=ACTION</code></p>
<dd> Perform an action that may be specific to this cloud provider. This argument requires one or more instance names to be specified.</p>
<dt><code>-f &lt;FUNC-NAME&gt; &lt;PROVIDER&gt;, &#8211;function=&lt;FUNC-NAME&gt; &lt;PROVIDER&gt;</code></p>
<dd> Perform an function that may be specific to this cloud provider, that does not apply to an instance. This argument requires a provider to be specified (i.e.: nova).</p>
<dt><code>-p PROFILE, &#8211;profile=PROFILE</code></p>
<dd> Select a single profile to build the named cloud VMs from. The profile must be defined in the specified profiles file.</p>
<dt><code>-m MAP, &#8211;map=MAP</code></p>
<dd> Specify a map file to use. If used without any other options, this option will ensure that all of the mapped VMs are created. If the named VM already exists then it will be skipped.</p>
<dt><code>-H, &#8211;hard</code></p>
<dd> When specifying a map file, the default behavior is to ensure that all of the VMs specified in the map file are created. If the &#8211;hard option is set, then any VMs that exist on configured cloud providers that are not specified in the map file will be destroyed. Be advised that this can be a destructive operation and should be used with care.</p>
<dt><code>-d, &#8211;destroy</code></p>
<dd> Pass in the name(s) of VMs to destroy, salt-cloud will search the configured cloud providers for the specified names and destroy the VMs. Be advised that this is a destructive operation and should be used with care. Can be used in conjunction with the -m option to specify a map of VMs to be deleted.</p>
<dt><code>-P, &#8211;parallel</code></p>
<dd> Normally when building many cloud VMs they are executed serially. The -P option will run each cloud vm build in a separate process allowing for large groups of VMs to be build at once. </p>
<p> Be advised that some cloud provider&#8217;s systems don&#8217;t seem to be well suited for this influx of vm creation. When creating large groups of VMs watch the cloud provider carefully.</p>
<dt><code>-u, &#8211;update-bootstrap</code></p>
<dd> Update salt-bootstrap to the latest develop version on GitHub.</p>
<dt><code>-y, &#8211;assume-yes</code></p>
<dd> Default yes in answer to all confirmation questions.</p>
<dt><code>-k, &#8211;keep-tmp</code></p>
<dd> Do not remove files from /tmp/ after deploy.sh finishes.</p>
<dt><code>&#8211;show-deploy-args</code></p>
<dd> Include the options used to deploy the minion in the data returned.</p>
<dt><code>&#8211;script-args=SCRIPT_ARGS</code></p>
<dd> Script arguments to be fed to the bootstrap script when deploying the VM.</dl>
<h3>Query Options</h3>
<dl>
<dt><code>-Q, &#8211;query</code></p>
<dd> Execute a query and return some information about the nodes running on configured cloud providers</p>
<dt><code>-F, &#8211;full-query</code></p>
<dd> Execute a query and print out all available information about all cloud VMs. Can be used in conjunction with -m to display only information about the specified map.</p>
<dt><code>-S, &#8211;select-query</code></p>
<dd> Execute a query and print out selected information about all cloud VMs. Can be used in conjunction with -m to display only information about the specified map.</p>
<dt><code>&#8211;list-providers</code></p>
<dd> Display a list of configured providers.</p>
<dt><code>&#8211;list-profiles</code></p>
<dd> New in version 2014.7.0. </p>
<p> Display a list of configured profiles. Pass in a cloud provider to view the provider&#8217;s associated profiles, such as <code>digital_ocean</code>, or pass in <code>all</code> to list all the configured profiles.</dl>
<h3>Cloud Providers Listings</h3>
<dl>
<dt><code>&#8211;list-locations=LIST_LOCATIONS</code></p>
<dd> Display a list of locations available in configured cloud providers. Pass the cloud provider that available locations are desired on, aka &quot;linode&quot;, or pass &quot;all&quot; to list locations for all configured cloud providers</p>
<dt><code>&#8211;list-images=LIST_IMAGES</code></p>
<dd> Display a list of images available in configured cloud providers. Pass the cloud provider that available images are desired on, aka &quot;linode&quot;, or pass &quot;all&quot; to list images for all configured cloud providers</p>
<dt><code>&#8211;list-sizes=LIST_SIZES</code></p>
<dd> Display a list of sizes available in configured cloud providers. Pass the cloud provider that available sizes are desired on, aka &quot;AWS&quot;, or pass &quot;all&quot; to list sizes for all configured cloud providers</dl>
<h3>Cloud Credentials</h3>
<dl>
<dt><code>&#8211;set-password=&lt;USERNAME&gt; &lt;PROVIDER&gt;</code></p>
<dd> Configure password for a cloud provider and save it to the keyring. PROVIDER can be specified with or without a driver, for example: &quot;&#8211;set-password bob rackspace&quot; or more specific &quot;&#8211;set-password bob rackspace:openstack&quot; DEPRECATED!</dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;out</code></p>
<dd> Pass in an alternative outputter to display the return of data. This outputter can be any of the available outputters: <code>grains</code>, <code>highstate</code>, <code>json</code>, <code>key</code>, <code>overstatestage</code>, <code>pprint</code>, <code>raw</code>, <code>txt</code>, <code>yaml</code> </p>
<p> Some outputters are formatted only for data returned from specific functions; for instance, the <code>grains</code> outputter will not work for non-grains data. </p>
<p> If an outputter is used that does not support the data passed into it, then Salt will fall back on the <code>pprint</code> outputter and display the return data using the Python <code>pprint</code> standard library module. </p>
<p> <code>NOTE:</code> If using <code>&#8211;out=json</code>, you will probably want <code>&#8211;static</code> as well. Without the static option, you will get a separate JSON string per minion which makes JSON output invalid as a whole. This is due to using an iterative outputter. So if you want to feed it to a JSON parser, use <code>&#8211;static</code> as well.</p>
<dt><code>&#8211;out-indent OUTPUT_INDENT, &#8211;output-indent OUTPUT_INDENT</code></p>
<dd> Print the output indented by the provided value in spaces. Negative values disable indentation. Only applicable in outputters that support indentation.</p>
<dt><code>&#8211;out-file=OUTPUT_FILE, &#8211;output-file=OUTPUT_FILE</code></p>
<dd> Write the output to the specified file.</p>
<dt><code>&#8211;no-color</code></p>
<dd> Disable all colored output</p>
<dt><code>&#8211;force-color</code></p>
<dd> Force colored output </p>
<p> <code>NOTE:</code> When using colored output the color codes are as follows: </p>
<p> <code>green</code> denotes success, <code>red</code> denotes failure, <code>blue</code> denotes changes and success and <code>yellow</code> denotes a expected future change in configuration.</dl>
<h3>Examples</h3>
<p> To create 4 VMs named web1, web2, db1, and db2 from specified profiles: </p>
<pre>
salt-cloud -p fedora_rackspace web1 web2 db1 db2
</pre>
<p> To read in a map file and create all VMs specified therein: </p>
<pre>
salt-cloud -m /path/to/cloud.map
</pre>
<p> To read in a map file and create all VMs specified therein in parallel: </p>
<pre>
salt-cloud -m /path/to/cloud.map -P
</pre>
<p> To delete any VMs specified in the map file: </p>
<pre>
salt-cloud -m /path/to/cloud.map -d
</pre>
<p> To delete any VMs NOT specified in the map file: </p>
<pre>
salt-cloud -m /path/to/cloud.map -H
</pre>
<p> To display the status of all VMs specified in the map file: </p>
<pre>
salt-cloud -m /path/to/cloud.map -Q
</pre>
<h3>See also</h3>
<p> <i><a href="/docs/linux/man/7-salt-cloud/">salt-cloud</a>(7)</i> <i><a href="/docs/linux/man/7-salt/">salt</a>(7)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h3>Salt Cloud basic usage</h3>
<p> Salt Cloud needs, at least, one configured Provider and <code>Profile</code> to be functional.</p>
<h3>Creating a VM</h3>
<p> To create a VM with salt cloud, use command: </p>
<pre>
salt-cloud -p &lt;profile&gt; name_of_vm
</pre>
<p> Assuming there is a profile configured as following: </p>
<pre>
fedora_rackspace:
    provider: rackspace
    image: Fedora 17
    size: 256 server
    script: bootstrap-salt
</pre>
<p> Then, the command to create new VM named <code>fedora_http_01</code> is: </p>
<pre>
salt-cloud -p fedora_rackspace fedora_http_01
</pre>
<h3>Destroying a VM</h3>
<p> To destroy a created-by-salt-cloud VM, use command: </p>
<pre>
salt-cloud -d name_of_vm
</pre>
<p> For example, to delete the VM created on above example, use: </p>
<pre>
salt-cloud -d fedora_http_01
</pre>
<h3>VM Profiles</h3>
<p> Salt cloud designates virtual machines inside the profile configuration file. The profile configuration file defaults to <code>/etc/salt/cloud.profiles</code> and is a yaml configuration. The syntax for declaring profiles is simple: </p>
<pre>
fedora_rackspace:
    provider: rackspace
    image: Fedora 17
    size: 256 server
    script: bootstrap-salt
</pre>
<p> It should be noted that the <code>script</code> option defaults to <code>bootstrap-salt</code>, and does not normally need to be specified. Further examples in this document will not show the <code>script</code> option. </p>
<p> A few key pieces of information need to be declared and can change based on the public cloud provider. A number of additional parameters can also be inserted: </p>
<pre>
centos_rackspace:
    provider: rackspace
    image: CentOS 6.2
    size: 1024 server
    minion:
        master: salt.example.com
        append_domain: webs.example.com
        grains:
            role: webserver
</pre>
<p> The image must be selected from available images. Similarly, sizes must be selected from the list of sizes. To get a list of available images and sizes use the following command: </p>
<pre>
salt-cloud --list-images openstack
salt-cloud --list-sizes openstack
</pre>
<p> Some parameters can be specified in the main Salt cloud configuration file and then are applied to all cloud profiles. For instance if only a single cloud provider is being used then the provider option can be declared in the Salt cloud configuration file.</p>
<h3>Multiple Configuration Files</h3>
<p> In addition to <code>/etc/salt/cloud.profiles</code>, profiles can also be specified in any file matching <code>cloud.profiles.d/*conf</code> which is a sub-directory relative to the profiles configuration file(with the above configuration file as an example, <code>/etc/salt/cloud.profiles.d/*.conf</code>). This allows for more extensible configuration, and plays nicely with various configuration management tools as well as version control systems.</p>
<h3>Larger Example</h3>
<pre>
rhel_ec2:
    provider: ec2
    image: ami-e565ba8c
    size: t1.micro
    minion:
        cheese: edam
ubuntu_ec2:
    provider: ec2
    image: ami-7e2da54e
    size: t1.micro
    minion:
        cheese: edam
ubuntu_rackspace:
    provider: rackspace
    image: Ubuntu 12.04 LTS
    size: 256 server
    minion:
        cheese: edam
fedora_rackspace:
    provider: rackspace
    image: Fedora 17
    size: 256 server
    minion:
        cheese: edam
cent_linode:
    provider: linode
    image: CentOS 6.2 64bit
    size: Linode 512
cent_gogrid:
    provider: gogrid
    image: 12834
    size: 512MB
cent_joyent:
    provider: joyent
    image: centos-6
    size: Small 1GB
</pre>
<h3>Cloud Map File</h3>
<p> A number of options exist when creating virtual machines. They can be managed directly from profiles and the command line execution, or a more complex map file can be created. The map file allows for a number of virtual machines to be created and associated with specific profiles. </p>
<p> Map files have a simple format, specify a profile and then a list of virtual machines to make from said profile: </p>
<pre>
fedora_small:
  - web1
  - web2
  - web3
fedora_high:
  - redis1
  - redis2
  - redis3
cent_high:
  - riak1
  - riak2
  - riak3
</pre>
<p> This map file can then be called to roll out all of these virtual machines. Map files are called from the salt-cloud command with the -m option: </p>
<pre>
$ salt-cloud -m /path/to/mapfile
</pre>
<p> Remember, that as with direct profile provisioning the -P option can be passed to create the virtual machines in parallel: </p>
<pre>
$ salt-cloud -m /path/to/mapfile -P
</pre>
<p> <code>NOTE:</code> Due to limitations in the GoGrid API, instances cannot be provisioned in parallel with the GoGrid driver. Map files will work with GoGrid, but the <code>-P</code> argument should not be used on maps referencing GoGrid instances. </p>
<p> A map file can also be enforced to represent the total state of a cloud deployment by using the <code>&#8211;hard</code> option. When using the hard option any vms that exist but are not specified in the map file will be destroyed: </p>
<pre>
$ salt-cloud -m /path/to/mapfile -P -H
</pre>
<p> Be careful with this argument, it is very dangerous! In fact, it is so dangerous that in order to use it, you must explicitly enable it in the main configuration file. </p>
<pre>
enable_hard_maps: True
</pre>
<p> A map file can include grains and minion configuration options: </p>
<pre>
fedora_small:
  - web1:
      minion:
        log_level: debug
      grains:
        cheese: tasty
        omelet: du fromage
  - web2:
      minion:
        log_level: warn
      grains:
        cheese: more tasty
        omelet: with peppers
</pre>
<p> A map file may also be used with the various query options: </p>
<p>$ salt &#8211; cloud &#8211; m / path / to / mapfile &#8211; Q<br />
{<br />
    &#8216;ec2&#8217; : {&#8216;web1&#8217; : {&#8216;id&#8217; : &#8216;i-e6aqfegb&#8217;,<br />
                       &#8216;image&#8217; : None,<br />
                       &#8216;private_ips&#8217; : [],<br />
                       &#8216;public_ips&#8217; : [],<br />
                       &#8216;size&#8217; : None,<br />
                       &#8216;state&#8217; : 0}},<br />
            &#8216;web2&#8217;:<br />
    {<br />
        &#8216;Absent&#8217;<br />
    }<br />
}</p>
<p> &#8230;or with the delete option: </p>
<pre>
$ salt-cloud -m /path/to/mapfile -d
The following virtual machines are set to be destroyed:
  web1
  web2
Proceed? [N/y]
</pre>
<p> <code>WARNING:</code> Specifying Nodes with Maps on the Command Line Specifying the name of a node or nodes with the maps options on the command line is <i>not</i> supported. This is especially important to remember when using <code>&#8211;destroy</code> with maps; <code>salt-cloud</code> will ignore any arguments passed in which are not directly relevant to the map file. <i>When using &#8220;&#8211;destroy&#8220; with a map, every node in the map file will be deleted!</i> Maps don&#8217;t provide any useful information for destroying individual nodes, and should not be used to destroy a subset of a map.</p>
<h3>Setting up New Salt Masters</h3>
<p> Bootstrapping a new master in the map is as simple as: </p>
<pre>
fedora_small:
  - web1:
      make_master: True
  - web2
  - web3
</pre>
<p> Notice that <code>ALL</code> bootstrapped minions from the map will answer to the newly created salt-master. </p>
<p> To make any of the bootstrapped minions answer to the bootstrapping salt-master as opposed to the newly created salt-master, as an example: </p>
<pre>
fedora_small:
  - web1:
      make_master: True
      minion:
        master: &lt;the local master ip address&gt;
        local_master: True
  - web2
  - web3
</pre>
<p> The above says the minion running on the newly created salt-master responds to the local master, ie, the master used to bootstrap these VMs. </p>
<p> Another example: </p>
<pre>
fedora_small:
  - web1:
      make_master: True
  - web2
  - web3:
      minion:
        master: &lt;the local master ip address&gt;
        local_master: True
</pre>
<p> The above example makes the <code>web3</code> minion answer to the local master, not the newly created master.</p>
<h3>Cloud Actions</h3>
<p> Once a VM has been created, there are a number of actions that can be performed on it. The &quot;reboot&quot; action can be used across all providers, but all other actions are specific to the cloud provider. In order to perform an action, you may specify it from the command line, including the name(s) of the VM to perform the action on: </p>
<pre>
$ salt-cloud -a reboot vm_name
$ salt-cloud -a reboot vm1 vm2 vm2
</pre>
<p> Or you may specify a map which includes all VMs to perform the action on: </p>
<pre>
$ salt-cloud -a reboot -m /path/to/mapfile
</pre>
<p> The following is a list of actions currently supported by salt-cloud: </p>
<pre>
all providers:
    - reboot
ec2:
    - start
    - stop
joyent:
    - stop
</pre>
<p> Another useful reference for viewing more salt-cloud actions is the :ref:Salt Cloud Feature Matrix &lt;salt-cloud-feature-matrix&gt;</p>
<h3>Cloud Functions</h3>
<p> Cloud functions work much the same way as cloud actions, except that they don&#8217;t perform an operation on a specific instance, and so do not need a machine name to be specified. However, since they perform an operation on a specific cloud provider, that provider must be specified. </p>
<pre>
$ salt-cloud -f show_image ec2 image=ami-fd20ad94
</pre>
<p> There are three universal salt-cloud functions that are extremely useful for gathering information about instances on a provider basis:</p>
<dl>
<dt>&bull;</p>
<dd> <code>list_nodes</code>: Returns some general information about the instances for the given provider.</p>
<dt>&bull;</p>
<dd> <code>list_nodes_full</code>: Returns all information about the instances for the given provider.</p>
<dt>&bull;</p>
<dd> <code>list_nodes_select</code>: Returns select information about the instances for the given provider. </p>
<pre>
$ salt-cloud -f list_nodes linode
$ salt-cloud -f list_nodes_full linode
$ salt-cloud -f list_nodes_select linode
</pre>
<p> Another useful reference for viewing salt-cloud functions is the :ref:Salt Cloud Feature Matrix &lt;salt-cloud-feature-matrix&gt;</dl>
<h3>Core Configuration</h3>
<h3>Install Salt Cloud</h3>
<p> Salt Cloud is now part of Salt proper. It was merged in as of <code>Salt version 2014.1.0</code>. </p>
<p> On Ubuntu, install Salt Cloud by using following command: </p>
<pre>
sudo add-apt-repository ppa:saltstack/salt
sudo apt-get install salt-cloud
</pre>
<p> If using Salt Cloud on OS X, <code>curl-ca-bundle</code> must be installed. Presently, this package is not available via <code>brew</code>, but it is available using MacPorts: </p>
<pre>
sudo port install curl-ca-bundle
</pre>
<p> Salt Cloud depends on <code>apache-libcloud</code>. Libcloud can be installed via pip with <code>pip install apache-libcloud</code>.</p>
<h3>Installing Salt Cloud for development</h3>
<p> Installing Salt for development enables Salt Cloud development as well, just make sure <code>apache-libcloud</code> is installed as per above paragraph. </p>
<p> See these instructions: <code>Installing Salt for development</code>.</p>
<h3>Core Configuration</h3>
<p> A number of core configuration options and some options that are global to the VM profiles can be set in the cloud configuration file. By default this file is located at <code>/etc/salt/cloud</code>.</p>
<h3>Thread Pool Size</h3>
<p> When salt cloud is operating in parallel mode via the <code>-P</code> argument, you can control the thread pool size by specifying the <code>pool_size</code> parameter with a positive integer value. </p>
<p> By default, the thread pool size will be set to the number of VMs that salt cloud is operating on. </p>
<pre>
pool_size: 10
</pre>
<h3>Minion Configuration</h3>
<p> The default minion configuration is set up in this file. Minions created by salt-cloud derive their configuration from this file. Almost all parameters found in Configuring the Salt Minion can be used here. </p>
<pre>
minion:
  master: saltmaster.example.com
</pre>
<p> In particular, this is the location to specify the location of the salt master and its listening port, if the port is not set to the default.</p>
<h3>Cloud Configuration Syntax</h3>
<p> The data specific to interacting with public clouds is set up here. </p>
<p> Cloud provider configuration syntax can live in several places. The first is in <code>/etc/salt/cloud</code>: </p>
<pre>
# /etc/salt/cloud
providers:
  my-aws-migrated-config:
    id: HJGRYCILJLKJYG
    key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
    keyname: test
    securitygroup: quick-start
    private_key: /root/test.pem
    provider: aws
</pre>
<p> Cloud provider configuration data can also be housed in <code>/etc/salt/cloud.providers</code> or any file matching <code>/etc/salt/cloud.providers.d/*.conf</code>. All files in any of these locations will be parsed for cloud provider data. </p>
<p> Using the example configuration above: </p>
<pre>
# /etc/salt/cloud.providers
# or could be /etc/salt/cloud.providers.d/*.conf
my-aws-config:
  id: HJGRYCILJLKJYG
  key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
  keyname: test
  securitygroup: quick-start
  private_key: /root/test.pem
  provider: aws
</pre>
<p> <code>NOTE:</code> Salt Cloud provider configurations within <code>/etc/cloud.provider.d/ should not specify the &#8220;providers</code> starting key. </p>
<p> It is also possible to have multiple cloud configuration blocks within the same alias block. For example: </p>
<pre>
production-config:
  - id: HJGRYCILJLKJYG
    key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
    keyname: test
    securitygroup: quick-start
    private_key: /root/test.pem
    provider: aws
  - user: example_user
    apikey: 123984bjjas87034
    provider: rackspace
</pre>
<p> However, using this configuration method requires a change with profile configuration blocks. The provider alias needs to have the provider key value appended as in the following example: </p>
<pre>
rhel_aws_dev:
  provider: production-config:aws
  image: ami-e565ba8c
  size: t1.micro
rhel_aws_prod:
  provider: production-config:aws
  image: ami-e565ba8c
  size: High-CPU Extra Large Instance
database_prod:
  provider: production-config:rackspace
  image: Ubuntu 12.04 LTS
  size: 256 server
</pre>
<p> Notice that because of the multiple entries, one has to be explicit about the provider alias and name, from the above example, <code>production-config: aws</code>. </p>
<p> This data interactions with the <code>salt-cloud</code> binary regarding its <code>&#8211;list-location</code>, <code>&#8211;list-images</code>, and <code>&#8211;list-sizes</code> which needs a cloud provider as an argument. The argument used should be the configured cloud provider alias. If the provider alias has multiple entries, <code>&lt;provider-alias&gt;: &lt;provider-name&gt;</code> should be used. </p>
<p> To allow for a more extensible configuration, <code>&#8211;providers-config</code>, which defaults to <code>/etc/salt/cloud.providers</code>, was added to the cli parser. It allows for the providers&#8217; configuration to be added on a per-file basis.</p>
<h3>Pillar Configuration</h3>
<p> It is possible to configure cloud providers using pillars. This is only used when inside the cloud module. You can setup a variable called <code>cloud</code> that contains your profile and provider to pass that information to the cloud servers instead of having to copy the full configuration to every minion. In your pillar file, you would use something like this: </p>
<pre>
cloud:
  ssh_key_name: saltstack
  ssh_key_file: /root/.ssh/id_rsa
  update_cachedir: True
  diff_cache_events: True
  change_password: True
  providers:
    my-nova:
      identity_url: <a rel="nofollow noopener" href="https://identity.api.rackspacecloud.com/v2.0/" target="_blank">https://identity.api.rackspacecloud.com/v2.0/</a>
      compute_region: IAD
      user: myuser
      api_key: apikey
      tenant: 123456
      provider: nova
    my-openstack:
      identity_url: <a rel="nofollow noopener" href="https://identity.api.rackspacecloud.com/v2.0/tokens" target="_blank">https://identity.api.rackspacecloud.com/v2.0/tokens</a>
      user: user2
      apikey: apikey2
      tenant: 654321
      compute_region: DFW
      provider: openstack
      compute_name: cloudServersOpenStack
  profiles:
    ubuntu-nova:
      provider: my-nova
      size: performance1-8
      image: bb02b1a3-bc77-4d17-ab5b-421d89850fca
      script_args: git develop
    ubuntu-openstack:
      provider: my-openstack
      size: performance1-8
      image: bb02b1a3-bc77-4d17-ab5b-421d89850fca
      script_args: git develop
</pre>
<h3>Cloud Configurations</h3>
<h3>Rackspace</h3>
<p> Rackspace cloud requires two configuration options; a <code>user</code> and an <code>apikey</code>: </p>
<pre>
my-rackspace-config:
  user: example_user
  apikey: 123984bjjas87034
  provider: rackspace-config
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-rackspace-config</code>.</p>
<h3>Amazon AWS</h3>
<p> A number of configuration options are required for Amazon AWS including <code>id</code>, <code>key</code>, <code>keyname</code>, <code>securitygroup</code>, and <code>private_key</code>: </p>
<pre>
my-aws-quick-start:
  id: HJGRYCILJLKJYG
  key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
  keyname: test
  securitygroup: quick-start
  private_key: /root/test.pem
  provider: aws
my-aws-default:
  id: HJGRYCILJLKJYG
  key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
  keyname: test
  securitygroup: default
  private_key: /root/test.pem
  provider: aws
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be either <code>provider: my-aws-quick-start</code> or <code>provider: my-aws-default</code>.</p>
<h3>Linode</h3>
<p> Linode requires a single API key, but the default root password also needs to be set: </p>
<p>my &#8211; linode &#8211; config : apikey : asldkgfakl;<br />
sdfjsjaslfjaklsdjf;<br />
askldjfaaklsjdfhasldsadfghdkf<br />
        password : F00barbaz<br />
                       ssh_pubkey : ssh &#8211;<br />
                                    ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKHEOLLbeXgaqRQT9NBAopVz366SdYc0KKX33vAnq + 2R user[at] host ssh_key_file : ~ /.ssh / id_ed25519 provider : linode</p>
<p> The password needs to be 8 characters and contain lowercase, uppercase, and numbers. </p>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-linode-config</code></p>
<h3>Joyent Cloud</h3>
<p> The Joyent cloud requires three configuration parameters: The username and password that are used to log into the Joyent system, as well as the location of the private SSH key associated with the Joyent account. The SSH key is needed to send the provisioning commands up to the freshly created virtual machine. </p>
<pre>
my-joyent-config:
  user: fred
  password: saltybacon
  private_key: /root/joyent.pem
  provider: joyent
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-joyent-config</code></p>
<h3>GoGrid</h3>
<p> To use Salt Cloud with GoGrid, log into the GoGrid web interface and create an API key. Do this by clicking on &quot;My Account&quot; and then going to the API Keys tab. </p>
<p> The <code>apikey</code> and the <code>sharedsecret</code> configuration parameters need to be set in the configuration file to enable interfacing with GoGrid: </p>
<pre>
my-gogrid-config:
  apikey: asdff7896asdh789
  sharedsecret: saltybacon
  provider: gogrid
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-gogrid-config</code>.</p>
<h3>OpenStack</h3>
<p> OpenStack configuration differs between providers, and at the moment several options need to be specified. This module has been officially tested against the HP and the Rackspace implementations, and some examples are provided for both. </p>
<pre>
# For HP
my-openstack-hp-config:
  identity_url:
  '<a rel="nofollow noopener" href="https://region-a.geo-1.identity.hpcloudsvc.com:35357/v2.0/&#039;" target="_blank">https://region-a.geo-1.identity.hpcloudsvc.com:35357/v2.0/'</a>
  compute_name: Compute
  compute_region: 'az-1.region-a.geo-1'
  tenant: myuser-tenant1
  user: myuser
  ssh_key_name: mykey
  ssh_key_file: '/etc/salt/hpcloud/mykey.pem'
  password: mypass
  provider: openstack
# For Rackspace
my-openstack-rackspace-config:
  identity_url: '<a rel="nofollow noopener" href="https://identity.api.rackspacecloud.com/v2.0/tokens&#039;" target="_blank">https://identity.api.rackspacecloud.com/v2.0/tokens'</a>
  compute_name: cloudServersOpenStack
  protocol: ipv4
  compute_region: DFW
  protocol: ipv4
  user: myuser
  tenant: 5555555
  password: mypass
  provider: openstack
</pre>
<p> If you have an API key for your provider, it may be specified instead of a password: </p>
<pre>
my-openstack-hp-config:
  apikey: 901d3f579h23c8v73q9
my-openstack-rackspace-config:
  apikey: 901d3f579h23c8v73q9
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be either <code>provider: my-openstack-hp-config</code> or <code>provider: my-openstack-rackspace-config</code>. </p>
<p> You will certainly need to configure the <code>user</code>, <code>tenant</code>, and either <code>password</code> or <code>apikey</code>. </p>
<p> If your OpenStack instances only have private IP addresses and a CIDR range of private addresses are not reachable from the salt-master, you may set your preference to have Salt ignore it: </p>
<pre>
my-openstack-config:
  ignore_cidr: 192.168.0.0/16
</pre>
<p> For in-house OpenStack Essex installation, libcloud needs the service_type : </p>
<pre>
my-openstack-config:
  identity_url: '<a rel="nofollow noopener" href="http://control.openstack.example.org:5000/v2.0/&#039;" target="_blank">http://control.openstack.example.org:5000/v2.0/'</a>
  compute_name : Compute Service
  service_type : compute
</pre>
<h3>DigitalOcean</h3>
<p> Using Salt for DigitalOcean requires a <code>client_key</code> and an <code>api_key</code>. These can be found in the DigitalOcean web interface, in the &quot;My Settings&quot; section, under the API Access tab. </p>
<pre>
my-digitalocean-config:
  provider: digital_ocean
  personal_access_token: xxx
  location: New York 1
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-digital-ocean-config</code>.</p>
<h3>Parallels</h3>
<p> Using Salt with Parallels requires a <code>user</code>, <code>password</code> and <code>URL</code>. These can be obtained from your cloud provider. </p>
<pre>
my-parallels-config:
  user: myuser
  password: xyzzy
  url: <a rel="nofollow noopener" href="https://api.cloud.xmission.com:4465/paci/v1.0/" target="_blank">https://api.cloud.xmission.com:4465/paci/v1.0/</a>
  provider: parallels
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-parallels-config</code>.</p>
<h3>Proxmox</h3>
<p> Using Salt with Proxmox requires a <code>user</code>, <code>password</code>, and <code>URL</code>. These can be obtained from your cloud provider. Both PAM and PVE users can be used. </p>
<pre>
my-proxmox-config:
  provider: proxmox
  user: saltcloud@pve
  password: xyzzy
  url: your.proxmox.host
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: my-proxmox-config</code>.</p>
<h3>LXC</h3>
<p> The lxc driver uses saltify to install salt and attach the lxc container as a new lxc minion. As soon as we can, we manage baremetal operation over SSH. You can also destroy those containers via this driver. </p>
<pre>
devhost10-lxc:
  target: devhost10
  provider: lxc
</pre>
<p> And in the map file: </p>
<pre>
devhost10-lxc:
  provider: devhost10-lxc
  from_container: ubuntu
  backing: lvm
  sudo: True
  size: 3g
  ip: 10.0.3.9
  minion:
    master: 10.5.0.1
    master_port: 4506
  lxc_conf:
    - lxc.utsname: superlxc
</pre>
<p> <code>NOTE:</code> In the cloud profile that uses this provider configuration, the syntax for the <code>provider</code> required field would be <code>provider: devhost10-lxc</code>.</p>
<h3>Saltify</h3>
<p> The Saltify driver is a new, experimental driver designed to install Salt on a remote machine, virtual or bare metal, using SSH. This driver is useful for provisioning machines which are already installed, but not Salted. For more information about using this driver and for configuration examples, please see the Gettting Started with Saltify documentation.</p>
<h3>Extending Profiles and Cloud Providers Configuration</h3>
<p> As of 0.8.7, the option to extend both the profiles and cloud providers configuration and avoid duplication was added. The extends feature works on the current profiles configuration, but, regarding the cloud providers configuration, <code>only</code> works in the new syntax and respective configuration files, i.e. <code>/etc/salt/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/*.conf</code>. </p>
<p> <code>NOTE:</code> Extending cloud profiles and providers is not recursive. For example, a profile that is extended by a second profile is possible, but the second profile cannot be extended by a third profile. </p>
<p> Also, if a profile (or provider) is extending another profile and each contains a list of values, the lists from the extending profile will override the list from the original profile. The lists are not merged together.</p>
<h3>Extending Profiles</h3>
<p> Some example usage on how to use <code>extends</code> with profiles. Consider <code>/etc/salt/salt/cloud.profiles</code> containing: </p>
<pre>
development-instances:
  provider: my-ec2-config
  size: t1.micro
  ssh_username: ec2_user
  securitygroup:
    - default
  deploy: False
Amazon-Linux-AMI-2012.09-64bit:
  image: ami-54cf5c3d
  extends: development-instances
Fedora-17:
  image: ami-08d97e61
  extends: development-instances
CentOS-5:
  provider: my-aws-config
  image: ami-09b61d60
  extends: development-instances
</pre>
<p> The above configuration, once parsed would generate the following profiles data: </p>
<p>[{&#8216;deploy&#8217; : False,<br />
  &#8216;image&#8217; : &#8216;ami-08d97e61&#8217;,<br />
  &#8216;profile&#8217; : &#8216;Fedora-17&#8217;,<br />
  &#8216;provider&#8217; : &#8216;my-ec2-config&#8217;,<br />
  &#8216;securitygroup&#8217; : [&#8216;default&#8217;],<br />
  &#8216;size&#8217; : &#8216;t1.micro&#8217;,<br />
  &#8216;ssh_username&#8217; : &#8216;ec2_user&#8217;},<br />
 {&#8216;deploy&#8217; : False,<br />
  &#8216;image&#8217; : &#8216;ami-09b61d60&#8217;,<br />
  &#8216;profile&#8217; : &#8216;CentOS-5&#8217;,<br />
  &#8216;provider&#8217; : &#8216;my-aws-config&#8217;,<br />
  &#8216;securitygroup&#8217; : [&#8216;default&#8217;],<br />
  &#8216;size&#8217; : &#8216;t1.micro&#8217;,<br />
  &#8216;ssh_username&#8217; : &#8216;ec2_user&#8217;},<br />
 {&#8216;deploy&#8217; : False,<br />
  &#8216;image&#8217; : &#8216;ami-54cf5c3d&#8217;,<br />
  &#8216;profile&#8217; : &#8216;Amazon-Linux-AMI-2012.09-64bit&#8217;,<br />
  &#8216;provider&#8217; : &#8216;my-ec2-config&#8217;,<br />
  &#8216;securitygroup&#8217; : [&#8216;default&#8217;],<br />
  &#8216;size&#8217; : &#8216;t1.micro&#8217;,<br />
  &#8216;ssh_username&#8217; : &#8216;ec2_user&#8217;},<br />
 {&#8216;deploy&#8217; : False,<br />
  &#8216;profile&#8217; : &#8216;development-instances&#8217;,<br />
  &#8216;provider&#8217; : &#8216;my-ec2-config&#8217;,<br />
  &#8216;securitygroup&#8217; : [&#8216;default&#8217;],<br />
  &#8216;size&#8217; : &#8216;t1.micro&#8217;,<br />
  &#8216;ssh_username&#8217; : &#8216;ec2_user&#8217;}]</p>
<p> Pretty cool right?</p>
<h3>Extending Providers</h3>
<p> Some example usage on how to use <code>extends</code> within the cloud providers configuration. Consider <code>/etc/salt/salt/cloud.providers</code> containing: </p>
<p>my &#8211; develop &#8211; envs : -id : HJGRYCILJLKJYG key : &#8216;kdjgfsgm;woormgl/aserigjksjdhasdfgn&#8217; keyname : test securitygroup : quick &#8211; start private_key : / root / test.pem location : ap &#8211; southeast &#8211; 1 availability_zone : ap &#8211; southeast &#8211; 1b provider : aws &#8211; user : myuser[at] mycorp.com password : mypass ssh_key_name : mykey ssh_key_file : &#8216;/etc/salt/ibm/mykey.pem&#8217; location : Raleigh provider : ibmsce my &#8211; productions &#8211; envs : -extends : my &#8211; develop &#8211; envs : ibmsce user : my &#8211; production &#8211; user[at] mycorp.com location : us &#8211; east &#8211; 1 availability_zone : us &#8211; east &#8211; 1</p>
<p> The above configuration, once parsed would generate the following providers data: </p>
<p>&#8216;providers&#8217;:<br />
{<br />
    &#8216;my-develop-envs&#8217; : [<br />
        {&#8216;availability_zone&#8217; : &#8216;ap-southeast-1b&#8217;,<br />
         &#8216;id&#8217; : &#8216;HJGRYCILJLKJYG&#8217;,<br />
         &#8216;key&#8217; : &#8216;kdjgfsgm;woormgl/aserigjksjdhasdfgn&#8217;,<br />
         &#8216;keyname&#8217; : &#8216;test&#8217;,<br />
         &#8216;location&#8217; : &#8216;ap-southeast-1&#8217;,<br />
         &#8216;private_key&#8217; : &#8216;/root/test.pem&#8217;,<br />
         &#8216;provider&#8217; : &#8216;aws&#8217;,<br />
         &#8216;securitygroup&#8217; : &#8216;quick-start&#8217;},<br />
        {&#8216;location&#8217; : &#8216;Raleigh&#8217;,<br />
         &#8216;password&#8217; : &#8216;mypass&#8217;,<br />
         &#8216;provider&#8217; : &#8216;ibmsce&#8217;,<br />
         &#8216;ssh_key_file&#8217; : &#8216;/etc/salt/ibm/mykey.pem&#8217;,<br />
         &#8216;ssh_key_name&#8217; : &#8216;mykey&#8217;,<br />
         &#8216;user&#8217; : &#8216;myuser [at] mycorp.com&#8217;}<br />
    ],<br />
                        &#8216;my-productions-envs&#8217; : [<br />
                            {&#8216;availability_zone&#8217; : &#8216;us-east-1&#8217;,<br />
                             &#8216;location&#8217; : &#8216;us-east-1&#8217;,<br />
                             &#8216;password&#8217; : &#8216;mypass&#8217;,<br />
                             &#8216;provider&#8217; : &#8216;ibmsce&#8217;,<br />
                             &#8216;ssh_key_file&#8217; : &#8216;/etc/salt/ibm/mykey.pem&#8217;,<br />
                             &#8216;ssh_key_name&#8217; : &#8216;mykey&#8217;,<br />
                             &#8216;user&#8217; : &#8216;my-production-user [at] mycorp.com&#8217;}<br />
                        ]<br />
}</p>
<h3>Windows Configuration</h3>
<h3>Spinning up Windows Minions</h3>
<p> It is possible to use Salt Cloud to spin up Windows instances, and then install Salt on them. This functionality is available on all cloud providers that are supported by Salt Cloud. However, it may not necessarily be available on all Windows images.</p>
<h3>Requirements</h3>
<p> Salt Cloud makes use of <i>impacket</i> and <i>winexe</i> to set up the Windows Salt Minion installer. </p>
<p> <i>impacket</i> is usually available as either the <i>impacket</i> or the <i>python-impacket</i> package, depending on the distribution. More information on <i>impacket</i> can be found at the project home:</p>
<dl>
<dt>&bull;</p>
<dd> <i>impacket project home</i> </p>
<p> <i>winexe</i> is less commonly available in distribution-specific repositories. However, it is currently being built for various distributions in 3rd party channels:</p>
<dt>&bull;</p>
<dd> <i>RPMs at pbone.net</i></p>
<dt>&bull;</p>
<dd> <i>OpenSuse Build Service</i> </p>
<p> Additionally, a copy of the Salt Minion Windows installer must be present on the system on which Salt Cloud is running. This installer may be downloaded from saltstack.com:</p>
<dt>&bull;</p>
<dd> <i>SaltStack Download Area</i></dl>
<h3>Firewall Settings</h3>
<p> Because Salt Cloud makes use of <i>smbclient</i> and <i>winexe</i>, port 445 must be open on the target image. This port is not generally open by default on a standard Windows distribution, and care must be taken to use an image in which this port is open, or the Windows firewall is disabled. </p>
<p> If supported by the cloud provider, a PowerShell script may be used to open up this port automatically, using the cloud provider&#8217;s <i>userdata</i>. The following script would open up port 445, and apply the changes: </p>
<pre>
&lt;powershell&gt;
New-NetFirewallRule -Name &quot;SMB445&quot; -DisplayName &quot;SMB445&quot; -Protocol TCP -LocalPort 445
Set-Item (dir wsman:\localhost\Listener\*\Port -Recurse).pspath 445 -Force
Restart-Service winrm
&lt;/powershell&gt;
</pre>
<p> For EC2, this script may be saved as a file, and specified in the provider or profile configuration as <i>userdata_file</i>. For instance: </p>
<pre>
userdata_file: /etc/salt/windows-firewall.ps1
</pre>
<h3>Configuration</h3>
<p> Configuration is set as usual, with some extra configuration settings. The location of the Windows installer on the machine that Salt Cloud is running on must be specified. This may be done in any of the regular configuration files (main, providers, profiles, maps). For example: </p>
<p> Setting the installer in <code>/etc/salt/cloud.providers</code>: </p>
<pre>
my-softlayer:
  provider: softlayer
  user: MYUSER1138
  apikey: 'e3b68aa711e6deadc62d5b76355674beef7cc3116062ddbacafe5f7e465bfdc9'
  minion:
    master: saltmaster.example.com
  win_installer: /root/Salt-Minion-2014.7.0-AMD64-Setup.exe
  win_username: Administrator
  win_password: letmein
</pre>
<p> The default Windows user is <i>Administrator</i>, and the default Windows password is blank.</p>
<h3>Auto-Generated Passwords on EC2</h3>
<p> On EC2, when the <i>win_password</i> is set to <i>auto</i>, Salt Cloud will query EC2 for an auto-generated password. This password is expected to take at least 4 minutes to generate, adding additional time to the deploy process. </p>
<p> When the EC2 API is queried for the auto-generated password, it will be returned in a message encrypted with the specified <i>keyname</i>. This requires that the appropriate <i>private_key</i> file is also specified. Such a profile configuration might look like: </p>
<pre>
windows-server-2012:
  provider: my-ec2-config
  image: ami-c49c0dac
  size: m1.small
  securitygroup: windows
  keyname: mykey
  private_key: /root/mykey.pem
  userdata_file: /etc/salt/windows-firewall.ps1
  win_installer: /root/Salt-Minion-2014.7.0-AMD64-Setup.exe
  win_username: Administrator
  win_password: auto
</pre>
<h3>Cloud Provider Specifics</h3>
<h3>Getting Started With Aliyun ECS</h3>
<p> The Aliyun ECS (Elastic Computer Service) is one of the most popular public cloud providers in China. This cloud provider can be used to manage aliyun instance using salt-cloud. </p>
<p> <i><a rel="nofollow noopener" href="http://www.aliyun.com/" target="_blank">http://www.aliyun.com/</a></i></p>
<h3>Dependencies</h3>
<p> This driver requires the Python <code>requests</code> library to be installed.</p>
<h3>Configuration</h3>
<p> Using Salt for Aliyun ECS requires aliyun access key id and key secret. These can be found in the aliyun web interface, in the &quot;User Center&quot; section, under &quot;My Service&quot; tab. </p>
<pre>
# Note: This example is for /etc/salt/cloud.providers or any file in the
# /etc/salt/cloud.providers.d/ directory.
my-aliyun-config:
  # aliyun Access Key ID
  id: wDGEwGregedg3435gDgxd
  # aliyun Access Key Secret
  key: GDd45t43RDBTrkkkg43934t34qT43t4dgegerGEgg
  location: cn-qingdao
  provider: aliyun
</pre>
<h3>Profiles</h3>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d/</code> directory: </p>
<pre>
aliyun_centos:
    provider: my-aliyun-config
    size: ecs.t1.small
    location: cn-qingdao
    securitygroup: G1989096784427999
    image: centos6u3_64_20G_aliaegis_20130816.vhd
</pre>
<p> Sizes can be obtained using the <code>&#8211;list-sizes</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; sizes my &#8211; aliyun &#8211; config<br />
my &#8211; aliyun &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;aliyun : &#8212; &#8212; &#8212; &#8212; &#8211;ecs.c1.large : &#8212; &#8212; &#8212; &#8212; &#8211;CpuCoreCount : 8 InstanceTypeId : ecs.c1.large MemorySize : 16.0 &#8230; SNIP&#8230;</p>
<p> Images can be obtained using the <code>&#8211;list-images</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; images my &#8211; aliyun &#8211; config<br />
my &#8211; aliyun &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;aliyun : &#8212; &#8212; &#8212; &#8212; &#8211;centos5u8_64_20G_aliaegis_20131231.vhd : &#8212; &#8212; &#8212; &#8212; &#8211;Architecture : x86_64 Description : ImageId : centos5u8_64_20G_aliaegis_20131231.vhd ImageName : CentOS 5.8 64ä½ ImageOwnerAlias : system ImageVersion : 1.0 OSName : CentOS 5.8 64ä½ Platform : CENTOS5 Size : 20 Visibility : public&#8230; SNIP&#8230;</p>
<p> Locations can be obtained using the <code>&#8211;list-locations</code> option for the <code>salt-cloud</code> command: </p>
<p>my &#8211; aliyun &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;aliyun : &#8212; &#8212; &#8212; &#8212; &#8211;cn &#8211; beijing : &#8212; &#8212; &#8212; &#8212; &#8211;LocalName : åäº¬ RegionId : cn &#8211; beijing cn &#8211; hangzhou : &#8212; &#8212; &#8212; &#8212; &#8211;LocalName : æ­å· RegionId : cn &#8211; hangzhou cn &#8211; hongkong : &#8212; &#8212; &#8212; &#8212; &#8211;LocalName : é¦æ¸¯ RegionId : cn &#8211; hongkong cn &#8211; qingdao : &#8212; &#8212; &#8212; &#8212; &#8211;LocalName : éå² RegionId : cn &#8211; qingdao</p>
<p> Security Group can be obtained using the <code>-f list_securitygroup</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; location = cn &#8211; qingdao &#8211; f list_securitygroup my &#8211; aliyun &#8211; config<br />
my &#8211; aliyun &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;aliyun : &#8212; &#8212; &#8212; &#8212; &#8211;G1989096784427999 : &#8212; &#8212; &#8212; &#8212; &#8211;Description : G1989096784427999 SecurityGroupId : G1989096784427999</p>
<p> <code>NOTE:</code> Aliyun ECS REST API documentation is available from <i>Aliyun ECS API</i>.</p>
<h3>Getting Started With Azure</h3>
<p> New in version 2014.1.0. </p>
<p> Azure is a cloud service by Microsoft providing virtual machines, SQL services, media services, and more. This document describes how to use Salt Cloud to create a virtual machine on Azure, with Salt installed. </p>
<p> More information about Azure is located at <i><a rel="nofollow noopener" href="http://www.windowsazure.com/" target="_blank">http://www.windowsazure.com/</a></i>.</p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> The <i>Azure</i> Python SDK.</p>
<dt>&bull;</p>
<dd> A Microsoft Azure account</p>
<dt>&bull;</p>
<dd> OpenSSL (to generate the certificates)</p>
<dt>&bull;</p>
<dd> <i>Salt</i></dl>
<h3>Configuration</h3>
<p> Set up the provider config at <code>/etc/salt/cloud.providers.d/azure.conf</code>: </p>
<pre>
# Note: This example is for /etc/salt/cloud.providers.d/azure.conf
my-azure-config:
  provider: azure
  subscription_id: 3287abc8-f98a-c678-3bde-326766fd3617
  certificate_path: /etc/salt/azure.pem
  # Set up the location of the salt master
  #
  minion:
    master: saltmaster.example.com
  # Optional
  management_host: management.core.windows.net
</pre>
<p> The certificate used must be generated by the user. OpenSSL can be used to create the management certificates. Two certificates are needed: a .cer file, which is uploaded to Azure, and a .pem file, which is stored locally. </p>
<p> To create the .pem file, execute the following command: </p>
<pre>
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout /etc/salt/azure.pem -out /etc/salt/azure.pem
</pre>
<p> To create the .cer file, execute the following command: </p>
<pre>
openssl x509 -inform pem -in /etc/salt/azure.pem -outform der -out /etc/salt/azure.cer
</pre>
<p> After creating these files, the .cer file will need to be uploaded to Azure via the &quot;Upload a Management Certificate&quot; action of the &quot;Management Certificates&quot; tab within the &quot;Settings&quot; section of the management portal. </p>
<p> Optionally, a <code>management_host</code> may be configured, if necessary for the region.</p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code>: </p>
<pre>
azure-ubuntu:
  provider: my-azure-config
  image: 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-12_04_3-LTS-amd64-server-20131003-en-us-30GB'
  size: Small
  location: 'East US'
  ssh_username: azureuser
  ssh_password: verybadpass
  slot: production
  media_link: '<a rel="nofollow noopener" href="http://portalvhdabcdefghijklmn.blob.core.windows.net/vhds&#039;" target="_blank">http://portalvhdabcdefghijklmn.blob.core.windows.net/vhds'</a>
</pre>
<p> These options are described in more detail below. Once configured, the profile can be realized with a salt command: </p>
<pre>
salt-cloud -p azure-ubuntu newinstance
</pre>
<p> This will create an salt minion instance named <code>newinstance</code> in Azure. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
salt newinstance test.ping
</pre>
<h3>Profile Options</h3>
<p> The following options are currently available for Azure.</p>
<h3>provider</h3>
<p> The name of the provider as configured in <i>/etc/salt/cloud.providers.d/azure.conf</i>.</p>
<h3>image</h3>
<p> The name of the image to use to create a VM. Available images can be viewed using the following command: </p>
<pre>
salt-cloud --list-images my-azure-config
</pre>
<h3>size</h3>
<p> The name of the size to use to create a VM. Available sizes can be viewed using the following command: </p>
<pre>
salt-cloud --list-sizes my-azure-config
</pre>
<h3>location</h3>
<p> The name of the location to create a VM in. Available locations can be viewed using the following command: </p>
<pre>
salt-cloud --list-locations my-azure-config
</pre>
<h3>ssh_username</h3>
<p> The user to use to log into the newly-created VM to install Salt.</p>
<h3>ssh_password</h3>
<p> The password to use to log into the newly-created VM to install Salt.</p>
<h3>slot</h3>
<p> The environment to which the hosted service is deployed. Valid values are <i>staging</i> or <i>production</i>. When set to <i>production</i>, the resulting URL of the new VM will be <i>&lt;vm_name&gt;.cloudapp.net</i>. When set to <i>staging</i>, the resulting URL will contain a generated hash instead.</p>
<h3>media_link</h3>
<p> This is the URL of the container that will store the disk that this VM uses. Currently, this container must already exist. If a VM has previously been created in the associated account, a container should already exist. In the web interface, go into the Storage area and click one of the available storage selections. Click the Containers link, and then copy the URL from the container that will be used. It generally looks like: </p>
<pre>
<a rel="nofollow noopener" href="http://portalvhdabcdefghijklmn.blob.core.windows.net/vhds" target="_blank">http://portalvhdabcdefghijklmn.blob.core.windows.net/vhds</a>
</pre>
<h3>Show Instance</h3>
<p> This action is a thin wrapper around <code>&#8211;full-query</code>, which displays details on a single instance only. In an environment with several machines, this will save a user from having to sort through all instance data, just to examine a single instance. </p>
<pre>
salt-cloud -a show_instance myinstance
</pre>
<h3>Getting Started With DigitalOcean</h3>
<p> DigitalOcean is a public cloud provider that specializes in Linux instances.</p>
<h3>Configuration</h3>
<p> Starting in Salt 2015.5.0, a new DigitalOcean driver was added to Salt Cloud to support DigitalOcean&#8217;s new API, APIv2. The original driver, referred to <code>digital_ocean</code> will be supported throughout the 2015.5.x releases of Salt, but will then be removed in Salt Beryllium in favor of the APIv2 driver, <code>digital_ocean_v2</code>. The following documentation is relevant to the new driver, <code>digital_ocean_v2</code>. To see documentation related to the original <code>digital_ocean</code> driver, please see the <code>DigitalOcean Salt Cloud Driver</code> </p>
<p> <code>NOTE:</code> When Salt Beryllium is released, the original <code>digital_ocean</code> driver will no longer be supported and the <code>digital_ocean_v2</code> driver will become the <code>digital_ocean</code> driver. </p>
<p> Using Salt for DigitalOcean requires a <code>personal_access_token</code>, an <code>ssh_key_file</code>, and at least one SSH key name in <code>ssh_key_names</code>. More can be added by separating each key with a comma. The <code>personal_access_token</code> can be found in the DigitalOcean web interface in the &quot;Apps &amp; API&quot; section. The SSH key name can be found under the &quot;SSH Keys&quot; section. </p>
<pre>
# Note: This example is for /etc/salt/cloud.providers or any file in the
# /etc/salt/cloud.providers.d/ directory.
my-digitalocean-config:
  provider: digital_ocean
  personal_access_token: xxx
  ssh_key_file: /path/to/ssh/key/file
  ssh_key_names: my-key-name,my-key-name-2
  location: New York 1
</pre>
<h3>Profiles</h3>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d/</code> directory: </p>
<pre>
digitalocean-ubuntu:
    provider: my-digitalocean-config
    image: Ubuntu 14.04 x32
    size: 512MB
    location: New York 1
    private_networking: True
    backups_enabled: True
    ipv6: True
</pre>
<p> Locations can be obtained using the <code>&#8211;list-locations</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; locations my &#8211; digitalocean &#8211; config<br />
my &#8211; digitalocean &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;digital_ocean : &#8212; &#8212; &#8212; &#8212; &#8211;Amsterdam 1 : &#8212; &#8212; &#8212; &#8212; &#8211;available : False features : [u&#8217;backups&#8217;] name : Amsterdam 1 sizes : [] slug : ams1&#8230; SNIP&#8230;</p>
<p> Sizes can be obtained using the <code>&#8211;list-sizes</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; sizes my &#8211; digitalocean &#8211; config<br />
my &#8211; digitalocean &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;digital_ocean : &#8212; &#8212; &#8212; &#8212; &#8211;512MB : &#8212; &#8212; &#8212; &#8212; &#8211;cost_per_hour : 0.00744 cost_per_month : 5.0 cpu : 1 disk : 20 id : 66 memory : 512 name : 512MB slug : None&#8230; SNIP&#8230;</p>
<p> Images can be obtained using the <code>&#8211;list-images</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; images my &#8211; digitalocean &#8211; config<br />
my &#8211; digitalocean &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;digital_ocean : &#8212; &#8212; &#8212; &#8212; &#8211;Arch Linux 2013.05 x64 : &#8212; &#8212; &#8212; &#8212; &#8211;distribution : Arch Linux id : 350424 name : Arch Linux 2013.05 x64 public : True slug : None&#8230; SNIP&#8230;</p>
<p> <code>NOTE:</code> DigitalOcean&#8217;s concept of <code>Applications</code> is nothing more than a pre-configured instance (same as a normal Droplet). You will find examples such <code>Docker 0.7 Ubuntu 13.04 x64</code> and <code>WordPress on Ubuntu 12.10</code> when using the <code>&#8211;list-images</code> option. These names can be used just like the rest of the standard instances when specifying an image in the cloud profile configuration. </p>
<p> <code>NOTE:</code> If your domain&#8217;s DNS is managed with DigitalOcean, you can automatically create A-records for newly created droplets. Use <code>create_dns_record: True</code> in your config to enable this. Add <code>delete_dns_record: True</code> to also delete records when a droplet is destroyed. </p>
<p> <code>NOTE:</code> Additional documentation is available from <i>DigitalOcean</i>.</p>
<h3>Getting Started With AWS EC2</h3>
<p> Amazon EC2 is a very widely used public cloud platform and one of the core platforms Salt Cloud has been built to support. </p>
<p> Previously, the suggested provider for AWS EC2 was the <code>aws</code> provider. This has been deprecated in favor of the <code>ec2</code> provider. Configuration using the old <code>aws</code> provider will still function, but that driver is no longer in active development.</p>
<h3>Dependencies</h3>
<p> This driver requires the Python <code>requests</code> library to be installed.</p>
<h3>Configuration</h3>
<p> The following example illustrates some of the options that can be set. These parameters are discussed in more detail below. </p>
<p>#Note : This example is for / etc / salt / cloud.providers or any file in the<br />
#/ etc / salt / cloud.providers.d / directory.<br />
my &#8211; ec2 &#8211; southeast &#8211; public &#8211; ips :<br />
#Set up the location of the salt master<br />
#<br />
    minion : master : saltmaster.example.com<br />
#Set up grains information, which will be common for all nodes<br />
#using this provider<br />
                          grains : node_type : broker release : 1.0.1<br />
#Specify whether to use public or private IP for deploy script.<br />
#<br />
#Valid options are:<br />
#private_ips &#8211; The salt &#8211; cloud command is run inside the EC2<br />
#public_ips &#8211; The salt &#8211; cloud command is run outside of EC2<br />
#<br />
                                               ssh_interface : public_ips<br />
#Optionally configure the Windows credential validation number of<br />
#retries and delay between retries.This defaults to 10 retries<br />
#with a one second delay betwee retries<br />
                                                                   win_deploy_auth_retries : 10 win_deploy_auth_retry_delay : 1<br />
#Set the EC2 access credentials(see below)<br />
#<br />
                                                               id : HJGRYCILJLKJYG key : &#8216;kdjgfsgm;woormgl/aserigjksjdhasdfgn&#8217;<br />
#Make sure this key is owned by root with permissions 0400.<br />
#<br />
                                                                                         private_key : /<br />
                                                                                                       etc / salt / my_test_key.pem keyname : my_test_key securitygroup : default<br />
#Optionally configure default region<br />
#Use salt &#8211; cloud&#8211; list &#8211; locations &lt; provider&gt; to obtain valid regions<br />
#<br />
                                                                                                                                                                          location : ap &#8211;<br />
    southeast &#8211; 1 availability_zone : ap &#8211; southeast &#8211; 1b<br />
#Configure which user to use to run the deploy script.This setting is<br />
#dependent upon the AMI that is used to deploy.It is usually safer to<br />
#configure this individually in a profile, than globally.Typical users<br />
#are:<br />
#<br />
#Amazon Linux-&gt;ec2 &#8211; user<br />
#RHEL-&gt;ec2 &#8211; user<br />
#CentOS-&gt;ec2 &#8211; user<br />
#Ubuntu-&gt;ubuntu<br />
#<br />
                                      ssh_username : ec2 &#8211;<br />
                                                     user<br />
#Optionally add an IAM profile<br />
                                                         iam_profile : &#8216;arn:aws:iam::123456789012:instance-profile/ExampleInstanceProfile&#8217; provider : ec2<br />
                                                                                                                                                          my &#8211;<br />
                                                                                                                                                      ec2 &#8211; southeast &#8211; private &#8211; ips :<br />
#Set up the location of the salt master<br />
#<br />
    minion : master : saltmaster.example.com<br />
#Specify whether to use public or private IP for deploy script.<br />
#<br />
#Valid options are:<br />
#private_ips &#8211; The salt &#8211; master is also hosted with EC2<br />
#public_ips &#8211; The salt &#8211; master is hosted outside of EC2<br />
#<br />
                          ssh_interface : private_ips<br />
#Optionally configure the Windows credential validation number of<br />
#retries and delay between retries.This defaults to 10 retries<br />
#with a one second delay betwee retries<br />
                                              win_deploy_auth_retries : 10 win_deploy_auth_retry_delay : 1<br />
#Set the EC2 access credentials(see below)<br />
#<br />
                                          id : HJGRYCILJLKJYG key : &#8216;kdjgfsgm;woormgl/aserigjksjdhasdfgn&#8217;<br />
#Make sure this key is owned by root with permissions 0400.<br />
#<br />
                                                                    private_key : /<br />
                                                                                  etc / salt / my_test_key.pem keyname : my_test_key securitygroup : default<br />
#Optionally configure default region<br />
#<br />
                                                                                                                                                     location : ap &#8211;<br />
                                                                                                                                                      southeast &#8211; 1 availability_zone : ap &#8211; southeast &#8211; 1b<br />
#Configure which user to use to run the deploy script.This setting is<br />
#dependent upon the AMI that is used to deploy.It is usually safer to<br />
#configure this individually in a profile, than globally.Typical users<br />
#are:<br />
#<br />
#Amazon Linux-&gt;ec2 &#8211; user<br />
#RHEL-&gt;ec2 &#8211; user<br />
#CentOS-&gt;ec2 &#8211; user<br />
#Ubuntu-&gt;ubuntu<br />
#<br />
                                                                                                                                                                                        ssh_username : ec2 &#8211;<br />
                                                                                                                                                                                                       user<br />
#Optionally add an IAM profile<br />
                                                                                                                                                                                                           iam_profile : &#8216;my other profile name&#8217; provider : ec2</p>
<h3>Access Credentials</h3>
<p> The <code>id</code> and <code>key</code> settings may be found in the Security Credentials area of the AWS Account page: </p>
<p> <i><a rel="nofollow noopener" href="https://portal.aws.amazon.com/gp/aws/securityCredentials" target="_blank">https://portal.aws.amazon.com/gp/aws/securityCredentials</a></i> </p>
<p> Both are located in the Access Credentials area of the page, under the Access Keys tab. The <code>id</code> setting is labeled Access Key ID, and the <code>key</code> setting is labeled Secret Access Key.</p>
<h3>Windows Deploy Timeouts</h3>
<p> For Windows instances, it may take longer than normal for the instance to be ready. In these circumstances, the provider configuration can be configured with a <code>win_deploy_auth_retries</code> and/or a <code>win_deploy_auth_retry_delay</code> setting, which default to 10 retries and a one second delay between retries. These retries and timeouts relate to validating the Administrator password once AWS provides the credentials via the AWS API.</p>
<h3>Key Pairs</h3>
<p> In order to create an instance with Salt installed and configured, a key pair will need to be created. This can be done in the EC2 Management Console, in the Key Pairs area. These key pairs are unique to a specific region. Keys in the us-east-1 region can be configured at: </p>
<p> <i><a rel="nofollow noopener" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#s=KeyPairs" target="_blank">https://console.aws.amazon.com/ec2/home?region=us-east-1#s=KeyPairs</a></i> </p>
<p> Keys in the us-west-1 region can be configured at </p>
<p> <i><a rel="nofollow noopener" href="https://console.aws.amazon.com/ec2/home?region=us-west-1#s=KeyPairs" target="_blank">https://console.aws.amazon.com/ec2/home?region=us-west-1#s=KeyPairs</a></i> </p>
<p> &#8230;and so on. When creating a key pair, the browser will prompt to download a pem file. This file must be placed in a directory accessible by Salt Cloud, with permissions set to either 0400 or 0600.</p>
<h3>Security Groups</h3>
<p> An instance on EC2 needs to belong to a security group. Like key pairs, these are unique to a specific region. These are also configured in the EC2 Management Console. Security groups for the us-east-1 region can be configured at: </p>
<p> <i><a rel="nofollow noopener" href="https://console.aws.amazon.com/ec2/home?region=us-east-1#s=SecurityGroups" target="_blank">https://console.aws.amazon.com/ec2/home?region=us-east-1#s=SecurityGroups</a></i> </p>
<p> &#8230;and so on. </p>
<p> A security group defines firewall rules which an instance will adhere to. If the salt-master is configured outside of EC2, the security group must open the SSH port (usually port 22) in order for Salt Cloud to install Salt.</p>
<h3>IAM Profile</h3>
<p> Amazon EC2 instances support the concept of an <i>instance profile</i>, which is a logical container for the IAM role. At the time that you launch an EC2 instance, you can associate the instance with an instance profile, which in turn corresponds to the IAM role. Any software that runs on the EC2 instance is able to access AWS using the permissions associated with the IAM role. </p>
<p> Scaffolding the profile is a 2-step configuration process:</p>
<dl>
<dt>1.</p>
<dd> Configure an IAM Role from the <i>IAM Management Console</i>.</p>
<dt>2.</p>
<dd> Attach this role to a new profile. It can be done with the <i>AWS CLI</i>: </p>
<pre>
&gt; aws iam create-instance-profile --instance-profile-name PROFILE_NAME
&gt; aws iam add-role-to-instance-profile --instance-profile-name PROFILE_NAME --role-name ROLE_NAME
</pre>
<p> Once the profile is created, you can use the <code>PROFILE_NAME</code> to configure your cloud profiles.</dl>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code>: </p>
<p>base_ec2_private : provider : my &#8211; ec2 &#8211; southeast &#8211; private &#8211; ips image : ami &#8211; e565ba8c size : t2.micro ssh_username : ec2 &#8211; user base_ec2_public : provider : my &#8211; ec2 &#8211; southeast &#8211; public &#8211; ips image : ami &#8211; e565ba8c size : t2.micro ssh_username : ec2 &#8211; user base_ec2_db : provider : my &#8211; ec2 &#8211; southeast &#8211; public &#8211; ips image : ami &#8211; e565ba8c size : m1.xlarge ssh_username : ec2 &#8211; user volumes : -{size : 10, device : / dev / sdf} &#8211; {size : 10, device : / dev / sdg, type : io1, iops : 1000} &#8211; {size : 10, device : / dev / sdh, type : io1, iops : 1000}<br />
#optionally add tags to profile:<br />
                                                                                                                                                                                                                                                                                                                                                                                                               tag : {&#8216;Environment&#8217; : &#8216;production&#8217;, &#8216;Role&#8217; : &#8216;database&#8217;}<br />
#force grains to sync after install<br />
                                                                                                                                                                                                                                                                                                                                                                                                                     sync_after_install : grains base_ec2_vpc : provider : my &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ec2 &#8211; southeast &#8211; public &#8211; ips image : ami &#8211; a73264ce size : m1.xlarge ssh_username : ec2 &#8211; user script : / etc / salt / cloud.deploy.d / user_data.sh network_interfaces : -DeviceIndex : 0 PrivateIpAddresses : -Primary : True<br />
#auto assign public ip(not EIP)<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            AssociatePublicIpAddress : True SubnetId : subnet &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  813d4bbf SecurityGroupId : -sg &#8211; 750af413 del_root_vol_on_destroy : True del_all_vol_on_destroy : True volumes : -{size : 10, device : / dev / sdf} &#8211; {size : 10, device : / dev / sdg, type : io1, iops : 1000} &#8211; {size : 10, device : / dev / sdh, type : io1, iops : 1000} tag : {&#8216;Environment&#8217; : &#8216;production&#8217;, &#8216;Role&#8217; : &#8216;database&#8217;} sync_after_install : grains</p>
<p> The profile can now be realized with a salt command: </p>
<pre>
# salt-cloud -p base_ec2 ami.example.com
# salt-cloud -p base_ec2_public ami.example.com
# salt-cloud -p base_ec2_private ami.example.com
</pre>
<p> This will create an instance named <code>ami.example.com</code> in EC2. The minion that is installed on this instance will have an <code>id</code> of <code>ami.example.com</code>. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
# salt 'ami.example.com' test.ping
</pre>
<h3>Required Settings</h3>
<p> The following settings are always required for EC2: </p>
<pre>
# Set the EC2 login data
my-ec2-config:
  id: HJGRYCILJLKJYG
  key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
  keyname: test
  securitygroup: quick-start
  private_key: /root/test.pem
  provider: ec2
</pre>
<h3>Optional Settings</h3>
<p> EC2 allows a userdata file to be passed to the instance to be created. This functionality was added to Salt in the 2015.5.0 release. </p>
<pre>
my-ec2-config:
  # Pass userdata to the instance to be created
  userdata_file: /etc/salt/my-userdata-file
</pre>
<p> EC2 allows a location to be set for servers to be deployed in. Availability zones exist inside regions, and may be added to increase specificity. </p>
<pre>
my-ec2-config:
  # Optionally configure default region
  location: ap-southeast-1
  availability_zone: ap-southeast-1b
</pre>
<p> EC2 instances can have a public or private IP, or both. When an instance is deployed, Salt Cloud needs to log into it via SSH to run the deploy script. By default, the public IP will be used for this. If the salt-cloud command is run from another EC2 instance, the private IP should be used. </p>
<pre>
my-ec2-config:
  # Specify whether to use public or private IP for deploy script
  # private_ips or public_ips
  ssh_interface: public_ips
</pre>
<p> Many EC2 instances do not allow remote access to the root user by default. Instead, another user must be used to run the deploy script using sudo. Some common usernames include ec2-user (for Amazon Linux), ubuntu (for Ubuntu instances), admin (official Debian) and bitnami (for images provided by Bitnami). </p>
<pre>
my-ec2-config:
  # Configure which user to use to run the deploy script
  ssh_username: ec2-user
</pre>
<p> Multiple usernames can be provided, in which case Salt Cloud will attempt to guess the correct username. This is mostly useful in the main configuration file: </p>
<pre>
my-ec2-config:
  ssh_username:
    - ec2-user
    - ubuntu
    - admin
    - bitnami
</pre>
<p> Multiple security groups can also be specified in the same fashion: </p>
<pre>
my-ec2-config:
  securitygroup:
    - default
    - extra
</pre>
<p> Your instances may optionally make use of EC2 Spot Instances. The following example will request that spot instances be used and your maximum bid will be $0.10. Keep in mind that different spot prices may be needed based on the current value of the various EC2 instance sizes. You can check current and past spot instance pricing via the EC2 API or AWS Console. </p>
<pre>
my-ec2-config:
  spot_config:
    spot_price: 0.10
</pre>
<p> By default, the spot instance type is set to &#8216;one-time&#8217;, meaning it will be launched and, if it&#8217;s ever terminated for whatever reason, it will not be recreated. If you would like your spot instances to be relaunched after a termination (by your or AWS), set the <code>type</code> to &#8216;persistent&#8217;. </p>
<p> NOTE: Spot instances are a great way to save a bit of money, but you do run the risk of losing your spot instances if the current price for the instance size goes above your maximum bid. </p>
<p> The following parameters may be set in the cloud configuration file to control various aspects of the spot instance launching:</p>
<dl>
<dt>&bull;</p>
<dd> <code>wait_for_spot_timeout</code>: seconds to wait before giving up on spot instance launch (default=600)</p>
<dt>&bull;</p>
<dd> <code>wait_for_spot_interval</code>: seconds to wait in between polling requests to determine if a spot instance is available (default=30)</p>
<dt>&bull;</p>
<dd> <code>wait_for_spot_interval_multiplier</code>: a multiplier to add to the interval in between requests, which is useful if AWS is throttling your requests (default=1)</p>
<dt>&bull;</p>
<dd> <code>wait_for_spot_max_failures</code>: maximum number of failures before giving up on launching your spot instance (default=10) </p>
<p> If you find that you&#8217;re being throttled by AWS while polling for spot instances, you can set the following in your core cloud configuration file that will double the polling interval after each request to AWS. </p>
<pre>
wait_for_spot_interval: 1
wait_for_spot_interval_multiplier: 2
</pre>
<p> See the <i>AWS Spot Instances</i> documentation for more information. </p>
<p> Block device mappings enable you to specify additional EBS volumes or instance store volumes when the instance is launched. This setting is also available on each cloud profile. Note that the number of instance stores varies by instance type. If more mappings are provided than are supported by the instance type, mappings will be created in the order provided and additional mappings will be ignored. Consult the <i>AWS documentation</i> for a listing of the available instance stores, and device names. </p>
<pre>
my-ec2-config:
  block_device_mappings:
    - DeviceName: /dev/sdb
      VirtualName: ephemeral0
    - DeviceName: /dev/sdc
      VirtualName: ephemeral1
</pre>
<p> You can also use block device mappings to change the size of the root device at the provisioning time. For example, assuming the root device is &#8216;/dev/sda&#8217;, you can set its size to 100G by using the following configuration. </p>
<pre>
my-ec2-config:
  block_device_mappings:
    - DeviceName: /dev/sda
      Ebs.VolumeSize: 100
      Ebs.VolumeType: gp2
      Ebs.SnapshotId: dummy0
</pre>
<p> Existing EBS volumes may also be attached (not created) to your instances or you can create new EBS volumes based on EBS snapshots. To simply attach an existing volume use the <code>volume_id</code> parameter. </p>
<pre>
device: /dev/xvdj
volume_id: vol-12345abcd
</pre>
<p> Or, to create a volume from an EBS snapshot, use the <code>snapshot</code> parameter. </p>
<pre>
device: /dev/xvdj
snapshot: snap-abcd12345
</pre>
<p> Note that <code>volume_id</code> will take precedence over the <code>snapshot</code> parameter. </p>
<p> Tags can be set once an instance has been launched. </p>
<pre>
my-ec2-config:
    tag:
        tag0: value
        tag1: value
</pre>
</dl>
<h3>Modify EC2 Tags</h3>
<p> One of the features of EC2 is the ability to tag resources. In fact, under the hood, the names given to EC2 instances by salt-cloud are actually just stored as a tag called Name. Salt Cloud has the ability to manage these tags: </p>
<pre>
salt-cloud -a get_tags mymachine
salt-cloud -a set_tags mymachine tag1=somestuff tag2='Other stuff'
salt-cloud -a del_tags mymachine tag1,tag2,tag3
</pre>
<p> It is possible to manage tags on any resource in EC2 with a Resource ID, not just instances: </p>
<pre>
salt-cloud -f get_tags my_ec2 resource_id=af5467ba
salt-cloud -f set_tags my_ec2 resource_id=af5467ba tag1=somestuff
salt-cloud -f del_tags my_ec2 resource_id=af5467ba tag1,tag2,tag3
</pre>
<h3>Rename EC2 Instances</h3>
<p> As mentioned above, EC2 instances are named via a tag. However, renaming an instance by renaming its tag will cause the salt keys to mismatch. A rename function exists which renames both the instance, and the salt keys. </p>
<pre>
salt-cloud -a rename mymachine newname=yourmachine
</pre>
<h3>EC2 Termination Protection</h3>
<p> EC2 allows the user to enable and disable termination protection on a specific instance. An instance with this protection enabled cannot be destroyed. </p>
<pre>
salt-cloud -a enable_term_protect mymachine
salt-cloud -a disable_term_protect mymachine
</pre>
<h3>Rename on Destroy</h3>
<p> When instances on EC2 are destroyed, there will be a lag between the time that the action is sent, and the time that Amazon cleans up the instance. During this time, the instance still retails a Name tag, which will cause a collision if the creation of an instance with the same name is attempted before the cleanup occurs. In order to avoid such collisions, Salt Cloud can be configured to rename instances when they are destroyed. The new name will look something like: </p>
<pre>
myinstance-DEL20f5b8ad4eb64ed88f2c428df80a1a0c
</pre>
<p> In order to enable this, add rename_on_destroy line to the main configuration file: </p>
<pre>
my-ec2-config:
  rename_on_destroy: True
</pre>
<h3>Listing Images</h3>
<p> Normally, images can be queried on a cloud provider by passing the <code>&#8211;list-images</code> argument to Salt Cloud. This still holds true for EC2: </p>
<pre>
salt-cloud --list-images my-ec2-config
</pre>
<p> However, the full list of images on EC2 is extremely large, and querying all of the available images may cause Salt Cloud to behave as if frozen. Therefore, the default behavior of this option may be modified, by adding an <code>owner</code> argument to the provider configuration: </p>
<pre>
owner: aws-marketplace
</pre>
<p> The possible values for this setting are <code>amazon</code>, <code>aws-marketplace</code>, <code>self</code>, <code>&lt;AWS account ID&gt;</code> or <code>all</code>. The default setting is <code>amazon</code>. Take note that <code>all</code> and <code>aws-marketplace</code> may cause Salt Cloud to appear as if it is freezing, as it tries to handle the large amount of data. </p>
<p> It is also possible to perform this query using different settings without modifying the configuration files. To do this, call the <code>avail_images</code> function directly: </p>
<pre>
salt-cloud -f avail_images my-ec2-config owner=aws-marketplace
</pre>
<h3>EC2 Images</h3>
<p> The following are lists of available AMI images, generally sorted by OS. These lists are on 3rd-party websites, are not managed by Salt Stack in any way. They are provided here as a reference for those who are interested, and contain no warranty (express or implied) from anyone affiliated with Salt Stack. Most of them have never been used, much less tested, by the Salt Stack team.</p>
<dl>
<dt>&bull;</p>
<dd> <i>Arch Linux</i></p>
<dt>&bull;</p>
<dd> <i>FreeBSD</i></p>
<dt>&bull;</p>
<dd> <i>Fedora</i></p>
<dt>&bull;</p>
<dd> <i>CentOS</i></p>
<dt>&bull;</p>
<dd> <i>Ubuntu</i></p>
<dt>&bull;</p>
<dd> <i>Debian</i></p>
<dt>&bull;</p>
<dd> <i>OmniOS</i></p>
<dt>&bull;</p>
<dd> <i>All Images on Amazon</i></dl>
<h3>show_image</h3>
<p> This is a function that describes an AMI on EC2. This will give insight as to the defaults that will be applied to an instance using a particular AMI. </p>
<pre>
$ salt-cloud -f show_image ec2 image=ami-fd20ad94
</pre>
<h3>show_instance</h3>
<p> This action is a thin wrapper around <code>&#8211;full-query</code>, which displays details on a single instance only. In an environment with several machines, this will save a user from having to sort through all instance data, just to examine a single instance. </p>
<pre>
$ salt-cloud -a show_instance myinstance
</pre>
<h3>ebs_optimized</h3>
<p> This argument enables switching of the EbsOptimized setting which default to &#8216;false&#8217;. Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn&#8217;t available with all instance types. Additional usage charges apply when using an EBS-optimized instance. </p>
<p> This setting can be added to the profile or map file for an instance. </p>
<p> If set to True, this setting will enable an instance to be EbsOptimized </p>
<pre>
ebs_optimized: True
</pre>
<p> This can also be set as a cloud provider setting in the EC2 cloud configuration: </p>
<pre>
my-ec2-config:
  ebs_optimized: True
</pre>
<h3>del_root_vol_on_destroy</h3>
<p> This argument overrides the default DeleteOnTermination setting in the AMI for the EBS root volumes for an instance. Many AMIs contain &#8216;false&#8217; as a default, resulting in orphaned volumes in the EC2 account, which may unknowingly be charged to the account. This setting can be added to the profile or map file for an instance. </p>
<p> If set, this setting will apply to the root EBS volume </p>
<pre>
del_root_vol_on_destroy: True
</pre>
<p> This can also be set as a cloud provider setting in the EC2 cloud configuration: </p>
<pre>
my-ec2-config:
  del_root_vol_on_destroy: True
</pre>
<h3>del_all_vols_on_destroy</h3>
<p> This argument overrides the default DeleteOnTermination setting in the AMI for the not-root EBS volumes for an instance. Many AMIs contain &#8216;false&#8217; as a default, resulting in orphaned volumes in the EC2 account, which may unknowingly be charged to the account. This setting can be added to the profile or map file for an instance. </p>
<p> If set, this setting will apply to any (non-root) volumes that were created by salt-cloud using the &#8216;volumes&#8217; setting. </p>
<p> The volumes will not be deleted under the following conditions * If a volume is detached before terminating the instance * If a volume is created without this setting and attached to the instance </p>
<pre>
del_all_vols_on_destroy: True
</pre>
<p> This can also be set as a cloud provider setting in the EC2 cloud configuration: </p>
<pre>
my-ec2-config:
  del_all_vols_on_destroy: True
</pre>
<p> The setting for this may be changed on all volumes of an existing instance using one of the following commands: </p>
<pre>
salt-cloud -a delvol_on_destroy myinstance
salt-cloud -a keepvol_on_destroy myinstance
salt-cloud -a show_delvol_on_destroy myinstance
</pre>
<p> The setting for this may be changed on a volume on an existing instance using one of the following commands: </p>
<pre>
salt-cloud -a delvol_on_destroy myinstance device=/dev/sda1
salt-cloud -a delvol_on_destroy myinstance volume_id=vol-1a2b3c4d
salt-cloud -a keepvol_on_destroy myinstance device=/dev/sda1
salt-cloud -a keepvol_on_destroy myinstance volume_id=vol-1a2b3c4d
salt-cloud -a show_delvol_on_destroy myinstance device=/dev/sda1
salt-cloud -a show_delvol_on_destroy myinstance volume_id=vol-1a2b3c4d
</pre>
<h3>EC2 Termination Protection</h3>
<p> EC2 allows the user to enable and disable termination protection on a specific instance. An instance with this protection enabled cannot be destroyed. The EC2 driver adds a show_term_protect action to the regular EC2 functionality. </p>
<pre>
salt-cloud -a show_term_protect mymachine
salt-cloud -a enable_term_protect mymachine
salt-cloud -a disable_term_protect mymachine
</pre>
<h3>Alternate Endpoint</h3>
<p> Normally, EC2 endpoints are build using the region and the service_url. The resulting endpoint would follow this pattern: </p>
<pre>
ec2.&lt;region&gt;.&lt;service_url&gt;
</pre>
<p> This results in an endpoint that looks like: </p>
<pre>
ec2.us-east-1.amazonaws.com
</pre>
<p> There are other projects that support an EC2 compatibility layer, which this scheme does not account for. This can be overridden by specifying the endpoint directly in the main cloud configuration file: </p>
<pre>
my-ec2-config:
  endpoint: myendpoint.example.com:1138/services/Cloud
</pre>
<h3>Volume Management</h3>
<p> The EC2 driver has several functions and actions for management of EBS volumes.</p>
<h3>Creating Volumes</h3>
<p> A volume may be created, independent of an instance. A zone must be specified. A size or a snapshot may be specified (in GiB). If neither is given, a default size of 10 GiB will be used. If a snapshot is given, the size of the snapshot will be used. </p>
<pre>
salt-cloud -f create_volume ec2 zone=us-east-1b
salt-cloud -f create_volume ec2 zone=us-east-1b size=10
salt-cloud -f create_volume ec2 zone=us-east-1b snapshot=snap12345678
salt-cloud -f create_volume ec2 size=10 type=standard
salt-cloud -f create_volume ec2 size=10 type=io1 iops=1000
</pre>
<h3>Attaching Volumes</h3>
<p> Unattached volumes may be attached to an instance. The following values are required; name or instance_id, volume_id, and device. </p>
<pre>
salt-cloud -a attach_volume myinstance volume_id=vol-12345 device=/dev/sdb1
</pre>
<h3>Show a Volume</h3>
<p> The details about an existing volume may be retrieved. </p>
<pre>
salt-cloud -a show_volume myinstance volume_id=vol-12345
salt-cloud -f show_volume ec2 volume_id=vol-12345
</pre>
<h3>Detaching Volumes</h3>
<p> An existing volume may be detached from an instance. </p>
<pre>
salt-cloud -a detach_volume myinstance volume_id=vol-12345
</pre>
<p> <a NAME="lb[A">&nbsp;<wbr></a></p>
<h3>Deleting Volumes</h3>
<p> A volume that is not attached to an instance may be deleted. </p>
<pre>
salt-cloud -f delete_volume ec2 volume_id=vol-12345
</pre>
<p> <a NAME="lb[B">&nbsp;<wbr></a></p>
<h3>Managing Key Pairs</h3>
<p> The EC2 driver has the ability to manage key pairs. <a NAME="lb[C">&nbsp;<wbr></a></p>
<h3>Creating a Key Pair</h3>
<p> A key pair is required in order to create an instance. When creating a key pair with this function, the return data will contain a copy of the private key. This private key is not stored by Amazon, will not be obtainable past this point, and should be stored immediately. </p>
<pre>
salt-cloud -f create_keypair ec2 keyname=mykeypair
</pre>
<p> <a NAME="lb[D">&nbsp;<wbr></a></p>
<h3>Show a Key Pair</h3>
<p> This function will show the details related to a key pair, not including the private key itself (which is not stored by Amazon). </p>
<pre>
salt-cloud -f show_keypair ec2 keyname=mykeypair
</pre>
<p> <a NAME="lb[E">&nbsp;<wbr></a></p>
<h3>Delete a Key Pair</h3>
<p> This function removes the key pair from Amazon. </p>
<pre>
salt-cloud -f delete_keypair ec2 keyname=mykeypair
</pre>
<p> <a NAME="lb[F">&nbsp;<wbr></a></p>
<h3>Launching instances into a VPC</h3>
<p> <a NAME="lb[G">&nbsp;<wbr></a></p>
<h3>Simple launching into a VPC</h3>
<p> In the amazon web interface, identify the id of the subnet into which your image should be created. Then, edit your cloud.profiles file like so:- </p>
<pre>
profile-id:
  provider: provider-name
  subnetid: subnet-XXXXXXXX
  image: ami-XXXXXXXX
  size: m1.medium
  ssh_username: ubuntu
  securitygroupid:
    - sg-XXXXXXXX
</pre>
<p> <a NAME="lb[H">&nbsp;<wbr></a></p>
<h3>Specifying interface properties</h3>
<p> New in version 2014.7.0. </p>
<p> Launching into a VPC allows you to specify more complex configurations for the network interfaces of your virtual machines, for example:- </p>
<pre>
profile-id:
  provider: provider-name
  image: ami-XXXXXXXX
  size: m1.medium
  ssh_username: ubuntu
  # Do not include either 'subnetid' or 'securitygroupid' here if you are
  # going to manually specify interface configuration
  #
  network_interfaces:
    - DeviceIndex: 0
      SubnetId: subnet-XXXXXXXX
      SecurityGroupId:
        - sg-XXXXXXXX
      # Uncomment this to associate an existing Elastic IP Address with
      # this network interface:
      #
      # associate_eip: eni-XXXXXXXX
      # You can allocate more than one IP address to an interface. Use the
      # 'ip addr list' command to see them.
      #
      # SecondaryPrivateIpAddressCount: 2
      # Uncomment this to allocate a new Elastic IP Address to this
      # interface (will be associated with the primary private ip address
      # of the interface
      #
      # allocate_new_eip: True
      # Uncomment this instead to allocate a new Elastic IP Address to
      # both the primary private ip address and each of the secondary ones
      #
      allocate_new_eips: True
</pre>
<p> Note that it is an error to assign a &#8216;subnetid&#8217; or &#8216;securitygroupid&#8217; to a profile where the interfaces are manually configured like this. These are both really properties of each network interface, not of the machine itself. <a NAME="lb[I">&nbsp;<wbr></a></p>
<h3>Getting Started With GoGrid</h3>
<p> GoGrid is a public cloud provider supporting Linux and Windows. <a NAME="lb[J">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> Libcloud &gt;= 0.13.2</dl>
<p> <a NAME="lb[K">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<p> To use Salt Cloud with GoGrid log into the GoGrid web interface and create an API key. Do this by clicking on &quot;My Account&quot; and then going to the API Keys tab. </p>
<p> The <code>apikey</code> and the <code>sharedsecret</code> configuration parameters need to be set in the configuration file to enable interfacing with GoGrid: </p>
<pre>
# Note: This example is for /etc/salt/cloud.providers or any file in the
# /etc/salt/cloud.providers.d/ directory.
my-gogrid-config:
  provider: gogrid
  apikey: asdff7896asdh789
  sharedsecret: saltybacon
</pre>
<p> <code>NOTE:</code> A Note about using Map files with GoGrid: </p>
<p> Due to limitations in the GoGrid API, instances cannot be provisioned in parallel with the GoGrid driver. Map files will work with GoGrid, but the <code>-P</code> argument should not be used on maps referencing GoGrid instances. <a NAME="lb[L">&nbsp;<wbr></a></p>
<h3>Profiles</h3>
<p> <a NAME="lb[M">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d/</code> directory: </p>
<pre>
gogrid_512:
  provider: my-gogrid-config
  size: 512MB
  image: CentOS 6.2 (64-bit) w/ None
</pre>
<p> Sizes can be obtained using the <code>&#8211;list-sizes</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; sizes my &#8211; gogrid &#8211; config<br />
my &#8211; gogrid &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;gogrid : &#8212; &#8212; &#8212; &#8212; &#8211;512MB : &#8212; &#8212; &#8212; &#8212; &#8211;bandwidth : None disk : 30 driver : get_uuid : id : 512MB name : 512MB price : 0.095 ram : 512 uuid : bde1e4d7c3a643536e42a35142c7caac34b060e9&#8230; SNIP&#8230;</p>
<p> Images can be obtained using the <code>&#8211;list-images</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; images my &#8211; gogrid &#8211; config<br />
my &#8211; gogrid &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;gogrid : &#8212; &#8212; &#8212; &#8212; &#8211;CentOS 6.4(64 &#8211; bit) w / None : &#8212; &#8212; &#8212; &#8212; &#8211;driver : extra : &#8212; &#8212; &#8212; &#8212; &#8211;get_uuid : id : 18094 name : CentOS 6.4(64 &#8211; bit) w / None uuid : bfd4055389919e01aa6261828a96cf54c8dcc2c4&#8230; SNIP&#8230;<br />
 <a NAME="lb[N">&nbsp;<wbr></a></p>
<h3>Getting Started With Google Compute Engine</h3>
<p> Google Compute Engine (GCE) is Google-infrastructure as a service that lets you run your large-scale computing workloads on virtual machines. This document covers how to use Salt Cloud to provision and manage your virtual machines hosted within Google&#8217;s infrastructure. </p>
<p> You can find out more about GCE and other Google Cloud Platform services at <i><a rel="nofollow noopener" href="https://cloud.google.com" target="_blank">https://cloud.google.com</a></i>. <a NAME="lb[O">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> Libcloud &gt;= 0.14.0-beta3</p>
<dt>&bull;</p>
<dd> PyCrypto &gt;= 2.1.</p>
<dt>&bull;</p>
<dd> A Google Cloud Platform account with Compute Engine enabled</p>
<dt>&bull;</p>
<dd> A registered Service Account for authorization</p>
<dt>&bull;</p>
<dd> Oh, and obviously you&#8217;ll need <i>salt</i></dl>
<p> <a NAME="lb[P">&nbsp;<wbr></a></p>
<h3>Google Compute Engine Setup</h3>
<dl>
<dt>1.</p>
<dd> Sign up for Google Cloud Platform </p>
<p> Go to <i><a rel="nofollow noopener" href="https://cloud.google.com" target="_blank">https://cloud.google.com</a></i> and use your Google account to sign up for Google Cloud Platform and complete the guided instructions.</p>
<dt>2.</p>
<dd> Create a Project </p>
<p> Next, go to the console at <i><a rel="nofollow noopener" href="https://cloud.google.com/console" target="_blank">https://cloud.google.com/console</a></i> and create a new Project. Make sure to select your new Project if you are not automatically directed to the Project. </p>
<p> Projects are a way of grouping together related users, services, and billing. You may opt to create multiple Projects and the remaining instructions will need to be completed for each Project if you wish to use GCE and Salt Cloud to manage your virtual machines.</p>
<dt>3.</p>
<dd> Enable the Google Compute Engine service </p>
<p> In your Project, either just click <i>Compute Engine</i> to the left, or go to the <i>APIs &amp; auth</i> section and <i>APIs</i> link and enable the Google Compute Engine service.</p>
<dt>4.</p>
<dd> Create a Service Account </p>
<p> To set up authorization, navigate to <i>APIs &amp; auth</i> section and then the <i>Credentials</i> link and click the <i>CREATE NEW CLIENT ID</i> button. Select <i>Service Account</i> and click the <i>Create Client ID</i> button. This will automatically download a <code>.json</code> file which can be ignored. </p>
<p> Look for a new <i>Service Account</i> section in the page and record the generated email address for the matching key/fingerprint. The email address will be used in the <code>service_account_email_address</code> of the <code>/etc/salt/cloud</code> file.</p>
<dt>5.</p>
<dd> Key Format </p>
<p> <i>If you are using &#8220;libcloud &gt;= 0.17.0&#8220; it is recommended that you use the &#8220;JSON format&#8220; file you downloaded above and skip to the &quot;Configuration&quot; section below, using the JSON file **_in place of &#8216;NEW.pem&#8217;_*</i> in the documentation. </p>
<p> If you are using an older version of libcloud or are unsure of the version you have, please follow the instructions below to generate and format a new P12 key.* </p>
<p> In the new <i>Service Account</i> section, click <i>Generate new P12 key</i>, which will automatically download a <code>.p12</code> private key file. The <code>.p12</code> private key needs to be converted to a format compatible with libcloud. This new Google-generated private key was encrypted using <i>notasecret</i> as a passphrase. Use the following command and record the location of the converted private key and record the location for use in the <code>service_account_private_key</code> of the <code>/etc/salt/cloud</code> file: </p>
<pre>
openssl pkcs12 -in ORIG.p12 -passin pass:notasecret \
-nodes -nocerts | openssl rsa -out NEW.pem
</pre>
</dl>
<p> <a NAME="lb[Q">&nbsp;<wbr></a></p>
<h3>Provider Configuration</h3>
<p> Set up the provider cloud config at <code>/etc/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/*.conf</code>: </p>
<pre>
gce-config:
  # Set up the Project name and Service Account authorization
  project: &quot;your-project-id&quot;
  service_account_email_address: &quot;123-a5gt [at] developer.gserviceaccount.com&quot;
  service_account_private_key: &quot;/path/to/your/NEW.pem&quot;
  # Set up the location of the salt master
  minion:
    master: saltmaster.example.com
  # Set up grains information, which will be common for all nodes
  # using this provider
  grains:
    node_type: broker
    release: 1.0.1
  provider: gce
</pre>
<p> <code>NOTE:</code> The value provided for <code>project</code> must not contain underscores or spaces and is labeled as &quot;Project ID&quot; on the Google Developers Console. <a NAME="lb[R">&nbsp;<wbr></a></p>
<h3>Profile Configuration</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or <code>/etc/salt/cloud.profiles.d/*.conf</code>: </p>
<p>my &#8211; gce &#8211; profile : image : centos &#8211; 6 size : n1 &#8211; standard &#8211; 1 location : europe &#8211; west1 &#8211; b network : default tags : &#8216;[&#8220;one&#8221;, &#8220;two&#8221;, &#8220;three&#8221;]&#8217; metadata : &#8216;{&#8220;one&#8221;: &#8220;1&#8221;, &#8220;2&#8221;: &#8220;two&#8221;}&#8217; use_persistent_disk : True delete_boot_pd : False deploy : True make_master : False provider : gce &#8211; config</p>
<p> The profile can be realized now with a salt command: </p>
<pre>
salt-cloud -p my-gce-profile gce-instance
</pre>
<p> This will create an salt minion instance named <code>gce-instance</code> in GCE. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Once the instance has been created with a salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
salt gce-instance test.ping
</pre>
<p> <a NAME="lb[S">&nbsp;<wbr></a></p>
<h3>GCE Specific Settings</h3>
<p> Consult the sample profile below for more information about GCE specific settings. Some of them are mandatory and are properly labeled below but typically also include a hard-coded default. <a NAME="lb[T">&nbsp;<wbr></a></p>
<h3>Initial Profile</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or <code>/etc/salt/cloud.profiles.d/gce.conf</code>: </p>
<p>my &#8211; gce &#8211; profile : image : centos &#8211; 6 size : n1 &#8211; standard &#8211; 1 location : europe &#8211; west1 &#8211; b network : default tags : &#8216;[&#8220;one&#8221;, &#8220;two&#8221;, &#8220;three&#8221;]&#8217; metadata : &#8216;{&#8220;one&#8221;: &#8220;1&#8221;, &#8220;2&#8221;: &#8220;two&#8221;}&#8217; use_persistent_disk : True delete_boot_pd : False ssh_interface : public_ips external_ip : &#8220;ephemeral&#8221;<br />
 <a NAME="lb[U">&nbsp;<wbr></a></p>
<h3>image</h3>
<p> Image is used to define what Operating System image should be used to for the instance. Examples are Debian 7 (wheezy) and CentOS 6. Required. <a NAME="lb[V">&nbsp;<wbr></a></p>
<h3>size</h3>
<p> A &#8216;size&#8217;, in GCE terms, refers to the instance&#8217;s &#8216;machine type&#8217;. See the on-line documentation for a complete list of GCE machine types. Required. <a NAME="lb[W">&nbsp;<wbr></a></p>
<h3>location</h3>
<p> A &#8216;location&#8217;, in GCE terms, refers to the instance&#8217;s &#8216;zone&#8217;. GCE has the notion of both Regions (e.g. us-central1, europe-west1, etc) and Zones (e.g. us-central1-a, us-central1-b, etc). Required. <a NAME="lb[X">&nbsp;<wbr></a></p>
<h3>network</h3>
<p> Use this setting to define the network resource for the instance. All GCE projects contain a network named &#8216;default&#8217; but it&#8217;s possible to use this setting to create instances belonging to a different network resource. <a NAME="lb[Y">&nbsp;<wbr></a></p>
<h3>tags</h3>
<p> GCE supports instance/network tags and this setting allows you to set custom tags. It should be a list of strings and must be parse-able by the python ast.literal_eval() function to convert it to a python list. <a NAME="lb[Z">&nbsp;<wbr></a></p>
<h3>metadata</h3>
<p> GCE supports instance metadata and this setting allows you to set custom metadata. It should be a hash of key/value strings and parse-able by the python ast.literal_eval() function to convert it to a python dictionary. <a NAME="lb\A">&nbsp;<wbr></a></p>
<h3>use_persistent_disk</h3>
<p> Use this setting to ensure that when new instances are created, they will use a persistent disk to preserve data between instance terminations and re-creations. <a NAME="lb\B">&nbsp;<wbr></a></p>
<h3>delete_boot_pd</h3>
<p> In the event that you wish the boot persistent disk to be permanently deleted when you destroy an instance, set delete_boot_pd to True. <a NAME="lb\C">&nbsp;<wbr></a></p>
<h3>ssh_interface</h3>
<p> New in version 2015.5.0. </p>
<p> Specify whether to use public or private IP for deploy script. </p>
<p> Valid options are:</p>
<dl>
<dt>&bull;</p>
<dd> private_ips: The salt-master is also hosted with GCE</p>
<dt>&bull;</p>
<dd> public_ips: The salt-master is hosted outside of GCE</dl>
<p> <a NAME="lb\D">&nbsp;<wbr></a></p>
<h3>external_ip</h3>
<p> Per instance setting: Used a named fixed IP address to this host. </p>
<p> Valid options are:</p>
<dl>
<dt>&bull;</p>
<dd> ephemeral: The host will use a GCE ephemeral IP</p>
<dt>&bull;</p>
<dd> None: No external IP will be configured on this host. </p>
<p> Optionally, pass the name of a GCE address to use a fixed IP address. If the address does not already exist, it will be created.</dl>
<p> <a NAME="lb\E">&nbsp;<wbr></a></p>
<h3>ex_disk_type</h3>
<p> GCE supports two different disk types, <code>pd-standard</code> and <code>pd-ssd</code>. The default disk type setting is <code>pd-standard</code>. To specify using an SSD disk, set <code>pd-ssd</code> as the value. </p>
<p> New in version 2014.7.0. </p>
<p> <a NAME="lb\F">&nbsp;<wbr></a></p>
<h3>SSH Remote Access</h3>
<p> GCE instances do not allow remote access to the root user by default. Instead, another user must be used to run the deploy script using sudo. Append something like this to <code>/etc/salt/cloud.profiles</code> or <code>/etc/salt/cloud.profiles.d/*.conf</code>: </p>
<pre>
my-gce-profile:
    ...
    # SSH to GCE instances as gceuser
    ssh_username: gceuser
    # Use the local private SSH key file located here
    ssh_keyfile: /etc/cloud/google_compute_engine
</pre>
<p> If you have not already used this SSH key to login to instances in this GCE project you will also need to add the public key to your projects metadata at <i><a rel="nofollow noopener" href="https://cloud.google.com/console" target="_blank">https://cloud.google.com/console</a></i>. You could also add it via the metadata setting too: </p>
<p>my &#8211; gce &#8211; profile : &#8230; metadata : &#8216;{&#8220;one&#8221;: &#8220;1&#8221;, &#8220;2&#8221;: &#8220;two&#8221;, &#8220;sshKeys&#8221; : &#8220;gceuser:ssh-rsa &lt;Your SSH Public Key&gt; gceuser [at] host&#8221;<br />
}<br />
&#8216;<br />
 <a NAME="lb\G">&nbsp;<wbr></a></p>
<h3>Single instance details</h3>
<p> This action is a thin wrapper around <code>&#8211;full-query</code>, which displays details on a single instance only. In an environment with several machines, this will save a user from having to sort through all instance data, just to examine a single instance. </p>
<pre>
salt-cloud -a show_instance myinstance
</pre>
<p> <a NAME="lb\H">&nbsp;<wbr></a></p>
<h3>Destroy, persistent disks, and metadata</h3>
<p> As noted in the provider configuration, it&#8217;s possible to force the boot persistent disk to be deleted when you destroy the instance. The way that this has been implemented is to use the instance metadata to record the cloud profile used when creating the instance. When <code>destroy</code> is called, if the instance contains a <code>salt-cloud-profile</code> key, it&#8217;s value is used to reference the matching profile to determine if <code>delete_boot_pd</code> is set to <code>True</code>. </p>
<p> Be aware that any GCE instances created with salt cloud will contain this custom <code>salt-cloud-profile</code> metadata entry. <a NAME="lb\I">&nbsp;<wbr></a></p>
<h3>List various resources</h3>
<p> It&#8217;s also possible to list several GCE resources similar to what can be done with other providers. The following commands can be used to list GCE zones (locations), machine types (sizes), and images. </p>
<pre>
salt-cloud --list-locations gce
salt-cloud --list-sizes gce
salt-cloud --list-images gce
</pre>
<p> <a NAME="lb\J">&nbsp;<wbr></a></p>
<h3>Persistent Disk</h3>
<p> The Compute Engine provider provides functions via salt-cloud to manage your Persistent Disks. You can create and destroy disks as well as attach and detach them from running instances. <a NAME="lb\K">&nbsp;<wbr></a></p>
<h3>Create</h3>
<p> When creating a disk, you can create an empty disk and specify its size (in GB), or specify either an &#8216;image&#8217; or &#8216;snapshot&#8217;. </p>
<pre>
salt-cloud -f create_disk gce disk_name=pd location=us-central1-b size=200
</pre>
<p> <a NAME="lb\L">&nbsp;<wbr></a></p>
<h3>Delete</h3>
<p> Deleting a disk only requires the name of the disk to delete </p>
<pre>
salt-cloud -f delete_disk gce disk_name=old-backup
</pre>
<p> <a NAME="lb\M">&nbsp;<wbr></a></p>
<h3>Attach</h3>
<p> Attaching a disk to an existing instance is really an &#8216;action&#8217; and requires both an instance name and disk name. It&#8217;s possible to use this ation to create bootable persistent disks if necessary. Compute Engine also supports attaching a persistent disk in READ_ONLY mode to multiple instances at the same time (but then cannot be attached in READ_WRITE to any instance). </p>
<pre>
salt-cloud -a attach_disk myinstance disk_name=pd mode=READ_WRITE boot=yes
</pre>
<p> <a NAME="lb\N">&nbsp;<wbr></a></p>
<h3>Detach</h3>
<p> Detaching a disk is also an action against an instance and only requires the name of the disk. Note that this does <i>not</i> safely sync and umount the disk from the instance. To ensure no data loss, you must first make sure the disk is unmounted from the instance. </p>
<pre>
salt-cloud -a detach_disk myinstance disk_name=pd
</pre>
<p> <a NAME="lb\O">&nbsp;<wbr></a></p>
<h3>Show disk</h3>
<p> It&#8217;s also possible to look up the details for an existing disk with either a function or an action. </p>
<pre>
salt-cloud -a show_disk myinstance disk_name=pd
salt-cloud -f show_disk gce disk_name=pd
</pre>
<p> <a NAME="lb\P">&nbsp;<wbr></a></p>
<h3>Create snapshot</h3>
<p> You can take a snapshot of an existing disk&#8217;s content. The snapshot can then in turn be used to create other persistent disks. Note that to prevent data corruption, it is strongly suggested that you unmount the disk prior to taking a snapshot. You must name the snapshot and provide the name of the disk. </p>
<pre>
salt-cloud -f create_snapshot gce name=backup-20140226 disk_name=pd
</pre>
<p> <a NAME="lb\Q">&nbsp;<wbr></a></p>
<h3>Delete snapshot</h3>
<p> You can delete a snapshot when it&#8217;s no longer needed by specifying the name of the snapshot. </p>
<pre>
salt-cloud -f delete_snapshot gce name=backup-20140226
</pre>
<p> <a NAME="lb\R">&nbsp;<wbr></a></p>
<h3>Show snapshot</h3>
<p> Use this function to look up information about the snapshot. </p>
<pre>
salt-cloud -f show_snapshot gce name=backup-20140226
</pre>
<p> <a NAME="lb\S">&nbsp;<wbr></a></p>
<h3>Networking</h3>
<p> Compute Engine supports multiple private networks per project. Instances within a private network can easily communicate with each other by an internal DNS service that resolves instance names. Instances within a private network can also communicate with either directly without needing special routing or firewall rules even if they span different regions/zones. </p>
<p> Networks also support custom firewall rules. By default, traffic between instances on the same private network is open to all ports and protocols. Inbound SSH traffic (port 22) is also allowed but all other inbound traffic is blocked. <a NAME="lb\T">&nbsp;<wbr></a></p>
<h3>Create network</h3>
<p> New networks require a name and CIDR range. New instances can be created and added to this network by setting the network name during create. It is not possible to add/remove existing instances to a network. </p>
<pre>
salt-cloud -f create_network gce name=mynet cidr=10.10.10.0/24
</pre>
<p> <a NAME="lb\U">&nbsp;<wbr></a></p>
<h3>Destroy network</h3>
<p> Destroy a network by specifying the name. Make sure that there are no instances associated with the network prior to deleting it or you&#8217;ll have a bad day. </p>
<pre>
salt-cloud -f delete_network gce name=mynet
</pre>
<p> <a NAME="lb\V">&nbsp;<wbr></a></p>
<h3>Show network</h3>
<p> Specify the network name to view information about the network. </p>
<pre>
salt-cloud -f show_network gce name=mynet
</pre>
<p> <a NAME="lb\W">&nbsp;<wbr></a></p>
<h3>Create address</h3>
<p> Create a new named static IP address in a region. </p>
<pre>
salt-cloud -f create_address gce name=my-fixed-ip region=us-central1
</pre>
<p> <a NAME="lb\X">&nbsp;<wbr></a></p>
<h3>Delete address</h3>
<p> Delete an existing named fixed IP address. </p>
<pre>
salt-cloud -f delete_address gce name=my-fixed-ip region=us-central1
</pre>
<p> <a NAME="lb\Y">&nbsp;<wbr></a></p>
<h3>Show address</h3>
<p> View details on a named address. </p>
<pre>
salt-cloud -f show_address gce name=my-fixed-ip region=us-central1
</pre>
<p> <a NAME="lb\Z">&nbsp;<wbr></a></p>
<h3>Create firewall</h3>
<p> You&#8217;ll need to create custom firewall rules if you want to allow other traffic than what is described above. For instance, if you run a web service on your instances, you&#8217;ll need to explicitly allow HTTP and/or SSL traffic. The firewall rule must have a name and it will use the &#8216;default&#8217; network unless otherwise specified with a &#8216;network&#8217; attribute. Firewalls also support instance tags for source/destination </p>
<pre>
salt-cloud -f create_fwrule gce name=web allow=tcp:80,tcp:443,icmp
</pre>
<p> <a NAME="lb]A">&nbsp;<wbr></a></p>
<h3>Delete firewall</h3>
<p> Deleting a firewall rule will prevent any previously allowed traffic for the named firewall rule. </p>
<pre>
salt-cloud -f delete_fwrule gce name=web
</pre>
<p> <a NAME="lb]B">&nbsp;<wbr></a></p>
<h3>Show firewall</h3>
<p> Use this function to review an existing firewall rule&#8217;s information. </p>
<pre>
salt-cloud -f show_fwrule gce name=web
</pre>
<p> <a NAME="lb]C">&nbsp;<wbr></a></p>
<h3>Load Balancer</h3>
<p> Compute Engine possess a load-balancer feature for splitting traffic across multiple instances. Please reference the <i>documentation</i> for a more complete discription. </p>
<p> The load-balancer functionality is slightly different than that described in Google&#8217;s documentation. The concept of <i>TargetPool</i> and <i>ForwardingRule</i> are consolidated in salt-cloud/libcloud. HTTP Health Checks are optional. <a NAME="lb]D">&nbsp;<wbr></a></p>
<h3>HTTP Health Check</h3>
<p> HTTP Health Checks can be used as a means to toggle load-balancing across instance members, or to detect if an HTTP site is functioning. A common use-case is to set up a health check URL and if you want to toggle traffic on/off to an instance, you can temporarily have it return a non-200 response. A non-200 response to the load-balancer&#8217;s health check will keep the LB from sending any new traffic to the &quot;down&quot; instance. Once the instance&#8217;s health check URL beings returning 200-responses, the LB will again start to send traffic to it. Review Compute Engine&#8217;s documentation for allowable parameters. You can use the following salt-cloud functions to manage your HTTP health checks. </p>
<pre>
salt-cloud -f create_hc gce name=myhc path=/ port=80
salt-cloud -f delete_hc gce name=myhc
salt-cloud -f show_hc gce name=myhc
</pre>
<p> <a NAME="lb]E">&nbsp;<wbr></a></p>
<h3>Load-balancer</h3>
<p> When creating a new load-balancer, it requires a name, region, port range, and list of members. There are other optional parameters for protocol, and list of health checks. Deleting or showing details about the LB only requires the name. </p>
<pre>
salt-cloud -f create_lb gce name=lb region=... ports=80 members=w1,w2,w3
salt-cloud -f delete_lb gce name=lb
salt-cloud -f show_lb gce name=lb
</pre>
<p> You can also create a load balancer using a named fixed IP addressby specifying the name of the address. If the address does not exist yet it will be created. </p>
<pre>
salt-cloud -f create_lb gce name=my-lb region=us-central1 ports=234 members=s1,s2,s3 address=my-lb-ip
</pre>
<p> <a NAME="lb]F">&nbsp;<wbr></a></p>
<h3>Attach and Detach LB</h3>
<p> It is possible to attach or detach an instance from an existing load-balancer. Both the instance and load-balancer must exist before using these functions. </p>
<pre>
salt-cloud -f attach_lb gce name=lb member=w4
salt-cloud -f detach_lb gce name=lb member=oops
</pre>
<p> <a NAME="lb]G">&nbsp;<wbr></a></p>
<h3>Getting Started With HP Cloud</h3>
<p> HP Cloud is a major public cloud platform and uses the libcloud <i>openstack</i> driver. The current version of OpenStack that HP Cloud uses is Havana. When an instance is booted, it must have a floating IP added to it in order to connect to it and further below you will see an example that adds context to this statement. <a NAME="lb]H">&nbsp;<wbr></a></p>
<h3>Set up a cloud provider configuration file</h3>
<p> To use the <i>openstack</i> driver for HP Cloud, set up the cloud provider configuration file as in the example shown below: </p>
<p> <code>/etc/salt/cloud.providers.d/hpcloud.conf</code>: </p>
<pre>
hpcloud-config:
  # Set the location of the salt-master
  #
  minion:
    master: saltmaster.example.com
  # Configure HP Cloud using the OpenStack plugin
  #
  identity_url: <a rel="nofollow noopener" href="https://region-b.geo-1.identity.hpcloudsvc.com:35357/v2.0/tokens" target="_blank">https://region-b.geo-1.identity.hpcloudsvc.com:35357/v2.0/tokens</a>
  compute_name: Compute
  protocol: ipv4
  # Set the compute region:
  #
  compute_region: region-b.geo-1
  # Configure HP Cloud authentication credentials
  #
  user: myname
  tenant: myname-project1
  password: xxxxxxxxx
  # keys to allow connection to the instance launched
  #
  ssh_key_name: yourkey
  ssh_key_file: /path/to/key/yourkey.priv
  provider: openstack
</pre>
<p> The subsequent example that follows is using the openstack driver. <a NAME="lb]I">&nbsp;<wbr></a></p>
<h3>Compute Region</h3>
<p> Originally, HP Cloud, in its OpenStack Essex version (1.0), had 3 availability zones in one region, US West (region-a.geo-1), which each behaved each as a region. </p>
<p> This has since changed, and the current OpenStack Havana version of HP Cloud (1.1) now has simplified this and now has two regions to choose from: </p>
<pre>
region-a.geo-1 -&gt; US West
region-b.geo-1 -&gt; US East
</pre>
<p> <a NAME="lb]J">&nbsp;<wbr></a></p>
<h3>Authentication</h3>
<p> The <code>user</code> is the same user as is used to log into the HP Cloud management UI. The <code>tenant</code> can be found in the upper left under &quot;Project/Region/Scope&quot;. It is often named the same as <code>user</code> albeit with a <code>-project1</code> appended. The <code>password</code> is of course what you created your account with. The management UI also has other information such as being able to select US East or US West. <a NAME="lb]K">&nbsp;<wbr></a></p>
<h3>Set up a cloud profile config file</h3>
<p> The profile shown below is a know working profile for an Ubuntu instance. The profile configuration file is stored in the following location: </p>
<p> <code>/etc/salt/cloud.profiles.d/hp_ae1_ubuntu.conf</code>: </p>
<pre>
hp_ae1_ubuntu:
    provider: hp_ae1
    image: 9302692b-b787-4b52-a3a6-daebb79cb498
    ignore_cidr: 10.0.0.1/24
    networks:
      - floating: Ext-Net
    size: standard.small
    ssh_key_file: /root/keys/test.key
    ssh_key_name: test
    ssh_username: ubuntu
</pre>
<p> Some important things about the example above:</p>
<dl>
<dt>&bull;</p>
<dd> The <code>image</code> parameter can use either the image name or image ID which you can obtain by running in the example below (this case US East): </p>
<pre>
# salt-cloud --list-images hp_ae1
</pre>
<dt>&bull;</p>
<dd> The parameter <code>ignore_cidr</code> specifies a range of addresses to ignore when trying to connect to the instance. In this case, it&#8217;s the range of IP addresses used for an private IP of the instance.</p>
<dt>&bull;</p>
<dd> The parameter <code>networks</code> is very important to include. In previous versions of Salt Cloud, this is what made it possible for salt-cloud to be able to attach a floating IP to the instance in order to connect to the instance and set up the minion. The current version of salt-cloud doesn&#8217;t require it, though having it is of no harm either. Newer versions of salt-cloud will use this, and without it, will attempt to find a list of floating IP addresses to use regardless.</p>
<dt>&bull;</p>
<dd> The <code>ssh_key_file</code> and <code>ssh_key_name</code> are the keys that will make it possible to connect to the instance to set up the minion</p>
<dt>&bull;</p>
<dd> The <code>ssh_username</code> parameter, in this case, being that the image used will be ubuntu, will make it possible to not only log in but install the minion</dl>
<p> <a NAME="lb]L">&nbsp;<wbr></a></p>
<h3>Launch an instance</h3>
<p> To instantiate a machine based on this profile (example): </p>
<pre>
# salt-cloud -p hp_ae1_ubuntu ubuntu_instance_1
</pre>
<p> After several minutes, this will create an instance named ubuntu_instance_1 running in HP Cloud in the US East region and will set up the minion and then return information about the instance once completed. <a NAME="lb]M">&nbsp;<wbr></a></p>
<h3>Manage the instance</h3>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
# salt ubuntu_instance_1 ping
</pre>
<p> <a NAME="lb]N">&nbsp;<wbr></a></p>
<h3>SSH to the instance</h3>
<p> Additionally, the instance can be accessed via SSH using the floating IP assigned to it </p>
<pre>
# ssh ubuntu@&lt;floating ip&gt;
</pre>
<p> <a NAME="lb]O">&nbsp;<wbr></a></p>
<h3>Using a private IP</h3>
<p> Alternatively, in the cloud profile, using the private IP to log into the instance to set up the minion is another option, particularly if salt-cloud is running within the cloud on an instance that is on the same network with all the other instances (minions) </p>
<p> The example below is a modified version of the previous example. Note the use of <code>ssh_interface</code>: </p>
<pre>
hp_ae1_ubuntu:
    provider: hp_ae1
    image: 9302692b-b787-4b52-a3a6-daebb79cb498
    size: standard.small
    ssh_key_file: /root/keys/test.key
    ssh_key_name: test
    ssh_username: ubuntu
    ssh_interface: private_ips
</pre>
<p> With this setup, salt-cloud will use the private IP address to ssh into the instance and set up the salt-minion <a NAME="lb]P">&nbsp;<wbr></a></p>
<h3>Getting Started With Joyent</h3>
<p> Joyent is a public cloud provider supporting SmartOS, Linux, FreeBSD, and Windows. <a NAME="lb]Q">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<p> This driver requires the Python <code>requests</code> library to be installed. <a NAME="lb]R">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<p> The Joyent cloud requires three configuration parameters. The user name and password that are used to log into the Joyent system, and the location of the private ssh key associated with the Joyent account. The ssh key is needed to send the provisioning commands up to the freshly created virtual machine. </p>
<pre>
# Note: This example is for /etc/salt/cloud.providers or any file in the
# /etc/salt/cloud.providers.d/ directory.
my-joyent-config:
    provider: joyent
    user: fred
    password: saltybacon
    private_key: /root/mykey.pem
    keyname: mykey
</pre>
<p> <a NAME="lb]S">&nbsp;<wbr></a></p>
<h3>Profiles</h3>
<p> <a NAME="lb]T">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d/</code> directory: </p>
<pre>
joyent_512
  provider: my-joyent-config
  size: Extra Small 512 MB
  image: Arch Linux 2013.06
</pre>
<p> Sizes can be obtained using the <code>&#8211;list-sizes</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; sizes my &#8211; joyent &#8211; config<br />
my &#8211; joyent &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;joyent : &#8212; &#8212; &#8212; &#8212; &#8211;Extra Small 512 MB : &#8212; &#8212; &#8212; &#8212; &#8211;default : false disk : 15360 id : Extra Small 512 MB memory : 512 name : Extra Small 512 MB swap : 1024 vcpus : 1 &#8230; SNIP&#8230;</p>
<p> Images can be obtained using the <code>&#8211;list-images</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; images my &#8211; joyent &#8211; config<br />
my-joyent-config:<br />
    &#8212;&#8212;&#8212;-<br />
    joyent:<br />
        &#8212;&#8212;&#8212;-<br />
        base:<br />
            &#8212;&#8212;&#8212;-<br />
            description:<br />
                A 32-bit SmartOS image with just essential packages<br />
                installed. Ideal for users who are comfortable with setting<br />
                up their own environment and tools.<br />
            disabled:<br />
                False<br />
            files:<br />
                &#8212;&#8212;&#8212;-<br />
                &#8211; compression:<br />
                    bzip2<br />
                &#8211; sha1:<br />
                    40cdc6457c237cf6306103c74b5f45f5bf2d9bbe<br />
                &#8211; size:<br />
                    82492182<br />
            name:<br />
                base<br />
            os:<br />
                smartos<br />
            owner:<br />
                352971aa-31ba-496c-9ade-a379feaecd52<br />
            public:<br />
                True<br />
&#8230;SNIP&#8230;<br />
 <a NAME="lb]U">&nbsp;<wbr></a></p>
<h3>SmartDataCenter</h3>
<p> This driver can also be used with the Joyent SmartDataCenter project. More details can be found at: </p>
<p> Using SDC requires that an api_host_suffix is set. The default value for this is <i>.api.joyentcloud.com</i>. All characters, including the leading <i>.</i>, should be included: </p>
<pre>
api_host_suffix: .api.myhostname.com
</pre>
<p> <a NAME="lb]V">&nbsp;<wbr></a></p>
<h3>Miscellaneous Configuration</h3>
<p> The following configuration items can be set in either <code>provider</code> or <code>profile</code> confuration files. <a NAME="lb]W">&nbsp;<wbr></a></p>
<h3>use_ssl</h3>
<p> When set to <code>True</code> (the default), attach <code>https://</code> to any URL that does not already have <code>http://</code> or <code>https://</code> included at the beginning. The best practice is to leave the protocol out of the URL, and use this setting to manage it. <a NAME="lb]X">&nbsp;<wbr></a></p>
<h3>verify_ssl</h3>
<p> When set to <code>True</code> (the default), the underlying web library will verify the SSL certificate. This should only be set to <code>False</code> for debugging.` <a NAME="lb]Y">&nbsp;<wbr></a></p>
<h3>Getting Started With LXC</h3>
<p> The LXC module is designed to install Salt in an LXC container on a controlled and possibly remote minion. </p>
<p> In other words, Salt will connect to a minion, then from that minion:</p>
<dl>
<dt>&bull;</p>
<dd> Provision and configure a container for networking access</p>
<dt>&bull;</p>
<dd> Use those modules to deploy salt and re-attach to master.</p>
<dt>&bull;</p>
<dd> <code>lxc runner</code></p>
<dt>&bull;</p>
<dd> <code>lxc module</code></p>
<dt>&bull;</p>
<dd> <code>seed</code></dl>
<p> <a NAME="lb]Z">&nbsp;<wbr></a></p>
<h3>Limitations</h3>
<dl>
<dt>&bull;</p>
<dd> You can only act on one minion and one provider at a time.</p>
<dt>&bull;</p>
<dd> Listing images must be targeted to a particular LXC provider (nothing will be outputted with <code>all</code>) </p>
<p> <code>WARNING:</code> On pre <code>2015.5.2</code>, you need to specify explitly the network bridge</dl>
<p> <a NAME="lb^A">&nbsp;<wbr></a></p>
<h3>Operation</h3>
<p> Salt&#8217;s LXC support does use <code>lxc.init</code> via the <code>lxc.cloud_init_interface</code> and seeds the minion via <code>seed.mkconfig</code>. </p>
<p> You can provide to those lxc VMs a profile and a network profile like if you were directly using the minion module. </p>
<p> Order of operation:</p>
<dl>
<dt>&bull;</p>
<dd> Create the LXC container on the desired minion (clone or template)</p>
<dt>&bull;</p>
<dd> Change LXC config options (if any need to be changed)</p>
<dt>&bull;</p>
<dd> Start container</p>
<dt>&bull;</p>
<dd> Change base passwords if any</p>
<dt>&bull;</p>
<dd> Change base DNS configuration if necessary</p>
<dt>&bull;</p>
<dd> Wait for LXC container to be up and ready for ssh</p>
<dt>&bull;</p>
<dd> Test SSH connection and bailout in error</p>
<dt>&bull;</p>
<dd> Upload deploy script and seeds, then re-attach the minion.</dl>
<p> <a NAME="lb^B">&nbsp;<wbr></a></p>
<h3>Provider configuration</h3>
<p> Here is a simple provider configuration: </p>
<pre>
# Note: This example goes in /etc/salt/cloud.providers or any file in the
# /etc/salt/cloud.providers.d/ directory.
devhost10-lxc:
  target: devhost10
  provider: lxc
</pre>
<p> <a NAME="lb^C">&nbsp;<wbr></a></p>
<h3>Profile configuration</h3>
<p> Please read tutorial-lxc before anything else. And specially tutorial-lxc-profiles. </p>
<p> Here are the options to configure your containers:</p>
<dl>
<dt><code>target</code></p>
<dd> Host minion id to install the lxc Container into</p>
<dt><code>lxc_profile</code></p>
<dd> Name of the profile or inline options for the LXC vm creation/cloning, please see tutorial-lxc-profiles-container.</p>
<dt><code>network_profile</code></p>
<dd> Name of the profile or inline options for the LXC vm network settings, please see tutorial-lxc-profiles-network.</p>
<dt><code>nic_opts</code></p>
<dd> Totally optionnal. Per interface new-style configuration options mappings which will override any profile default option: </p>
<pre>
eth0: {'mac': '00:16:3e:01:29:40',
              'gateway': None, (default)
              'link': 'br0', (default)
              'gateway': None, (default)
              'netmask': '', (default)
              'ip': '22.1.4.25'}}
</pre>
<dt><code>password</code></p>
<dd> password for root and sysadmin users</p>
<dt><code>dnsservers</code></p>
<dd> List of DNS servers to use. This is optional.</p>
<dt><code>minion</code></p>
<dd> minion configuration (see <code>Minion Configuration in Salt Cloud</code>)</p>
<dt><code>bootstrap_shell</code></p>
<dd> shell for bootstraping script (default: /bin/sh)</p>
<dt><code>script</code></p>
<dd> defaults to salt-boostrap</p>
<dt><code>script_args</code></p>
<dd> arguments which are given to the bootstrap script. the {0} placeholder will be replaced by the path which contains the minion config and key files, eg: </p>
<pre>
script_args=&quot;-c {0}&quot;
</pre>
<p> Using profiles: </p>
<pre>
# Note: This example would go in /etc/salt/cloud.profiles or any file in the
# /etc/salt/cloud.profiles.d/ directory.
devhost10-lxc:
  provider: devhost10-lxc
  lxc_profile: foo
  network_profile: bar
  minion:
    master: 10.5.0.1
    master_port: 4506
</pre>
<p> Using inline profiles (eg to override the network bridge): </p>
<pre>
devhost11-lxc:
  provider: devhost10-lxc
  lxc_profile:
    clone_from: foo
  network_profile:
    etho:
      link: lxcbr0
  minion:
    master: 10.5.0.1
    master_port: 4506
</pre>
<p> Template instead of a clone: </p>
<pre>
devhost11-lxc:
  provider: devhost10-lxc
  lxc_profile:
    template: ubuntu
  network_profile:
    etho:
      link: lxcbr0
  minion:
    master: 10.5.0.1
    master_port: 4506
</pre>
<p> Static ip: </p>
<pre>
# Note: This example would go in /etc/salt/cloud.profiles or any file in the
# /etc/salt/cloud.profiles.d/ directory.
devhost10-lxc:
  provider: devhost10-lxc
  nic_opts:
    eth0:
      ipv4: 10.0.3.9
  minion:
    master: 10.5.0.1
    master_port: 4506
</pre>
<p> DHCP: </p>
<pre>
# Note: This example would go in /etc/salt/cloud.profiles or any file in the
# /etc/salt/cloud.profiles.d/ directory.
devhost10-lxc:
  provider: devhost10-lxc
  minion:
    master: 10.5.0.1
    master_port: 4506
</pre>
</dl>
<p> <a NAME="lb^D">&nbsp;<wbr></a></p>
<h3>Driver Support</h3>
<dl>
<dt>&bull;</p>
<dd> Container creation</p>
<dt>&bull;</p>
<dd> Image listing (LXC templates)</p>
<dt>&bull;</p>
<dd> Running container information (IP addresses, etc.)</dl>
<p> <a NAME="lb^E">&nbsp;<wbr></a></p>
<h3>Getting Started With Linode</h3>
<p> Linode is a public cloud provider with a focus on Linux instances. <a NAME="lb^F">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> linode-python &gt;= 1.1.1 </p>
<p> OR</p>
<dt>&bull;</p>
<dd> Libcloud &gt;= 0.13.2 </p>
<p> This driver supports accessing Linode via linode-python or Apache Libcloud. Linode-python is recommended, it is more full-featured than Libcloud. In particular using linode-python enables stopping, starting, and cloning machines. </p>
<p> Driver selection is automatic. If linode-python is present it will be used. If it is absent, salt-cloud will fall back to Libcloud. If neither are present salt-cloud will abort. </p>
<p> NOTE: linode-python 1.1.1 or later is recommended. Earlier versions of linode-python should work but leak sensitive information into the debug logs. </p>
<p> Linode-python can be downloaded from <i><a rel="nofollow noopener" href="https://github.com/tjfontaine/linode-python" target="_blank">https://github.com/tjfontaine/linode-python</a></i> or installed via pip.</dl>
<p> <a NAME="lb^G">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<p> Linode requires a single API key, but the default root password for new instances also needs to be set: </p>
<p>#Note : This example is for / etc / salt / cloud.providers or any file in the<br />
#/ etc / salt / cloud.providers.d / directory.<br />
my &#8211; linode &#8211; config : apikey : asldkgfakl;<br />
sdfjsjaslfjaklsdjf;<br />
askldjfaaklsjdfhasldsadfghdkf<br />
        password : F00barbaz<br />
                       ssh_pubkey : ssh &#8211;<br />
                                    ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKHEOLLbeXgaqRQT9NBAopVz366SdYc0KKX33vAnq + 2R user[at] host ssh_key_file : ~ /.ssh / id_ed25519 provider : linode</p>
<p> The password needs to be 8 characters and contain lowercase, uppercase, and numbers. <a NAME="lb^H">&nbsp;<wbr></a></p>
<h3>Profiles</h3>
<p> <a NAME="lb^I">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d/</code> directory: </p>
<pre>
linode_1024:
  provider: my-linode-config
  size: Linode 1024
  image: Arch Linux 2013.06
  location: london
</pre>
<p> Sizes can be obtained using the <code>&#8211;list-sizes</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; sizes my &#8211; linode &#8211; config<br />
my &#8211; linode &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;linode : &#8212; &#8212; &#8212; &#8212; &#8211;Linode 1024 : &#8212; &#8212; &#8212; &#8212; &#8211;bandwidth : 2000 disk : 49152 driver : get_uuid : id : 1 name : Linode 1024 price : 20.0 ram : 1024 uuid : 03e18728ce4629e2ac07c9cbb48afffb8cb499c4 &#8230; SNIP&#8230;</p>
<p> Images can be obtained using the <code>&#8211;list-images</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; images my &#8211; linode &#8211; config<br />
my &#8211; linode &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;linode : &#8212; &#8212; &#8212; &#8212; &#8211;Arch Linux 2013.06 : &#8212; &#8212; &#8212; &#8212; &#8211;driver : extra : &#8212; &#8212; &#8212; &#8212; &#8211;64bit : 1 pvops : 1 get_uuid : id : 112 name : Arch Linux 2013.06 uuid : 8457f92eaffc92b7666b6734a96ad7abe1a8a6dd &#8230; SNIP&#8230;</p>
<p> Locations can be obtained using the <code>&#8211;list-locations</code> option for the <code>salt-cloud</code> command: </p>
<p>#salt &#8211; cloud&#8211; list &#8211; locations my &#8211; linode &#8211; config<br />
my &#8211; linode &#8211; config : &#8212; &#8212; &#8212; &#8212; &#8211;linode : &#8212; &#8212; &#8212; &#8212; &#8211;Atlanta, GA, USA : &#8212; &#8212; &#8212; &#8212; &#8211;abbreviation : atlanta id : 4 Dallas, TX, USA : &#8212; &#8212; &#8212; &#8212; &#8211;abbreviation : dallas id : 2 &#8230; SNIP&#8230;<br />
 <a NAME="lb^J">&nbsp;<wbr></a></p>
<h3>Cloning</h3>
<p> When salt-cloud accesses Linode via linode-python it can clone machines. </p>
<p> It is safest to clone a stopped machine. To stop a machine run </p>
<pre>
salt-cloud -a stop machine_to_clone
</pre>
<p> To create a new machine based on another machine, add an entry to your linode cloud profile that looks like this: </p>
<pre>
li-clone:
  provider: linode
  clonefrom: machine_to_clone
  script_args: -C
</pre>
<p> Then run salt-cloud as normal, specifying <i>-p li-clone</i>. The profile name can be anything&#8211;it doesn&#8217;t have to be <i>li-clone</i>. </p>
<p> <i>Clonefrom:</i> is the name of an existing machine in Linode from which to clone. <i>Script_args: -C</i> is necessary to avoid re-deploying Salt via salt-bootstrap. <i>-C</i> will just re-deploy keys so the new minion will not have a duplicate key or minion_id on the master. <a NAME="lb^K">&nbsp;<wbr></a></p>
<h3>Getting Started With OpenStack</h3>
<p> OpenStack is one the most popular cloud projects. It&#8217;s an open source project to build public and/or private clouds. You can use Salt Cloud to launch OpenStack instances. <a NAME="lb^L">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> Libcloud &gt;= 0.13.2</dl>
<p> <a NAME="lb^M">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<dl>
<dt>&bull;</p>
<dd> Using the new format, set up the cloud configuration at <code>/etc/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/openstack.conf</code>: </p>
<pre>
my-openstack-config:
  # Set the location of the salt-master
  #
  minion:
    master: saltmaster.example.com
  # Configure the OpenStack driver
  #
  identity_url: <a rel="nofollow noopener" href="http://identity.youopenstack.com/v2.0/tokens" target="_blank">http://identity.youopenstack.com/v2.0/tokens</a>
  compute_name: nova
  protocol: ipv4
  compute_region: RegionOne
  # Configure Openstack authentication credentials
  #
  user: myname
  password: 123456
  # tenant is the project name
  tenant: myproject
  provider: openstack
  # skip SSL certificate validation (default false)
  insecure: false
</pre>
</dl>
<p> <a NAME="lb^N">&nbsp;<wbr></a></p>
<h3>Using nova client to get information from OpenStack</h3>
<p> One of the best ways to get information about OpenStack is using the novaclient python package (available in pypi as python-novaclient). The client configuration is a set of environment variables that you can get from the Dashboard. Log in and then go to Project -&gt; Access &amp; security -&gt; API Access and download the &quot;OpenStack RC file&quot;. Then: </p>
<pre>
source /path/to/your/rcfile
nova credentials
nova endpoints
</pre>
<p> In the <code>nova endpoints</code> output you can see the information about <code>compute_region</code> and <code>compute_name</code>. <a NAME="lb^O">&nbsp;<wbr></a></p>
<h3>Compute Region</h3>
<p> It depends on the OpenStack cluster that you are using. Please, have a look at the previous sections. <a NAME="lb^P">&nbsp;<wbr></a></p>
<h3>Authentication</h3>
<p> The <code>user</code> and <code>password</code> is the same user as is used to log into the OpenStack Dashboard. <a NAME="lb^Q">&nbsp;<wbr></a></p>
<h3>Profiles</h3>
<p> Here is an example of a profile: </p>
<pre>
openstack_512:
  provider: my-openstack-config
  size: m1.tiny
  image: cirros-0.3.1-x86_64-uec
  ssh_key_file: /tmp/test.pem
  ssh_key_name: test
  ssh_interface: private_ips
</pre>
<p> The following list explains some of the important properties.</p>
<dl>
<dt><code>size</code></p>
<dd> can be one of the options listed in the output of <code>nova flavor-list</code>.</p>
<dt><code>image</code></p>
<dd> can be one of the options listed in the output of <code>nova image-list</code>.</p>
<dt><code>ssh_key_file</code></p>
<dd> The SSH private key that the salt-cloud uses to SSH into the VM after its first booted in order to execute a command or script. This private key&#8217;s <i>public key</i> must be the openstack public key inserted into the authorized_key&#8217;s file of the VM&#8217;s root user account.</p>
<dt><code>ssh_key_name</code></p>
<dd> The name of the openstack SSH public key that is inserted into the authorized_keys file of the VM&#8217;s root user account. Prior to using this public key, you must use openstack commands or the horizon web UI to load that key into the tenant&#8217;s account. Note that this openstack tenant must be the one you defined in the cloud provider.</p>
<dt><code>ssh_interface</code></p>
<dd> This option allows you to create a VM without a public IP. If this option is omitted and the VM does not have a public IP, then the salt-cloud waits for a certain period of time and then destroys the VM. </p>
<p> For more information concerning cloud profiles, see <code>here</code>.</dl>
<p> <a NAME="lb^R">&nbsp;<wbr></a></p>
<h3>change_password</h3>
<p> If no ssh_key_file is provided, and the server already exists, change_password will use the api to change the root password of the server so that it can be bootstrapped. </p>
<pre>
change_password: True
</pre>
<p> <a NAME="lb^S">&nbsp;<wbr></a></p>
<h3>userdata_file</h3>
<p> Use <i>userdata_file</i> to specify the userdata file to upload for use with cloud-init if available. </p>
<pre>
userdata_file: /etc/salt/cloud-init/packages.yml
</pre>
<p> <a NAME="lb^T">&nbsp;<wbr></a></p>
<h3>Getting Started With Parallels</h3>
<p> Parallels Cloud Server is a product by Parallels that delivers a cloud hosting solution. The PARALLELS module for Salt Cloud enables you to manage instances hosted by a provider using PCS. Further information can be found at: </p>
<p> <i><a rel="nofollow noopener" href="http://www.parallels.com/products/pcs/" target="_blank">http://www.parallels.com/products/pcs/</a></i></p>
<dl>
<dt>&bull;</p>
<dd> Using the old format, set up the cloud configuration at <code>/etc/salt/cloud</code>: </p>
<pre>
# Set up the location of the salt master
#
minion:
    master: saltmaster.example.com
# Set the PARALLELS access credentials (see below)
#
PARALLELS.user: myuser
PARALLELS.password: badpass
# Set the access URL for your PARALLELS provider
#
PARALLELS.url: <a rel="nofollow noopener" href="https://api.cloud.xmission.com:4465/paci/v1.0/" target="_blank">https://api.cloud.xmission.com:4465/paci/v1.0/</a>
</pre>
<dt>&bull;</p>
<dd> Using the new format, set up the cloud configuration at <code>/etc/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/parallels.conf</code>: </p>
<pre>
my-parallels-config:
  # Set up the location of the salt master
  #
  minion:
    master: saltmaster.example.com
  # Set the PARALLELS access credentials (see below)
  #
  user: myuser
  password: badpass
  # Set the access URL for your PARALLELS provider
  #
  url: <a rel="nofollow noopener" href="https://api.cloud.xmission.com:4465/paci/v1.0/" target="_blank">https://api.cloud.xmission.com:4465/paci/v1.0/</a>
  provider: parallels
</pre>
</dl>
<p> <a NAME="lb^U">&nbsp;<wbr></a></p>
<h3>Access Credentials</h3>
<p> The <code>user</code>, <code>password</code>, and <code>url</code> will be provided to you by your cloud provider. These are all required in order for the PARALLELS driver to work. <a NAME="lb^V">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or <code>/etc/salt/cloud.profiles.d/parallels.conf</code>:</p>
<dl>
<dt>&bull;</p>
<dd> Using the old cloud configuration format: </p>
<pre>
parallels-ubuntu:
    provider: parallels
    image: ubuntu-12.04-x86_64
</pre>
<dt>&bull;</p>
<dd> Using the new cloud configuration format and the cloud configuration example from above: </p>
<pre>
parallels-ubuntu:
    provider: my-parallels-config
    image: ubuntu-12.04-x86_64
</pre>
<p> The profile can be realized now with a salt command: </p>
<pre>
# salt-cloud -p parallels-ubuntu myubuntu
</pre>
<p> This will create an instance named <code>myubuntu</code> on the cloud provider. The minion that is installed on this instance will have an <code>id</code> of <code>myubuntu</code>. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
# salt myubuntu test.ping
</pre>
</dl>
<p> <a NAME="lb^W">&nbsp;<wbr></a></p>
<h3>Required Settings</h3>
<p> The following settings are always required for PARALLELS:</p>
<dl>
<dt>&bull;</p>
<dd> Using the old cloud configuration format: </p>
<pre>
PARALLELS.user: myuser
PARALLELS.password: badpass
PARALLELS.url: <a rel="nofollow noopener" href="https://api.cloud.xmission.com:4465/paci/v1.0/" target="_blank">https://api.cloud.xmission.com:4465/paci/v1.0/</a>
</pre>
<dt>&bull;</p>
<dd> Using the new cloud configuration format: </p>
<pre>
my-parallels-config:
  user: myuser
  password: badpass
  url: <a rel="nofollow noopener" href="https://api.cloud.xmission.com:4465/paci/v1.0/" target="_blank">https://api.cloud.xmission.com:4465/paci/v1.0/</a>
  provider: parallels
</pre>
</dl>
<p> <a NAME="lb^X">&nbsp;<wbr></a></p>
<h3>Optional Settings</h3>
<p> Unlike other cloud providers in Salt Cloud, Parallels does not utilize a <code>size</code> setting. This is because Parallels allows the end-user to specify a more detailed configuration for their instances, than is allowed by many other cloud providers. The following options are available to be used in a profile, with their default settings listed. </p>
<pre>
# Description of the instance. Defaults to the instance name.
desc: &lt;instance_name&gt;
# How many CPU cores, and how fast they are (in MHz)
cpu_number: 1
cpu_power: 1000
# How many megabytes of RAM
ram: 256
# Bandwidth available, in kbps
bandwidth: 100
# How many public IPs will be assigned to this instance
ip_num: 1
# Size of the instance disk (in GiB)
disk_size: 10
# Username and password
ssh_username: root
password: &lt;value from PARALLELS.password&gt;
# The name of the image, from ``salt-cloud --list-images parallels``
image: ubuntu-12.04-x86_64
</pre>
<p> <a NAME="lb^Y">&nbsp;<wbr></a></p>
<h3>Getting Started With Proxmox</h3>
<p> Proxmox Virtual Environment is a complete server virtualization management solution, based on KVM virtualization and OpenVZ containers. Further information can be found at: </p>
<p> <i><a rel="nofollow noopener" href="http://www.proxmox.org/" target="_blank">http://www.proxmox.org/</a></i> <a NAME="lb^Z">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> IPy &gt;= 0.81</p>
<dt>&bull;</p>
<dd> requests &gt;= 2.2.1 </p>
<p> Please note: This module allows you to create both OpenVZ and KVM but installing Salt on it will only be done when the VM is an OpenVZ container rather than a KVM virtual machine.</p>
<dt>&bull;</p>
<dd> Set up the cloud configuration at <code>/etc/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/proxmox.conf</code>: </p>
<pre>
my-proxmox-config:
  # Set up the location of the salt master
  #
  minion:
    master: saltmaster.example.com
  # Set the PROXMOX access credentials (see below)
  #
  user: myuser@pve
  password: badpass
  # Set the access URL for your PROXMOX provider
  #
  url: your.proxmox.host
  provider: proxmox
</pre>
</dl>
<p> <a NAME="lb_A">&nbsp;<wbr></a></p>
<h3>Access Credentials</h3>
<p> The <code>user</code>, <code>password</code>, and <code>url</code> will be provided to you by your cloud provider. These are all required in order for the PROXMOX driver to work. <a NAME="lb_B">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or <code>/etc/salt/cloud.profiles.d/proxmox.conf</code>:</p>
<dl>
<dt>&bull;</p>
<dd> Configure a profile to be used: </p>
<pre>
proxmox-ubuntu:
    provider: proxmox
    image: local:vztmpl/ubuntu-12.04-standard_12.04-1_amd64.tar.gz
    technology: openvz
    host: myvmhost
    ip_address: 192.168.100.155
    password: topsecret
</pre>
<p> The profile can be realized now with a salt command: </p>
<pre>
# salt-cloud -p proxmox-ubuntu myubuntu
</pre>
<p> This will create an instance named <code>myubuntu</code> on the cloud provider. The minion that is installed on this instance will have a <code>hostname</code> of <code>myubuntu</code>. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
# salt myubuntu test.ping
</pre>
</dl>
<p> <a NAME="lb_C">&nbsp;<wbr></a></p>
<h3>Required Settings</h3>
<p> The following settings are always required for PROXMOX:</p>
<dl>
<dt>&bull;</p>
<dd> Using the new cloud configuration format: </p>
<pre>
my-proxmox-config:
  provider: proxmox
  user: saltcloud@pve
  password: xyzzy
  url: your.proxmox.host
</pre>
</dl>
<p> <a NAME="lb_D">&nbsp;<wbr></a></p>
<h3>Optional Settings</h3>
<p> Unlike other cloud providers in Salt Cloud, Proxmox does not utilize a <code>size</code> setting. This is because Proxmox allows the end-user to specify a more detailed configuration for their instances, than is allowed by many other cloud providers. The following options are available to be used in a profile, with their default settings listed. </p>
<pre>
# Description of the instance.
desc: &lt;instance_name&gt;
# How many CPU cores, and how fast they are (in MHz)
cpus: 1
cpuunits: 1000
# How many megabytes of RAM
memory: 256
# How much swap space in MB
swap: 256
# Whether to auto boot the vm after the host reboots
onboot: 1
# Size of the instance disk (in GiB)
disk: 10
# Host to create this vm on
host: myvmhost
# Nameservers. Defaults to host
nameserver: 8.8.8.8 8.8.4.4
# Username and password
ssh_username: root
password: &lt;value from PROXMOX.password&gt;
# The name of the image, from ``salt-cloud --list-images proxmox``
image: local:vztmpl/ubuntu-12.04-standard_12.04-1_amd64.tar.gz
</pre>
<p> <a NAME="lb_E">&nbsp;<wbr></a></p>
<h3>Getting Started With Rackspace</h3>
<p> Rackspace is a major public cloud platform which may be configured using either the <i>rackspace</i> or the <i>openstack</i> driver, depending on your needs. </p>
<p> Please note that the <i>rackspace</i> driver is only intended for 1st gen instances, aka, &quot;the old cloud&quot; at Rackspace. It is required for 1st gen instances, but will <i>not</i> work with OpenStack-based instances. Unless you explicitly have a reason to use it, it is highly recommended that you use the <i>openstack</i> driver instead. <a NAME="lb_F">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<dl>
<dt>&bull;</p>
<dd> Libcloud &gt;= 0.13.2</dl>
<p> <a NAME="lb_G">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<dl>
<dt><code>To use the </code><i>openstack</i> driver (recommended), set up the cloud configuration at</p>
<dd> <code>/etc/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/rackspace.conf</code>: </p>
<pre>
my-rackspace-config:
  # Set the location of the salt-master
  #
  minion:
    master: saltmaster.example.com
  # Configure Rackspace using the OpenStack plugin
  #
  identity_url: '<a rel="nofollow noopener" href="https://identity.api.rackspacecloud.com/v2.0/tokens&#039;" target="_blank">https://identity.api.rackspacecloud.com/v2.0/tokens'</a>
  compute_name: cloudServersOpenStack
  protocol: ipv4
  # Set the compute region:
  #
  compute_region: DFW
  # Configure Rackspace authentication credentials
  #
  user: myname
  tenant: 123456
  apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  provider: openstack
</pre>
<dt><code>To use the </code><i>rackspace</i> driver, set up the cloud configuration at</p>
<dd> <code>/etc/salt/cloud.providers</code> or <code>/etc/salt/cloud.providers.d/rackspace.conf</code>: </p>
<pre>
my-rackspace-config:
  provider: rackspace
  # The Rackspace login user
  user: fred
  # The Rackspace user's apikey
  apikey: 901d3f579h23c8v73q9
</pre>
<p> The settings that follow are for using Rackspace with the <i>openstack</i> driver, and will not work with the <i>rackspace</i> driver.</dl>
<p> <a NAME="lb_H">&nbsp;<wbr></a></p>
<h3>Compute Region</h3>
<p> Rackspace currently has six compute regions which may be used: </p>
<p>DFW-&gt;Dallas / Forth Worth<br />
                  ORD-&gt;Chicago<br />
                      SYD-&gt;Sydney<br />
                          LON-&gt;London<br />
                              IAD-&gt;Northern Virginia<br />
                                  HKG-&gt;Hong Kong</p>
<p> Note: Currently the LON region is only available with a UK account, and UK accounts cannot access other regions <a NAME="lb_I">&nbsp;<wbr></a></p>
<h3>Authentication</h3>
<p> The <code>user</code> is the same user as is used to log into the Rackspace Control Panel. The <code>tenant</code> and <code>apikey</code> can be found in the API Keys area of the Control Panel. The <code>apikey</code> will be labeled as API Key (and may need to be generated), and <code>tenant</code> will be labeled as Cloud Account Number. </p>
<p> An initial profile can be configured in <code>/etc/salt/cloud.profiles</code> or <code>/etc/salt/cloud.profiles.d/rackspace.conf</code>: </p>
<pre>
openstack_512:
    provider: my-rackspace-config
    size: 512 MB Standard
    image: Ubuntu 12.04 LTS (Precise Pangolin)
</pre>
<p> To instantiate a machine based on this profile: </p>
<pre>
# salt-cloud -p openstack_512 myinstance
</pre>
<p> This will create a virtual machine at Rackspace with the name <code>myinstance</code>. This operation may take several minutes to complete, depending on the current load at the Rackspace data center. </p>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
# salt myinstance test.ping
</pre>
<p> <a NAME="lb_J">&nbsp;<wbr></a></p>
<h3>RackConnect Environments</h3>
<p> Rackspace offers a hybrid hosting configuration option called RackConnect that allows you to use a physical firewall appliance with your cloud servers. When this service is in use the public_ip assigned by nova will be replaced by a NAT ip on the firewall. For salt-cloud to work properly it must use the newly assigned &quot;access ip&quot; instead of the Nova assigned public ip. You can enable that capability by adding this to your profiles: </p>
<pre>
openstack_512:
    provider: my-openstack-config
    size: 512 MB Standard
    image: Ubuntu 12.04 LTS (Precise Pangolin)
    rackconnect: True
</pre>
<p> <a NAME="lb_K">&nbsp;<wbr></a></p>
<h3>Managed Cloud Environments</h3>
<p> Rackspace offers a managed service level of hosting. As part of the managed service level you have the ability to choose from base of lamp installations on cloud server images. The post build process for both the base and the lamp installations used Chef to install things such as the cloud monitoring agent and the cloud backup agent. It also takes care of installing the lamp stack if selected. In order to prevent the post installation process from stomping over the bootstrapping you can add the below to your profiles. </p>
<pre>
openstack_512:
    provider: my-rackspace-config
    size: 512 MB Standard
    image: Ubuntu 12.04 LTS (Precise Pangolin)
    managedcloud: True
</pre>
<p> <a NAME="lb_L">&nbsp;<wbr></a></p>
<h3>First and Next Generation Images</h3>
<p> Rackspace provides two sets of virtual machine images, <i>first</i>, and <i>next</i> generation. As of <code>0.8.9</code> salt-cloud will default to using the <i>next</i> generation images. To force the use of first generation images, on the profile configuration please add: </p>
<pre>
FreeBSD-9.0-512:
  provider: my-rackspace-config
  size: 512 MB Standard
  image: FreeBSD 9.0
  force_first_gen: True
</pre>
<p> <a NAME="lb_M">&nbsp;<wbr></a></p>
<h3>Private Subnets</h3>
<p> By default salt-cloud will not add Rackspace private networks to new servers. To enable a private network to a server instantiated by salt cloud, add the following section to the provider file (typically <code>/etc/salt/cloud.providers.d/rackspace.conf</code>) </p>
<pre>
networks:
  - fixed:
    # This is the private network
    - private-network-id
    # This is Rackspace's &quot;PublicNet&quot;
    - 00000000-0000-0000-0000-000000000000
    # This is Rackspace's &quot;ServiceNet&quot;
    - 11111111-1111-1111-1111-111111111111
</pre>
<p> To get the Rackspace private network ID, go to Networking, Networks and hover over the private network name. </p>
<p> The order of the networks in the above code block does not map to the order of the ethernet devices on newly created servers. Public IP will always be first ( eth0 ) followed by servicenet ( eth1 ) and then private networks. </p>
<p> Enabling the private network per above gives the option of using the private subnet for all master-minion communication, including the bootstrap install of salt-minion. To enable the minion to use the private subnet, update the master: line in the minion: section of the providers file. To configure the master to only listen on the private subnet IP, update the interface: line in the /etc/salt/master file to be the private subnet IP of the salt master. <a NAME="lb_N">&nbsp;<wbr></a></p>
<h3>Getting Started With Saltify</h3>
<p> The Saltify driver is a new, experimental driver for installing Salt on existing machines (virtual or bare metal). <a NAME="lb_O">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<p> The Saltify driver has no external dependencies. <a NAME="lb_P">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<p> Because the Saltify driver does not use an actual cloud provider host, it has a simple provider configuration. The only thing that is required to be set is the driver name, and any other potentially useful information, like the location of the salt-master: </p>
<pre>
# Note: This example is for /etc/salt/cloud.providers file or any file in
# the /etc/salt/cloud.providers.d/ directory.
my-saltify-config:
  minion:
    master: 111.222.333.444
  provider: saltify
</pre>
<p> <a NAME="lb_Q">&nbsp;<wbr></a></p>
<h3>Profiles</h3>
<p> Saltify requires a profile to be configured for each machine that needs Salt installed. The initial profile can be set up at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d/</code> directory. Each profile requires both an <code>ssh_host</code> and an <code>ssh_username</code> key parameter as well as either an <code>key_filename</code> or a <code>password</code>. </p>
<p> Profile configuration example: </p>
<pre>
# /etc/salt/cloud.profiles.d/saltify.conf
salt-this-machine:
  ssh_host: 12.34.56.78
  ssh_username: root
  key_filename: '/etc/salt/mysshkey.pem'
  provider: my-saltify-config
</pre>
<p> The machine can now be &quot;Salted&quot; with the following command: </p>
<pre>
salt-cloud -p salt-this-machine my-machine
</pre>
<p> This will install salt on the machine specified by the cloud profile, <code>salt-this-machine</code>, and will give the machine the minion id of <code>my-machine</code>. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Once a salt-minion has been successfully installed on the instance, connectivity to it can be verified with Salt: </p>
<pre>
salt my-machine test.ping
</pre>
<p> <a NAME="lb_R">&nbsp;<wbr></a></p>
<h3>Using Map Files</h3>
<p> The settings explained in the section above may also be set in a map file. An example of how to use the Saltify driver with a map file follows: </p>
<pre>
# /etc/salt/saltify-map
make_salty:
  - my-instance-0:
      ssh_host: 12.34.56.78
      ssh_username: root
      password: very-bad-password
  - my-instance-1:
      ssh_host: 44.33.22.11
      ssh_username: root
      password: another-bad-pass
</pre>
<p> Note: When using a cloud map with the Saltify driver, the name of the profile to use, in this case <code>make_salty</code>, must be defined in a profile config. For example: </p>
<pre>
# /etc/salt/cloud.profiles.d/saltify.conf
make_salty:
  provider: my-saltify-config
</pre>
<p> The machines listed in the map file can now be &quot;Salted&quot; by applying the following salt map command: </p>
<pre>
salt-cloud -m /etc/salt/saltify-map
</pre>
<p> This command will install salt on the machines specified in the map and will give each machine their minion id of <code>my-instance-0</code> and <code>my-instance-1</code>, respectively. If the command was executed on the salt-master, its Salt key will automatically be signed on the master. </p>
<p> Connectivity to the new &quot;Salted&quot; instances can now be verified with Salt: </p>
<pre>
salt 'my-instance-*' test.ping
</pre>
<p> <a NAME="lb_S">&nbsp;<wbr></a></p>
<h3>Getting Started With SoftLayer</h3>
<p> SoftLayer is a public cloud provider, and baremetal hardware hosting provider. <a NAME="lb_T">&nbsp;<wbr></a></p>
<h3>Dependencies</h3>
<p> The SoftLayer driver for Salt Cloud requires the softlayer package, which is available at PyPI: </p>
<p> <i><a rel="nofollow noopener" href="https://pypi.python.org/pypi/SoftLayer" target="_blank">https://pypi.python.org/pypi/SoftLayer</a></i> </p>
<p> This package can be installed using <code>pip</code> or <code>easy_install</code>: </p>
<pre>
# pip install softlayer
# easy_install softlayer
</pre>
<p> <a NAME="lb_U">&nbsp;<wbr></a></p>
<h3>Configuration</h3>
<p> Set up the cloud config at <code>/etc/salt/cloud.providers</code>: </p>
<pre>
# Note: These examples are for /etc/salt/cloud.providers
  my-softlayer:
    # Set up the location of the salt master
    minion:
      master: saltmaster.example.com
    # Set the SoftLayer access credentials (see below)
    user: MYUSER1138
    apikey: 'e3b68aa711e6deadc62d5b76355674beef7cc3116062ddbacafe5f7e465bfdc9'
    provider: softlayer
  my-softlayer-hw:
    # Set up the location of the salt master
    minion:
      master: saltmaster.example.com
    # Set the SoftLayer access credentials (see below)
    user: MYUSER1138
    apikey: 'e3b68aa711e6deadc62d5b76355674beef7cc3116062ddbacafe5f7e465bfdc9'
    provider: softlayer_hw
</pre>
<p> <a NAME="lb_V">&nbsp;<wbr></a></p>
<h3>Access Credentials</h3>
<p> The <code>user</code> setting is the same user as is used to log into the SoftLayer Administration area. The <code>apikey</code> setting is found inside the Admin area after logging in:</p>
<dl>
<dt>&bull;</p>
<dd> Hover over the <code>Account</code> menu item.</p>
<dt>&bull;</p>
<dd> Click the <code>Users</code> link.</p>
<dt>&bull;</p>
<dd> Find the <code>API Key</code> column and click <code>View</code>.</dl>
<p> <a NAME="lb_W">&nbsp;<wbr></a></p>
<h3>Profiles</h3>
<p> <a NAME="lb_X">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code>: </p>
<pre>
base_softlayer_ubuntu:
  provider: my-softlayer
  image: UBUNTU_LATEST
  cpu_number: 1
  ram: 1024
  disk_size: 100
  local_disk: True
  hourly_billing: True
  domain: example.com
  location: sjc01
  # Optional
  max_net_speed: 1000
  private_vlan: 396
  private_network: True
  private_ssh: True
  # May be used _instead_of_ image
  global_identifier: 320d8be5-46c0-dead-cafe-13e3c51
</pre>
<p> Most of the above items are required; optional items are specified below. <a NAME="lb_Y">&nbsp;<wbr></a></p>
<h3>image</h3>
<p> Images to build an instance can be found using the <code>&#8211;list-images</code> option: </p>
<pre>
# salt-cloud --list-images my-softlayer
</pre>
<p> The setting used will be labeled as <code>template</code>. <a NAME="lb_Z">&nbsp;<wbr></a></p>
<h3>cpu_number</h3>
<p> This is the number of CPU cores that will be used for this instance. This number may be dependent upon the image that is used. For instance: </p>
<p>Red Hat Enterprise Linux 6 &#8211; Minimal Install(64 bit)(1 &#8211; 4 Core)<br />
    : &#8212; &#8212; &#8212; &#8212; &#8211;name : Red Hat Enterprise Linux 6 &#8211; Minimal Install(64 bit)(1 &#8211; 4 Core) template : REDHAT_6_64 Red Hat Enterprise Linux 6 &#8211; Minimal Install(64 bit)(5 &#8211; 100 Core)<br />
    : &#8212; &#8212; &#8212; &#8212; &#8211;name : Red Hat Enterprise Linux 6 &#8211; Minimal Install(64 bit)(5 &#8211; 100 Core) template : REDHAT_6_64</p>
<p> Note that the template (meaning, the <i>image</i> option) for both of these is the same, but the names suggests how many CPU cores are supported. <a NAME="lb`A">&nbsp;<wbr></a></p>
<h3>ram</h3>
<p> This is the amount of memory, in megabytes, that will be allocated to this instance. <a NAME="lb`B">&nbsp;<wbr></a></p>
<h3>disk_size</h3>
<p> The amount of disk space that will be allocated to this image, in megabytes. <a NAME="lb`C">&nbsp;<wbr></a></p>
<h3>local_disk</h3>
<p> When true the disks for the computing instance will be provisioned on the host which it runs, otherwise SAN disks will be provisioned. <a NAME="lb`D">&nbsp;<wbr></a></p>
<h3>hourly_billing</h3>
<p> When true the computing instance will be billed on hourly usage, otherwise it will be billed on a monthly basis. <a NAME="lb`E">&nbsp;<wbr></a></p>
<h3>domain</h3>
<p> The domain name that will be used in the FQDN (Fully Qualified Domain Name) for this instance. The <i>domain</i> setting will be used in conjunction with the instance name to form the FQDN. <a NAME="lb`F">&nbsp;<wbr></a></p>
<h3>location</h3>
<p> Images to build an instance can be found using the <i>&#8211;list-locations</i> option: </p>
<pre>
# salt-cloud --list-location my-softlayer
</pre>
<p> <a NAME="lb`G">&nbsp;<wbr></a></p>
<h3>max_net_speed</h3>
<p> Specifies the connection speed for the instance&#8217;s network components. This setting is optional. By default, this is set to 10. <a NAME="lb`H">&nbsp;<wbr></a></p>
<h3>public_vlan</h3>
<p> If it is necessary for an instance to be created within a specific frontend VLAN, the ID for that VLAN can be specified in either the provider or profile configuration. </p>
<p> This ID can be queried using the <i>list_vlans</i> function, as described below. This setting is optional. <a NAME="lb`I">&nbsp;<wbr></a></p>
<h3>private_vlan</h3>
<p> If it is necessary for an instance to be created within a specific backend VLAN, the ID for that VLAN can be specified in either the provider or profile configuration. </p>
<p> This ID can be queried using the <i>list_vlans</i> function, as described below. This setting is optional. <a NAME="lb`J">&nbsp;<wbr></a></p>
<h3>private_network</h3>
<p> If a server is to only be used internally, meaning it does not have a public VLAN associated with it, this value would be set to True. This setting is optional. The default is False. <a NAME="lb`K">&nbsp;<wbr></a></p>
<h3>private_ssh</h3>
<p> Whether to run the deploy script on the server using the public IP address or the private IP address. If set to True, Salt Cloud will attempt to SSH into the new server using the private IP address. The default is False. This settiong is optional. <a NAME="lb`L">&nbsp;<wbr></a></p>
<h3>global_identifier</h3>
<p> When creating an instance using a custom template, this option is set to the corresponding value obtained using the <i>list_custom_images</i> function. This option will not be used if an <i>image</i> is set, and if an <i>image</i> is not set, it is required. </p>
<p> The profile can be realized now with a salt command: </p>
<pre>
# salt-cloud -p base_softlayer_ubuntu myserver
</pre>
<p> Using the above configuration, this will create <i>myserver.example.com</i>. </p>
<p> Once the instance has been created with salt-minion installed, connectivity to it can be verified with Salt: </p>
<pre>
# salt 'myserver.example.com' test.ping
</pre>
<p> <a NAME="lb`M">&nbsp;<wbr></a></p>
<h3>Cloud Profiles</h3>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code>: </p>
<pre>
base_softlayer_hw_centos:
  provider: my-softlayer-hw
  # CentOS 6.0 - Minimal Install (64 bit)
  image: 13963
  # 2 x 2.0 GHz Core Bare Metal Instance - 2 GB Ram
  size: 1921
  # 500GB SATA II
  hdd: 1267
  # San Jose 01
  location: 168642
  domain: example.com
  # Optional
  vlan: 396
  port_speed: 273
  banwidth: 248
</pre>
<p> Most of the above items are required; optional items are specified below. <a NAME="lb`N">&nbsp;<wbr></a></p>
<h3>image</h3>
<p> Images to build an instance can be found using the <i>&#8211;list-images</i> option: </p>
<pre>
# salt-cloud --list-images my-softlayer-hw
</pre>
<p> A list of <i>id`s and names will be provided. The `name</i> will describe the operating system and architecture. The <i>id</i> will be the setting to be used in the profile. <a NAME="lb`O">&nbsp;<wbr></a></p>
<h3>size</h3>
<p> Sizes to build an instance can be found using the <i>&#8211;list-sizes</i> option: </p>
<pre>
# salt-cloud --list-sizes my-softlayer-hw
</pre>
<p> A list of <i>id`s and names will be provided. The `name</i> will describe the speed and quantity of CPU cores, and the amount of memory that the hardware will contain. The <i>id</i> will be the setting to be used in the profile. <a NAME="lb`P">&nbsp;<wbr></a></p>
<h3>hdd</h3>
<p> There is currently only one size of hard disk drive (HDD) that is available for hardware instances on SoftLayer: </p>
<pre>
1267: 500GB SATA II
</pre>
<p> The <i>hdd</i> setting in the profile should be 1267. Other sizes may be added in the future. <a NAME="lb`Q">&nbsp;<wbr></a></p>
<h3>location</h3>
<p> Locations to build an instance can be found using the <i>&#8211;list-images</i> option: </p>
<pre>
# salt-cloud --list-locations my-softlayer-hw
</pre>
<p> A list of IDs and names will be provided. The <i>location</i> will describe the location in human terms. The <i>id</i> will be the setting to be used in the profile. <a NAME="lb`R">&nbsp;<wbr></a></p>
<h3>domain</h3>
<p> The domain name that will be used in the FQDN (Fully Qualified Domain Name) for this instance. The <i>domain</i> setting will be used in conjunction with the instance name to form the FQDN. <a NAME="lb`S">&nbsp;<wbr></a></p>
<h3>vlan</h3>
<p> If it is necessary for an instance to be created within a specific VLAN, the ID for that VLAN can be specified in either the provider or profile configuration. </p>
<p> This ID can be queried using the <i>list_vlans</i> function, as described below. <a NAME="lb`T">&nbsp;<wbr></a></p>
<h3>port_speed</h3>
<p> Specifies the speed for the instance&#8217;s network port. This setting refers to an ID within the SoftLayer API, which sets the port speed. This setting is optional. The default is 273, or, 100 Mbps Public &amp; Private Networks. The following settings are available:</p>
<dl>
<dt>&bull;</p>
<dd> 273: 100 Mbps Public &amp; Private Networks</p>
<dt>&bull;</p>
<dd> 274: 1 Gbps Public &amp; Private Networks</p>
<dt>&bull;</p>
<dd> 21509: 10 Mbps Dual Public &amp; Private Networks (up to 20 Mbps)</p>
<dt>&bull;</p>
<dd> 21513: 100 Mbps Dual Public &amp; Private Networks (up to 200 Mbps)</p>
<dt>&bull;</p>
<dd> 2314: 1 Gbps Dual Public &amp; Private Networks (up to 2 Gbps)</p>
<dt>&bull;</p>
<dd> 272: 10 Mbps Public &amp; Private Networks</dl>
<p> <a NAME="lb`U">&nbsp;<wbr></a></p>
<h3>bandwidth</h3>
<p> Specifies the network bandwidth available for the instance. This setting refers to an ID within the SoftLayer API, which sets the bandwidth. This setting is optional. The default is 248, or, 5000 GB Bandwidth. The following settings are available:</p>
<dl>
<dt>&bull;</p>
<dd> 248: 5000 GB Bandwidth</p>
<dt>&bull;</p>
<dd> 129: 6000 GB Bandwidth</p>
<dt>&bull;</p>
<dd> 130: 8000 GB Bandwidth</p>
<dt>&bull;</p>
<dd> 131: 10000 GB Bandwidth</p>
<dt>&bull;</p>
<dd> 36: Unlimited Bandwidth (10 Mbps Uplink)</p>
<dt>&bull;</p>
<dd> 125: Unlimited Bandwidth (100 Mbps Uplink)</dl>
<p> <a NAME="lb`V">&nbsp;<wbr></a></p>
<h3>Actions</h3>
<p> The following actions are currently supported by the SoftLayer Salt Cloud driver. <a NAME="lb`W">&nbsp;<wbr></a></p>
<h3>show_instance</h3>
<p> This action is a thin wrapper around <i>&#8211;full-query</i>, which displays details on a single instance only. In an environment with several machines, this will save a user from having to sort through all instance data, just to examine a single instance. </p>
<pre>
$ salt-cloud -a show_instance myinstance
</pre>
<p> <a NAME="lb`X">&nbsp;<wbr></a></p>
<h3>Functions</h3>
<p> The following functions are currently supported by the SoftLayer Salt Cloud driver. <a NAME="lb`Y">&nbsp;<wbr></a></p>
<h3>list_vlans</h3>
<p> This function lists all VLANs associated with the account, and all known data from the SoftLayer API concerning those VLANs. </p>
<pre>
$ salt-cloud -f list_vlans my-softlayer
$ salt-cloud -f list_vlans my-softlayer-hw
</pre>
<p> The <i>id</i> returned in this list is necessary for the <i>vlan</i> option when creating an instance. <a NAME="lb`Z">&nbsp;<wbr></a></p>
<h3>list_custom_images</h3>
<p> This function lists any custom templates associated with the account, that can be used to create a new instance. </p>
<pre>
$ salt-cloud -f list_custom_images my-softlayer
</pre>
<p> The <i>globalIdentifier</i> returned in this list is necessary for the <i>global_identifier</i> option when creating an image using a custom template.</p>
<h3>Optional Products for SoftLayer HW</h3>
<p> The softlayer_hw provider supports the ability to add optional products, which are supported by SoftLayer&#8217;s API. These products each have an ID associated with them, that can be passed into Salt Cloud with the <i>optional_products</i> option: </p>
<pre>
softlayer_hw_test:
  provider: my-softlayer-hw
  # CentOS 6.0 - Minimal Install (64 bit)
  image: 13963
  # 2 x 2.0 GHz Core Bare Metal Instance - 2 GB Ram
  size: 1921
  # 500GB SATA II
  hdd: 1267
  # San Jose 01
  location: 168642
  domain: example.com
  optional_products:
    # MySQL for Linux
    - id: 28
    # Business Continuance Insurance
    - id: 104
</pre>
<p> These values can be manually obtained by looking at the source of an order page on the SoftLayer web interface. For convenience, many of these values are listed here:</p>
<h3>Public Secondary IP Addresses</h3>
<dl>
<dt>&bull;</p>
<dd> 22: 4 Public IP Addresses</p>
<dt>&bull;</p>
<dd> 23: 8 Public IP Addresses</dl>
<h3>Primary IPv6 Addresses</h3>
<dl>
<dt>&bull;</p>
<dd> 17129: 1 IPv6 Address</dl>
<h3>Public Static IPv6 Addresses</h3>
<dl>
<dt>&bull;</p>
<dd> 1481: /64 Block Static Public IPv6 Addresses</dl>
<h3>OS-Specific Addon</h3>
<dl>
<dt>&bull;</p>
<dd> 17139: XenServer Advanced for XenServer 6.x</p>
<dt>&bull;</p>
<dd> 17141: XenServer Enterprise for XenServer 6.x</p>
<dt>&bull;</p>
<dd> 2334: XenServer Advanced for XenServer 5.6</p>
<dt>&bull;</p>
<dd> 2335: XenServer Enterprise for XenServer 5.6</p>
<dt>&bull;</p>
<dd> 13915: Microsoft WebMatrix</p>
<dt>&bull;</p>
<dd> 21276: VMware vCenter 5.1 Standard</dl>
<h3>Control Panel Software</h3>
<dl>
<dt>&bull;</p>
<dd> 121: cPanel/WHM with Fantastico and RVskin</p>
<dt>&bull;</p>
<dd> 20778: Parallels Plesk Panel 11 (Linux) 100 Domain w/ Power Pack</p>
<dt>&bull;</p>
<dd> 20786: Parallels Plesk Panel 11 (Windows) 100 Domain w/ Power Pack</p>
<dt>&bull;</p>
<dd> 20787: Parallels Plesk Panel 11 (Linux) Unlimited Domain w/ Power Pack</p>
<dt>&bull;</p>
<dd> 20792: Parallels Plesk Panel 11 (Windows) Unlimited Domain w/ Power Pack</p>
<dt>&bull;</p>
<dd> 2340: Parallels Plesk Panel 10 (Linux) 100 Domain w/ Power Pack</p>
<dt>&bull;</p>
<dd> 2339: Parallels Plesk Panel 10 (Linux) Unlimited Domain w/ Power Pack</p>
<dt>&bull;</p>
<dd> 13704: Parallels Plesk Panel 10 (Windows) Unlimited Domain w/ Power Pack</dl>
<h3>Database Software</h3>
<dl>
<dt>&bull;</p>
<dd> 29: MySQL 5.0 for Windows</p>
<dt>&bull;</p>
<dd> 28: MySQL for Linux</p>
<dt>&bull;</p>
<dd> 21501: Riak 1.x</p>
<dt>&bull;</p>
<dd> 20893: MongoDB</p>
<dt>&bull;</p>
<dd> 30: Microsoft SQL Server 2005 Express</p>
<dt>&bull;</p>
<dd> 92: Microsoft SQL Server 2005 Workgroup</p>
<dt>&bull;</p>
<dd> 90: Microsoft SQL Server 2005 Standard</p>
<dt>&bull;</p>
<dd> 94: Microsoft SQL Server 2005 Enterprise</p>
<dt>&bull;</p>
<dd> 1330: Microsoft SQL Server 2008 Express</p>
<dt>&bull;</p>
<dd> 1340: Microsoft SQL Server 2008 Web</p>
<dt>&bull;</p>
<dd> 1337: Microsoft SQL Server 2008 Workgroup</p>
<dt>&bull;</p>
<dd> 1334: Microsoft SQL Server 2008 Standard</p>
<dt>&bull;</p>
<dd> 1331: Microsoft SQL Server 2008 Enterprise</p>
<dt>&bull;</p>
<dd> 2179: Microsoft SQL Server 2008 Express R2</p>
<dt>&bull;</p>
<dd> 2173: Microsoft SQL Server 2008 Web R2</p>
<dt>&bull;</p>
<dd> 2183: Microsoft SQL Server 2008 Workgroup R2</p>
<dt>&bull;</p>
<dd> 2180: Microsoft SQL Server 2008 Standard R2</p>
<dt>&bull;</p>
<dd> 2176: Microsoft SQL Server 2008 Enterprise R2</dl>
<h3>Anti-Virus &amp; Spyware Protection</h3>
<dl>
<dt>&bull;</p>
<dd> 594: McAfee VirusScan Anti-Virus &#8211; Windows</p>
<dt>&bull;</p>
<dd> 414: McAfee Total Protection &#8211; Windows</dl>
<h3>Insurance</h3>
<dl>
<dt>&bull;</p>
<dd> 104: Business Continuance Insurance</dl>
<h3>Monitoring</h3>
<dl>
<dt>&bull;</p>
<dd> 55: Host Ping</p>
<dt>&bull;</p>
<dd> 56: Host Ping and TCP Service Monitoring</dl>
<h3>Notification</h3>
<dl>
<dt>&bull;</p>
<dd> 57: Email and Ticket</dl>
<h3>Advanced Monitoring</h3>
<dl>
<dt>&bull;</p>
<dd> 2302: Monitoring Package &#8211; Basic</p>
<dt>&bull;</p>
<dd> 2303: Monitoring Package &#8211; Advanced</p>
<dt>&bull;</p>
<dd> 2304: Monitoring Package &#8211; Premium Application</dl>
<h3>Response</h3>
<dl>
<dt>&bull;</p>
<dd> 58: Automated Notification</p>
<dt>&bull;</p>
<dd> 59: Automated Reboot from Monitoring</p>
<dt>&bull;</p>
<dd> 60: 24x7x365 NOC Monitoring, Notification, and Response</dl>
<h3>Intrusion Detection &amp; Protection</h3>
<dl>
<dt>&bull;</p>
<dd> 413: McAfee Host Intrusion Protection w/Reporting</dl>
<h3>Hardware &amp; Software Firewalls</h3>
<dl>
<dt>&bull;</p>
<dd> 411: APF Software Firewall for Linux</p>
<dt>&bull;</p>
<dd> 894: Microsoft Windows Firewall</p>
<dt>&bull;</p>
<dd> 410: 10Mbps Hardware Firewall</p>
<dt>&bull;</p>
<dd> 409: 100Mbps Hardware Firewall</p>
<dt>&bull;</p>
<dd> 408: 1000Mbps Hardware Firewall</dl>
<h3>Getting Started with VEXXHOST</h3>
<p> <i>VEXXHOST</i> is an cloud computing provider which provides <i>Canadian cloud computing</i> services which are based in Monteral and uses the libcloud OpenStack driver. VEXXHOST currently runs the Havana release of OpenStack. When provisioning new instances, they automatically get a public IP and private IP address. Therefore, you do not need to assign a floating IP to access your instance once it&#8217;s booted.</p>
<h3>Cloud Provider Configuration</h3>
<p> To use the <i>openstack</i> driver for the VEXXHOST public cloud, you will need to set up the cloud provider configuration file as in the example below: </p>
<p> <code>/etc/salt/cloud.providers.d/vexxhost.conf</code>: In order to use the VEXXHOST public cloud, you will need to setup a cloud provider configuration file as in the example below which uses the OpenStack driver. </p>
<pre>
vexxhost:
  # Set the location of the salt-master
  #
  minion:
    master: saltmaster.example.com
  # Configure VEXXHOST using the OpenStack plugin
  #
  identity_url: <a rel="nofollow noopener" href="http://auth.api.thenebulacloud.com:5000/v2.0/tokens" target="_blank">http://auth.api.thenebulacloud.com:5000/v2.0/tokens</a>
  compute_name: nova
  # Set the compute region:
  #
  compute_region: na-yul-nhs1
  # Configure VEXXHOST authentication credentials
  #
  user: your-tenant-id
  password: your-api-key
  tenant: your-tenant-name
  # keys to allow connection to the instance launched
  #
  ssh_key_name: yourkey
  ssh_key_file: /path/to/key/yourkey.priv
  provider: openstack
</pre>
<h3>Authentication</h3>
<p> All of the authentication fields that you need can be found by logging into your VEXXHOST customer center. Once you&#8217;ve logged in, you will need to click on &quot;CloudConsole&quot; and then click on &quot;API Credentials&quot;.</p>
<h3>Cloud Profile Configuration</h3>
<p> In order to get the correct image UUID and the instance type to use in the cloud profile, you can run the following command respectively: </p>
<pre>
# salt-cloud --list-images=vexxhost-config
# salt-cloud --list-sizes=vexxhost-config
</pre>
<p> Once you have that, you can go ahead and create a new cloud profile. This profile will build an Ubuntu 12.04 LTS <i>nb.2G</i> instance. </p>
<p> <code>/etc/salt/cloud.profiles.d/vh_ubuntu1204_2G.conf</code>: </p>
<pre>
vh_ubuntu1204_2G:
    provider: vexxhost
    image: 4051139f-750d-4d72-8ef0-074f2ccc7e5a
    size: nb.2G
</pre>
<h3>Provision an instance</h3>
<p> To create an instance based on the sample profile that we created above, you can run the following <i>salt-cloud</i> command. </p>
<pre>
# salt-cloud -p vh_ubuntu1204_2G vh_instance1
</pre>
<p> Typically, instances are provisioned in under 30 seconds on the VEXXHOST public cloud. After the instance provisions, it will be set up a minion and then return all the instance information once it&#8217;s complete. </p>
<p> Once the instance has been setup, you can test connectivity to it by running the following command: </p>
<pre>
# salt vh_instance1 test.ping
</pre>
<p> You can now continue to provision new instances and they will all automatically be set up as minions of the master you&#8217;ve defined in the configuration file.</p>
<h3>Getting Started With vSphere</h3>
<p> <code>NOTE:</code> Deprecated since version Carbon: The <code>vsphere</code> cloud driver has been deprecated in favor of the <code>vmware</code> cloud driver and will be removed in Salt Carbon. Please refer to <code>Getting started with VMware</code> instead to get started with the configuration. </p>
<p> VMware vSphere is a management platform for virtual infrastructure and cloud computing.</p>
<h3>Dependencies</h3>
<p> The vSphere module for Salt Cloud requires the PySphere package, which is available at PyPI: </p>
<p> <i><a rel="nofollow noopener" href="https://pypi.python.org/pypi/pysphere" target="_blank">https://pypi.python.org/pypi/pysphere</a></i> </p>
<p> This package can be installed using <i>pip</i> or <i>easy_install</i>: </p>
<pre>
# pip install pysphere
# easy_install pysphere
</pre>
<h3>Configuration</h3>
<p> Set up the cloud config at <code>/etc/salt/cloud.providers</code> or in the <code>/etc/salt/cloud.providers.d/</code> directory: </p>
<pre>
my-vsphere-config:
  provider: vsphere
  # Set the vSphere access credentials
  user: marco
  password: polo
  # Set the URL of your vSphere server
  url: 'vsphere.example.com'
</pre>
<h3>Profiles</h3>
<h3>Cloud Profiles</h3>
<p> vSphere uses a Managed Object Reference to identify objects located in vCenter. The MOR ID&#8217;s are used when configuring a vSphere cloud profile. Use the following reference when locating the MOR&#8217;s for the cloud profile. </p>
<p> <i><a rel="nofollow noopener" href="http://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC" target="_blank">http://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC</a>&amp;docType=kc&amp;externalId=1017126&amp;sliceId=1&amp;docTypeID=DT_KB_1_1&amp;dialogID=520386078&amp;stateId=1%200%20520388386</i> </p>
<p> Set up an initial profile at <code>/etc/salt/cloud.profiles</code> or in the <code>/etc/salt/cloud.profiles.d</code> directory: </p>
<pre>
vsphere-centos:
  provider: my-vsphere-config
  image: centos
  # Optional
  datastore: datastore-15
  resourcepool: resgroup-8
  folder: salt-cloud
  host: host-9
  template: False
</pre>
<h3>provider</h3>
<p> Enter the name that was specified when the cloud provider profile was created.</p>
<h3>image</h3>
<p> Images available to build an instance can be found using the <i>&#8211;list-images</i> option: </p>
<pre>
# salt-cloud --list-images my-vsphere-config
</pre>
<h3>datastore</h3>
<p> The MOR of the datastore where the virtual machine should be located. If not specified, the current datastore is used.</p>
<h3>resourcepool</h3>
<p> The MOR of the resourcepool to be used for the new vm. If not set, it will use the same resourcepool as the original vm.</p>
<h3>folder</h3>
<p> Name of the folder that will contain the new VM. If not set, the VM will be added to the folder the original VM belongs to.</p>
<h3>host</h3>
<p> The MOR of the host where the vm should be registered.</p>
<dl>
<dt><code>If not specified:</code></p>
<dd>
<dt>&bull;</p>
<dd> if resourcepool is not specified, the current host is used.</p>
<dt>&bull;</p>
<dd> if resourcepool is specified, and the target pool represents a stand-alone host, the host is used.</p>
<dt>&bull;</p>
<dd> if resourcepool is specified, and the target pool represents a DRS-enabled cluster, a host selected by DRS is used.</p>
<dt>&bull;</p>
<dd> if resourcepool is specified, and the target pool represents a cluster without DRS enabled, an InvalidArgument exception will be thrown.</dl>
<h3>template</h3>
<p> Specifies whether or not the new virtual machine should be marked as a template. Default is False.</p>
<h3>Miscellaneous Options</h3>
<h3>Miscellaneous Salt Cloud Options</h3>
<p> This page describes various miscellaneous options available in Salt Cloud</p>
<h3>Deploy Script Arguments</h3>
<p> Custom deploy scripts are unlikely to need custom arguments to be passed to them, but salt-bootstrap has been extended quite a bit, and this may be necessary. script_args can be specified in either the profile or the map file, to pass arguments to the deploy script: </p>
<pre>
ec2-amazon:
    provider: ec2
    image: ami-1624987f
    size: t1.micro
    ssh_username: ec2-user
    script: bootstrap-salt
    script_args: -c /tmp/
</pre>
<p> This has also been tested to work with pipes, if needed: </p>
<pre>
script_args: | head
</pre>
<h3>Selecting the File Transport</h3>
<p> By default, Salt Cloud uses SFTP to transfer files to Linux hosts. However, if SFTP is not available, or specific SCP functionality is needed, Salt Cloud can be configured to use SCP instead. </p>
<pre>
file_transport: sftp
file_transport: scp
</pre>
<h3>Sync After Install</h3>
<p> Salt allows users to create custom modules, grains, and states which can be synchronised to minions to extend Salt with further functionality. </p>
<p> This option will inform Salt Cloud to synchronise your custom modules, grains, states or all these to the minion just after it has been created. For this to happen, the following line needs to be added to the main cloud configuration file: </p>
<pre>
sync_after_install: all
</pre>
<p> The available options for this setting are: </p>
<pre>
modules
grains
states
all
</pre>
<h3>Setting up New Salt Masters</h3>
<p> It has become increasingly common for users to set up multi-hierarchal infrastructures using Salt Cloud. This sometimes involves setting up an instance to be a master in addition to a minion. With that in mind, you can now lay down master configuration on a machine by specifying master options in the profile or map file. </p>
<pre>
make_master: True
</pre>
<p> This will cause Salt Cloud to generate master keys for the instance, and tell salt-bootstrap to install the salt-master package, in addition to the salt-minion package. </p>
<p> The default master configuration is usually appropriate for most users, and will not be changed unless specific master configuration has been added to the profile or map: </p>
<pre>
master:
    user: root
    interface: 0.0.0.0
</pre>
<h3>Delete SSH Keys</h3>
<p> When Salt Cloud deploys an instance, the SSH pub key for the instance is added to the known_hosts file for the user that ran the salt-cloud command. When an instance is deployed, a cloud provider generally recycles the IP address for the instance. When Salt Cloud attempts to deploy an instance using a recycled IP address that has previously been accessed from the same machine, the old key in the known_hosts file will cause a conflict. </p>
<p> In order to mitigate this issue, Salt Cloud can be configured to remove old keys from the known_hosts file when destroying the node. In order to do this, the following line needs to be added to the main cloud configuration file: </p>
<pre>
delete_sshkeys: True
</pre>
<h3>Keeping /tmp/ Files</h3>
<p> When Salt Cloud deploys an instance, it uploads temporary files to /tmp/ for salt-bootstrap to put in place. After the script has run, they are deleted. To keep these files around (mostly for debugging purposes), the &#8211;keep-tmp option can be added: </p>
<pre>
salt-cloud -p myprofile mymachine --keep-tmp
</pre>
<p> For those wondering why /tmp/ was used instead of /root/, this had to be done for images which require the use of sudo, and therefore do not allow remote root logins, even for file transfers (which makes /root/ unavailable).</p>
<h3>Hide Output From Minion Install</h3>
<p> By default Salt Cloud will stream the output from the minion deploy script directly to STDOUT. Although this can been very useful, in certain cases you may wish to switch this off. The following config option is there to enable or disable this output: </p>
<pre>
display_ssh_output: False
</pre>
<h3>Connection Timeout</h3>
<p> There are several stages when deploying Salt where Salt Cloud needs to wait for something to happen. The VM getting it&#8217;s IP address, the VM&#8217;s SSH port is available, etc. </p>
<p> If you find that the Salt Cloud defaults are not enough and your deployment fails because Salt Cloud did not wait log enough, there are some settings you can tweak.</p>
<dl>
<dt>Note</p>
<dd>
<p> All settings should be provided in lowercase All values should be provided in seconds </p>
<p> You can tweak these settings globally, per cloud provider, or event per profile definition.</dl>
<h3>wait_for_ip_timeout</h3>
<p> The amount of time Salt Cloud should wait for a VM to start and get an IP back from the cloud provider. Default: 5 minutes.</p>
<h3>wait_for_ip_interval</h3>
<p> The amount of time Salt Cloud should sleep while querying for the VM&#8217;s IP. Default: 5 seconds.</p>
<h3>ssh_connect_timeout</h3>
<p> The amount of time Salt Cloud should wait for a successful SSH connection to the VM. Default: 5 minutes.</p>
<h3>wait_for_passwd_timeout</h3>
<p> The amount of time until an ssh connection can be established via password or ssh key. Default 15 seconds.</p>
<h3>wait_for_passwd_maxtries</h3>
<p> The number of attempts to connect to the VM until we abandon. Default 15 attempts</p>
<h3>wait_for_fun_timeout</h3>
<p> Some cloud drivers check for an available IP or a successful SSH connection using a function, namely, SoftLayer, and SoftLayer-HW. So, the amount of time Salt Cloud should retry such functions before failing. Default: 5 minutes.</p>
<h3>wait_for_spot_timeout</h3>
<p> The amount of time Salt Cloud should wait before an EC2 Spot instance is available. This setting is only available for the EC2 cloud driver.</p>
<h3>Salt Cloud Cache</h3>
<p> Salt Cloud can maintain a cache of node data, for supported providers. The following options manage this functionality.</p>
<h3>update_cachedir</h3>
<p> On supported cloud providers, whether or not to maintain a cache of nodes returned from a &#8211;full-query. The data will be stored in <code>msgpack</code> format under <code>&lt;SALT_CACHEDIR&gt;/cloud/active/&lt;DRIVER&gt;/&lt;PROVIDER&gt;/&lt;NODE_NAME&gt;.p</code>. This setting can be True or False.</p>
<h3>diff_cache_events</h3>
<p> When the cloud cachedir is being managed, if differences are encountered between the data that is returned live from the cloud provider and the data in the cache, fire events which describe the changes. This setting can be True or False. </p>
<p> Some of these events will contain data which describe a node. Because some of the fields returned may contain sensitive data, the <code>cache_event_strip_fields</code> configuration option exists to strip those fields from the event return. </p>
<pre>
cache_event_strip_fields:
  - password
  - priv_key
</pre>
<p> The following are events that can be fired based on this data.</p>
<h3>salt/cloud/minionid/cache_node_new</h3>
<p> A new node was found on the cloud provider which was not listed in the cloud cachedir. A dict describing the new node will be contained in the event.</p>
<h3>salt/cloud/minionid/cache_node_missing</h3>
<p> A node that was previously listed in the cloud cachedir is no longer available on the cloud provider.</p>
<h3>salt/cloud/minionid/cache_node_diff</h3>
<p> One or more pieces of data in the cloud cachedir has changed on the cloud provider. A dict containing both the old and the new data will be contained in the event.</p>
<h3>SSH Known Hosts</h3>
<p> Normally when bootstrapping a VM, salt-cloud will ignore the SSH host key. This is because it does not know what the host key is before starting (because it doesn&#8217;t exist yet). If strict host key checking is turned on without the key in the <code>known_hosts</code> file, then the host will never be available, and cannot be bootstrapped. </p>
<p> If a provider is able to determine the host key before trying to bootstrap it, that provider&#8217;s driver can add it to the <code>known_hosts</code> file, and then turn on strict host key checking. This can be set up in the main cloud configuration file (normally <code>/etc/salt/cloud</code>) or in the provider-specific configuration file: </p>
<pre>
known_hosts_file: /path/to/.ssh/known_hosts
</pre>
<p> If this is not set, it will default to <code>/dev/null</code>, and strict host key checking will be turned off. </p>
<p> It is highly recommended that this option is <i>not</i> set, unless the user has verified that the provider supports this functionality, and that the image being used is capable of providing the necessary information. At this time, only the EC2 driver supports this functionality.</p>
<h3>SSH Agent</h3>
<p> New in version 2015.5.0. </p>
<p> If the ssh key is not stored on the server salt-cloud is being run on, set ssh_agent, and salt-cloud will use the forwarded ssh-agent to authenticate. </p>
<pre>
ssh_agent: True
</pre>
<h3>File Map Upload</h3>
<p> New in version 2014.7.0. </p>
<p> The <code>file_map</code> option allows an arbitrary group of files to be uploaded to the target system before running the deploy script. This functionality requires a provider uses salt.utils.cloud.bootstrap(), which is currently limited to the ec2, gce, openstack and nova drivers. </p>
<p> The <code>file_map</code> can be configured globally in <code>/etc/salt/cloud</code>, or in any cloud provider or profile file. For example, to upload an extra package or a custom deploy script, a cloud profile using <code>file_map</code> might look like: </p>
<pre>
ubuntu14:
  provider: ec2-config
  image: ami-98aa1cf0
  size: t1.micro
  ssh_username: root
  securitygroup: default
  file_map:
    /local/path/to/custom/script: /remote/path/to/use/custom/script
    /local/path/to/package: /remote/path/to/store/package
</pre>
<h3>Troubleshooting Steps</h3>
<h3>Troubleshooting Salt Cloud</h3>
<p> This page describes various steps for troubleshooting problems that may arise while using Salt Cloud.</p>
<h3>Virtual Machines Are Created, But Do Not Respond</h3>
<p> Are TCP ports 4505 and 4506 open on the master? This is easy to overlook on new masters. Information on how to open firewall ports on various platforms can be found <code>here</code>.</p>
<h3>Generic Troubleshooting Steps</h3>
<p> This section describes a set of instructions that are useful to a large number of situations, and are likely to solve most issues that arise.</p>
<dl>
<dt>Version Compatibility</p>
<dd>
<p> One of the most common issues that Salt Cloud users run into is import errors. These are often caused by version compatibility issues with Salt. </p>
<p> Salt 0.16.x works with Salt Cloud 0.8.9 or greater. </p>
<p> Salt 0.17.x requires Salt Cloud 0.8.11. </p>
<p> Releases after 0.17.x (0.18 or greater) should not encounter issues as Salt Cloud has been merged into Salt itself.</dl>
<h3>Debug Mode</h3>
<p> Frequently, running Salt Cloud in debug mode will reveal information about a deployment which would otherwise not be obvious: </p>
<pre>
salt-cloud -p myprofile myinstance -l debug
</pre>
<p> Keep in mind that a number of messages will appear that look at first like errors, but are in fact intended to give developers factual information to assist in debugging. A number of messages that appear will be for cloud providers that you do not have configured; in these cases, the message usually is intended to confirm that they are not configured.</p>
<h3>Salt Bootstrap</h3>
<p> By default, Salt Cloud uses the Salt Bootstrap script to provision instances: </p>
<p> This script is packaged with Salt Cloud, but may be updated without updating the Salt package: </p>
<pre>
salt-cloud -u
</pre>
<h3>The Bootstrap Log</h3>
<p> If the default deploy script was used, there should be a file in the <code>/tmp/</code> directory called <code>bootstrap-salt.log</code>. This file contains the full output from the deployment, including any errors that may have occurred.</p>
<h3>Keeping Temp Files</h3>
<p> Salt Cloud uploads minion-specific files to instances once they are available via SSH, and then executes a deploy script to put them into the correct place and install Salt. The <code>&#8211;keep-tmp</code> option will instruct Salt Cloud not to remove those files when finished with them, so that the user may inspect them for problems: </p>
<pre>
salt-cloud -p myprofile myinstance --keep-tmp
</pre>
<p> By default, Salt Cloud will create a directory on the target instance called <code>/tmp/.saltcloud/</code>. This directory should be owned by the user that is to execute the deploy script, and should have permissions of <code>0700</code>. </p>
<p> Most cloud providers are configured to use <code>root</code> as the default initial user for deployment, and as such, this directory and all files in it should be owned by the <code>root</code> user. </p>
<p> The <code>/tmp/.saltcloud/</code> directory should the following files:</p>
<dl>
<dt>&bull;</p>
<dd> A <code>deploy.sh</code> script. This script should have permissions of <code>0755</code>.</p>
<dt>&bull;</p>
<dd> A <code>.pem</code> and <code>.pub</code> key named after the minion. The <code>.pem</code> file should have permissions of <code>0600</code>. Ensure that the <code>.pem</code> and <code>.pub</code> files have been properly copied to the <code>/etc/salt/pki/minion/</code> directory.</p>
<dt>&bull;</p>
<dd> A file called <code>minion</code>. This file should have been copied to the <code>/etc/salt/</code> directory.</p>
<dt>&bull;</p>
<dd> Optionally, a file called <code>grains</code>. This file, if present, should have been copied to the <code>/etc/salt/</code> directory.</dl>
<h3>Unprivileged Primary Users</h3>
<p> Some providers, most notably EC2, are configured with a different primary user. Some common examples are <code>ec2-user</code>, <code>ubuntu</code>, <code>fedora</code>, and <code>bitnami</code>. In these cases, the <code>/tmp/.saltcloud/</code> directory and all files in it should be owned by this user. </p>
<p> Some providers, such as EC2, are configured to not require these users to provide a password when using the <code>sudo</code> command. Because it is more secure to require <code>sudo</code> users to provide a password, other providers are configured that way. </p>
<p> If this instance is required to provide a password, it needs to be configured in Salt Cloud. A password for sudo to use may be added to either the provider configuration or the profile configuration: </p>
<pre>
sudo_password: mypassword
</pre>
<h3><code>/tmp/</code> is Mounted as <code>noexec</code></h3>
<p> It is more secure to mount the <code>/tmp/</code> directory with a <code>noexec</code> option. This is uncommon on most cloud providers, but very common in private environments. To see if the <code>/tmp/</code> directory is mounted this way, run the following command: </p>
<pre>
mount | grep tmp
</pre>
<p> The if the output of this command includes a line that looks like this, then the <code>/tmp/</code> directory is mounted as <code>noexec</code>: </p>
<pre>
tmpfs on /tmp type tmpfs (rw,noexec)
</pre>
<p> If this is the case, then the <code>deploy_command</code> will need to be changed in order to run the deploy script through the <code>sh</code> command, rather than trying to execute it directly. This may be specified in either the provider or the profile config: </p>
<pre>
deploy_command: sh /tmp/.saltcloud/deploy.sh
</pre>
<p> Please note that by default, Salt Cloud will place its files in a directory called <code>/tmp/.saltcloud/</code>. This may be also be changed in the provider or profile configuration: </p>
<pre>
tmp_dir: /tmp/.saltcloud/
</pre>
<p> If this directory is changed, then the <code>deploy_command</code> need to be changed in order to reflect the <code>tmp_dir</code> configuration.</p>
<h3>Executing the Deploy Script Manually</h3>
<p> If all of the files needed for deployment were successfully uploaded to the correct locations, and contain the correct permissions and ownerships, the deploy script may be executed manually in order to check for other issues: </p>
<pre>
cd /tmp/.saltcloud/
./deploy.sh
</pre>
<h3>Extending Salt Cloud</h3>
<h3>Writing Cloud Provider Modules</h3>
<p> Salt Cloud runs on a module system similar to the main Salt project. The modules inside saltcloud exist in the <code>salt/cloud/clouds</code> directory of the salt source. </p>
<p> There are two basic types of cloud modules. If a cloud provider is supported by libcloud, then using it is the fastest route to getting a module written. The Apache Libcloud project is located at: </p>
<p> <i><a rel="nofollow noopener" href="http://libcloud.apache.org/" target="_blank">http://libcloud.apache.org/</a></i> </p>
<p> Not every cloud provider is supported by libcloud. Additionally, not every feature in a supported cloud provider is necessary supported by libcloud. In either of these cases, a module can be created which does not rely on libcloud.</p>
<h3>All Modules</h3>
<p> The following functions are required by all modules, whether or not they are based on libcloud.</p>
<h3>The __virtual__() Function</h3>
<p> This function determines whether or not to make this cloud module available upon execution. Most often, it uses <code>get_configured_provider()</code> to determine if the necessary configuration has been set up. It may also check for necessary imports, to decide whether to load the module. In most cases, it will return a <code>True</code> or <code>False</code> value. If the name of the driver used does not match the filename, then that name should be returned instead of <code>True</code>. An example of this may be seen in the Azure module: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt/tree/develop/salt/cloud/clouds/msazure.py" target="_blank">https://github.com/saltstack/salt/tree/develop/salt/cloud/clouds/msazure.py</a></i></p>
<h3>The get_configured_provider() Function</h3>
<p> This function uses <code>config.is_provider_configured()</code> to determine wither all required information for this driver has been configured. The last value in the list of required settings should be followed by a comma.</p>
<h3>Libcloud Based Modules</h3>
<p> Writing a cloud module based on libcloud has two major advantages. First of all, much of the work has already been done by the libcloud project. Second, most of the functions necessary to Salt have already been added to the Salt Cloud project.</p>
<h3>The create() Function</h3>
<p> The most important function that does need to be manually written is the <code>create()</code> function. This is what is used to request a virtual machine to be created by the cloud provider, wait for it to become available, and then (optionally) log in and install Salt on it. </p>
<p> A good example to follow for writing a cloud provider module based on libcloud is the module provided for Linode: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt/tree/develop/salt/cloud/clouds/linode.py" target="_blank">https://github.com/saltstack/salt/tree/develop/salt/cloud/clouds/linode.py</a></i> </p>
<p> The basic flow of a <code>create()</code> function is as follows:</p>
<dl>
<dt>&bull;</p>
<dd> Send a request to the cloud provider to create a virtual machine.</p>
<dt>&bull;</p>
<dd> Wait for the virtual machine to become available.</p>
<dt>&bull;</p>
<dd> Generate kwargs to be used to deploy Salt.</p>
<dt>&bull;</p>
<dd> Log into the virtual machine and deploy Salt.</p>
<dt>&bull;</p>
<dd> Return a data structure that describes the newly-created virtual machine. </p>
<p> At various points throughout this function, events may be fired on the Salt event bus. Four of these events, which are described below, are required. Other events may be added by the user, where appropriate. </p>
<p> When the <code>create()</code> function is called, it is passed a data structure called <code>vm_</code>. This dict contains a composite of information describing the virtual machine to be created. A dict called <code>__opts__</code> is also provided by Salt, which contains the options used to run Salt Cloud, as well as a set of configuration and environment variables. </p>
<p> The first thing the <code>create()</code> function must do is fire an event stating that it has started the create process. This event is tagged <code>salt/cloud/&lt;vm name&gt;/creating</code>. The payload contains the names of the VM, profile and provider. </p>
<p> A set of kwargs is then usually created, to describe the parameters required by the cloud provider to request the virtual machine. </p>
<p> An event is then fired to state that a virtual machine is about to be requested. It is tagged as <code>salt/cloud/&lt;vm name&gt;/requesting</code>. The payload contains most or all of the parameters that will be sent to the cloud provider. Any private information (such as passwords) should not be sent in the event. </p>
<p> After a request is made, a set of deploy kwargs will be generated. These will be used to install Salt on the target machine. Windows options are supported at this point, and should be generated, even if the cloud provider does not currently support Windows. This will save time in the future if the provider does eventually decide to support Windows. </p>
<p> An event is then fired to state that the deploy process is about to begin. This event is tagged <code>salt/cloud/&lt;vm name&gt;/deploying</code>. The payload for the event will contain a set of deploy kwargs, useful for debugging purposed. Any private data, including passwords and keys (including public keys) should be stripped from the deploy kwargs before the event is fired. </p>
<p> If any Windows options have been passed in, the <code>salt.utils.cloud.deploy_windows()</code> function will be called. Otherwise, it will be assumed that the target is a Linux or Unix machine, and the <code>salt.utils.cloud.deploy_script()</code> will be called. </p>
<p> Both of these functions will wait for the target machine to become available, then the necessary port to log in, then a successful login that can be used to install Salt. Minion configuration and keys will then be uploaded to a temporary directory on the target by the appropriate function. On a Windows target, the Windows Minion Installer will be run in silent mode. On a Linux/Unix target, a deploy script (bootstrap-salt.sh, by default) will be run, which will auto-detect the operating system, and install Salt using its native package manager. These do not need to be handled by the developer in the cloud module. </p>
<p> The <code>salt.utils.cloud.validate_windows_cred()</code> function has been extended to take the number of retries and retry_delay parameters in case a specific cloud provider has a delay between providing the Windows credentials and the credentials being available for use. In their <code>create()</code> function, or as a a sub-function called during the creation process, developers should use the <code>win_deploy_auth_retries</code> and <code>win_deploy_auth_retry_delay</code> parameters from the provider configuration to allow the end-user the ability to customize the number of tries and delay between tries for their particular provider. </p>
<p> After the appropriate deploy function completes, a final event is fired which describes the virtual machine that has just been created. This event is tagged <code>salt/cloud/&lt;vm name&gt;/created</code>. The payload contains the names of the VM, profile, and provider. </p>
<p> Finally, a dict (queried from the provider) which describes the new virtual machine is returned to the user. Because this data is not fired on the event bus it can, and should, return any passwords that were returned by the cloud provider. In some cases (for example, Rackspace), this is the only time that the password can be queried by the user; post-creation queries may not contain password information (depending upon the provider).</dl>
<h3>The libcloudfuncs Functions</h3>
<p> A number of other functions are required for all cloud providers. However, with libcloud-based modules, these are all provided for free by the libcloudfuncs library. The following two lines set up the imports: </p>
<pre>
from salt.cloud.libcloudfuncs import *   # pylint: disable=W0614,W0401
from salt.utils import namespaced_function
</pre>
<p> And then a series of declarations will make the necessary functions available within the cloud module. </p>
<pre>
get_size = namespaced_function(get_size, globals())
get_image = namespaced_function(get_image, globals())
avail_locations = namespaced_function(avail_locations, globals())
avail_images = namespaced_function(avail_images, globals())
avail_sizes = namespaced_function(avail_sizes, globals())
script = namespaced_function(script, globals())
destroy = namespaced_function(destroy, globals())
list_nodes = namespaced_function(list_nodes, globals())
list_nodes_full = namespaced_function(list_nodes_full, globals())
list_nodes_select = namespaced_function(list_nodes_select, globals())
show_instance = namespaced_function(show_instance, globals())
</pre>
<p> If necessary, these functions may be replaced by removing the appropriate declaration line, and then adding the function as normal. </p>
<p> These functions are required for all cloud modules, and are described in detail in the next section.</p>
<h3>Non-Libcloud Based Modules</h3>
<p> In some cases, using libcloud is not an option. This may be because libcloud has not yet included the necessary driver itself, or it may be that the driver that is included with libcloud does not contain all of the necessary features required by the developer. When this is the case, some or all of the functions in <code>libcloudfuncs</code> may be replaced. If they are all replaced, the libcloud imports should be absent from the Salt Cloud module. </p>
<p> A good example of a non-libcloud provider is the DigitalOcean module: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt/tree/develop/salt/cloud/clouds/digital_ocean.py" target="_blank">https://github.com/saltstack/salt/tree/develop/salt/cloud/clouds/digital_ocean.py</a></i></p>
<h3>The <code>create()</code> Function</h3>
<p> The <code>create()</code> function must be created as described in the libcloud-based module documentation.</p>
<h3>The get_size() Function</h3>
<p> This function is only necessary for libcloud-based modules, and does not need to exist otherwise.</p>
<h3>The get_image() Function</h3>
<p> This function is only necessary for libcloud-based modules, and does not need to exist otherwise.</p>
<h3>The avail_locations() Function</h3>
<p> This function returns a list of locations available, if the cloud provider uses multiple data centers. It is not necessary if the cloud provider only uses one data center. It is normally called using the <code>&#8211;list-locations</code> option. </p>
<pre>
salt-cloud --list-locations my-cloud-provider
</pre>
<h3>The avail_images() Function</h3>
<p> This function returns a list of images available for this cloud provider. There are not currently any known cloud providers that do not provide this functionality, though they may refer to images by a different name (for example, &quot;templates&quot;). It is normally called using the <code>&#8211;list-images</code> option. </p>
<pre>
salt-cloud --list-images my-cloud-provider
</pre>
<h3>The avail_sizes() Function</h3>
<p> This function returns a list of sizes available for this cloud provider. Generally, this refers to a combination of RAM, CPU, and/or disk space. This functionality may not be present on some cloud providers. For example, the Parallels module breaks down RAM, CPU, and disk space into separate options, whereas in other providers, these options are baked into the image. It is normally called using the <code>&#8211;list-sizes</code> option. </p>
<pre>
salt-cloud --list-sizes my-cloud-provider
</pre>
<h3>The script() Function</h3>
<p> This function builds the deploy script to be used on the remote machine. It is likely to be moved into the <code>salt.utils.cloud</code> library in the near future, as it is very generic and can usually be copied wholesale from another module. An excellent example is in the Azure driver.</p>
<h3>The destroy() Function</h3>
<p> This function irreversibly destroys a virtual machine on the cloud provider. Before doing so, it should fire an event on the Salt event bus. The tag for this event is <code>salt/cloud/&lt;vm name&gt;/destroying</code>. Once the virtual machine has been destroyed, another event is fired. The tag for that event is <code>salt/cloud/&lt;vm name&gt;/destroyed</code>. </p>
<p> This function is normally called with the <code>-d</code> options: </p>
<pre>
salt-cloud -d myinstance
</pre>
<h3>The list_nodes() Function</h3>
<p> This function returns a list of nodes available on this cloud provider, using the following fields:</p>
<dl>
<dt>&bull;</p>
<dd> id (str)</p>
<dt>&bull;</p>
<dd> image (str)</p>
<dt>&bull;</p>
<dd> size (str)</p>
<dt>&bull;</p>
<dd> state (str)</p>
<dt>&bull;</p>
<dd> private_ips (list)</p>
<dt>&bull;</p>
<dd> public_ips (list) </p>
<p> No other fields should be returned in this function, and all of these fields should be returned, even if empty. The private_ips and public_ips fields should always be of a list type, even if empty, and the other fields should always be of a str type. This function is normally called with the <code>-Q</code> option: </p>
<pre>
salt-cloud -Q
</pre>
</dl>
<h3>The list_nodes_full() Function</h3>
<p> All information available about all nodes should be returned in this function. The fields in the list_nodes() function should also be returned, even if they would not normally be provided by the cloud provider. This is because some functions both within Salt and 3rd party will break if an expected field is not present. This function is normally called with the <code>-F</code> option: </p>
<pre>
salt-cloud -F
</pre>
<h3>The list_nodes_select() Function</h3>
<p> This function returns only the fields specified in the <code>query.selection</code> option in <code>/etc/salt/cloud</code>. Because this function is so generic, all of the heavy lifting has been moved into the <code>salt.utils.cloud</code> library. </p>
<p> A function to call <code>list_nodes_select()</code> still needs to be present. In general, the following code can be used as-is: </p>
<pre>
def list_nodes_select(call=None):
    '''
    Return a list of the VMs that are on the provider, with select fields
    '''
    return salt.utils.cloud.list_nodes_select(
        list_nodes_full('function'), __opts__['query.selection'], call,
    )
</pre>
<p> However, depending on the cloud provider, additional variables may be required. For instance, some modules use a <code>conn</code> object, or may need to pass other options into <code>list_nodes_full()</code>. In this case, be sure to update the function appropriately: </p>
<pre>
def list_nodes_select(conn=None, call=None):
    '''
    Return a list of the VMs that are on the provider, with select fields
    '''
    if not conn:
        conn = get_conn()   # pylint: disable=E0602
    return salt.utils.cloud.list_nodes_select(
        list_nodes_full(conn, 'function'),
        __opts__['query.selection'],
        call,
    )
</pre>
<p> This function is normally called with the <code>-S</code> option: </p>
<pre>
salt-cloud -S
</pre>
<h3>The show_instance() Function</h3>
<p> This function is used to display all of the information about a single node that is available from the cloud provider. The simplest way to provide this is usually to call <code>list_nodes_full()</code>, and return just the data for the requested node. It is normally called as an action: </p>
<pre>
salt-cloud -a show_instance myinstance
</pre>
<h3>Actions and Functions</h3>
<p> Extra functionality may be added to a cloud provider in the form of an <code>&#8211;action</code> or a <code>&#8211;function</code>. Actions are performed against a cloud instance/virtual machine, and functions are performed against a cloud provider.</p>
<h3>Actions</h3>
<p> Actions are calls that are performed against a specific instance or virtual machine. The <code>show_instance</code> action should be available in all cloud modules. Actions are normally called with the <code>-a</code> option: </p>
<pre>
salt-cloud -a show_instance myinstance
</pre>
<p> Actions must accept a <code>name</code> as a first argument, may optionally support any number of kwargs as appropriate, and must accept an argument of <code>call</code>, with a default of <code>None</code>. </p>
<p> Before performing any other work, an action should normally verify that it has been called correctly. It may then perform the desired feature, and return useful information to the user. A basic action looks like: </p>
<p>def show_instance(name, call = None)<br />
    :<br />
&#8221;&#8217; Show the details from EC2 concerning an AMI<br />
&#8221;&#8217; if call != &#8216;action&#8217; : raise SaltCloudSystemExit(<br />
                               &#8216;The show_instance action must be called with -a or &#8211;action.&#8217;) return _get_node(name)</p>
<p> Please note that generic kwargs, if used, are passed through to actions as <code>kwargs</code> and not <code>**kwargs</code>. An example of this is seen in the Functions section.</p>
<h3>Functions</h3>
<p> Functions are called that are performed against a specific cloud provider. An optional function that is often useful is <code>show_image</code>, which describes an image in detail. Functions are normally called with the <code>-f</code> option: </p>
<pre>
salt-cloud -f show_image my-cloud-provider image='Ubuntu 13.10 64-bit'
</pre>
<p> A function may accept any number of kwargs as appropriate, and must accept an argument of <code>call</code> with a default of <code>None</code>. </p>
<p> Before performing any other work, a function should normally verify that it has been called correctly. It may then perform the desired feature, and return useful information to the user. A basic function looks like: </p>
<p>def show_image(kwargs, call = None)<br />
    :<br />
    &#8221;&#8217; Show the details from EC2 concerning an AMI<br />
    &#8221;&#8217; if call != &#8216;function&#8217; : raise SaltCloudSystemExit(<br />
                                     &#8216;The show_image action must be called with -f or &#8211;function.&#8217;)<br />
                                     params = {&#8216;ImageId.1&#8217; : kwargs[&#8216;image&#8217;],<br />
                                               &#8216;Action&#8217; : &#8216;DescribeImages&#8217;} result = query(params)<br />
                                                                                         log.info(result) return result</p>
<p> Take note that generic kwargs are passed through to functions as <code>kwargs</code> and not <code>**kwargs</code>.</p>
<h3>OS Support for Cloud VMs</h3>
<p> Salt Cloud works primarily by executing a script on the virtual machines as soon as they become available. The script that is executed is referenced in the cloud profile as the <code>script</code>. In older versions, this was the <code>os</code> argument. This was changed in 0.8.2. </p>
<p> A number of legacy scripts exist in the deploy directory in the saltcloud source tree. The preferred method is currently to use the salt-bootstrap script. A stable version is included with each release tarball starting with 0.8.4. The most updated version can be found at: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-bootstrap" target="_blank">https://github.com/saltstack/salt-bootstrap</a></i> </p>
<p> If you do not specify a script argument, this script will be used at the default. </p>
<p> If the Salt Bootstrap script does not meet your needs, you may write your own. The script should be written in bash and is a Jinja template. Deploy scripts need to execute a number of functions to do a complete salt setup. These functions include:</p>
<dl>
<dt>1.</p>
<dd> Install the salt minion. If this can be done via system packages this method is HIGHLY preferred.</p>
<dt>2.</p>
<dd> Add the salt minion keys before the minion is started for the first time. The minion keys are available as strings that can be copied into place in the Jinja template under the dict named &quot;vm&quot;.</p>
<dt>3.</p>
<dd> Start the salt-minion daemon and enable it at startup time.</p>
<dt>4.</p>
<dd> Set up the minion configuration file from the &quot;minion&quot; data available in the Jinja template. </p>
<p> A good, well commented, example of this process is the Fedora deployment script: </p>
<p> <i><a rel="nofollow noopener" href="https://github.com/saltstack/salt-cloud/blob/master/saltcloud/deploy/Fedora.sh" target="_blank">https://github.com/saltstack/salt-cloud/blob/master/saltcloud/deploy/Fedora.sh</a></i> </p>
<p> A number of legacy deploy scripts are included with the release tarball. None of them are as functional or complete as Salt Bootstrap, and are still included for academic purposes.</dl>
<h3>Other Generic Deploy Scripts</h3>
<p> If you want to be assured of always using the latest Salt Bootstrap script, there are a few generic templates available in the deploy directory of your saltcloud source tree: </p>
<pre>
curl-bootstrap
curl-bootstrap-git
python-bootstrap
wget-bootstrap
wget-bootstrap-git
</pre>
<p> These are example scripts which were designed to be customized, adapted, and refit to meet your needs. One important use of them is to pass options to the salt-bootstrap script, such as updating to specific git tags.</p>
<h3>Post-Deploy Commands</h3>
<p> Once a minion has been deployed, it has the option to run a salt command. Normally, this would be the state.highstate command, which would finish provisioning the VM. Another common option is state.sls, or for just testing, test.ping. This is configured in the main cloud config file: </p>
<pre>
start_action: state.highstate
</pre>
<p> This is currently considered to be experimental functionality, and may not work well with all providers. If you experience problems with Salt Cloud hanging after Salt is deployed, consider using Startup States instead: </p>
<p> <i><a rel="nofollow noopener" href="http://docs.saltstack.com/ref/states/startup.html" target="_blank">http://docs.saltstack.com/ref/states/startup.html</a></i></p>
<h3>Skipping the Deploy Script</h3>
<p> For whatever reason, you may want to skip the deploy script altogether. This results in a VM being spun up much faster, with absolutely no configuration. This can be set from the command line: </p>
<pre>
salt-cloud --no-deploy -p micro_aws my_instance
</pre>
<p> Or it can be set from the main cloud config file: </p>
<pre>
deploy: False
</pre>
<p> Or it can be set from the provider&#8217;s configuration: </p>
<pre>
RACKSPACE.user: example_user
RACKSPACE.apikey: 123984bjjas87034
RACKSPACE.deploy: False
</pre>
<p> Or even on the VM&#8217;s profile settings: </p>
<pre>
ubuntu_aws:
  provider: aws
  image: ami-7e2da54e
  size: t1.micro
  deploy: False
</pre>
<p> The default for deploy is True. </p>
<p> In the profile, you may also set the script option to <code>None</code>: </p>
<pre>
script: None
</pre>
<p> This is the slowest option, since it still uploads the None deploy script and executes it.</p>
<h3>Updating Salt Bootstrap</h3>
<p> Salt Bootstrap can be updated automatically with salt-cloud: </p>
<pre>
salt-cloud -u
salt-cloud --update-bootstrap
</pre>
<p> Bear in mind that this updates to the latest (unstable) version, so use with caution.</p>
<h3>Keeping /tmp/ Files</h3>
<p> When Salt Cloud deploys an instance, it uploads temporary files to /tmp/ for salt-bootstrap to put in place. After the script has run, they are deleted. To keep these files around (mostly for debugging purposes), the &#8211;keep-tmp option can be added: </p>
<pre>
salt-cloud -p myprofile mymachine --keep-tmp
</pre>
<p> For those wondering why /tmp/ was used instead of /root/, this had to be done for images which require the use of sudo, and therefore do not allow remote root logins, even for file transfers (which makes /root/ unavailable).</p>
<h3>Deploy Script Arguments</h3>
<p> Custom deploy scripts are unlikely to need custom arguments to be passed to them, but salt-bootstrap has been extended quite a bit, and this may be necessary. script_args can be specified in either the profile or the map file, to pass arguments to the deploy script: </p>
<pre>
aws-amazon:
    provider: aws
    image: ami-1624987f
    size: t1.micro
    ssh_username: ec2-user
    script: bootstrap-salt
    script_args: -c /tmp/
</pre>
<p> This has also been tested to work with pipes, if needed: </p>
<pre>
script_args: | head
</pre>
<h3>Using Salt Cloud from Salt</h3>
<h3>Using the Salt Modules for Cloud</h3>
<p> In addition to the <code>salt-cloud</code> command, Salt Cloud can be called from Salt, in a variety of different ways. Most users will be interested in either the execution module or the state module, but it is also possible to call Salt Cloud as a runner. </p>
<p> Because the actual work will be performed on a remote minion, the normal Salt Cloud configuration must exist on any target minion that needs to execute a Salt Cloud command. Because Salt Cloud now supports breaking out configuration into individual files, the configuration is easily managed using Salt&#8217;s own <code>file.managed</code> state function. For example, the following directories allow this configuration to be managed easily: </p>
<pre>
/etc/salt/cloud.providers.d/
/etc/salt/cloud.profiles.d/
</pre>
<h3>Minion Keys</h3>
<p> Keep in mind that when creating minions, Salt Cloud will create public and private minion keys, upload them to the minion, and place the public key on the machine that created the minion. It will <i>not</i> attempt to place any public minion keys on the master, unless the minion which was used to create the instance is also the Salt Master. This is because granting arbitrary minions access to modify keys on the master is a serious security risk, and must be avoided.</p>
<h3>Execution Module</h3>
<p> The <code>cloud</code> module is available to use from the command line. At the moment, almost every standard Salt Cloud feature is available to use. The following commands are available:</p>
<h3>list_images</h3>
<p> This command is designed to show images that are available to be used to create an instance using Salt Cloud. In general they are used in the creation of profiles, but may also be used to create an instance directly (see below). Listing images requires a provider to be configured, and specified: </p>
<pre>
salt myminion cloud.list_images my-cloud-provider
</pre>
<h3>list_sizes</h3>
<p> This command is designed to show sizes that are available to be used to create an instance using Salt Cloud. In general they are used in the creation of profiles, but may also be used to create an instance directly (see below). This command is not available for all cloud providers; see the provider-specific documentation for details. Listing sizes requires a provider to be configured, and specified: </p>
<pre>
salt myminion cloud.list_sizes my-cloud-provider
</pre>
<h3>list_locations</h3>
<p> This command is designed to show locations that are available to be used to create an instance using Salt Cloud. In general they are used in the creation of profiles, but may also be used to create an instance directly (see below). This command is not available for all cloud providers; see the provider-specific documentation for details. Listing locations requires a provider to be configured, and specified: </p>
<pre>
salt myminion cloud.list_locations my-cloud-provider
</pre>
<h3>query</h3>
<p> This command is used to query all configured cloud providers, and display all instances associated with those accounts. By default, it will run a standard query, returning the following fields:</p>
<dl>
<dt><code>id</code></p>
<dd> The name or ID of the instance, as used by the cloud provider.</p>
<dt><code>image</code></p>
<dd> The disk image that was used to create this instance.</p>
<dt><code>private_ips</code></p>
<dd> Any public IP addresses currently assigned to this instance.</p>
<dt><code>public_ips</code></p>
<dd> Any private IP addresses currently assigned to this instance.</p>
<dt><code>size</code></p>
<dd> The size of the instance; can refer to RAM, CPU(s), disk space, etc., depending on the cloud provider.</p>
<dt><code>state</code></p>
<dd> The running state of the instance; for example, <code>running</code>, <code>stopped</code>, <code>pending</code>, etc. This state is dependent upon the provider. </p>
<p> This command may also be used to perform a full query or a select query, as described below. The following usages are available: </p>
<pre>
salt myminion cloud.query
salt myminion cloud.query list_nodes
salt myminion cloud.query list_nodes_full
</pre>
</dl>
<h3>full_query</h3>
<p> This command behaves like the <code>query</code> command, but lists all information concerning each instance as provided by the cloud provider, in addition to the fields returned by the <code>query</code> command. </p>
<pre>
salt myminion cloud.full_query
</pre>
<h3>select_query</h3>
<p> This command behaves like the <code>query</code> command, but only returned select fields as defined in the <code>/etc/salt/cloud</code> configuration file. A sample configuration for this section of the file might look like: </p>
<pre>
query.selection:
  - id
  - key_name
</pre>
<p> This configuration would only return the <code>id</code> and <code>key_name</code> fields, for those cloud providers that support those two fields. This would be called using the following command: </p>
<pre>
salt myminion cloud.select_query
</pre>
<h3>profile</h3>
<p> This command is used to create an instance using a profile that is configured on the target minion. Please note that the profile must be configured before this command can be used with it. </p>
<pre>
salt myminion cloud.profile ec2-centos64-x64 my-new-instance
</pre>
<p> Please note that the execution module does <i>not</i> run in parallel mode. Using multiple minions to create instances can effectively perform parallel instance creation.</p>
<h3>create</h3>
<p> This command is similar to the <code>profile</code> command, in that it is used to create a new instance. However, it does not require a profile to be pre-configured. Instead, all of the options that are normally configured in a profile are passed directly to Salt Cloud to create the instance: </p>
<pre>
salt myminion cloud.create my-ec2-config my-new-instance \
    image=ami-1624987f size='t1.micro' ssh_username=ec2-user \
    securitygroup=default delvol_on_destroy=True
</pre>
<p> Please note that the execution module does <i>not</i> run in parallel mode. Using multiple minions to create instances can effectively perform parallel instance creation.</p>
<h3>destroy</h3>
<p> This command is used to destroy an instance or instances. This command will search all configured providers and remove any instance(s) which matches the name(s) passed in here. The results of this command are <i>non-reversable</i> and should be used with caution. </p>
<pre>
salt myminion cloud.destroy myinstance
salt myminion cloud.destroy myinstance1,myinstance2
</pre>
<h3>action</h3>
<p> This command implements both the <code>action</code> and the <code>function</code> commands used in the standard <code>salt-cloud</code> command. If one of the standard <code>action</code> commands is used, an instance name must be provided. If one of the standard <code>function</code> commands is used, a provider configuration must be named. </p>
<pre>
salt myminion cloud.action start instance=myinstance
salt myminion cloud.action show_image provider=my-ec2-config \
    image=ami-1624987f
</pre>
<p> The actions available are largely dependent upon the module for the specific cloud provider. The following actions are available for all cloud providers:</p>
<dl>
<dt><code>list_nodes</code></p>
<dd> This is a direct call to the <code>query</code> function as described above, but is only performed against a single cloud provider. A provider configuration must be included.</p>
<dt><code>list_nodes_select</code></p>
<dd> This is a direct call to the <code>full_query</code> function as described above, but is only performed against a single cloud provider. A provider configuration must be included.</p>
<dt><code>list_nodes_select</code></p>
<dd> This is a direct call to the <code>select_query</code> function as described above, but is only performed against a single cloud provider. A provider configuration must be included.</p>
<dt><code>show_instance</code></p>
<dd> This is a thin wrapper around <code>list_nodes</code>, which returns the full information about a single instance. An instance name must be provided.</dl>
<h3>State Module</h3>
<p> A subset of the execution module is available through the <code>cloud</code> state module. Not all functions are currently included, because there is currently insufficient code for them to perform statefully. For example, a command to create an instance may be issued with a series of options, but those options cannot currently be statefully managed. Additional states to manage these options will be released at a later time.</p>
<h3>cloud.present</h3>
<p> This state will ensure that an instance is present inside a particular cloud provider. Any option that is normally specified in the <code>cloud.create</code> execution module and function may be declared here, but only the actual presence of the instance will be managed statefully. </p>
<pre>
my-instance-name:
  cloud.present:
    - provider: my-ec2-config
    - image: ami-1624987f
    - size: 't1.micro'
    - ssh_username: ec2-user
    - securitygroup: default
    - delvol_on_destroy: True
</pre>
<h3>cloud.profile</h3>
<p> This state will ensure that an instance is present inside a particular cloud provider. This function calls the <code>cloud.profile</code> execution module and function, but as with <code>cloud.present</code>, only the actual presence of the instance will be managed statefully. </p>
<pre>
my-instance-name:
  cloud.profile:
    - profile: ec2-centos64-x64
</pre>
<h3>cloud.absent</h3>
<p> This state will ensure that an instance (identified by name) does not exist in any of the cloud providers configured on the target minion. Please note that this state is <i>non-reversable</i> and may be considered especially destructive when issued as a cloud state. </p>
<pre>
my-instance-name:
  cloud.absent
</pre>
<h3>Runner Module</h3>
<p> The <code>cloud</code> runner module is executed on the master, and performs actions using the configuration and Salt modules on the master itself. This means that any public minion keys will also be properly accepted by the master. </p>
<p> Using the functions in the runner module is no different than using those in the execution module, outside of the behavior described in the above paragraph. The following functions are available inside the runner:</p>
<dl>
<dt>&bull;</p>
<dd> list_images</p>
<dt>&bull;</p>
<dd> list_sizes</p>
<dt>&bull;</p>
<dd> list_locations</p>
<dt>&bull;</p>
<dd> query</p>
<dt>&bull;</p>
<dd> full_query</p>
<dt>&bull;</p>
<dd> select_query</p>
<dt>&bull;</p>
<dd> profile</p>
<dt>&bull;</p>
<dd> destroy</p>
<dt>&bull;</p>
<dd> action </p>
<p> Outside of the standard usage of <code>salt-run</code> itself, commands are executed as usual: </p>
<pre>
salt-run cloud.profile ec2-centos64-x86_64 my-instance-name
</pre>
</dl>
<h3>CloudClient</h3>
<p> The execution, state, and runner modules ultimately all use the CloudClient library that ships with Salt. To use the CloudClient library locally (either on the master or a minion), create a client object and issue a command against it: </p>
<pre>
import salt.cloud
import pprint
client = salt.cloud.CloudClient('/etc/salt/cloud')
nodes = client.query()
pprint.pprint(nodes)
</pre>
<h3>Feature Comparison</h3>
<h3>Feature Matrix</h3>
<p> A number of features are available in most cloud providers, but not all are available everywhere. This may be because the feature isn&#8217;t supported by the cloud provider itself, or it may only be that the feature has not yet been added to Salt Cloud. In a handful of cases, it is because the feature does not make sense for a particular cloud provider (Saltify, for instance). </p>
<p> This matrix shows which features are available in which cloud providers, as far as Salt Cloud is concerned. This is not a comprehensive list of all features available in all cloud providers, and should not be used to make business decisions concerning choosing a cloud provider. In most cases, adding support for a feature to Salt Cloud requires only a little effort.</p>
<h3>Legacy Drivers</h3>
<p> Both AWS and Rackspace are listed as &quot;Legacy&quot;. This is because those drivers have been replaced by other drivers, which are generally the preferred method for working with those providers. </p>
<p> The EC2 driver should be used instead of the AWS driver, when possible. The OpenStack driver should be used instead of the Rackspace driver, unless the user is dealing with instances in &quot;the old cloud&quot; in Rackspace.</p>
<h3>Note for Developers</h3>
<p> When adding new features to a particular cloud provider, please make sure to add the feature to this table. Additionally, if you notice a feature that is not properly listed here, pull requests to fix them is appreciated.</p>
<h3>Standard Features</h3>
<p> These are features that are available for almost every provider. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> AWS (Legacy) </td>
<td> CloudStack </td>
<td> Digital Ocean </td>
<td> EC2 </td>
<td> GoGrid </td>
<td> JoyEnt </td>
<td> Linode </td>
<td> OpenStack </td>
<td> Parallels </td>
<td> Rackspace (Legacy) </td>
<td> Saltify </td>
<td> Softlayer </td>
<td> Softlayer Hardware </td>
<td> Aliyun
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Query </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Full Query </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Selective Query </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> List Sizes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> List Images </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> List Locations </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> create </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> destroy </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Actions</h3>
<p> These are features that are performed on a specific instance, and require an instance name to be passed in. For example: </p>
<pre>
# salt-cloud -a attach_volume ami.example.com
</pre>
<p> <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Actions </td>
<td> AWS (Legacy) </td>
<td> CloudStack </td>
<td> Digital Ocean </td>
<td> EC2 </td>
<td> GoGrid </td>
<td> JoyEnt </td>
<td> Linode </td>
<td> OpenStack </td>
<td> Parallels </td>
<td> Rackspace (Legacy) </td>
<td> Saltify </td>
<td> Softlayer </td>
<td> Softlayer Hardware </td>
<td> Aliyun
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> attach_volume </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> create_attach_volumes </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> del_tags </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> delvol_on_destroy </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> detach_volume </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> disable_term_protect </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> enable_term_protect </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_tags </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> keepvol_on_destroy </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_keypairs </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> rename </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> set_tags </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_delvol_on_destroy </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_instance </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_term_protect </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> start </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> stop </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> take_action </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Functions</h3>
<p> These are features that are performed against a specific cloud provider, and require the name of the provider to be passed in. For example: </p>
<pre>
# salt-cloud -f list_images my_digitalocean
</pre>
<p> <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Functions </td>
<td> AWS (Legacy) </td>
<td> CloudStack </td>
<td> Digital Ocean </td>
<td> EC2 </td>
<td> GoGrid </td>
<td> JoyEnt </td>
<td> Linode </td>
<td> OpenStack </td>
<td> Parallels </td>
<td> Rackspace (Legacy) </td>
<td> Saltify </td>
<td> Softlayer </td>
<td> Softlayer Hardware </td>
<td> Aliyun
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> block_device_mappings </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> create_keypair </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> create_volume </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> delete_key </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> delete_keypair </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> delete_volume </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_image </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_ip </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_key </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_keyid </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_keypair </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_networkid </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_node </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_password </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_size </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_spot_config </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> get_subnetid </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> iam_profile </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> import_key </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> key_list </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> keyname </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_availability_zones </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_custom_images </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_keys </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_nodes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_nodes_full </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_nodes_select </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> list_vlans </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> rackconnect </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> reboot </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> reformat_node </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> securitygroup </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> securitygroupid </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_image </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_key </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_keypair </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> show_volume </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> Yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=15>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Tutorials</h3>
<h3>Using Salt Cloud with the Event Reactor</h3>
<p> One of the most powerful features of the Salt framework is the Event Reactor. As the Reactor was in development, Salt Cloud was regularly updated to take advantage of the Reactor upon completion. As such, various aspects of both the creation and destruction of instances with Salt Cloud fire events to the Salt Master, which can be used by the Event Reactor.</p>
<h3>Event Structure</h3>
<p> As of this writing, all events in Salt Cloud have a tag, which includes the ID of the instance being managed, and a payload which describes the task that is currently being handled. A Salt Cloud tag looks like: </p>
<pre>
salt/cloud/&lt;minion_id&gt;/&lt;task&gt;
</pre>
<p> For instance, the first event fired when creating an instance named <code>web1</code> would look like: </p>
<pre>
salt/cloud/web1/creating
</pre>
<p> Assuming this instance is using the <code>ec2-centos</code> profile, which is in turn using the <code>ec2-config</code> provider, the payload for this tag would look like: </p>
<pre>
{'name': 'web1',
 'profile': 'ec2-centos',
 'provider': 'ec2-config'}
</pre>
<h3>Available Events</h3>
<p> When an instance is created in Salt Cloud, whether by map, profile, or directly through an API, a minimum of five events are normally fired. More may be available, depending upon the cloud provider being used. Some of the common events are described below.</p>
<h3>salt/cloud/&lt;minion_id&gt;/creating</h3>
<p> This event states simply that the process to create an instance has begun. At this point in time, no actual work has begun. The payload for this event includes: </p>
<p> name profile provider</p>
<h3>salt/cloud/&lt;minion_id&gt;/requesting</h3>
<p> Salt Cloud is about to make a request to the cloud provider to create an instance. At this point, all of the variables required to make the request have been gathered, and the payload of the event will reflect those variables which do not normally pose a security risk. What is returned here is dependent upon the cloud provider. Some common variables are: </p>
<p> name image size location</p>
<h3>salt/cloud/&lt;minion_id&gt;/querying</h3>
<p> The instance has been successfully requested, but the necessary information to log into the instance (such as IP address) is not yet available. This event marks the beginning of the process to wait for this information. </p>
<p> The payload for this event normally only includes the <code>instance_id</code>.</p>
<h3>salt/cloud/&lt;minion_id&gt;/waiting_for_ssh</h3>
<p> The information required to log into the instance has been retrieved, but the instance is not necessarily ready to be accessed. Following this event, Salt Cloud will wait for the IP address to respond to a ping, then wait for the specified port (usually 22) to respond to a connection, and on Linux systems, for SSH to become available. Salt Cloud will attempt to issue the <code>date</code> command on the remote system, as a means to check for availability. If no <code>ssh_username</code> has been specified, a list of usernames (starting with <code>root</code>) will be attempted. If one or more usernames was configured for <code>ssh_username</code>, they will be added to the beginning of the list, in order. </p>
<p> The payload for this event normally only includes the <code>ip_address</code>.</p>
<h3>salt/cloud/&lt;minion_id&gt;/deploying</h3>
<p> The necessary port has been detected as available, and now Salt Cloud can log into the instance, upload any files used for deployment, and run the deploy script. Once the script has completed, Salt Cloud will log back into the instance and remove any remaining files. </p>
<p> A number of variables are used to deploy instances, and the majority of these will be available in the payload. Any keys, passwords or other sensitive data will be scraped from the payload. Most of the variables returned will be related to the profile or provider config, and any default values that could have been changed in the profile or provider, but weren&#8217;t.</p>
<h3>salt/cloud/&lt;minion_id&gt;/created</h3>
<p> The deploy sequence has completed, and the instance is now available, Salted, and ready for use. This event is the final task for Salt Cloud, before returning instance information to the user and exiting. </p>
<p> The payload for this event contains little more than the initial <code>creating</code> event. This event is required in all cloud providers.</p>
<h3>Configuring the Event Reactor</h3>
<p> The Event Reactor is built into the Salt Master process, and as such is configured via the master configuration file. Normally this will will be a YAML file located at <code>/etc/salt/master</code>. Additionally, master configuration items can be stored, in YAML format, inside the <code>/etc/salt/master.d/</code> directory. </p>
<p> These configuration items may be stored in either location; however, they may only be stored in one location. For organizational and security purposes, it may be best to create a single configuration file, which contains only Event Reactor configuration, at <code>/etc/salt/master.d/reactor</code>. </p>
<p> The Event Reactor uses a top-level configuration item called <code>reactor</code>. This block contains a list of tags to be watched for, each of which also includes a list of <code>sls</code> files. For instance: </p>
<pre>
reactor:
  - 'salt/minion/*/start':
    - '/srv/reactor/custom-reactor.sls'
  - 'salt/cloud/*/created':
    - '/srv/reactor/cloud-alert.sls'
  - 'salt/cloud/*/destroyed':
    - '/srv/reactor/cloud-destroy-alert.sls'
</pre>
<p> The above configuration configures reactors for three different tags: one which is fired when a minion process has started and is available to receive commands, one which is fired when a cloud instance has been created, and one which is fired when a cloud instance is destroyed. </p>
<p> Note that each tag contains a wildcard (<code>*</code>) in it. For each of these tags, this will normally refer to a <code>minion_id</code>. This is not required of event tags, but is very common.</p>
<h3>Reactor SLS Files</h3>
<p> Reactor <code>sls</code> files should be placed in the <code>/srv/reactor/</code> directory for consistency between environments, but this is not currently enforced by Salt. </p>
<p> Reactor <code>sls</code> files follow a similar format to other <code>sls</code> files in Salt. By default they are written in YAML and can be templated using Jinja, but since they are processed through Salt&#8217;s rendering system, any available renderer (JSON, Mako, Cheetah, etc.) can be used. </p>
<p> As with other <code>sls</code> files, each stanza will start with a declaration ID, followed by the function to run, and then any arguments for that function. For example: </p>
<p>#/ srv / reactor / cloud &#8211; alert.sls<br />
new_instance_alert : cmd.pagerduty.create_event : -tgt : alertserver &#8211; kwarg : description : &#8220;New instance: &#123;&#123; data[&#8216;name&#8217;] }}&#8221; details : &#8220;New cloud instance created on &#123;&#123; data[&#8216;provider&#8217;] }}&#8221; service_key : 1626dead5ecafe46231e968eb1be29c4 profile : my &#8211; pagerduty &#8211; account</p>
<p> When the Event Reactor receives an event notifying it that a new instance has been created, this <code>sls</code> will create a new incident in PagerDuty, using the configured PagerDuty account. </p>
<p> The declaration ID in this example is <code>new_instance_alert</code>. The function called is <code>cmd.pagerduty.create_event</code>. The <code>cmd</code> portion of this function specifies that an execution module and function will be called, in this case, the <code>pagerduty.create_event</code> function. </p>
<p> Because an execution module is specified, a target (<code>tgt</code>) must be specified on which to call the function. In this case, a minion called <code>alertserver</code> has been used. Any arguments passed through to the function are declared in the <code>kwarg</code> block.</p>
<h3>Example: Reactor-Based Highstate</h3>
<p> When Salt Cloud creates an instance, by default it will install the Salt Minion onto the instance, along with any specified minion configuration, and automatically accept that minion&#8217;s keys on the master. One of the configuration options that can be specified is <code>startup_states</code>, which is commonly set to <code>highstate</code>. This will tell the minion to immediately apply a highstate, as soon as it is able to do so. </p>
<p> This can present a problem with some system images on some cloud providers. For instance, Salt Cloud can be configured to log in as either the <code>root</code> user, or a user with <code>sudo</code> access. While some providers commonly use images that lock out remote <code>root</code> access and require a user with <code>sudo</code> privileges to log in (notably EC2, with their <code>ec2-user</code> login), most cloud providers fall back to <code>root</code> as the default login on all images, including for operating systems (such as Ubuntu) which normally disallow remote <code>root</code> login. </p>
<p> For users of these operating systems, it is understandable that a highstate would include configuration to block remote <code>root</code> logins again. However, Salt Cloud may not have finished cleaning up its deployment files by the time the minion process has started, and kicked off a highstate run. Users have reported errors from Salt Cloud getting locked out while trying to clean up after itself. </p>
<p> The goal of a startup state may be achieved using the Event Reactor. Because a minion fires an event when it is able to receive commands, this event can effectively be used inside the reactor system instead. The following will point the reactor system to the right <code>sls</code> file: </p>
<pre>
reactor:
  - 'salt/cloud/*/created':
    - '/srv/reactor/startup_highstate.sls'
</pre>
<p> And the following <code>sls</code> file will start a highstate run on the target minion: </p>
<p>#/ srv / reactor / startup_highstate.sls<br />
reactor_highstate : cmd.state.highstate : -tgt:<br />
{<br />
    {<br />
        data[&#8216;name&#8217;]<br />
    }<br />
}</p>
<p> Because this event will not be fired until Salt Cloud has cleaned up after itself, the highstate run will not step on Salt Cloud&#8217;s toes. And because every file on the minion is configurable, including <code>/etc/salt/minion</code>, the <code>startup_states</code> can still be configured for future minion restarts, if desired.</p>
<h2 id="NETAPI MODULES"></h2>
<h3>Writing netapi modules</h3>
<p> <code>netapi</code> modules, put simply, bind a port and start a service. They are purposefully open-ended and can be used to present a variety of external interfaces to Salt, and even present multiple interfaces at once. </p>
<p> <code>SEE ALSO:</code> The full list of netapi modules</p>
<h3>Configuration</h3>
<p> All <code>netapi</code> configuration is done in the Salt master config and takes a form similar to the following: </p>
<pre>
rest_cherrypy:
  port: 8000
  debug: True
  ssl_crt: /etc/pki/tls/certs/localhost.crt
  ssl_key: /etc/pki/tls/certs/localhost.key
</pre>
<h3>The <code>__virtual__</code> function</h3>
<p> Like all module types in Salt, <code>netapi</code> modules go through Salt&#8217;s loader interface to determine if they should be loaded into memory and then executed. </p>
<p> The <code>__virtual__</code> function in the module makes this determination and should return <code>False</code> or a string that will serve as the name of the module. If the module raises an <code>ImportError</code> or any other errors, it will not be loaded.</p>
<h3>The <code>start</code> function</h3>
<p> The <code>start()</code> function will be called for each <code>netapi</code> module that is loaded. This function should contain the server loop that actually starts the service. This is started in a multiprocess.</p>
<h3>Inline documentation</h3>
<p> As with the rest of Salt, it is a best-practice to include liberal inline documentation in the form of a module docstring and docstrings on any classes, methods, and functions in your <code>netapi</code> module.</p>
<h3>Loader âmagicâ methods</h3>
<p> The loader makes the <code>__opts__</code> data structure available to any function in a <code>netapi</code> module.</p>
<h3>Introduction to netapi modules</h3>
<p> netapi modules provide API-centric access to Salt. Usually externally-facing services such as REST or WebSockets, XMPP, XMLRPC, etc. </p>
<p> In general netapi modules bind to a port and start a service. They are purposefully open-ended. A single module can be configured to run as well as multiple modules simultaneously. </p>
<p> netapi modules are enabled by adding configuration to your Salt Master config file and then starting the <code>salt-api</code> daemon. Check the docs for each module to see external requirements and configuration settings. </p>
<p> Communication with Salt and Salt satellite projects is done using Salt&#8217;s own Python API. A list of available client interfaces is below.</p>
<dl>
<dt>salt-api</p>
<dd>
<p> Prior to Salt&#8217;s 2014.7.0 release, netapi modules lived in the separate sister projected <code>salt-api</code>. That project has been merged into the main Salt project. </p>
<p> <code>SEE ALSO:</code> The full list of netapi modules</dl>
<h3>Client interfaces</h3>
<p> Salt&#8217;s client interfaces expose executing functions by crafting a dictionary of values that are mapped to function arguments. This allows calling functions simply by creating a data structure. (And this is exactly how much of Salt&#8217;s own internals work!)</p>
<dl>
<dt><code>class salt.netapi.NetapiClient(opts)</code></p>
<dd> Provide a uniform method of accessing the various client interfaces in Salt in the form of low-data data structures. For example: </p>
<pre>
&gt;&gt;&gt; client = NetapiClient(__opts__)
&gt;&gt;&gt; lowstate = {'client': 'local', 'tgt': '*', 'fun': 'test.ping', 'arg': ''}
&gt;&gt;&gt; client.run(lowstate)
</pre>
<dt><code>local(*args, **kwargs)</code></p>
<dd> Run execution modules synchronously </p>
<p> See <code>salt.client.LocalClient.cmd()</code> for all available parameters. </p>
<p> Sends a command from the master to the targeted minions. This is the same interface that Salt&#8217;s own CLI uses. Note the <code>arg</code> and <code>kwarg</code> parameters are sent down to the minion(s) and the given function, <code>fun</code>, is called with those parameters.</p>
<dt><code>Returns</code></p>
<dd> Returns the result from the execution module</p>
<dt><code>local_async(*args, **kwargs)</code></p>
<dd> Run execution modules asynchronously </p>
<p> Wraps <code>salt.client.LocalClient.run_job()</code>.</p>
<dt><code>Returns</code></p>
<dd> job ID</p>
<dt><code>local_batch(*args, **kwargs)</code></p>
<dd> Run execution modules against batches of minions </p>
<p> New in version 0.8.4. </p>
<p> Wraps <code>salt.client.LocalClient.cmd_batch()</code></p>
<dt><code>Returns</code></p>
<dd> Returns the result from the exeuction module for each batch of returns</p>
<dt><code>runner(fun, timeout=None, **kwargs)</code></p>
<dd> Run <i>runner modules &lt;all-salt.runners&gt;</i> synchronously </p>
<p> Wraps <code>salt.runner.RunnerClient.cmd_sync()</code>. </p>
<p> Note that runner functions must be called using keyword arguments. Positional arguments are not supported.</p>
<dt><code>Returns</code></p>
<dd> Returns the result from the runner module</p>
<dt><code>wheel(fun, **kwargs)</code></p>
<dd> Run wheel modules synchronously </p>
<p> Wraps <code>salt.wheel.WheelClient.master_call()</code>. </p>
<p> Note that wheel functions must be called using keyword arguments. Positional arguments are not supported.</p>
<dt><code>Returns</code></p>
<dd> Returns the result from the wheel module</dl>
<h2 id="SALT VIRT"></h2>
<p> The Salt Virt cloud controller capability was initially added to Salt in version 0.14.0 as an alpha technology. </p>
<p> The initial Salt Virt system supports core cloud operations:</p>
<dl>
<dt>&bull;</p>
<dd> Virtual machine deployment</p>
<dt>&bull;</p>
<dd> Inspection of deployed VMs</p>
<dt>&bull;</p>
<dd> Virtual machine migration</p>
<dt>&bull;</p>
<dd> Network profiling</p>
<dt>&bull;</p>
<dd> Automatic VM integration with all aspects of Salt</p>
<dt>&bull;</p>
<dd> Image Pre-seeding </p>
<p> Many features are currently under development to enhance the capabilities of the Salt Virt systems. </p>
<p> <code>NOTE:</code> It is noteworthy that Salt was originally developed with the intent of using the Salt communication system as the backbone to a cloud controller. This means that the Salt Virt system is not an afterthought, simply a system that took the back seat to other development. The original attempt to develop the cloud control aspects of Salt was a project called butter. This project never took off, but was functional and proves the early viability of Salt to be a cloud controller.</dl>
<h3>Salt Virt Tutorial</h3>
<p> A tutorial about how to get Salt Virt up and running has been added to the tutorial section: </p>
<p> <code>Cloud Controller Tutorial</code></p>
<h3>The Salt Virt Runner</h3>
<p> The point of interaction with the cloud controller is the <code>virt</code> runner. The <code>virt</code> runner comes with routines to execute specific virtual machine routines. </p>
<p> Reference documentation for the virt runner is available with the runner module documentation: </p>
<p> <code>Virt Runner Reference</code></p>
<h3>Based on Live State Data</h3>
<p> The Salt Virt system is based on using Salt to query live data about hypervisors and then using the data gathered to make decisions about cloud operations. This means that no external resources are required to run Salt Virt, and that the information gathered about the cloud is live and accurate.</p>
<h3>Deploy from Network or Disk</h3>
<h3>Virtual Machine Disk Profiles</h3>
<p> Salt Virt allows for the disks created for deployed virtual machines to be finely configured. The configuration is a simple data structure which is read from the <code>config.option</code> function, meaning that the configuration can be stored in the minion config file, the master config file, or the minion&#8217;s pillar. </p>
<p> This configuration option is called <code>virt.disk</code>. The default <code>virt.disk</code> data structure looks like this: </p>
<pre>
virt.disk:
  default:
    - system:
      size: 8192
      format: qcow2
      model: virtio
</pre>
<p> <code>NOTE:</code> The format and model does not need to be defined, Salt will default to the optimal format used by the underlying hypervisor, in the case of kvm this it is <code>qcow2</code> and <code>virtio</code>. </p>
<p> This configuration sets up a disk profile called default. The default profile creates a single system disk on the virtual machine.</p>
<h3>Define More Profiles</h3>
<p> Many environments will require more complex disk profiles and may require more than one profile, this can be easily accomplished: </p>
<pre>
virt.disk:
  default:
    - system:
        size: 8192
  database:
    - system:
        size: 8192
    - data:
        size: 30720
  web:
    - system:
        size: 1024
    - logs:
        size: 5120
</pre>
<p> This configuration allows for one of three profiles to be selected, allowing virtual machines to be created with different storage needs of the deployed vm.</p>
<h3>Virtual Machine Network Profiles</h3>
<p> Salt Virt allows for the network devices created for deployed virtual machines to be finely configured. The configuration is a simple data structure which is read from the <code>config.option</code> function, meaning that the configuration can be stored in the minion config file, the master config file, or the minion&#8217;s pillar. </p>
<p> This configuration option is called <code>virt.nic</code>. By default the <code>virt.nic</code> option is empty but defaults to a data structure which looks like this: </p>
<pre>
virt.nic:
  default:
    eth0:
      bridge: br0
      model: virtio
</pre>
<p> <code>NOTE:</code> The model does not need to be defined, Salt will default to the optimal model used by the underlying hypervisor, in the case of kvm this model is <code>virtio</code> </p>
<p> This configuration sets up a network profile called default. The default profile creates a single Ethernet device on the virtual machine that is bridged to the hypervisor&#8217;s <code>br0</code> interface. This default setup does not require setting up the <code>virt.nic</code> configuration, and is the reason why a default install only requires setting up the <code>br0</code> bridge device on the hypervisor.</p>
<h3>Define More Profiles</h3>
<p> Many environments will require more complex network profiles and may require more than one profile, this can be easily accomplished: </p>
<pre>
virt.nic:
  dual:
    eth0:
      bridge: service_br
    eth1:
      bridge: storage_br
  single:
    eth0:
      bridge: service_br
  triple:
    eth0:
      bridge: service_br
    eth1:
      bridge: storage_br
    eth2:
      bridge: dmz_br
  all:
    eth0:
      bridge: service_br
    eth1:
      bridge: storage_br
    eth2:
      bridge: dmz_br
    eth3:
      bridge: database_br
  dmz:
    eth0:
      bridge: service_br
    eth1:
      bridge: dmz_br
  database:
    eth0:
      bridge: service_br
    eth1:
      bridge: database_br
</pre>
<p> This configuration allows for one of six profiles to be selected, allowing virtual machines to be created which attach to different network depending on the needs of the deployed vm.</p>
<h2 id="UNDERSTANDING YAML"></h2>
<p> The default renderer for SLS files is the YAML renderer. YAML is a markup language with many powerful features. However, Salt uses a small subset of YAML that maps over very commonly used data structures, like lists and dictionaries. It is the job of the YAML renderer to take the YAML data structure and compile it into a Python data structure for use by Salt. </p>
<p> Though YAML syntax may seem daunting and terse at first, there are only three very simple rules to remember when writing YAML for SLS files.</p>
<h3>Rule One: Indentation</h3>
<p> YAML uses a fixed indentation scheme to represent relationships between data layers. Salt requires that the indentation for each level consists of exactly two spaces. Do not use tabs.</p>
<h3>Rule Two: Colons</h3>
<p> Python dictionaries are, of course, simply key-value pairs. Users from other languages may recognize this data type as hashes or associative arrays. </p>
<p> Dictionary keys are represented in YAML as strings terminated by a trailing colon. Values are represented by either a string following the colon, separated by a space: </p>
<pre>
my_key: my_value
</pre>
<p> In Python, the above maps to: </p>
<pre>
{'my_key': 'my_value'}
</pre>
<p> Alternatively, a value can be associated with a key through indentation. </p>
<pre>
my_key:
  my_value
</pre>
<p> <code>NOTE:</code> The above syntax is valid YAML but is uncommon in SLS files because most often, the value for a key is not singular but instead is a <i>list</i> of values. </p>
<p> In Python, the above maps to: </p>
<pre>
{'my_key': 'my_value'}
</pre>
<p> Dictionaries can be nested: </p>
<pre>
first_level_dict_key:
  second_level_dict_key: value_in_second_level_dict
</pre>
<p> And in Python: </p>
<p>{<br />
    &#8216;first_level_dict_key&#8217;:<br />
    {<br />
        &#8216;second_level_dict_key&#8217; : &#8216;value_in_second_level_dict&#8217;<br />
    }<br />
}</p>
<h3>Rule Three: Dashes</h3>
<p> To represent lists of items, a single dash followed by a space is used. Multiple items are a part of the same list as a function of their having the same level of indentation. </p>
<pre>
- list_value_one
- list_value_two
- list_value_three
</pre>
<p> Lists can be the value of a key-value pair. This is quite common in Salt: </p>
<pre>
my_dictionary:
  - list_value_one
  - list_value_two
  - list_value_three
</pre>
<p> In Python, the above maps to: </p>
<p>{<br />
    &#8216;my_dictionary&#8217; : [ &#8216;list_value_one&#8217;, &#8216;list_value_two&#8217;, &#8216;list_value_three&#8217; ]<br />
}</p>
<h3>Learning More</h3>
<p> One easy way to learn more about how YAML gets rendered into Python data structures is to use an online YAML parser to see the Python output. </p>
<p> One excellent choice for experimenting with YAML parsing is: <i><a rel="nofollow noopener" href="http://yaml-online-parser.appspot.com/" target="_blank">http://yaml-online-parser.appspot.com/</a></i></p>
<h2 id="MASTER TOPS SYSTEM"></h2>
<p> In 0.10.4 the <i>external_nodes</i> system was upgraded to allow for modular subsystems to be used to generate the top file data for a highstate run on the master. </p>
<p> The old <i>external_nodes</i> option has been removed. The master tops system contains a number of subsystems that are loaded via the Salt loader interfaces like modules, states, returners, runners, etc. </p>
<p> Using the new <i>master_tops</i> option is simple: </p>
<pre>
master_tops:
  ext_nodes: cobbler-external-nodes
</pre>
<p> for <code>Cobbler</code> or: </p>
<pre>
master_tops:
  reclass:
    inventory_base_uri: /etc/reclass
    classes_uri: roles
</pre>
<p> for <code>Reclass</code>. </p>
<p> It&#8217;s also possible to create custom master_tops modules. These modules must go in a subdirectory called <i>tops</i> in the <i>extension_modules</i> directory. The <i>extension_modules</i> directory is not defined by default (the default <i>/srv/salt/_modules</i> will NOT work as of this release) </p>
<p> Custom tops modules are written like any other execution module, see the source for the two modules above for examples of fully functional ones. Below is a degenerate example: </p>
<p> /etc/salt/master: </p>
<pre>
extension_modules: /srv/salt/modules
master_tops:
  customtop: True
</pre>
<p> /srv/salt/modules/tops/customtop.py: </p>
<p>import logging import sys<br />
#Define the module&#8217;s virtual name<br />
    __virtualname__ = &#8216;customtop&#8217; log = logging.getLogger(__name__)<br />
        def __virtual__() : return __virtualname__ def top(** kwargs) :log.debug(&#8216;Calling top in customtop&#8217;) return {&#8216;base&#8217; : [&#8216;test&#8217;] }</p>
<p> <i>salt minion state.show_top</i> should then display something like: </p>
<p>$ salt minion state.show_top<br />
    minion&#8211; &#8212; &#8212; &#8212; &#8211;base : -test</p>
<h2 id="SALT SSH"></h2>
<h3>Getting Started</h3>
<p> Salt SSH is very easy to use, simply set up a basic <i>roster</i> file of the systems to connect to and run <code>salt-ssh</code> commands in a similar way as standard <code>salt</code> commands.</p>
<dl>
<dt>&bull;</p>
<dd> Salt ssh is considered production ready in version 2014.7.0</p>
<dt>&bull;</p>
<dd> Python is required on the remote system (unless using the <code>-r</code> option to send raw ssh commands)</p>
<dt>&bull;</p>
<dd> On many systems, the <code>salt-ssh</code> executable will be in its own package, usually named <code>salt-ssh</code></p>
<dt>&bull;</p>
<dd> The Salt SSH system does not supercede the standard Salt communication systems, it simply offers an SSH-based alternative that does not require ZeroMQ and a remote agent. Be aware that since all communication with Salt SSH is executed via SSH it is substantially slower than standard Salt with ZeroMQ.</p>
<dt>&bull;</p>
<dd> At the moment fileserver operations must be wrapped to ensure that the relevant files are delivered with the <code>salt-ssh</code> commands. The state module is an exception, which compiles the state run on the master, and in the process finds all the references to <code>salt://</code> paths and copies those files down in the same tarball as the state run. However, needed fileserver wrappers are still under development.</dl>
<h3>Salt SSH Roster</h3>
<p> The roster system in Salt allows for remote minions to be easily defined. </p>
<p> <code>NOTE:</code> See the <code>Roster documentation</code> for more details. </p>
<p> Simply create the roster file, the default location is <i>/etc/salt/roster</i>: </p>
<pre>
web1: 192.168.42.1
</pre>
<p> This is a very basic roster file where a Salt ID is being assigned to an IP address. A more elaborate roster can be created: </p>
<pre>
web1:
  host: 192.168.42.1 # The IP addr or DNS hostname
  user: fred         # Remote executions will be executed as user fred
  passwd: foobarbaz  # The password to use for login, if omitted, keys are used
  sudo: True         # Whether to sudo to root, not enabled by default
web2:
  host: 192.168.42.2
</pre>
<p> <code>NOTE:</code> sudo works only if NOPASSWD is set for user in /etc/sudoers: <code>fred ALL=(ALL) NOPASSWD: ALL</code></p>
<h3>Deploy ssh key for salt-ssh</h3>
<p> By default, salt-ssh will generate key pairs for ssh, the default path will be /etc/salt/pki/master/ssh/salt-ssh.rsa </p>
<p> You can use ssh-copy-id, (the OpenSSH key deployment tool) to deploy keys to your servers. </p>
<pre>
ssh-copy-id -i /etc/salt/pki/master/ssh/salt-ssh.rsa.pub user [at] server.demo.com
</pre>
<p> One could also create a simple shell script, named salt-ssh-copy-id.sh as follows: </p>
<p>#!/ bin / bash<br />
if<br />
    [-z $1];<br />
then<br />
        echo $0 user[at] host.com<br />
            exit 0 fi<br />
                ssh &#8211;<br />
    copy &#8211; id &#8211; i / etc / salt / pki / master / ssh / salt &#8211; ssh.rsa.pub $1</p>
<p> <code>NOTE:</code> Be certain to chmod +x salt-ssh-copy-id.sh. </p>
<pre><code>
./ salt - ssh - copy - id.sh user[at] server1.host.com./ salt - ssh - copy - id.sh user[at] server2.host.com
</code></pre>
<p> Once keys are successfully deployed, salt-ssh can be used to control them.</p>
<h3>Calling Salt SSH</h3>
<p> The <code>salt-ssh</code> command can be easily executed in the same way as a salt command: </p>
<pre>
salt-ssh '*' test.ping
</pre>
<p> Commands with <code>salt-ssh</code> follow the same syntax as the <code>salt</code> command. </p>
<p> The standard salt functions are available! The output is the same as <code>salt</code> and many of the same flags are available. Please see <i><a rel="nofollow noopener" href="http://docs.saltstack.com/ref/cli/salt-ssh.html" target="_blank">http://docs.saltstack.com/ref/cli/salt-ssh.html</a></i> for all of the available options.</p>
<h3>Raw Shell Calls</h3>
<p> By default <code>salt-ssh</code> runs Salt execution modules on the remote system, but <code>salt-ssh</code> can also execute raw shell commands: </p>
<pre>
salt-ssh '*' -r 'ifconfig'
</pre>
<h3>States Via Salt SSH</h3>
<p> The Salt State system can also be used with <code>salt-ssh</code>. The state system abstracts the same interface to the user in <code>salt-ssh</code> as it does when using standard <code>salt</code>. The intent is that Salt Formulas defined for standard <code>salt</code> will work seamlessly with <code>salt-ssh</code> and vice-versa. </p>
<p> The standard Salt States walkthroughs function by simply replacing <code>salt</code> commands with <code>salt-ssh</code>.</p>
<h3>Targeting with Salt SSH</h3>
<p> Due to the fact that the targeting approach differs in salt-ssh, only glob and regex targets are supported as of this writing, the remaining target systems still need to be implemented.</p>
<h3>Configuring Salt SSH</h3>
<p> Salt SSH takes its configuration from a master configuration file. Normally, this file is in <code>/etc/salt/master</code>. If one wishes to use a customized configuration file, the <code>-c</code> option to Salt SSH facilitates passing in a directory to look inside for a configuration file named <code>master</code>.</p>
<h3>Minion Config</h3>
<p> New in version 2015.5.1. </p>
<p> Minion config options can be defined globally using the master configuration option <code>ssh_minion_opts</code>. It can also be defined on a per-minion basis with the <code>minion_opts</code> entry in the roster.</p>
<h3>Running Salt SSH as non-root user</h3>
<p> By default, Salt read all the configuration from /etc/salt/. If you are running Salt SSH with a regular user you have to modify some paths or you will get &quot;Permission denied&quot; messages. You have to modify two parameters: <code>pki_dir</code> and <code>cachedir</code>. Those should point to a full path writable for the user. </p>
<p> It&#8217;s recommed not to modify /etc/salt for this purpose. Create a private copy of /etc/salt for the user and run the command with <code>-c /new/config/path</code>.</p>
<h3>Define CLI Options with Saltfile</h3>
<p> If you are commonly passing in CLI options to <code>salt-ssh</code>, you can create a <code>Saltfile</code> to automatically use these options. This is common if you&#8217;re managing several different salt projects on the same server. </p>
<p> So if you <code>cd</code> into a directory with a <code>Saltfile</code> with the following YAML contents: </p>
<pre>
salt-ssh:
  config_dir: path/to/config/dir
  max_prox: 30
  wipe_ssh: true
</pre>
<p> Instead of having to call <code>salt-ssh &#8211;config-dir=path/to/config/dir &#8211;max-procs=30 &#8211;wipe \* test.ping</code> you can call <code>salt-ssh \* test.ping</code>. </p>
<p> Boolean-style options should be specified in their YAML representation. </p>
<p> <code>NOTE:</code> The option keys specified must match the destination attributes for the options specified in the parser <code>salt.utils.parsers.SaltSSHOptionParser</code>. For example, in the case of the <code>&#8211;wipe</code> command line option, its <code>dest</code> is configured to be <code>wipe_ssh</code> and thus this is what should be configured in the <code>Saltfile</code>. Using the names of flags for this option, being <code>wipe: true</code> or <code>w: true</code>, will not work.</p>
<h3>Debugging salt-ssh</h3>
<p> One common approach for debugging <code>salt-ssh</code> is to simply use the tarball that salt ships to the remote machine and call <code>salt-call</code> directly. </p>
<p> To determine the location of <code>salt-call</code>, simply run <code>salt-ssh</code> with the <code>-ldebug</code> flag and look for a line containing the string, <code>SALT_ARGV</code>. This contains the <code>salt-call</code> command that <code>salt-ssh</code> attempted to execute. </p>
<p> It is recommended that one modify this command a bit by removing the <code>-l quiet</code>, <code>&#8211;metadata</code> and <code>&#8211;output json</code> to get a better idea of what&#8217;s going on on the target system.</p>
<h2 id="SALT ROSTERS"></h2>
<p> Salt rosters are pluggable systems added in Salt 0.17.0 to facilitate the <code>salt-ssh</code> system. The roster system was created because <code>salt-ssh</code> needs a means to identify which systems need to be targeted for execution. </p>
<p> <code>SEE ALSO:</code> all-salt.roster </p>
<p> <code>NOTE:</code> The Roster System is not needed or used in standard Salt because the master does not need to be initially aware of target systems, since the Salt Minion checks itself into the master. </p>
<p> Since the roster system is pluggable, it can be easily augmented to attach to any existing systems to gather information about what servers are presently available and should be attached to by <code>salt-ssh</code>. By default the roster file is located at /etc/salt/roster.</p>
<h3>How Rosters Work</h3>
<p> The roster system compiles a data structure internally referred to as <code>targets</code>. The <code>targets</code> is a list of target systems and attributes about how to connect to said systems. The only requirement for a roster module in Salt is to return the <code>targets</code> data structure.</p>
<h3>Targets Data</h3>
<p> The information which can be stored in a roster <code>target</code> is the following: </p>
<pre>
&lt;Salt ID&gt;:       # The id to reference the target system with
    host:        # The IP address or DNS name of the remote host
    user:        # The user to log in as
    passwd:      # The password to log in with
    # Optional parameters
    port:        # The target system's ssh port number
    sudo:        # Boolean to run command via sudo
    priv:        # File path to ssh private key, defaults to salt-ssh.rsa
    timeout:     # Number of seconds to wait for response when establishing
                 # an SSH connection
    timeout:     # Number of seconds to wait for response
    minion_opts: # Dictionary of minion opts
</pre>
<p><em>For the complete reference documentation including all modules, states, and runners, please check the Linux command <code>man 7 salt</code> on your system.</em></p>


