---
title: "prelink(5)"
name: "prelink"
section: "5"
letter: "p"
url: "/docs/linux/man/5-prelink/"
description: "prelink – prelink ELF shared libraries and binaries to speed up startup time"
---

<p>prelink &#8211; prelink ELF shared libraries and binaries to speed up startup time</p>
<h2>Synopsis</h2>
<p>prelink [OPTION&#8230;]&nbsp;<wbr>[FILES]</p>
<h2>Description</h2>
<p><code>prelink</code> is a program that modifies ELF shared libraries and ELF dynamically linked binaries in such a way that the time needed for the dynamic linker to perform relocations at startup significantly decreases. Due to fewer relocations, the run-time memory consumption decreases as well (especially the number of unshareable pages). The prelinking information is only used at startup time if none of the dependent libraries have changed since prelinking; otherwise programs are relocated normally. </p>
<p> <code>prelink</code> first collects ELF binaries to be prelinked and all the ELF shared libraries they depend on. Then it assigns a unique virtual address space slot to each library and relinks the shared library to that base address. When the dynamic linker attempts to load such a library, unless that virtual address space slot is already occupied, it maps the library into the given slot. After this is done, <code>prelink</code>, with the help of dynamic linker, resolves all relocations in the binary or library against its dependent libraries and stores the relocations into the ELF object. It also stores a list of all dependent libraries together with their checksums into the binary or library. For binaries, it also computes a list of <i>conflicts</i> (relocations that resolve differently in the binary&#8217;s symbol search scope than in the smaller search scope in which the dependent library was resolved) and stores it into a special ELF section. </p>
<p> At runtime, the dynamic linker first checks whether all dependent libraries were successfully mapped into their designated address space slots, and whether they have not changed since the prelinking was done. If all checks are successful, the dynamic linker just replays the list of conflicts (which is usually significantly shorter than total number of relocations) instead of relocating each library.</p>
<h2>Options</h2>
<dl>
<dt><code>-v &#8211;verbose</code></p>
<dd>Verbose mode. Print the virtual address slots assigned to libraries and what binary or library is currently being prelinked.</p>
<dt><code>-n &#8211;dry-run</code></p>
<dd>Don&#8217;t actually prelink anything; just collect the binaries/libraries, assign them addresses, and with <code>-v </code> print what would be prelinked.</p>
<dt><code>-a &#8211;all</code></p>
<dd>Prelink all binaries and dependent libraries found in directory hierarchies specified in <i>/etc/prelink.conf</i>. Normally, only binaries specified on the command line and their dependent libraries are prelinked.</p>
<dt><code>-m &#8211;conserve-memory</code></p>
<dd>When assigning addresses to libraries, allow overlap of address space slots provided that the two libraries are not present together in any of the binaries or libraries. This results in a smaller virtual address space range used for libraries. On the other hand, if <code>prelink</code> sees a binary during incremental prelinking which puts together two libraries which were not present together in any other binary and were given the same virtual address space slots, then the binary cannot be prelinked. Without this option, each library is assigned a unique virtual address space slot.</p>
<dt><code>-R &#8211;random</code></p>
<dd>When assigning addresses to libraries, start with a random address within the architecture-dependent virtual address space range. This can make some buffer overflow attacks slightly harder to exploit, because libraries are not present on the same addresses across different machines. Normally, assigning virtual addresses starts at the bottom of the architecture-dependent range.</p>
<dt><code>-r &#8211;reloc-only=ADDRESS</code></p>
<dd>Instead of prelinking, just relink given shared libraries to the specified base address.</p>
<dt><code>-N &#8211;no-update-cache</code></p>
<dd>Don&#8217;t save the cache file after prelinking. Normally, the list of libraries (and with <code>-m</code> binaries also) is stored into the <i>/etc/prelink.cache</i> file together with their given address space slots and dependencies, so the cache can be used during incremental prelinking (prelinking without <code>-a</code> option).</p>
<dt><code>-c &#8211;config-file=CONFIG</code></p>
<dd>Specify an alternate config file instead of default <i>/etc/prelink.conf</i>.</p>
<dt><code>-C &#8211;cache-file=CACHE</code></p>
<dd>Specify an alternate cache file instead of default <i>/etc/prelink.cache</i>.</p>
<dt><code>-f &#8211;force</code></p>
<dd>Force re-prelinking even for already prelinked objects whose dependencies are unchanged. This option causes new virtual address space slots to be assigned to all libraries. Normally, only binaries or libraries which are either not prelinked yet, or whose dependencies have changed, are prelinked.</p>
<dt><code>-q &#8211;quick</code></p>
<dd>Run prelink in quick mode. This mode checks just mtime and ctime timestamps of libraries and binaries stored in the cache file. If they are unchanged from the last prelink run, it is assumed that the library in question did not change, without parsing or verifying its ELF headers.</p>
<dt><code>-p &#8211;print-cache</code></p>
<dd>Print the contents of the cache file (normally <i>/etc/prelink.cache</i>) and exit.</p>
<dt><code>&#8211;dynamic-linker=LDSO</code></p>
<dd>Specify an alternate dynamic linker instead of the default.</p>
<dt><code>&#8211;ld-library-path=PATH</code></p>
<dd>Specify a special <i>LD_LIBRARY_PATH</i> to be used when <code>prelink</code> queries the dynamic linker about symbol resolution details.</p>
<dt><code>&#8211;libs-only</code></p>
<dd>Only prelink ELF shared libraries, don&#8217;t prelink any binaries.</p>
<dt><code>-h &#8211;dereference</code></p>
<dd>When processing command line directory arguments, follow symbolic links when walking directory hierarchies.</p>
<dt><code>-l &#8211;one-file-system</code></p>
<dd>When processing command line directory arguments, limit directory tree walk to a single file system.</p>
<dt><code>-u &#8211;undo</code></p>
<dd>Revert binaries and libraries to their original content before they were prelinked. Without the <i>-a</i> option, this causes only the binaries and libraries specified on the command line to be reverted to their original state (and e.g. not their dependencies). If used together with the <i>-a</i> option, all binaries and libraries from command line, all their dependencies, all binaries found in directories specified on command line and in the config file, and all their dependencies are undone.</p>
<dt><code>-y &#8211;verify</code></p>
<dd>Verifies a prelinked binary or library. This option can be used only on a single binary or library. It first applies an <i>&#8211;undo</i> operation on the file, then prelinks just that file again and compares this with the original file. If both are identical, it prints the file after <i>&#8211;undo</i> operation on standard output and exits with zero status. Otherwise it exits with error status. Thus if <i>&#8211;verify</i> operation returns zero exit status and its standard output is equal to the content of the binary or library before prelinking, you can be sure that nobody modified the binaries or libraries after prelinking. Similarly with message digests and checksums (unless you trigger the improbable case of modified file and original file having the same digest or checksum).</p>
<dt><code>&#8211;md5</code></p>
<dd>This is similar to <i>&#8211;verify</i> option, except instead of outputting the content of the binary or library before prelinking to standard output, MD5 digest is printed. See <code><a href="/docs/linux/man/1-md5sum/">md5sum</a></code>(1).</p>
<dt><code>&#8211;sha</code></p>
<dd>This is similar to <i>&#8211;verify</i> option, except instead of outputting the content of the binary or library before prelinking to standard output, SHA1 digest is printed. See <code><a href="/docs/linux/man/1-sha1sum/">sha1sum</a></code>(1).</p>
<dt><code>&#8211;exec-shield &#8211;no-exec-shield</code></p>
<dd>On IA-32, if the kernel supports Exec-Shield, prelink attempts to lay libraries out similarly to how the kernel places them (i.e. if possible below the binary, most widely used into the ASCII armor zone). These switches allow overriding prelink detection of whether Exec-Shield is supported or not.</p>
<dt><code>-b &#8211;black-list=PATH</code></p>
<dd>This option allows blacklisting certain paths, libraries or binaries. Prelink will not touch them during prelinking.</p>
<dt><code>-o &#8211;undo-output=FILE</code></p>
<dd>When performing an <code>&#8211;undo</code> operation, don&#8217;t overwrite the prelinked binary or library with its original content (before it was prelinked), but save that into the specified file.</p>
<dt><code>-V &#8211;version</code></p>
<dd>Print version and exit.</p>
<dt><code>-? &#8211;help</code></p>
<dd>Print short help and exit.</dl>
<h2>Arguments</h2>
<p>Command-line arguments should be either directory hierarchies (in which case <i>-l</i> and <i>-h</i> options apply), or particular ELF binaries or shared libraries. Specifying a shared library explicitly on the command line causes it to be prelinked even if no binary is linked against it. Otherwise, binaries are collected together and only the libraries they depend on are prelinked with them.</p>
<h2>Examples</h2>
<dl>
<dd># /usr/sbin/prelink -avmR</dl>
<p> prelinks all binaries found in directories specified in <i>/etc/prelink.conf</i> and all their dependent libraries, assigning libraries unique virtual address space slots only if they ever appear together, and starts assigning libraries at a random address.</p>
<dl>
<dd># /usr/sbin/prelink -vm ~/bin/progx</dl>
<p> prelinks ~/bin/progx program and all its dependent libraries (unless they were prelinked already e.g. during <i>prelink -a</i> invocation).</p>
<dl>
<dd># /usr/sbin/prelink -au</dl>
<p> reverts all binaries and libraries to their original content.</p>
<dl>
<dd># /usr/sbin/prelink -y /bin/prelinked_prog &gt; /tmp/original_prog; echo $? verifies whether /bin/prelinked_prog is unchanged.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/prelink.cache</code></p>
<dd>Binary file containing a list of prelinked libraries and/or binaries together with their assigned virtual address space slots and dependencies. You can run <i>/usr/sbin/prelink -p</i> to see what is stored in there.</p>
<dt><code>/etc/prelink.conf</code></p>
<dd>Configuration file containing a list of directory hierarchies that contain ELF shared libraries or binaries which should be prelinked. This configuration file is used in <code>-a</code> mode to find binaries which should be prelinked and also, no matter whether <code>-a</code> is given or not, to limit which dependent shared libraries should be prelinked. If <code>prelink</code> finds a dependent library of some binary or other library which is not present in any of the directories specified either in <code>/etc/prelink.conf</code> or on the command line, then it cannot be prelinked. Each line of the config file should be either a comment starting with <code>#</code>, or a directory name, or a blacklist specification. Directory names can be prefixed by the <code>-l</code> switch, meaning the tree walk of the given directory is only limited to one file system; or the <code>-h</code> switch, meaning the tree walk of the given directory follows symbolic links. A blacklist specification should be prefixed by <code>-b</code> and optionally also <code>-l</code> or <code>-h</code> if needed. A blacklist entry can be either an absolute directory name (in that case all files in that directory hierarchy are ignored by the prelinker); an absolute filename (then that particular library or binary is skipped); or a glob pattern without a <code>/</code> character in it (then all files matching that glob in any directory are ignored).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8).</p>
<h2>Bugs</h2>
<p><code>prelink</code> Some architectures, including IA-64 and HPPA, are not yet supported.</p>
<h2>Authors</h2>
<p>Jakub Jelinek &lt;jakub [at] redhat.com&gt;.</p>
