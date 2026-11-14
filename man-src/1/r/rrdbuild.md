---
title: "rrdbuild(1)"
name: "rrdbuild"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdbuild/"
description: "rrdbuild – Instructions for building RRDtool"
---

<h2 class="name">NAME</h2>
<p> rrdbuild &#8211; Instructions for building RRDtool </p>
<h2>OVERVIEW</h2>
<p> If you downloaded the source of RRDtool you have to compile it. This document will give some information on how this is done. </p>
<p> RRDtool relies on services of third part libraries. Some of these libraries may already be installed on your system. You have to compile copies of the other ones before you can build RRDtool. </p>
<p> This document will tell you about all the necessary steps to get going. </p>
<p> These instructions assume you are using a <code>bash</code> shell. If you use csh/tcsh, then you can either type <i>bash</i> to switch to bash for the compilation or if you know what you are doing just replace the export bits with setenv. </p>
<p> We further assume that your copies of <code>tar</code> and <code>make</code> are actually <font SIZE="-1"><code>GNU</code></font><code> tar</code> and <font SIZE="-1"><code>GNU</code></font><code> make</code> respectively. It could be that they are installed as <code>gtar</code> and <code>gmake</code> on your system.</p>
<h2>OPTIMISTIC BUILD</h2>
<p> Before you start to build RRDtool, you have to decide two things:</p>
<dl>
<dt>1.</p>
<dd> In which directory you want to build the software.</p>
<dt>2.</p>
<dd> Where you want to install the software.</dl>
<p> Once you have decided. Save the two locations into environment variables. </p>
<pre>
 BUILD_DIR=/tmp/rrdbuild
 INSTALL_DIR=/opt/rrdtool-1.4.8
</pre>
<p> If your <i>/tmp</i> is mounted with the option noexec (<font SIZE="-1">RHEL</font> seems todo that) you have to choose a different directory! </p>
<p> Now make sure the <font SIZE="-1">BUILD_DIR</font> exists and go there: </p>
<pre>
 mkdir -p $BUILD_DIR
 cd $BUILD_DIR
</pre>
<p> Lets first assume you already have all the necessary libraries pre-installed. </p>
<pre>
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/rrdtool-1.4.8.tar.gz">http://oss.oetiker.ch/rrdtool/pub/rrdtool-1.4.8.tar.gz</a>
 gunzip -c rrdtool-1.4.8.tar.gz | tar xf -
 cd rrdtool-1.4.8
 ./configure --prefix=$INSTALL_DIR &amp;&amp; make &amp;&amp; make install
</pre>
<p> Ok, this was very optimistic. This try will probably have ended with <code>configure</code> complaining about several missing libraries.</p>
<h2>INSTALLING DEPENDENCIES</h2>
<p> If your <font SIZE="-1">OS</font> lets you install additional packages from a software repository, you may get away with installing the missing packages. When the packages are installed, run configure again and try to compile again. Below you find some hints on getting your <font SIZE="-1">OS</font> ready for compiling RRDtool. </p>
<p> Additions to this list are welcome. In general RRDtool should work with the latest versions of the libraries. The versions listed here are just what was current when I tested this.</p>
<h3>OpenSolaris 2008.05</h3>
<p> Just add a compiler and the gnome development package: </p>
<pre>
 pkg install sunstudioexpress
 pkg install SUNWgnome-common-devel
</pre>
<p> There is a problem with <i>cairo.pc</i> on OpenSolaris. It suggests that xrender is required for compilation with cairo. This is not true and also bad since OpenSolaris does not include an <i>xrender.pc</i> file. Use Perl to fix this: </p>
<pre>
 perl -i~ -p -e 's/(Requires.*?)\s*xrender.*/$1/' /usr/lib/pkgconfig/cairo.pc
</pre>
<p> Make sure the RRDtool build system finds your new compiler </p>
<pre>
 export PATH=/opt/SunStudioExpress/bin
</pre>
<h3>Debian / Ubuntu</h3>
<p> Use apt-get to make sure you have all that is required. A number of packages will get added through dependencies. </p>
<pre>
 apt-get install libpango1.0-dev libxml2-dev
</pre>
<h3>Gentoo</h3>
<p> In Gentoo installing RRDtool is really simple you just need to <code>emerge rrdtool</code>. All dependencies will be handled automatically by the portage system. The only thing you should care about are <font SIZE="-1">USE</font> flags, which allow you fine tune features RRDtool will be built with. Currently the following <font SIZE="-1">USE</font> flags are available: </p>
<pre>
 doc    - install .html and .txt documentation
          into /usr/share/doc/rrdtool-1.x.xx/
 perl   - build and install perl language bindings
 python - build and install python language bindings
 ruby   - build and install ruby language bindings
 tcl    - build and install tcl language bindings
 rrdcgi - build and install rrdcgi
</pre>
<p> After you&#8217;ve decided which <font SIZE="-1">USE</font> flags you need, set them either in <i>make.conf</i> or <i>/etc/portage/package.use</i> and finally run: </p>
<pre>
 # emerge -va rrdtool
</pre>
<p> Take a look at Gentoo handbook for further details on how to manage <font SIZE="-1">USE</font> flags: <a rel="nofollow" href="http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2">http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2</a></p>
<h2>BUILDING DEPENDENCIES</h2>
<p> But again this may have been too optimistic still, and you actually have to compile your own copies of some of the required libraries. Things like libpng and zlib are pretty standard so you will probably have them on your system anyway. Freetype, Fontinst, Cairo, Pango may be installed, but it is possible that they are pretty old and thus don&#8217;t live up to our expectations, so you may want to compile their latest versions.</p>
<h3>General build tips for <font SIZE="-1">AIX</font></h3>
<p> If you are working with <font SIZE="-1">AIX</font>, you may find the <code>&#8211;disable-shared</code> option will cause things to break for you. In that case you may have to install the shared libraries into the RRDtool <font SIZE="-1">PREFIX</font> and work with <code>&#8211;disable-static</code> instead. </p>
<p> Another hint to get RRDtool working on <font SIZE="-1">AIX</font> is to use the <font SIZE="-1">IBM</font> <font SIZE="-1">XL</font> C Compiler: </p>
<pre>
 export CC=/usr/vac/bin/cc
 export PERLCC=$CC
</pre>
<p> (Better instructions for <font SIZE="-1">AIX</font> welcome!)</p>
<h3>Build Instructions</h3>
<p> Some libraries want to know where other libraries are. For this to work, set the following environment variable </p>
<pre>
 export PKG_CONFIG_PATH=${INSTALL_DIR}/lib/pkgconfig
 export PATH=$INSTALL_DIR/bin:$PATH
</pre>
<p> The above relies on the presence of the <i>pkgconfig</i> program. Below you find instructions on how to compile pkgconfig. </p>
<p> Since we are compiling libraries dynamically, they must know where to find each other. This is done by setting an appropriate <font SIZE="-1">LDFLAGS</font>. Unfortunately, the syntax again differs from system to system:</p>
<dl>
<dt>Solaris</p>
<dd>
<pre>
 export LDFLAGS=-R${INSTALL_DIR}/lib
</pre>
<p> if you are using the Sun Studio/Forte compiler, you may also want to set </p>
<pre>
 CFLAGS=&quot;-xO3 -xcode=pic13&quot;   (SPARC)
 CFLAGS=&quot;-xO3 -Kpic&quot;          (x86)
</pre>
<dt>Linux</p>
<dd>
<pre>
 export LDFLAGS=&quot;-Wl,--rpath -Wl,${INSTALL_DIR}/lib&quot;
</pre>
<dt><font SIZE="-1">HPUX</font></p>
<dd>
<pre>
 export LDFLAGS=&quot;+b${INSTALL_DIR}/lib&quot;
</pre>
<dt><font SIZE="-1">AIX</font></p>
<dd>
<pre>
 export LDFLAGS=&quot;-Wl,-blibpath:${INSTALL_DIR}/lib&quot;
</pre>
</dl>
<p> If you have <font SIZE="-1">GNU</font> make installed and it is not called &#8216;make&#8217;, then do </p>
<pre>
 export MAKE=gmake
 export GNUMAKE=gmake
</pre>
<p> otherwise just do </p>
<pre>
 export MAKE=make
</pre>
<p> <i>Building pkgconfig</i> </p>
<p> As mentioned above, without pkgconfig the whole build process will be lots of pain and suffering, so make sure you have a copy on your system. If it is not available natively, here is how to compile it. </p>
<pre>
 wget <a rel="nofollow" href="http://pkgconfig.freedesktop.org/releases/pkg-config-0.23.tar.gz">http://pkgconfig.freedesktop.org/releases/pkg-config-0.23.tar.gz</a>
 gunzip -c pkg-config-0.23.tar.gz | tar xf -
 cd pkg-config-0.23
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot;
 $MAKE
 $MAKE install
</pre>
<p> After installing pkgconfig in a custom directory, setting up the corresponding environment variable will be helpful. </p>
<pre>
 export PKG_CONFIG=$INSTALL_DIR/bin/pkg-config
</pre>
<p> <i>Building zlib</i> </p>
<p> Chances are very high that you already have that on your system &#8230; </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/zlib-1.2.3.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/zlib-1.2.3.tar.gz</a>
 gunzip -c zlib-1.2.3.tar.gz | tar xf -
 cd zlib-1.2.3
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot; --shared
 $MAKE
 $MAKE install
</pre>
<p> <i>Building libpng</i> </p>
<p> Libpng itself requires zlib to build, so we need to help a bit. If you already have a copy of zlib on your system (which is very likely) you can drop the settings of <font SIZE="-1">LDFLAGS</font> and <font SIZE="-1">CPPFLAGS</font>. Note that the backslash (\) at the end of line 4 means that line 4 and line 5 are on one line. </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/libpng-1.2.18.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/libpng-1.2.18.tar.gz</a>
 gunzip -c libpng-1.2.18.tar.gz | tar xf -
 cd libpng-1.2.10
 env CFLAGS=&quot;-O3 -fPIC&quot; ./configure --prefix=$INSTALL_DIR
 $MAKE
 $MAKE install
</pre>
<p> <i>Building freetype</i> </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/freetype-2.3.5.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/freetype-2.3.5.tar.gz</a>
 gunzip -c freetype-2.3.5.tar.gz | tar xf -
 cd freetype-2.3.5
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot;
 $MAKE
 $MAKE install
</pre>
<p> If you run into problems building freetype on Solaris, you may want to try to add the following at the start the configure line: </p>
<pre>
 env EGREP=egrep
</pre>
<p> <i>Building LibXML2</i> </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/libxml2-2.6.32.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/libxml2-2.6.32.tar.gz</a>
 gunzip -c libxml2-2.6.32.tar.gz | tar xf -
 cd libxml2-2.6.32
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot;
 $MAKE
 $MAKE install
</pre>
<p> <i>Building fontconfig</i> </p>
<p> Note that fontconfig has a run time configuration file in INSTALL_DIR/etc you may want to adjust that so that fontconfig finds the fonts on your system. Run the fc-cache program to build the fontconfig cache after changing the config file. </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/fontconfig-2.4.2.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/fontconfig-2.4.2.tar.gz</a>
 gunzip -c fontconfig-2.4.2.tar.gz   | tar xf -
 cd fontconfig-2.4.2
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot; --with-freetype-config=$INSTALL_DIR/bin/freetype-config
 $MAKE
 $MAKE install
</pre>
<p> <i>Building Pixman</i> </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/pixman-0.10.0.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/pixman-0.10.0.tar.gz</a>
 gunzip -c pixman-0.10.0.tar.gz  | tar xf -
 cd pixman-0.10.0
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot;
 $MAKE
 $MAKE install
</pre>
<p> <i>Building Cairo</i> </p>
<pre><code>
cd $BUILD_DIR
            wget http : // oss.oetiker.ch/rrdtool/pub/libs/cairo-1.6.4.tar.gz
                        gunzip -
                        c cairo - 1.6.4.tar.gz |
    tar xf -
        cd cairo - 1.6.4./ configure-- prefix = $INSTALL_DIR-- enable - xlib = no-- enable - xlib - render = no-- enable - win32 = no
                                                                                                                 CFLAGS = "-O3 -fPIC" $MAKE
                                                                                                                     $MAKE install
</code></pre>
<p> When building on Solaris you may want todo </p>
<pre><code>
./ configure-- prefix = $INSTALL_DIR-- enable - xlib = no-- enable - xlib - render = no-- enable - win32 = no
                                                                                         CFLAGS = "-O3 -fPIC -D_POSIX_PTHREAD_SEMANTICS"
</code></pre>
<p> <i>Building Glib</i> </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/glib-2.15.4.tar.gz">http://oss.oetiker.ch/rrdtool/pub/libs/glib-2.15.4.tar.gz</a>
 gunzip -c glib-2.15.4.tar.gz  | tar xf -
 cd glib-2.15.4
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot;
 $MAKE
 $MAKE install
</pre>
<p> <i>Building Pango</i> </p>
<pre>
 cd $BUILD_DIR
 wget <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/pub/libs/pango-1.21.1.tar.bz2">http://oss.oetiker.ch/rrdtool/pub/libs/pango-1.21.1.tar.bz2</a>
 bunzip2 -c pango-1.21.1.tar.bz2 | tar xf -
 cd pango-1.21.1
 ./configure --prefix=$INSTALL_DIR CFLAGS=&quot;-O3 -fPIC&quot; --without-x
 $MAKE
 $MAKE install
</pre>
<h3>Building rrdtool (second try)</h3>
<p> Now all the dependent libraries are built and you can try again. This time you tell configure where it should be looking for libraries and include files. This is done via environment variables. Depending on the shell you are running, the syntax for setting environment variables is different. </p>
<p> And finally try building again. We disable the python and tcl bindings because it seems that a fair number of people have ill configured python and tcl setups that would prevent RRDtool from building if they are included in their current state. </p>
<pre>
 cd $BUILD_DIR/rrdtool-1.4.8
 ./configure --prefix=$INSTALL_DIR --disable-tcl --disable-python
 $MAKE clean
 $MAKE
 $MAKE install
</pre>
<p> <font SIZE="-1">SOLARIS</font> <font SIZE="-1">HINT:</font> if you want to build the Perl module for the native Perl (the one shipping with Solaris) you will need the Sun Forte compiler installed on your box or you have to hand-tune bindings/perl-shared/Makefile while building! </p>
<p> Now go to <i></i>$INSTALL_DIR<i></i><code>/share/rrdtool/examples/</code> and run them to see if your build has been successful.</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAM">AUTHOR</a></p>
<dd></dl>
