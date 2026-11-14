---
title: "mrtg-unix-guide(1)"
name: "mrtg-unix-guide"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-unix-guide/"
description: "mrtg-unix-guide – The MRTG 2.17.4 Linux/Unix Installation Guide"
---

<h2 class="name">NAME</h2>
<p> mrtg-unix-guide &#8211; The MRTG 2.17.4 Linux/Unix Installation Guide </p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">MRTG</font> comes to you in Source Code. This means that you have to compile parts of it before you can use it on a Unix machine. These instructions help you to do so.</p>
<h2>PREPARATION</h2>
<p> In order to compile and use mrtg you need a C compiler and a copy of perl installed on your machine. In most cases this will already be available. In case it is not, here are some starting points. Below I&#8217;ll give you a detailed run through the whole compilation process.</p>
<dl>
<dt><font SIZE="-1">GCC</font></p>
<dd> The <font SIZE="-1">GNU</font> C compiler comes preinstalled on most of the free Unicies out there. For commercial derivatives you may have to download and compile it first. If you have no compiler at all there is a chicken and egg problem, but there are also precompiled versions of gcc available for most operating systems. </p>
<pre>
 <a rel="nofollow" href="http://gcc.gnu.org/">http://gcc.gnu.org/</a>
</pre>
<dt>Perl</p>
<dd> Large parts of the <font SIZE="-1">MRTG</font> system are written in the Perl scripting language. Make sure there is a recent copy of perl on your machine (try perl -v). At least version 5.005 is required for mrtg to work well. If you use <font SIZE="-1">SNMPV3</font> and other new features you should use at least 5.8. </p>
<p> You can get the latest perl from </p>
<pre>
 <a rel="nofollow" href="http://www.perl.com/">http://www.perl.com/</a>
</pre>
</dl>
<p> <font SIZE="-1">MRTG</font> generates traffic graphs in the <font SIZE="-1">PNG</font> format. To be able to do this it needs several 3rd party libraries. When compiling these libraries I urge you to make sure you compile them as <code>static</code> libraries. There is just much less trouble ahead if you are doing it like this. See the Instructions in the next section for inspiration. Note that many free unices have all the required libraries already in place so there is no need to install another copy. To check it is best to skip all the library instructions below and go straight into the mrtg compile. </p>
<p> If the first attempt fails and you do not get a working version of mrtg, try compiling new copies of all libraries as explained below. Do this <font SIZE="-1"><code>BEFORE</code></font> you send email to me about problems compiling mrtg.</p>
<dl>
<dt>gd</p>
<dd> This is a basic graph drawing library created by Thomas Boutell. Note that all releases after Version 1.3 only create <font SIZE="-1">PNG</font> images. This is because a) Thomas got into trouble because the <font SIZE="-1">GIF</font> format which it used to produce uses a compression technology patented by Unisys. b) <font SIZE="-1">PNG</font> is more efficient and patent free. <font SIZE="-1">MRTG</font> can work with old and new version of the <font SIZE="-1">GD</font> library. You can get a recent copy of <font SIZE="-1">GD</font> from: </p>
<pre>
 <a rel="nofollow" href="http://www.boutell.com/gd/">http://www.boutell.com/gd/</a>
</pre>
<dt>libpng</p>
<dd> Is required by gd in order to produce <font SIZE="-1">PNG</font> graphics files. Get it from: </p>
<pre>
 <a rel="nofollow" href="http://www.libpng.org/pub/png/libpng.html">http://www.libpng.org/pub/png/libpng.html</a>
</pre>
<dt>zlib</p>
<dd> Is needed by libpng to compress the graphics files you create. Get a copy from </p>
<pre>
 <a rel="nofollow" href="http://www.gzip.org/zlib">http://www.gzip.org/zlib</a>
</pre>
</dl>
<p> And last but not least you also need mrtg itself. In case you have not yet downloaded it, you can find a copy on my website: </p>
<pre>
 <a rel="nofollow" href="http://oss.oetiker.ch/mrtg/pub">http://oss.oetiker.ch/mrtg/pub</a>
</pre>
<h2>LIBRARY COMPILATION</h2>
<p> In this section I will give you step by step instructions on how to compile the various libraries required for the compilation of mrtg. Note that these libraries may already be installed if you have a <i>*BSD</i> or <i>Linux</i> system so you can skip recompiling them. The <code>wget</code> program used below is a simple web downloader. You can also enter the address into your <code>netscape</code> if you don&#8217;t have <code>wget</code> available. </p>
<p> First let&#8217;s create a directory for the compilation. Note that this may already exist on your system. No problem, just use it. </p>
<pre>
 mkdir -p /usr/local/src
 cd /usr/local/src
</pre>
<p> If you do not have zlib installed: </p>
<pre>
 wget <a rel="nofollow" href="http://www.zlib.net/zlib-1.2.3.tar.gz">http://www.zlib.net/zlib-1.2.3.tar.gz</a>
 gunzip -c zlib-*.tar.gz | tar xf -
 rm zlib-*.tar.gz
 mv zlib-* zlib
 cd zlib
 ./configure
 make
 cd ..
</pre>
<p> If you don&#8217;t have libpng installed </p>
<pre>
 wget <a href="ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng-1.2.40.tar.gz">ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng-1.2.40.tar.gz</a>
 gunzip -c libpng-1.2.34.tar.gz | tar xf -
 mv libpng-* libpng
 cd libpng
 env CFLAGS=&quot;-O3 -fPIC&quot; ./configure --prefix=$INSTALL_DIR 
 make
 rm *.so.* *.so
 cd ..
</pre>
<p> And now you can compile gd </p>
<p> For versions up to 1.8.4, try: </p>
<pre>
 wget <a rel="nofollow" href="http://www.boutell.com/gd/http/gd-1.8.4.tar.gz">http://www.boutell.com/gd/http/gd-1.8.4.tar.gz</a>
 gunzip -c gd-*.tar.gz |tar xf -
 rm gd-*.tar.gz
 mv gd-* gd
 cd gd
</pre>
<p> The \ characters at the end of the following lines mean that all the following material should actually be written on a single line. </p>
<pre>
 perl -i~ -p -e s/gd_jpeg.o//g Makefile            
 make INCLUDEDIRS=&quot;-I. -I../zlib -I../libpng&quot; \
      LIBDIRS=&quot;-L../zlib -L. -L../libpng&quot; \
      LIBS=&quot;-lgd -lpng -lz -lm&quot; \
      CFLAGS=&quot;-O -DHAVE_LIBPNG&quot;
 cd ..
</pre>
<p> For versions starting around 2.0.11, try: </p>
<pre>
 wget <a rel="nofollow" href="http://www.boutell.com/gd/http/gd-2.0.33.tar.gz">http://www.boutell.com/gd/http/gd-2.0.33.tar.gz</a>
 gunzip -c gd-2.0.33.tar.gz |tar xf -
 mv gd-2.0.33 gd
 cd gd
 env CPPFLAGS=&quot;-I../zlib -I../libpng&quot; LDFLAGS=&quot;-L../zlib -L../libpng&quot; \
     ./configure --disable-shared --without-freetype --without-jpeg
 make
 cp .libs/* .
</pre>
<h2>MRTG COMPILATION</h2>
<p> Ok, now everything is ready for the mrtg compilation. </p>
<pre>
 cd /usr/local/src
 gunzip -c mrtg-2.17.4.tar.gz | tar xvf -
 cd mrtg-2.17.4
</pre>
<p> If all the libraries have been preinstalled on your system you can configure mrtg by doing a simple: </p>
<pre>
 ./configure --prefix=/usr/local/mrtg-2
</pre>
<p> Otherwise you may have to give some hints on where to find the various libraries required to compile mrtg: </p>
<pre><code>
./ configure-- prefix = / usr / local / mrtg - 2 --with - gd = / usr / local / src / gd-- with - z = / usr / local / src / zlib-- with - png = / usr / local / src / libpng
</code></pre>
<p> If you have RRDtool available you might want to tell mrtg about it so that you can opt to use rrdtool with mrtg. Check mrtg-rrd. </p>
<p> Configure will make sure your environment is fit for building mrtg. If it finds a problem, it will tell you so and it will also tell you what to do about it. If everything is <font SIZE="-1">OK</font>, you will end up with a custom Makefile for your system. Now type: </p>
<pre>
 make
</pre>
<p> This builds the rateup binary and edits all the perl pathnames in the scripts. You can now install mrtg by typing </p>
<pre>
 make install   (requires gnu install)
</pre>
<p> All the software required by <font SIZE="-1">MRTG</font> is now installed under the <i>/usr/local/mrtg-2</i> subdirectory. </p>
<p> You can now safely delete the libraries we compiled above. Then again, you might want to keep them around so that you have them available when compiling the next version of mrtg.</p>
<h2>CONFIGURATION</h2>
<p> The next step is to configure mrtg for monitoring a network device. This is done by creating an <i>mrtg.cfg</i> file which defines what you want to monitor. Luckily, you don&#8217;t have to dive straight in and start writing your own configuration file all by yourself. Together with mrtg you also got a copy of <code>cfgmaker</code>. This is a script you can point at a router of your choice; it will create a mrtg configuration file for you. You can find the script in the <i>bin</i> subdirectory. </p>
<pre><code>
cfgmaker-- global 'WorkDir: /home/httpd/mrtg' --global 'Options[_]: bits,growright' --output / home / mrtg / cfg / mrtg.cfg community[at] router.abc.xyz
</code></pre>
<p> This example above will create an mrtg config file in <i>/home/mrtg/cfg</i> assuming this is a directory visible on your webserver. You can read all about cfgmaker in cfgmaker. One area you might want to look at is the possibility of using <code>&#8211;ifref=ip</code> to prevent interface renumbering troubles from catching you. </p>
<p> If you want to start rolling your own mrtg configuration files, make sure you read mrtg-reference to learn all about the possible configuration options.</p>
<h2>RUNNING MRTG</h2>
<p> Once you have created a configuration file, try the following: </p>
<pre>
 /usr/local/mrtg-2/bin/mrtg /home/mrtg/cfg/mrtg.cfg
</pre>
<p> This will query your router and also create your first mrtg trafic graphs and webpages. When you run mrtg for the first time there will be a lot of complaints about missing log files. Don&#8217;t worry, this is normal for the first 2 times you start mrtg. If it keeps complaining after this time you might want to look into the problem. </p>
<p> Starting mrtg by hand is not ideal in the long run. So when you are satisfied with the results you can automate the process of running mrtg in regular intervals (this means every 5 minutes by default). </p>
<p> You can either add mrtg to your crontab with a line like this: </p>
<pre>
 0,5,10,15,20,25,30,35,40,45,50,55 * * * * \
       &lt;mrtg-bin&gt;/mrtg &lt;path to mrtg-cfg&gt;/mrtg.cfg \
                --logging /var/log/mrtg.log
</pre>
<p> or if you live in Linux Land the line may look like this if you are using <tt>&quot;crontab -e&quot;</tt> </p>
<pre>
 */5 * * * *  &lt;mrtg-bin&gt;/mrtg &lt;path to mrtg-cfg&gt;/mrtg.cfg \
                       --logging /var/log/mrtg.log
</pre>
<p> or like this if you use <i>/etc/crontab</i> </p>
<pre>
 */5 * * * *  mrtg-user  &lt;mrtg-bin&gt;/mrtg &lt;path to mrtg-cfg&gt;/mrtg.cfg \
                                 --logging /var/log/mrtg.log
</pre>
<p> You can also run mrtg as a daemon process by adding the line </p>
<pre>
 RunAsDaemon: Yes
</pre>
<p> to your mrtg configuration file and then creating a startup script in your system startup sequence. Unfortunately, adding startup scripts differs widely amongst different unix systems. The modern ones normally have a directory called <i>/etc/init.d</i> or <i>/etc/rc.d/init.d</i> where you put scripts which starts the process you want to run when the system boots. Further you must create a symbolic link in <i>/etc/rc3.d</i> or <i>/etc/rc.d/rc?.d</i> called <i>S65mrtg</i> (this is just a sample name &#8230; it is just important that it starts with S followed by a two digit number). If you are not sure about this, make sure you consult the documentation of your system to make sure you get this right. </p>
<p> A <code>minimal</code> script to put into <i>init.d</i> might look like this: </p>
<pre>
 #! /bin/sh
 cd /usr/local/mrtg-2.17.4/bin &amp;&amp; ./mrtg --user=mrtg-user \
       /home/httpd/mrtg/mrtg.cfg  --logging /var/log/mrtg.log
</pre>
<p> Note that this will only work with <code>RunAsDaemon: Yes</code> in your mrtg.cfg file.</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
