---
title: "guestfs-building(1)"
name: "guestfs-building"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-building/"
description: "guestfs-building – How to build libguestfs from source"
---

<h2 class="name">NAME</h2>
<p> guestfs-building &#8211; How to build libguestfs from source </p>
<h2>DESCRIPTION</h2>
<p> This manual page describes how to build libguestfs from source. </p>
<p> The main steps are:</p>
<dl>
<dt>&bull;</p>
<dd> Install the requirements.</p>
<dt>&bull;</p>
<dd> Build, either from the git repository or from a tarball.</p>
<dt>&bull;</p>
<dd> Run the tests.</p>
<dt>&bull;</p>
<dd> Run the tools from the source directory, or install.</dl>
<h2>REQUIREMENTS</h2>
<h3>Short cut for Fedora or Red Hat Enterprise Linux (<font SIZE="-1">RHEL</font>) users</h3>
<p> On Fedora, use <code><a href="/docs/linux/man/8-dnf/">dnf</a></code>(8) to install all the requirements: </p>
<pre>
 dnf builddep libguestfs
 dnf install autoconf automake libtool gettext-devel
</pre>
<p> On systems still using <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8), do: </p>
<pre>
 yum-builddep libguestfs
 yum install autoconf automake libtool gettext-devel
</pre>
<h3>Short cut for Debian or Ubuntu users</h3>
<p> Use <font SIZE="-1">APT</font> to install all the requirements: </p>
<pre>
 apt-get build-dep libguestfs
 apt-get install autoconf automake libtool-bin gettext
</pre>
<p> If that command doesn&#8217;t work, take a look at the Debian source package <a rel="nofollow" href="http://packages.debian.org/source/libguestfs,">http://packages.debian.org/source/libguestfs,</a> at the list of <tt>&quot;build-depends&quot;</tt> and <tt>&quot;build-depends-indep&quot;</tt>, and install everything listed there.</p>
<h3>Full list of requirements</h3>
<dl>
<dt><i>appliance/packagelist.in</i></p>
<dd> Install as many package names found in this file as possible. (It is not strictly required to install all of them). </p>
<p> <i>Note</i>: If you build libguestfs followed by installing appliance packages, the build will not pick them up automatically, even if you do <tt>&quot;make clean&quot;</tt>. You have to do this command to clean the old supermin appliance and force a new one to be prepared: </p>
<pre>
 make -C appliance clean-supermin-appliance
</pre>
<dt>qemu ≥ 1.3.0</p>
<dd> <i>Required</i>.</p>
<dt>qemu-img ≥ 1.3.0</p>
<dd> <i>Required</i>. Virt-p2v and virt-v2v requires qemu-img ≥ 2.2.0.</p>
<dt>kernel ≥ 2.6.34</p>
<dd> <i>Required</i>. The following features must be enabled: <tt>&quot;virtio-pci&quot;</tt>, <tt>&quot;virtio-serial&quot;</tt>, <tt>&quot;virtio-block&quot;</tt>, <tt>&quot;virtio-net&quot;</tt>.</p>
<dt>supermin ≥ 5.1.0</p>
<dd> <i>Required</i>. For alternatives, see &#8220;<font SIZE="-1">USING A PREBUILT BINARY APPLIANCE&#8221;</font> below.</p>
<dt>glibc</p>
<dd> <i>Required</i>. We use the custom printf formatters extension of glibc (see &#8220;<font SIZE="-1">DAEMON CUSTOM PRINTF FORMATTERS&#8221;</font> in <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1)).</p>
<dt><font SIZE="-1">XDR</font> (tirpc, glibc or other)</p>
<dd> <i>Required</i>. We use the <font SIZE="-1">XDR</font> implementation from <tt>&quot;&lt;rpc/xdr.h&gt;&quot;</tt>, which may come from glibc, tirpc or another library. </p>
<p> The <tt>&quot;rpcgen&quot;</tt> tool is optional, except if you want to compile from git and/or patch libguestfs with new APIs.</p>
<dt>Gcc or Clang</p>
<dd> <i>Required</i>. We use <tt>&quot;__attribute__((cleanup))&quot;</tt> which is a <font SIZE="-1">GCC</font> extension also supported by Clang.</p>
<dt>Perl</p>
<dd> <i>Required</i>. Various build steps and tests are written in Perl. Perl is not needed at runtime except if you need to run a small number of virt tools which are still written in Perl.</p>
<dt>Perl &quot;Pod::Man&quot;</p>
<dd>
<dt>Perl &quot;Pod::Simple&quot;</p>
<dd> <i>Required</i>. Part of Perl core.</p>
<dt>OCaml ≥ 4.01</p>
<dd>
<dt>OCaml findlib</p>
<dd> <i>Required</i>.</p>
<dt>autoconf</p>
<dd>
<dt>automake</p>
<dd>
<dt>gettext</p>
<dd> <i>Required</i> if compiling from git. Optional if compiling from tarball.</p>
<dt>cpio</p>
<dd> <i>Required</i>.</p>
<dt>gperf</p>
<dd> <i>Required</i>.</p>
<dt>flex</p>
<dd>
<dt>bison</p>
<dd> <i>Required</i>.</p>
<dt>Perl-compatible Regular Expressions (<font SIZE="-1">PCRE</font>) library</p>
<dd> <i>Required</i>.</p>
<dt>genisoimage</p>
<dd> <i>Required</i>.</p>
<dt>libxml2</p>
<dd> <i>Required</i>.</p>
<dt>ncurses</p>
<dd> <i>Required</i>.</p>
<dt>augeas ≥ 1.0.0</p>
<dd> <i>Required</i>.</p>
<dt>xz</p>
<dd> <i>Required</i>.</p>
<dt>Jansson ≥ 2.7</p>
<dd> <i>Required</i>.</p>
<dt>po4a</p>
<dd> <i>Required</i> if compiling from git. Optional if compiling from tarball.</p>
<dt>hivex ≥ 1.2.7</p>
<dd>
<dt>ocaml-hivex</p>
<dd> <i>Required</i>. ocaml-hivex is the OCaml binding for hivex, which is required when building the daemon.</p>
<dt>libmagic</p>
<dd> <i>Required</i>. This is the library used by the <code><a href="/docs/linux/man/1-file/">file</a></code>(1) command.</p>
<dt>libvirt ≥ 0.10.2</p>
<dd> Optional. Always use the latest possible version of libvirt.</p>
<dt>xmllint</p>
<dd> Optional. Used only for tests.</p>
<dt>libconfig</p>
<dd> Optional. Used to parse libguestfs’s own config files, eg. <i>/etc/libguestfs-tools.conf</i>.</p>
<dt>libselinux</p>
<dd> Optional. Used by the libvirt backend to securely confine the appliance (sVirt).</p>
<dt>Berkeley <font SIZE="-1">DB</font> utils (db_dump, db_load, etc)</p>
<dd> Optional. Usually found in a package called <tt>&quot;db-utils&quot;</tt>, <tt>&quot;db4-utils&quot;</tt>, <tt>&quot;db4.X-utils&quot;</tt> etc.</p>
<dt>systemtap</p>
<dd> Optional. For userspace probes.</p>
<dt>readline</p>
<dd> Optional. For nicer command line editing in <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1).</p>
<dt>acl</p>
<dd> Optional. Library and programs for handling <font SIZE="-1">POSIX</font> ACLs.</p>
<dt>libcap</p>
<dd> Optional. Library and programs for handling Linux capabilities.</p>
<dt>libldm</p>
<dd> Optional. Library and <code><a href="/docs/linux/man/1-ldmtool/">ldmtool</a></code>(1) for handling Windows Dynamic Disks.</p>
<dt>sd-journal</p>
<dd> Optional. Library for accessing systemd journals.</p>
<dt>gdisk</p>
<dd> Optional. <font SIZE="-1">GPT</font> disk support.</p>
<dt>netpbm</p>
<dd> Optional. Render icons from guests.</p>
<dt>icoutils</p>
<dd> Optional. Render icons from Windows guests.</p>
<dt>Perl &quot;Expect&quot;</p>
<dd> Optional. Perl module used to test <code><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></code>(1).</p>
<dt><font SIZE="-1">FUSE</font></p>
<dd> Optional. <code><a href="/docs/linux/man/1-fusermount/">fusermount</a></code>(1), libfuse and kernel module are all needed if you want <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1) and/or mount-local support.</p>
<dt>static glibc</p>
<dd> Optional. Used only for testing.</p>
<dt>qemu-nbd</p>
<dd>
<dt>nbdkit</p>
<dd> Optional. qemu-nbd is used for testing. </p>
<p> <code><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></code>(1) requires either qemu-nbd or nbdkit, but these only need to be present on the virt-p2v <font SIZE="-1">ISO,</font> they do not need to be installed at compile time.</p>
<dt>uml_mkcow</p>
<dd> Optional. For the <font SIZE="-1">UML</font> backend.</p>
<dt>curl</p>
<dd> Optional. Used by virt-builder for downloads.</p>
<dt><font SIZE="-1">GNU</font> Privacy Guard (GnuPG, gpg) v1 or v2</p>
<dd> Optional. Used by virt-builder for checking digital signatures.</p>
<dt>liblzma</p>
<dd> Optional. If available, virt-builder will use this library for fast, parallel uncompression of templates.</p>
<dt>Gtk ≥ 2.24, or 3</p>
<dd> Optional. </p>
<p> Used by the virt-p2v graphical user interface. </p>
<p> Either Gtk 2 or Gtk 3 can be used. If you want to select a specific version of Gtk, use <tt>&quot;./configure --with-gtk=2&quot;</tt> or <tt>&quot;./configure --with-gtk=3&quot;</tt>.</p>
<dt>D-Bus</p>
<dd> Optional. </p>
<p> If the D-Bus low level C <font SIZE="-1">API</font> is available, virt-p2v can send a D-Bus message to logind to inhibit power saving (sleep, suspend, etc) during P2V conversions. </p>
<p> If this <font SIZE="-1">API</font> is not available at build time, then very long conversions might be interrupted if the physical machine goes to sleep.</p>
<dt>zip</p>
<dd>
<dt>unzip</p>
<dd> Optional. Used by virt-v2v to handle <font SIZE="-1">OVA</font> files.</p>
<dt>python-evtx</p>
<dd> Optional. Used by <code><a href="/docs/linux/man/1-virt-log/">virt-log</a></code>(1) to parse Windows Event Log files.</p>
<dt>OCaml gettext</p>
<dd> Optional. For localizing OCaml virt tools.</p>
<dt>ocaml-ounit ≥ 2.0.0</p>
<dd> Optional. For testing the common OCaml modules.</p>
<dt>ocaml-libvirt ≥ 0.6.1.5</p>
<dd> Optional. For building the optional virt-v2v test harness.</p>
<dt>Perl &quot;Module::Build&quot; ≥ 0.19</p>
<dd>
<dt>Perl &quot;Test::More&quot;</p>
<dd> Optional. Used to build and test the Perl bindings.</p>
<dt>Python ≥ 2.2</p>
<dd> Optional. Used to build the Python bindings. For building Python 2 or Python 3 bindings, see &#8220;<font SIZE="-1">BUILDING PYTHON 2 AND PYTHON 3 BINDINGS&#8221;</font> below.</p>
<dt>Python &quot;unittest&quot;</p>
<dd> Optional. Used to run the Python testsuite.</p>
<dt>Ruby</p>
<dd>
<dt>rake</p>
<dd>
<dt>rubygem-minitest</p>
<dd>
<dt>rubygem-rdoc</p>
<dd> Optional. Used to build the Ruby bindings.</p>
<dt>Java ≥ 1.6</p>
<dd> Optional. Java, <font SIZE="-1">JNI</font> and jpackage-utils are needed for building Java bindings.</p>
<dt><font SIZE="-1">GHC</font></p>
<dd> Optional. Used to build the Haskell bindings.</p>
<dt><font SIZE="-1">PHP</font></p>
<dd>
<dt>phpize</p>
<dd> Optional. Used to build the <font SIZE="-1">PHP</font> bindings.</p>
<dt>glib2</p>
<dd>
<dt>gobject-introspection</p>
<dd>
<dt>gjs</p>
<dd> Optional. Used to build and test the GObject bindings.</p>
<dt><font SIZE="-1">LUA</font></p>
<dd> Optional. Used to build the <font SIZE="-1">LUA</font> bindings.</p>
<dt>Erlang</p>
<dd>
<dt>erl_interface</p>
<dd> Optional. Used to build the Erlang bindings.</p>
<dt>golang ≥ 1.1.1</p>
<dd> Optional. Used to build the Go bindings.</p>
<dt>valgrind</p>
<dd> Optional. For testing memory problems.</p>
<dt>Perl &quot;Sys::Virt&quot;</p>
<dd> Optional.</p>
<dt>libvirt-python</p>
<dd> Optional. For testing Python libvirt/libguestfs interactions.</p>
<dt>Perl &quot;Win::Hivex&quot;</p>
<dd> Optional. Used by the <code><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></code>(1) tool.</p>
<dt>Perl &quot;Pod::Usage&quot;</p>
<dd> Optional. Used by some Perl virt tools.</p>
<dt>Perl &quot;libintl&quot;</p>
<dd> Optional.</p>
<dt>bash-completion</p>
<dd> Optional. For tab-completion of commands in bash.</p>
<dt>libtsk</p>
<dd> Optional. Library for filesystem forensics analysis.</p>
<dt>yara</p>
<dd> Optional. Tool for categorizing files based on their content.</dl>
<h2>BUILDING FROM GIT</h2>
<p> You will need to install additional dependencies <tt>&quot;autoconf&quot;</tt>, <tt>&quot;automake&quot;</tt>, <tt>&quot;gettext&quot;</tt>, OCaml findlib and po4a when building from git. </p>
<pre>
 git clone <a rel="nofollow" href="https://github.com/libguestfs/libguestfs">https://github.com/libguestfs/libguestfs</a>
 cd libguestfs
 ./autogen.sh
 make
</pre>
<h2>BUILDING FROM TARBALLS</h2>
<p> Tarballs are downloaded from <a rel="nofollow" href="http://download.libguestfs.org/.">http://download.libguestfs.org/.</a> Stable tarballs are signed with the GnuPG key for <tt>&quot;rich [at] annexia.org&quot;</tt>, see <a rel="nofollow" href="https://pgp.mit.edu/pks/lookup?op=vindex">https://pgp.mit.edu/pks/lookup?op=vindex</a>&amp;search=0x91738F73E1B768A0. The fingerprint is <tt>&quot;F777 4FB1 AD07 4A7E 8C87 67EA 9173 8F73 E1B7 68A0&quot;</tt>. </p>
<p> Download and unpack the tarball. </p>
<pre>
 cd libguestfs-1.xx.yy
 ./configure
 make
</pre>
<h2>RUNNING THE TESTS</h2>
<p> <font SIZE="-1"><code>DO NOT</code></font><code> run the tests as root!</code> Libguestfs can be built and tested as non-root. Running the tests as root could even be dangerous, don&#8217;t do it. </p>
<p> To sanity check that the build worked, do: </p>
<pre>
 make quickcheck
</pre>
<p> To run the basic tests, do: </p>
<pre>
 make check
</pre>
<p> There are many more tests you can run. See <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1) for details.</p>
<h2>INSTALLING</h2>
<p> <font SIZE="-1"><code>DO NOT</code></font><code> use </code>&quot;make install&quot;<code>!</code> You&#8217;ll end up with conflicting versions of libguestfs installed, and this causes constant headaches for users. See the next section for how to use the <i>./run</i> script instead. </p>
<p> Distro packagers can use: </p>
<pre>
 make INSTALLDIRS=vendor DESTDIR=[temp-build-dir] install
</pre>
<h2>THE ./run SCRIPT</h2>
<p> You can run <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1), <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1) and the virt tools without needing to install them by using the <i>./run</i> script in the top directory. This script works by setting several environment variables. </p>
<p> For example: </p>
<pre><code>
./ run guestfish[usual guestfish args...]./ run virt - inspector[usual virt - inspector args...]
</code></pre>
<p> The <i>./run</i> script adds every libguestfs binary to the <tt>$PATH</tt>, so the above examples run guestfish and virt-inspector from the build directory (not the globally installed guestfish if there is one). </p>
<p> You can use the script from any directory. If you wanted to run your own libguestfs-using program, then the following command will also work: </p>
<pre>
 /path/to/libguestfs/run ./my_program [...]
</pre>
<p> You can also run the C programs under valgrind like this: </p>
<pre><code>
./ run valgrind[valgrind opts...] virt - cat[virt - cat opts...]
</code></pre>
<p> or under gdb: </p>
<pre>
 ./run gdb --args virt-cat [virt-cat opts...]
</pre>
<p> This also works with sudo (eg. if you need root access for libvirt or to access a block device): </p>
<pre>
 sudo ./run virt-cat -d LinuxGuest /etc/passwd
</pre>
<p> To set environment variables, you can either do: </p>
<pre>
 LIBGUESTFS_HV=/my/qemu ./run guestfish
</pre>
<p> or: </p>
<pre>
 ./run env LIBGUESTFS_HV=/my/qemu guestfish
</pre>
<h2><i>local*</i> FILES</h2>
<p> Files in the top source directory that begin with the prefix <i>local*</i> are ignored by git. These files can contain local configuration or scripts that you need to build libguestfs. </p>
<p> I have a file called <i>localconfigure</i> which is a simple wrapper around <i>autogen.sh</i> containing local configure customizations that I need. It looks like this: </p>
<pre>
 . localenv
 ./autogen.sh \
     -C \
     --enable-werror \
     &quot;$@&quot;
</pre>
<p> So I can use this to build libguestfs: </p>
<pre>
 ./localconfigure &amp;&amp; make
</pre>
<p> If there is a file in the top build directory called <i>localenv</i>, then it will be sourced by <tt>&quot;make&quot;</tt>. This file can contain any local environment variables needed, eg. for skipping tests: </p>
<pre>
 # Use an alternate python binary.
 export PYTHON=python3
 # Skip this test, it is broken.
 export SKIP_TEST_BTRFS_FSCK=1
</pre>
<p> Note that <i>localenv</i> is included by the top Makefile (so it’s a Makefile fragment). But if it is also sourced by your <i>localconfigure</i> script then it is used as a shell script.</p>
<h2>SELECTED ./configure SETTINGS</h2>
<p> There are many <tt>&quot;./configure&quot;</tt> options. Use: </p>
<pre>
 ./configure --help
</pre>
<p> to list them all. This section covers some of the more important ones.</p>
<dl>
<dt><code>&#8211;disable-appliance &#8211;disable-daemon</code></p>
<dd> See &#8220;<font SIZE="-1">USING A PREBUILT BINARY APPLIANCE&#8221;</font> below.</p>
<dt><code>&#8211;disable-erlang</code></p>
<dd>
<dt><code>&#8211;disable-gobject</code></p>
<dd>
<dt><code>&#8211;disable-golang</code></p>
<dd>
<dt><code>&#8211;disable-haskell</code></p>
<dd>
<dt><code>&#8211;disable-lua</code></p>
<dd>
<dt><code>&#8211;disable-ocaml</code></p>
<dd>
<dt><code>&#8211;disable-perl</code></p>
<dd>
<dt><code>&#8211;disable-php</code></p>
<dd>
<dt><code>&#8211;disable-python</code></p>
<dd>
<dt><code>&#8211;disable-ruby</code></p>
<dd> Disable specific language bindings, even if <tt>&quot;./configure&quot;</tt> finds all the necessary libraries are installed so that they could be compiled. </p>
<p> Note that disabling OCaml (bindings) or Perl will have the knock-on effect of disabling parts of the test suite and some tools. </p>
<p> OCaml is required to build libguestfs and this requirement cannot be removed. Using <i>&#8211;disable-ocaml</i> only disables the bindings and OCaml tools.</p>
<dt><code>&#8211;disable-fuse</code></p>
<dd> Disable <font SIZE="-1">FUSE</font> support in the <font SIZE="-1">API</font> and the <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1) tool.</p>
<dt><code>&#8211;disable-gnulib-tests</code></p>
<dd> On some platforms the GNUlib test suite can be flaky. This disables it, since errors in the GNUlib test suite are often not important.</p>
<dt><code>&#8211;disable-static</code></p>
<dd> Don’t build a static linked version of the libguestfs library.</p>
<dt><code>&#8211;enable-install-daemon</code></p>
<dd> Normally <code><a href="/docs/linux/man/8-guestfsd/">guestfsd</a></code>(8) is not installed by <tt>&quot;make install&quot;</tt>, since that wouldn&#8217;t be useful (instead it is &#8220;installed&#8221; inside the supermin appliance). However if packagers are building &#8220;libguestfs live&#8221; then they should use this option.</p>
<dt><code>&#8211;enable-werror</code></p>
<dd> This turns compiler warnings into errors (ie. <tt>&quot;-Werror&quot;</tt>). Use this for development, especially when submitting patches. It should generally <i>not</i> be used for production or distro builds.</p>
<dt><code>&#8211;with-default-backend=libvirt</code></p>
<dd> This controls the default method that libguestfs uses to run qemu (see &#8220;<font SIZE="-1">BACKEND&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)). If not specified, the default backend is <tt>&quot;direct&quot;</tt>, which means libguestfs runs qemu directly. </p>
<p> Fedora and Red Hat Enterprise Linux (<font SIZE="-1">RHEL</font>) ≥ 7 use this flag to change the default backend to <tt>&quot;libvirt&quot;</tt>, because (especially in <font SIZE="-1">RHEL</font>) the policy is not to allow any program to run qemu except via libvirt. </p>
<p> Note that despite this setting, all backends are built into libguestfs, and you can override the backend at runtime by setting the <tt>$LIBGUESTFS_BACKEND</tt> environment variable (or using <font SIZE="-1">API</font> methods).</p>
<dt><code>&#8211;with-distro=REDHAT|DEBIAN|&#8230;</code></p>
<dd> Libguestfs needs to know which Linux distro is in use so it can choose package names for the appliance correctly (see for example <i>appliance/packagelist.in</i>). It normally does this automatically. </p>
<p> However if you can building or packaging libguestfs on a new distro then you can use <i>&#8211;with-distro</i> to specify that the distro is similar to an existing one (eg. <i>&#8211;with-distro=REDHAT</i> if the distro is a new Red Hat or CentOS derivative). </p>
<p> Note that if your distro is completely new then it may still require upstream modifications.</p>
<dt><code>&#8211;with-extra=&quot;</code><i>distroname</i>=<i>version</i>,libvirt,&#8230;<code>&quot;</code></p>
<dd>
<dt><code>&#8211;with-extra=&quot;local&quot;</code></p>
<dd> This option controls the &#8220;extra&#8221; field returned by &#8220;guestfs_version&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) and also printed by virt tools&#8217; <i>&#8211;version</i> option. It is a free text field, but a good idea is to encode a comma-separated list of facts such as the distro name and version, whether libvirt is the default backend, and anything else that may help with debugging problems raised by users. </p>
<p> For custom and/or local builds, this can be set to <tt>&quot;local&quot;</tt> to indicate this is <i>not</i> a distro build.</p>
<dt><code>&#8211;without-libvirt</code></p>
<dd> Compile libguestfs without libvirt support, even if libvirt development libraries are installed.</p>
<dt><code>&#8211;with-gtk=2</code></p>
<dd> This option forces virt-p2v to be built against Gtk 2, which is currently the most widely tested configuration.</p>
<dt><code>&#8211;with-qemu=&quot;</code>bin1 bin2 &#8230;<code>&quot;</code></p>
<dd> Provide an alternate qemu binary (or list of binaries). This can be overridden at runtime by setting the <tt>&quot;LIBGUESTFS_HV&quot;</tt> environment variable.</p>
<dt><code>&#8211;with-supermin-packager-config=</code><i>yum.conf</i></p>
<dd> This passes the <i>&#8211;packager-config</i> option to <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1). </p>
<p> The most common use for this is to build the appliance using an alternate repository (instead of using the installed yum/dnf/apt/etc configuration to find and download packages). You might need to use this if you want to build libguestfs without having a network connection. Examples of using this can be found in the Fedora <tt>&quot;libguestfs.spec&quot;</tt> file (see &#8220;<font SIZE="-1">BUILDING A PACKAGE FOR FEDORA&#8221;</font> below for resources).</p>
<dt><code>&#8211;with-supermin-extra-options=&quot;</code>&#8211;opt1 &#8211;opt2 &#8230;<code>&quot;</code></p>
<dd> Pass additional options to <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1). See <i>appliance/make.sh.in</i> to understand precisely what this does.</p>
<dt><font SIZE="-1"><code>PYTHON</code></font></p>
<dd> This environment variable may be set to point to a python binary (eg. <tt>&quot;python3&quot;</tt>). When <tt>&quot;./configure&quot;</tt> runs, it inspects this python binary to find the version of Python, the location of Python libraries and so on. See &#8220;<font SIZE="-1">BUILDING PYTHON 2 AND PYTHON 3 BINDINGS&#8221;</font> below.</p>
<dt><font SIZE="-1"><code>SUPERMIN</code></font></p>
<dd> This environment variable can be set to choose an alternative <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1) binary. This might be used, for example, if you want to use a newer upstream version of supermin than is packaged for your distro, or if supermin is not packaged at all. On <font SIZE="-1">RHEL 7,</font> you must set <tt>&quot;SUPERMIN=/usr/bin/supermin5&quot;</tt> when compiling libguestfs.</dl>
<h2>NOTES ABOUT QEMU AND KVM</h2>
<p> A common problem is with broken or incompatible qemu releases. </p>
<p> Different versions of qemu have problems booting the appliance for different reasons. This varies between versions of qemu, and Linux distributions which add their own patches. </p>
<p> If you find a problem, you could try using your own qemu built from source (qemu is very easy to build from source), with a &#8220;qemu wrapper&#8221;. See &#8220;<font SIZE="-1">QEMU WRAPPERS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3). </p>
<p> By default the configure script will look for qemu-kvm (<font SIZE="-1">KVM</font> support). <font SIZE="-1">KVM</font> is much faster than using plain qemu. </p>
<p> You may also need to enable <font SIZE="-1">KVM</font> support for non-root users, by following these instructions: <a rel="nofollow" href="http://www.linux-kvm.org/page/FAQ#How_can_I_use_kvm_with_a_non-privileged_user.3F">http://www.linux-kvm.org/page/FAQ#How_can_I_use_kvm_with_a_non-privileged_user.3F</a> </p>
<p> On some systems, this will work too: </p>
<pre>
 chmod 0666 /dev/kvm
</pre>
<p> On some systems, the chmod will not survive a reboot, and you will need to make edits to the udev configuration.</p>
<h2>USING CLANG (LLVM) INSTEAD OF GCC</h2>
<pre>
 export CC=clang
 ./configure
 make
</pre>
<h2>USING A PREBUILT BINARY APPLIANCE</h2>
<p> To understand what the libguestfs appliance means, see <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1). </p>
<p> If you are using non-Linux, or a Linux distribution that does not have <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1) support, or simply if you don&#8217;t want to build your own libguestfs appliance, then you can use one of the prebuilt binary appliances that we supply: <a rel="nofollow" href="http://libguestfs.org/download/binaries/appliance">http://libguestfs.org/download/binaries/appliance</a> </p>
<p> Build libguestfs like this: </p>
<pre>
 ./configure --disable-appliance --disable-daemon
 make
</pre>
<p> Set <tt>$LIBGUESTFS_PATH</tt> to the path where you unpacked the appliance tarball, eg: </p>
<pre>
 export LIBGUESTFS_PATH=/usr/local/lib/guestfs/appliance
</pre>
<p> and run the libguestfs programs and virt tools in the normal way, eg. using the <i>./run</i> script (see above).</p>
<h2>BUILDING PYTHON 2 AND PYTHON 3 BINDINGS</h2>
<p> The <i>./configure</i> script detects the currently installed version of Python using whatever program is called <tt>&quot;python&quot;</tt> in the current <tt>$PATH</tt>. Libguestfs will build Python 2 or Python 3 bindings as appropriate. </p>
<p> You can override this behaviour by specifying an alternate Python binary, eg: </p>
<pre>
 PYTHON=/usr/bin/python3 ./configure
</pre>
<p> To build parallel Python 2 and Python 3 bindings, you will need to build libguestfs twice. The second time, you can disable all the other bindings and tools and just build the Python bindings. See the Fedora spec file (see below) for a complete example of how to do this.</p>
<h2>BUILDING A PACKAGE FOR FEDORA</h2>
<p> The Fedora spec file is stored under: <a rel="nofollow" href="http://pkgs.fedoraproject.org/cgit/rpms/libguestfs.git/">http://pkgs.fedoraproject.org/cgit/rpms/libguestfs.git/</a> </p>
<p> Libguestfs is built in Fedora using the ordinary Fedora build system (Koji).</p>
<h2>BUILDING A PACKAGE FOR RED HAT ENTERPRISE LINUX</h2>
<p> Red Hat Enterprise Linux (<font SIZE="-1">RHEL</font>) builds of libguestfs are heavily patched. There are broadly two types of patches we apply:</p>
<dl>
<dt>&bull;</p>
<dd> We disable many features that we do not wish to support for <font SIZE="-1">RHEL</font> customers. For example, the &#8220;libguestfs live&#8221; feature is disabled.</p>
<dt>&bull;</p>
<dd> We backport upstream features.</dl>
<p> The patches we apply to <font SIZE="-1">RHEL</font> releases are available publically in the upstream git repository, in a branch called <tt>&quot;rhel-x.y&quot;</tt> </p>
<p> For example, the <font SIZE="-1">RHEL 7.3</font> patches are available here: <a rel="nofollow" href="https://github.com/libguestfs/libguestfs/commits/rhel-7.3">https://github.com/libguestfs/libguestfs/commits/rhel-7.3</a> </p>
<p> The sources and spec files for <font SIZE="-1">RHEL</font> versions of libguestfs are available on <a rel="nofollow" href="https://git.centos.org/project/rpms,">https://git.centos.org/project/rpms,</a> and see also <a rel="nofollow" href="https://wiki.centos.org/Sources.">https://wiki.centos.org/Sources.</a></p>
<h2>BUILDING i686 32 BIT VIRT-P2V</h2>
<p> <i>(This section only applies on the x86-64 architecture.)</i> </p>
<p> Building a 32 bit virt-p2v (i686) binary improves compatibility with older hardware. See <code><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></code>(1) for details. Although virt-p2v is a simple Gtk application, it is not especially easy to build just virt-p2v as a 32 bit application on a 64 bit host. Usually the simplest way is to use a 32 bit chroot or even a 32 bit virtual machine to build libguestfs. </p>
<p> On Fedora you can use the <code><a href="/docs/linux/man/1-mock/">mock</a></code>(1) tool. For example: </p>
<pre>
 fedpkg mockbuild --root fedora-23-i386
</pre>
<p> This will result in a <i>virt-v2v-*.i686.rpm</i> file which can be unpacked to extract the 32 bit virt-p2v binary. </p>
<p> The binary may be compressed to either <i>p2v/virt-p2v.i686.xz</i>, or <i></i>$libdir<i>/virt-p2v/virt-p2v.i686.xz</i> or <i></i>$VIRT_P2V_DATA_DIR<i>/virt-p2v.i686.xz</i> as appropriate. This enables the <code><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></code>(1) <i>&#8211;arch</i> option.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), <code><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></code>(3), <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-performance/">guestfs-performance</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-release-notes/">guestfs-release-notes</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-testing/">guestfs-testing</a></code>(1), <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1), <code><a href="/docs/linux/man/1-libguestfs-make-fixed-appliance/">libguestfs-make-fixed-appliance</a></code>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2019 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> Lesser General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAH">BUILDING FROM GIT</a></p>
<dd>
<dt><a href="#lbAI">BUILDING FROM TARBALLS</a></p>
<dd>
<dt><a href="#lbAJ">RUNNING THE TESTS</a></p>
<dd>
<dt><a href="#lbAK">INSTALLING</a></p>
<dd>
<dt><a href="#lbAL">THE ./run SCRIPT</a></p>
<dd>
<dt><a href="#lbAM"><i>local*</i> FILES</a></p>
<dd>
<dt><a href="#lbAN">SELECTED ./configure SETTINGS</a></p>
<dd>
<dt><a href="#lbAO">NOTES ABOUT QEMU AND KVM</a></p>
<dd>
<dt><a href="#lbAP">USING CLANG (LLVM) INSTEAD OF GCC</a></p>
<dd>
<dt><a href="#lbAQ">USING A PREBUILT BINARY APPLIANCE</a></p>
<dd>
<dt><a href="#lbAR">BUILDING PYTHON 2 AND PYTHON 3 BINDINGS</a></p>
<dd>
<dt><a href="#lbAS">BUILDING A PACKAGE FOR FEDORA</a></p>
<dd>
<dt><a href="#lbAT">BUILDING A PACKAGE FOR RED HAT ENTERPRISE LINUX</a></p>
<dd>
<dt><a href="#lbAU">BUILDING i686 32 BIT VIRT-P2V</a></p>
<dd>
<dt><a href="#lbAV">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAW">AUTHORS</a></p>
<dd>
<dt><a href="#lbAX">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAY">LICENSE</a></p>
<dd>
<dt><a href="#lbAZ">BUGS</a></p>
<dd></dl>
