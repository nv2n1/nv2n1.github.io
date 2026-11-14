---
title: "perlandroid(1)"
name: "perlandroid"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlandroid/"
description: "perlandroid – Perl under Android"
---

<h2 class="name">NAME</h2>
<p> perlandroid &#8211; Perl under Android </p>
<h2>SYNOPSIS</h2>
<p> The first portions of this documents contains instructions to cross-compile Perl for Android 2.0 and later, using the binaries provided by Google. The latter portion describes how to build perl native using one of the toolchains available on the Play Store.</p>
<h2>DESCRIPTION</h2>
<p> This document describes how to set up your host environment when attempting to build Perl for Android.</p>
<h2>Cross-compilation</h2>
<p> These instructions assume an Unixish build environment on your host system; they&#8217;ve been tested on Linux and <font SIZE="-1">OS X,</font> and may work on Cygwin and <font SIZE="-1">MSYS.</font> While Google also provides an <font SIZE="-1">NDK</font> for Windows, these steps won&#8217;t work native there, although it may be possible to cross-compile through different means. </p>
<p> If your host system&#8217;s architecture is 32 bits, remember to change the <tt>&quot;x86_64&quot;</tt>&#8216;s below to <tt>&quot;x86&quot;</tt>&#8216;s. On a similar vein, the examples below use the 4.8 toolchain; if you want to use something older or newer (for example, the 4.4.3 toolchain included in the 8th revision of the <font SIZE="-1">NDK</font>), just change those to the relevant version.</p>
<h3>Get the Android Native Development Kit (<font SIZE="-1">NDK</font>)</h3>
<p> You can download the <font SIZE="-1">NDK</font> from &lt;<a rel="nofollow" href="https://developer.android.com/tools/sdk/ndk/index.html">https://developer.android.com/tools/sdk/ndk/index.html</a>&gt;. You&#8217;ll want the normal, non-legacy version.</p>
<h3>Determine the architecture you&#8217;ll be cross-compiling for</h3>
<p> There&#8217;s three possible options: arm-linux-androideabi for <font SIZE="-1">ARM,</font> mipsel-linux-android for <font SIZE="-1">MIPS,</font> and simply x86 for x86. As of 2014, most Android devices run on <font SIZE="-1">ARM,</font> so that is generally a safe bet. </p>
<p> With those two in hand, you should add </p>
<pre><code>
$ANDROID_NDK / toolchains / $TARGETARCH - 4.8 / prebuilt /`uname | tr '[A-Z]' '[a-z]'`- x86_64 / bin
</code></pre>
<p> to your <tt>&quot;PATH&quot;</tt>, where <tt>$ANDROID_NDK</tt> is the location where you unpacked the <font SIZE="-1">NDK,</font> and <tt>$TARGETARCH</tt> is your target&#8217;s architecture.</p>
<h3>Set up a standalone toolchain</h3>
<p> This creates a working sysroot that we can feed to Configure later. </p>
<pre><code>
$ export ANDROID_TOOLCHAIN = / tmp / my - toolchain - $TARGETARCH $ export SYSROOT = $ANDROID_TOOLCHAIN / sysroot $ $ANDROID_NDK / build / tools / make - standalone - toolchain.sh-- platform = android - 9 --install - dir = $ANDROID_TOOLCHAIN-- system =`uname | tr '[A-Z]' '[a-z]'`- x86_64-- toolchain = $TARGETARCH - 4.8
</code></pre>
<h3>adb or ssh?</h3>
<p> adb is the Android Debug Bridge. For our purposes, it&#8217;s basically a way of establishing an ssh connection to an Android device without having to install anything on the device itself, as long as the device is either on the same local network as the host, or it is connected to the host through <font SIZE="-1">USB.</font> </p>
<p> Perl can be cross-compiled using either adb or a normal ssh connection; in general, if you can connect your device to the host using a <font SIZE="-1">USB</font> port, or if you don&#8217;t feel like installing an sshd app on your device, you may want to use adb, although you may be forced to switch to ssh if your device is not rooted and you&#8217;re unlucky &#8212; more on that later. Alternatively, if you&#8217;re cross-compiling to an emulator, you&#8217;ll have to use adb. </p>
<p> <i>adb</i> </p>
<p> To use adb, download the Android <font SIZE="-1">SDK</font> from &lt;<a rel="nofollow" href="https://developer.android.com/sdk/index.html">https://developer.android.com/sdk/index.html</a>&gt;. The &#8220;<font SIZE="-1">SDK</font> Tools Only&#8221; version should suffice &#8212; if you downloaded the <font SIZE="-1">ADT</font> Bundle, you can find the sdk under <i></i>$ADT_BUNDLE<i>/sdk/</i>. </p>
<p> Add <i></i>$ANDROID_SDK<i>/platform-tools</i> to your <tt>&quot;PATH&quot;</tt>, which should give you access to adb. You&#8217;ll now have to find your device&#8217;s name using <tt>&quot;adb devices&quot;</tt>, and later pass that to Configure through <tt>&quot;-Dtargethost=$DEVICE&quot;</tt>. </p>
<p> However, before calling Configure, you need to check if using adb is a viable choice in the first place. Because Android doesn&#8217;t have a <i>/tmp</i>, nor does it allow executables in the sdcard, we need to find somewhere in the device for Configure to put some files in, as well as for the tests to run in. If your device is rooted, then you&#8217;re good. Try running these: </p>
<pre>
    $ export TARGETDIR=/mnt/asec/perl
    $ adb -s $DEVICE shell &quot;echo sh -c '\&quot;mkdir $TARGETDIR\&quot;' | su --&quot;
</pre>
<p> Which will create the directory we need, and you can move on to the next step. <i>/mnt/asec</i> is mounted as a tmpfs in Android, but it&#8217;s only accessible to root. </p>
<p> If your device is not rooted, you may still be in luck. Try running this: </p>
<pre>
    $ export TARGETDIR=/data/local/tmp/perl
    $ adb -s $DEVICE shell &quot;mkdir $TARGETDIR&quot;
</pre>
<p> If the command works, you can move to the next step, but beware: <code>You&#8217;ll have to remove the directory from the device once you are done! Unlike </code>/mnt/asec<code>, </code>/data/local/tmp<code> may not get automatically garbage collected once you shut off the phone</code>. </p>
<p> If neither of those work, then you can&#8217;t use adb to cross-compile to your device. Either try rooting it, or go for the ssh route. </p>
<p> <i>ssh</i> </p>
<p> To use ssh, you&#8217;ll need to install and run a sshd app and set it up properly. There are several paid and free apps that do this rather easily, so you should be able to spot one on the store. Remember that Perl requires a passwordless connection, so set up a public key. </p>
<p> Note that several apps spew crap to stderr every time you connect, which can throw off Configure. You may need to monkeypatch the part of Configure that creates <tt>&quot;run-ssh&quot;</tt> to have it discard stderr. </p>
<p> Since you&#8217;re using ssh, you&#8217;ll have to pass some extra arguments to Configure: </p>
<pre>
  -Dtargetrun=ssh -Dtargethost=$TARGETHOST -Dtargetuser=$TARGETUSER -Dtargetport=$TARGETPORT
</pre>
<h3>Configure and beyond</h3>
<p> With all of the previous done, you&#8217;re now ready to call Configure. </p>
<p> If using adb, a &#8220;basic&#8221; Configure line will look like this: </p>
<pre>
  $ ./Configure -des -Dusedevel -Dusecrosscompile -Dtargetrun=adb \
      -Dcc=$TARGETARCH-gcc   \
      -Dsysroot=$SYSROOT     \
      -Dtargetdir=$TARGETDIR \
      -Dtargethost=$DEVICE
</pre>
<p> If using ssh, it&#8217;s not too different &#8212; we just change targetrun to ssh, and pass in targetuser and targetport. It ends up looking like this: </p>
<pre>
  $ ./Configure -des -Dusedevel -Dusecrosscompile -Dtargetrun=ssh \
      -Dcc=$TARGETARCH-gcc        \
      -Dsysroot=$SYSROOT          \
      -Dtargetdir=$TARGETDIR      \
      -Dtargethost=&quot;$TARGETHOST&quot;  \
      -Dtargetuser=$TARGETUSER    \
      -Dtargetport=$TARGETPORT
</pre>
<p> Now you&#8217;re ready to run <tt>&quot;make&quot;</tt> and <tt>&quot;make test&quot;</tt>! </p>
<p> As a final word of warning, if you&#8217;re using adb, <tt>&quot;make test&quot;</tt> may appear to hang; this is because it doesn&#8217;t output anything until it finishes running all tests. You can check its progress by logging into the device, moving to <i></i>$TARGETDIR<i></i>, and looking at the file <i>output.stdout</i>. </p>
<p> <i>Notes</i></p>
<dl>
<dt>&bull;</p>
<dd> If you are targetting x86 Android, you will have to change <tt>&quot;$TARGETARCH-gcc&quot;</tt> to <tt>&quot;i686-linux-android-gcc&quot;</tt>.</p>
<dt>&bull;</p>
<dd> On some older low-end devices &#8212; think early 2.2 era &#8212; some tests, particularly <i>t/re/uniprops.t</i>, may crash the phone, causing it to turn itself off once, and then back on again.</dl>
<h2>Native Builds</h2>
<p> While Google doesn&#8217;t provide a native toolchain for Android, you can still get one from the Play Store; for example, there&#8217;s the CCTools app which you can get for free. Keep in mind that you want a full toolchain; some apps tend to default to installing only a barebones version without some important utilities, like ar or nm. </p>
<p> Once you have the toolchain set up properly, the only remaining hurdle is actually locating where in the device it was installed in. For example, CCTools installs its toolchain in <i>/data/data/com.pdaxrom.cctools/root/cctools</i>. With the path in hand, compiling perl is little more than: </p>
<pre>
 export SYSROOT=&lt;location of the native toolchain&gt;
 export LD_LIBRARY_PATH=&quot;$SYSROOT/lib:`pwd`:`pwd`/lib:`pwd`/lib/auto:$LD_LIBRARY_PATH&quot;
 sh Configure -des -Dsysroot=$SYSROOT -Alibpth=&quot;/system/lib /vendor/lib&quot;
</pre>
<h2>AUTHOR</h2>
<p> Brian Fraser &lt;fraserbn [at] gmail.com&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAK">Native Builds</a></p>
<dd>
<dt><a href="#lbAL">AUTHOR</a></p>
<dd></dl>
