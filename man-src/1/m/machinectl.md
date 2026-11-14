---
title: "machinectl(1)"
name: "machinectl"
section: "1"
letter: "m"
url: "/docs/linux/man/1-machinectl/"
description: "machinectl – Control the systemd machine manager"
---

<h2 class="name">NAME</h2>
<p> machinectl &#8211; Control the systemd machine manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>machinectl</code> [OPTIONS&#8230;] {COMMAND} [NAME&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>machinectl</code></p>
<dd>may be used to introspect and control the state of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) virtual machine and container registration manager <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8).</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-p</code>, <code>&#8211;property=</code></p>
<dl>
<dt>
<dd> When showing machine or image properties, limit the output to certain properties as specified by the argument. If not specified, all set properties are shown. The argument should be a property name, such as &quot;Name&quot;. If specified more than once, all properties with the specified names are shown.</dl>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> When showing machine or image properties, show all properties regardless of whether they are set or not. </p>
<p> When listing VM or container images, do not suppress images beginning in a dot character (&quot;.&quot;).</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize process tree entries.</dl>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;kill-who=</code></p>
<dl>
<dt>
<dd> When used with <code>kill</code>, choose which processes to kill. Must be one of <code>leader</code>, or <code>all</code> to select whether to kill only the leader process of the machine or all processes of the machine. If omitted, defaults to <code>all</code>.</dl>
<p> <code>-s</code>, <code>&#8211;signal=</code></p>
<dl>
<dt>
<dd> When used with <code>kill</code>, choose which signal to send to selected processes. Must be one of the well-known signal specifiers, such as <code>SIGTERM</code>, <code>SIGINT</code> or <code>SIGSTOP</code>. If omitted, defaults to <code>SIGTERM</code>.</dl>
<p> <code>&#8211;mkdir</code></p>
<dl>
<dt>
<dd> When used with <code>bind</code> creates the destination directory before applying the bind mount.</dl>
<p> <code>&#8211;read-only</code></p>
<dl>
<dt>
<dd> When used with <code>bind</code> applies a read-only bind mount.</dl>
<p> <code>-n</code>, <code>&#8211;lines=</code></p>
<dl>
<dt>
<dd> When used with <code>status</code>, controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument. Defaults to 10.</dl>
<p> <code>-o</code>, <code>&#8211;output=</code></p>
<dl>
<dt>
<dd> When used with <code>status</code>, controls the formatting of the journal entries that are shown. For the available choices, see <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). Defaults to &quot;short&quot;.</dl>
<p> <code>&#8211;verify=</code></p>
<dl>
<dt>
<dd> When downloading a container or VM image, specify whether the image shall be verified before it is made available. Takes one of &quot;no&quot;, &quot;checksum&quot; and &quot;signature&quot;. If &quot;no&quot; no verification is done. If &quot;checksum&quot; is specified the download is checked for integrity after transfer is complete, but no signatures are verified. If &quot;signature&quot; is specified, the checksum is verified and the images&#8217;s signature is checked against a local keyring of trustable vendors. It is strongly recommended to set this option to &quot;signature&quot; if the server and protocol support this. Defaults to &quot;signature&quot;.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> When downloading a container or VM image, and a local copy by the specified local machine name already exists, delete it first and replace it by the newly downloaded image.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a container name, separated by &quot;:&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
<dd> Do not print the legend, i.e. column headers and the footer with hints.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>COMMANDS</h2>
<p> The following commands are understood:</p>
<h3>Machine Commands</h3>
<p> <code>list</code></p>
<dl>
<dt>
<dd> List currently running (online) virtual machines and containers. To enumerate container images that can be started, use <code>list-images</code> (see below).</dl>
<p> <code>status</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more virtual machines and containers, followed by the most recent log data from the journal. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show</code> instead. Note that the log data shown is reported by the virtual machine or container manager, and frequently contains console output of the machine, but not necessarily journal contents of the machine itself.</dl>
<p> <code>show</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Show properties of one or more registered virtual machines or containers or the manager itself. If no argument is specified, properties of the manager will be shown. If an NAME is specified, properties of this virtual machine or container are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>start</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Start a container as a system service, using <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1). This starts systemd-nspawn [at] .service, instantiated for the specified machine name, similar to the effect of <code>systemctl start</code> on the service name. <code>systemd-nspawn</code> looks for a container image by the specified name in /var/lib/machines/ (and other search paths, see below) and runs it. Use <code>list-images</code> (see below), for listing available container images to start. </p>
<p> Note that <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8) also interfaces with a variety of other container and VM managers, <code>systemd-nspawn</code> is just one implementation of it. Most of the commands available in <code>machinectl</code> may be used on containers or VMs controlled by other managers, not just <code>systemd-nspawn</code>. Starting VMs and container images on those managers requires manager-specific tools. </p>
<p> To interactively start a container on the command line with full access to the container&#8217;s console, please invoke <code>systemd-nspawn</code> directly. To stop a running container use <code>machinectl poweroff</code>, see below.</dl>
<p> <code>login</code> <i>NAME</i></p>
<dl>
<dt>
<dd> Open an interactive terminal login session to a container. This will create a TTY connection to a specific container and asks for the execution of a getty on it. Note that this is only supported for containers running <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) as init system. </p>
<p> This command will open a full login prompt on the container, which then asks for username and password. Use <code><a href="/docs/linux/man/1-systemd-run/">systemd-run</a></code>(1) with the <code>&#8211;machine=</code> switch to invoke a single command, either interactively or in the background within a local container.</dl>
<p> <code>enable</code> <i>NAME</i>&#8230;, <code>disable</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Enable or disable a container as a system service to start at system boot, using <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1). This enables or disables systemd-nspawn [at] .service, instantiated for the specified machine name, similar to the effect of <code>systemctl enable</code> or <code>systemctl disable</code> on the service name.</dl>
<p> <code>poweroff</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Power off one or more containers. This will trigger a reboot by sending SIGRTMIN+4 to the container&#8217;s init process, which causes systemd-compatible init systems to shut down cleanly. This operation does not work on containers that do not run a <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)-compatible init system, such as sysvinit. Use <code>terminate</code> (see below) to immediately terminate a container or VM, without cleanly shutting it down.</dl>
<p> <code>reboot</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Reboot one or more containers. This will trigger a reboot by sending SIGINT to the container&#8217;s init process, which is roughly equivalent to pressing Ctrl+Alt+Del on a non-containerized system, and is compatible with containers running any system manager.</dl>
<p> <code>terminate</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Immediately terminates a virtual machine or container, without cleanly shutting it down. This kills all processes of the virtual machine or container and deallocates all resources attached to that instance. Use <code>poweroff</code> to issue a clean shutdown request.</dl>
<p> <code>kill</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Send a signal to one or more processes of the virtual machine or container. This means processes as seen by the host, not the processes inside the virtual machine or container. Use <code>&#8211;kill-who=</code> to select which process to kill. Use <code>&#8211;signal=</code> to select the signal to send.</dl>
<p> <code>bind</code> <i>NAME</i> <i>PATH</i> [<i>PATH</i>]</p>
<dl>
<dt>
<dd> Bind mounts a directory from the host into the specified container. The first directory argument is the source directory on the host, the second directory argument the source directory on the host. When the latter is omitted the destination path in the container is the same as the source path on the host. When combined with the <code>&#8211;read-only</code> switch a ready-only bind mount is created. When combined with the <code>&#8211;mkdir</code> switch the destination path is first created before the mount is applied. Note that this option is currently only supported for <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) containers.</dl>
<p> <code>copy-to</code> <i>NAME</i> <i>PATH</i> [<i>PATH</i>]</p>
<dl>
<dt>
<dd> Copies files or directories from the host system into a running container. Takes a container name, followed by the source path on the host and the destination path in the container. If the destination path is omitted the same as the source path is used.</dl>
<p> <code>copy-from</code> <i>NAME</i> <i>PATH</i> [<i>PATH</i>]</p>
<dl>
<dt>
<dd> Copies files or directories from a container into the host system. Takes a container name, followed by the source path in the container the destination path on the host. If the destination path is omitted the same as the source path is used.</dl>
<h3>Image Commands</h3>
<p> <code>list-images</code></p>
<dl>
<dt>
<dd> Show a list of locally installed container and VM images. This enumerates all raw disk images and container directories and subvolumes in /var/lib/machines/ (and other search paths, see below). Use <code>start</code> (see above) to run a container off one of the listed images. Note that by default containers whose name begins with a dot (&quot;.&quot;) are not shown. To show these too, specify <code>&#8211;all</code>. Note that a special image &quot;.host&quot; always implicitly exists and refers to the image the host itself is booted from.</dl>
<p> <code>image-status</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Show terse status information about one or more container or VM images. This function is intended to generate human-readable output. Use <code>show-image</code> (see below) to generate computer-parsable output instead.</dl>
<p> <code>show-image</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Show properties of one or more registered virtual machine or container images, or the manager itself. If no argument is specified, properties of the manager will be shown. If an NAME is specified, properties of this virtual machine or container image are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>image-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>clone</code> <i>NAME</i> <i>NAME</i></p>
<dl>
<dt>
<dd> Clones a container or disk image. The arguments specify the name of the image to clone and the name of the newly cloned image. Note that plain directory container images are cloned into subvolume images with this command. Note that cloning a container or VM image is optimized for btrfs file systems, and might not be efficient on others, due to file system limitations.</dl>
<p> <code>rename</code> <i>NAME</i> <i>NAME</i></p>
<dl>
<dt>
<dd> Renames a container or disk image. The arguments specify the name of the image to rename and the new name of the image.</dl>
<p> <code>read-only</code> <i>NAME</i> [<i>BOOL</i>]</p>
<dl>
<dt>
<dd> Marks or (unmarks) a container or disk image read-only. Takes a VM or container image name, followed by a boolean as arguments. If the boolean is omitted, positive is implied, i.e. the image is marked read-only.</dl>
<p> <code>remove</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Removes one or more container or disk images. The special image &quot;.host&quot;, which refers to the host&#8217;s own directory tree may not be removed.</dl>
<h3>Image Transfer Commands</h3>
<p> <code>pull-tar</code> <i>URL</i> [<i>NAME</i>]</p>
<dl>
<dt>
<dd> Downloads a .tar container image from the specified URL, and makes it available under the specified local machine name. The URL must be of type &quot;http://&quot; or &quot;https://&quot;, and must refer to a .tar, .tar.gz, .tar.xz or .tar.bz2 archive file. If the local machine name is omitted the name it is automatically derived from the last component of the URL, with its suffix removed. </p>
<p> The image is verified before it is made available, unless <code>&#8211;verify=no</code> is specified. Verification is done via SHA256SUMS and SHA256SUMS.gpg files, that need to be made available on the same web server, under the same URL as the .tar file, but with the last component (the filename) of the URL replaced. With <code>&#8211;verify=checksum</code> only the SHA256 checksum for the file is verified, based on the SHA256SUMS file. With <code>&#8211;verify=signature</code> the SHA256SUMS file is first verified with detached GPG signature file SHA256SUMS.gpg. The public key for this verification step needs to be available in /usr/lib/systemd/import-pubring.gpg or /etc/systemd/import-pubring.gpg. </p>
<p> The container image will be downloaded and stored in a read-only subvolume in /var/lib/machines/, that is named after the specified URL and its HTTP etag. A writable snapshot is then taken from this subvolume, and named after the specified local name. This behaviour ensures that creating multiple container instances of the same URL is efficient, as multiple downloads are not necessary. In order to create only the read-only image, and avoid creating its writable snapshot, specify &quot;-&quot; as local machine name. </p>
<p> Note that the read-only subvolume is prefixed with .tar-, and is thus now shown by <code>list-images</code>, unless <code>&#8211;all</code> is passed. </p>
<p> Note that pressing C-c during execution of this command will not abort the download. Use <code>cancel-transfer</code>, described below.</dl>
<p> <code>pull-raw</code> <i>URL</i> [<i>NAME</i>]</p>
<dl>
<dt>
<dd> Downloads a .raw container or VM disk image from the specified URL, and makes it available under the specified local machine name. The URL must be of type &quot;http://&quot; or &quot;https://&quot;. The container image must either be a .qcow2 or raw disk image, optionally compressed as .gz, .xz, or .bz2. If the local machine name is omitted the name it is automatically derived from the last component of the URL, with its suffix removed. </p>
<p> Image verification is identical for raw and tar images (see above). </p>
<p> If the the downloaded image is in .qcow2 format it es converted into a raw image file before it is made available. </p>
<p> Downloaded images of this type will be placed as read-only .raw file in /var/lib/machines/. A local, writable (reflinked) copy is then made under the specified local machine name. To omit creation of the local, writable copy pass &quot;-&quot; as local machine name. </p>
<p> Similar to the behaviour of <code>pull-tar</code>, the read-only image is prefixed with .raw-, and thus now shown by <code>list-images</code>, unless <code>&#8211;all</code> is passed. </p>
<p> Note that pressing C-c during execution of this command will not abort the download. Use <code>cancel-transfer</code>, described below.</dl>
<p> <code>list-transfers</code></p>
<dl>
<dt>
<dd> Shows a list of container or VM image downloads that are currently in progress.</dl>
<p> <code>cancel-transfers</code> <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Aborts download of the container or VM image with the specified ID. To list ongoing transfers and their IDs, use <code>list-transfers</code>.</dl>
<h2>FILES AND DIRECTORIES</h2>
<p> Machine images are preferably stored in /var/lib/machines/, but are also searched for in /usr/local/lib/machines/ and /usr/lib/machines/. For compatibility reasons the directory /var/lib/container/ is searched, too. Note that images stored below /usr are always considered read-only. It is possible to symlink machines images from other directories into /var/lib/machines/ to make them available for control with <code>machinectl</code>. </p>
<p> Disk images are understood by <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) and <code>machinectl</code> in three formats: </p>
<dl>
<dt>
<dd> &bull; A simple directory tree, containing the files and directories of the container to boot.</dl>
<dl>
<dt>
<dd> &bull; A subvolume (on btrfs file systems), which are similar to the simple directories, described above. However, they have additional benefits, such as efficient cloning and quota reporting.</dl>
<dl>
<dt>
<dd> &bull; &quot;Raw&quot; disk images, i.e. binary images of disks with a GPT or MBR partition table. Images of this type are regular files with the suffix &quot;.raw&quot;.</dl>
<p> See <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) for more information on image formats, in particular it&#8217;s <code>&#8211;directory=</code> and <code>&#8211;image=</code> options.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Download an Ubuntu image and open a shell in it</code> </p>
<dl>
<dt>
<dd>
<pre>
# machinectl pull-tar <a rel="nofollow" href="https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz">https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz</a>
# systemd-nspawn -M trusty-server-cloudimg-amd64-root
</pre>
</dl>
<p> This downloads and verifies the specified .tar image, and then uses <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) to open a shell in it. </p>
<p> <code>Example 2. Download a Fedora image, set a root password in it, start it as service</code> </p>
<dl>
<dt>
<dd>
<pre>
# machinectl pull-raw --verify=no <a rel="nofollow" href="http://ftp.halifax.rwth-aachen.de/fedora/linux/releases/21/Cloud/Images/x86_64/Fedora-Cloud-Base-20141203-21.x86_64.raw.xz">http://ftp.halifax.rwth-aachen.de/fedora/linux/releases/21/Cloud/Images/x86_64/Fedora-Cloud-Base-20141203-21.x86_64.raw.xz</a>
# systemd-nspawn -M Fedora-Cloud-Base-20141203-21
# passwd
# exit
# machinectl start Fedora-Cloud-Base-20141203-21
# machinectl login Fedora-Cloud-Base-20141203-21
</pre>
</dl>
<p> This downloads the specified .raw image with verification disabled. Then a shell is opened in it and a root password is set. Afterwards the shell is left, and the machine started as system service. With the last command a login prompt into the container is requested.</p>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. Setting this to an empty string or the value &quot;cat&quot; is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<p> <i>$SYSTEMD_LESS</i></p>
<dl>
<dt>
<dd> Override the default options passed to <code>less</code> (&quot;FRSXMK&quot;).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) </p>
<h2>Index</h2>
