---
title: "apt-mirror(1)"
name: "apt-mirror"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-mirror/"
---

<h2 class="name">NAME</h2>
 

 apt-mirror - apt sources mirroring tool 

<h2>SYNOPSIS</h2>

 apt-mirror [configfile]

<h2>DESCRIPTION</h2>

 A small and efficient tool that lets you mirror a part of or the whole Debian GNU/Linux distribution or any other apt sources. 

 Main features: 
&nbsp;<wbr>*&nbsp;<wbr>It uses a config similar to apts&nbsp;<wbr><i>sources.list</i> 
&nbsp;<wbr>*&nbsp;<wbr>It's fully pool comply 
&nbsp;<wbr>*&nbsp;<wbr>It supports multithreaded downloading 
&nbsp;<wbr>*&nbsp;<wbr>It supports multiple architectures at the same time 
&nbsp;<wbr>*&nbsp;<wbr>It can automatically remove unneeded files 
&nbsp;<wbr>*&nbsp;<wbr>It works well on overloaded channel to internet 
&nbsp;<wbr>*&nbsp;<wbr>It never produces an inconsistent mirror including while mirroring 
&nbsp;<wbr>*&nbsp;<wbr>It works on all&nbsp;<wbr><font SIZE="-1">POSIX</font>&nbsp;<wbr>complied systems with perl and wget

<h2>COMMENTS</h2>

 apt-mirror uses <i>/etc/apt-mirror.list</i> as a configuration file. By default it is tuned to official debian mirror in Finland. Change it for your needs. 

 After you setup the configuration file you may run as root: 

 <pre>
    # su - apt-mirror -c apt-mirror
</pre> 

 Or uncomment line in <i>/etc/cron.d/apt-mirror</i> to enable daily mirror upgrades.

<h2>FILES</h2>

 <i>/etc/apt-mirror.list</i> 
&nbsp;<wbr>&nbsp;<wbr>Main configuration file 

 <i>/etc/cron.d/apt-mirror</i> 
&nbsp;<wbr>&nbsp;<wbr>Cron configuration template 

 <i>/var/spool/apt-mirror/mirror</i> 
&nbsp;<wbr>&nbsp;<wbr>Mirror places here 

 <i>/var/spool/apt-mirror/skel</i> 
&nbsp;<wbr>&nbsp;<wbr>Place for temporarily downloaded indexes 

 <i>/var/spool/apt-mirror/var</i> 
&nbsp;<wbr>&nbsp;<wbr>Log files placed here. URLs and&nbsp;<wbr><font SIZE="-1">MD5</font>&nbsp;<wbr>summs also here.

<h2>KNOWN BUGS</h2>

 Do not specify default http port (80) explicitly. (i.e. deb <a rel="nofollow" HREF="http://server:80/">http://server:80/</a> sid ...)

<h2>AUTHOR</h2>

 Dmitry N. Hramtsov &lt;hdn [at] nsu.ru&gt; 

<h2>Index</h2>


