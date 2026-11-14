---
title: "sd-boot(7)"
name: "sd-boot"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sd-boot/"
description: "systemd-boot, sd-boot – A simple UEFI boot manager"
---

<p>systemd-boot, sd-boot &#8211; A simple UEFI boot manager</p>
<h2>Description</h2>
<p><code>systemd-boot</code> (short: <code>sd-boot</code>) is a simple UEFI boot manager. It provides a graphical menu to select the entry to boot and an editor for the kernel command line. <code>systemd-boot</code> supports systems with UEFI firmware only. </p>
<p> <code>systemd-boot</code> loads boot entry information from the EFI system partition (ESP), usually mounted at /efi/, /boot/, or /boot/efi/ during OS runtime, as well as from the Extended Boot Loader partition if it exists (usually mounted to /boot/). Configuration file fragments, kernels, initrds and other EFI images to boot generally need to reside on the ESP or the Extended Boot Loader partition. Linux kernels must be built with <code>CONFIG_EFI_STUB</code> to be able to be directly executed as an EFI image. During boot <code>systemd-boot</code> automatically assembles a list of boot entries from the following sources: </p>
<dl>
<dd>&bull; Boot entries defined with m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font> description files located in /loader/entries/ on the ESP and the Extended Boot Loader Partition. These usually describe Linux kernel images with associated initrd images, but alternatively may also describe arbitrary other EFI executables.</dl>
<dl>
<dd>&bull; Unified kernel images following the m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font>, as executable EFI binaries in /EFI/Linux/ on the ESP and the Extended Boot Loader Partition.</dl>
<dl>
<dd>&bull; The Microsoft Windows EFI boot manager, if installed</dl>
<dl>
<dd>&bull; The Apple macOS boot manager, if installed</dl>
<dl>
<dd>&bull; The EFI Shell binary, if installed</dl>
<dl>
<dd>&bull; A reboot into the UEFI firmware setup option, if supported by the firmware</dl>
<p> <code>systemd-boot</code> supports the following features: </p>
<dl>
<dd>&bull; Basic boot manager configuration changes (such as timeout configuration, default boot entry selection, &#8230;) may be made directly from the boot loader UI at boot-time, as well as during system runtime with EFI variables.</dl>
<dl>
<dd>&bull; The boot manager integrates with the <code>systemctl</code> command to implement features such as <code>systemctl reboot &#8211;boot-loader-entry=&#8230;</code> (for rebooting into a specific boot menu entry, i.e. &quot;reboot into Windows&quot;) and <code>systemctl reboot &#8211;boot-loader-menu=&#8230;</code> (for rebooting into the boot loader menu), by implementing the m[blue]<code>Boot Loader Interface</code>m[]<font SIZE="-2">[2]</font>. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for details.</dl>
<dl>
<dd>&bull; An EFI variable set by the boot loader informs the OS about the EFI System Partition used during boot. This is then used to automatically mount the correct EFI System Partition to /efi/ or /boot/ during OS runtime. See <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8) for details.</dl>
<dl>
<dd>&bull; The boot manager provides information about the boot time spent in UEFI firmware using the m[blue]<code>Boot Loader Interface</code>m[]<font SIZE="-2">[2]</font>. This information can be displayed using <code><a href="/docs/linux/man/1-systemd-analyze/">systemd-analyze</a></code>(1).</dl>
<dl>
<dd>&bull; The boot manager implements boot counting and automatic fallback to older, working boot entries on failure. See m[blue]<code>Automatic Boot Assessment</code>m[]<font SIZE="-2">[3]</font>.</dl>
<dl>
<dd>&bull; The boot manager optionally reads a random seed from the ESP partition, combines it with a &#8216;system token&#8217; stored in a persistent EFI variable and derives a random seed to use by the OS as entropy pool initialization, providing a full entropy pool during early boot.</dl>
<p> <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1) may be used from a running system to locate the ESP and the Extended Boot Loader Partition, list available entries, and install <code>systemd-boot</code> itself. </p>
<p> <code><a href="/docs/linux/man/8-kernel-install/">kernel-install</a></code>(8) may be used to copy kernel images onto the ESP or the Extended Boot Loader Partition and to generate description files compliant with the Boot Loader Specification.</p>
<h2>Key Bindings</h2>
<p>The following keys may be used in the boot menu: </p>
<p> ↑ (Up), ↓ (Down), j, k, PageUp, PageDown, Home, End</p>
<dl>
<dd>Navigate up/down in the entry list</dl>
<p> ↵ (Enter), → (Right)</p>
<dl>
<dd>Boot selected entry</dl>
<p> d</p>
<dl>
<dd>Make selected entry the default</dl>
<p> e</p>
<dl>
<dd>Edit the kernel command line for selected entry</dl>
<p> +, t</p>
<dl>
<dd>Increase the timeout before default entry is booted</dl>
<p> -, T</p>
<dl>
<dd>Decrease the timeout</dl>
<p> v</p>
<dl>
<dd>Show systemd-boot, UEFI, and firmware versions</dl>
<p> P</p>
<dl>
<dd>Print status</dl>
<p> Q</p>
<dl>
<dd>Quit</dl>
<p> h, ?, F1</p>
<dl>
<dd>Show a help screen</dl>
<p> Ctrl+l</p>
<dl>
<dd>Reprint the screen</dl>
<p> The following keys may be pressed during bootup or in the boot menu to directly boot a specific entry: </p>
<p> l</p>
<dl>
<dd>Linux</dl>
<p> w</p>
<dl>
<dd>Windows</dl>
<p> a</p>
<dl>
<dd>macOS</dl>
<p> s</p>
<dl>
<dd>EFI shell</dl>
<p> 1, 2, 3, 4, 5, 6, 7, 8, 9</p>
<dl>
<dd>Boot entry number 1 &#8230; 9</dl>
<p> The boot menu is shown when a non-zero menu timeout has been configured. If the menu timeout has been set to zero, it is sufficient to press any key &#8212; before the boot loader initializes &#8212; to bring up the boot menu, except for the keys listed immediately above as they directly boot into the selected boot menu item. Note that depending on the firmware implementation the time window where key presses are accepted before the boot loader initializes might be short. If the window is missed, reboot and try again, possibly pressing a suitable key (e.g. the space bar) continuously; on most systems it should be possible to hit the time window after a few attempts. To avoid this problem, consider setting a non-zero timeout, thus showing the boot menu unconditionally. Some desktop environments might offer an option to directly boot into the boot menu, to avoid the problem altogether. Alternatively, use the command line <code>systemctl reboot &#8211;boot-loader-menu=0</code> from the shell. </p>
<p> In the editor, most keys simply insert themselves, but the following keys may be used to perform additional actions: </p>
<p> ← (Left), → (Right), Home, End</p>
<dl>
<dd>Navigate left/right</dl>
<p> Esc</p>
<dl>
<dd>Abort the edit and quit the editor</dl>
<p> Ctrl+k</p>
<dl>
<dd>Clear the command line</dl>
<p> Ctrl+w, Alt+Backspace</p>
<dl>
<dd>Delete word backwards</dl>
<p> Alt+d</p>
<dl>
<dd>Delete word forwards</dl>
<p> ↵ (Enter)</p>
<dl>
<dd>Boot entry with the edited command line</dl>
<p> Note that unless configured otherwise in the UEFI firmware, systemd-boot will use the US keyboard layout, so key labels might not match for keys like +/-.</p>
<h2>Files</h2>
<p>The files <code>systemd-boot</code> processes generally reside on the UEFI ESP which is usually mounted to /efi/, /boot/ or /boot/efi/ during OS runtime. It also processes files on the Extended Boot Loader partition which is typically mounted to /boot/, if it exists. <code>systemd-boot</code> reads runtime configuration such as the boot timeout and default entry from /loader/loader.conf on the ESP (in combination with data read from EFI variables). See <code><a href="/docs/linux/man/5-loader-conf/">loader.conf</a></code>(5). Boot entry description files following the m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font> are read from /loader/entries/ on the ESP and the Extended Boot Loader partition. Unified kernel boot entries following the m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font> are read from /EFI/Linux/ on the ESP and the Extended Boot Loader partition. Optionally, a random seed for early boot entropy pool provisioning is stored in /loader/random-seed in the ESP.</p>
<h2>Efi Variables</h2>
<p>The following EFI variables are defined, set and read by <code>systemd-boot</code>, under the vendor UUID &quot;4a67b082-0a4c-41cf-b6c7-440b29bb8c4f&quot;, for communication between the OS and the boot loader: </p>
<p> <i>LoaderBootCountPath</i></p>
<dl>
<dd>If boot counting is enabled, contains the path to the file in whose name the boot counters are encoded. Set by the boot loader. <code><a href="/docs/linux/man/8-systemd-bless-boot-service/">systemd-bless-boot.service</a></code>(8) uses this information to mark a boot as successful as determined by the successful activation of the boot-complete.target target unit.</dl>
<p> <i>LoaderConfigTimeout</i>, <i>LoaderConfigTimeoutOneShot</i></p>
<dl>
<dd>The menu timeout in seconds. Read by the boot loader. <i>LoaderConfigTimeout</i> is maintained persistently, while <i>LoaderConfigTimeoutOneShot</i> is a one-time override which is read once (in which case it takes precedence over <i>LoaderConfigTimeout</i>) and then removed. <i>LoaderConfigTimeout</i> may be manipulated with the t/T keys, see above.</dl>
<p> <i>LoaderDevicePartUUID</i></p>
<dl>
<dd>Contains the partition UUID of the EFI System Partition the boot loader was run from. Set by the boot loader. <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8) uses this information to automatically find the disk booted from, in order to discover various other partitions on the same disk automatically.</dl>
<p> <i>LoaderEntries</i></p>
<dl>
<dd>A list of the identifiers of all discovered boot loader entries. Set by the boot loader.</dl>
<p> <i>LoaderEntryDefault</i>, <i>LoaderEntryOneShot</i></p>
<dl>
<dd>The identifier of the default boot loader entry. Set primarily by the OS and read by the boot loader. <i>LoaderEntryOneShot</i> sets the default entry for the next boot only, while <i>LoaderEntryDefault</i> sets it persistently for all future boots. <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1)&#8217;s <code>set-default</code> and <code>set-oneshot</code> commands make use of these variables. The boot loader modifies <i>LoaderEntryDefault</i> on request, when the d key is used, see above.</dl>
<p> <i>LoaderEntrySelected</i></p>
<dl>
<dd>The identifier of the boot loader entry currently being booted. Set by the boot loader.</dl>
<p> <i>LoaderFeatures</i></p>
<dl>
<dd>A set of flags indicating the features the boot loader supports. Set by the boot loader. Use <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1) to view this data.</dl>
<p> <i>LoaderFirmwareInfo</i>, <i>LoaderFirmwareType</i></p>
<dl>
<dd>Brief firmware information. Set by the boot loader. Use <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1) to view this data.</dl>
<p> <i>LoaderImageIdentifier</i></p>
<dl>
<dd>The path of executable of the boot loader used for the current boot, relative to the EFI System Partition&#8217;s root directory. Set by the boot loader. Use <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1) to view this data.</dl>
<p> <i>LoaderInfo</i></p>
<dl>
<dd>Brief information about the boot loader. Set by the boot loader. Use <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1) to view this data.</dl>
<p> <i>LoaderTimeExecUSec</i>, <i>LoaderTimeInitUSec</i>, <i>LoaderTimeMenuUsec</i></p>
<dl>
<dd>Information about the time spent in various parts of the boot loader. Set by the boot loader. Use <code><a href="/docs/linux/man/1-systemd-analyze/">systemd-analyze</a></code>(1) to view this data.</dl>
<p> <i>LoaderRandomSeed</i></p>
<dl>
<dd>A binary random seed <code>systemd-boot</code> may optionally pass to the OS. This is a volatile EFI variable that is hashed at boot from the combination of a random seed stored in the ESP (in /loader/random-seed) and a &quot;system token&quot; persistently stored in the EFI variable <i>LoaderSystemToken</i> (see below). During early OS boot the system manager reads this variable and passes it to the OS kernel&#8217;s random pool, crediting the full entropy it contains. This is an efficient way to ensure the system starts up with a fully initialized kernel random pool &#8212; as early as the initial RAM disk phase. <code>systemd-boot</code> reads the random seed from the ESP, combines it with the &quot;system token&quot;, and both derives a new random seed to update in-place the seed stored in the ESP, and the random seed to pass to the OS from it via SHA256 hashing in counter mode. This ensures that different physical systems that boot the same &quot;golden&quot; OS image &#8212; i.e. containing the same random seed file in the ESP &#8212; will still pass a different random seed to the OS. It is made sure the random seed stored in the ESP is fully overwritten before the OS is booted, to ensure different random seed data is used between subsequent boots. </p>
<p> See m[blue]<code>Random Seeds</code>m[]<font SIZE="-2">[4]</font> for further information.</dl>
<p> <i>LoaderSystemToken</i></p>
<dl>
<dd>A binary random data field, that is used for generating the random seed to pass to the OS (see above). Note that this random data is generally only generated once, during OS installation, and is then never updated again.</dl>
<p> Many of these variables are defined by the m[blue]<code>Boot Loader Interface</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Boot Counting</h2>
<p><code>systemd-boot</code> implements a simple boot counting mechanism on top of the m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font>, for automatic and unattended fallback to older kernel versions/boot loader entries when a specific entry continuously fails. Any boot loader entry file and unified kernel image file that contains a &quot;+&quot; followed by one or two numbers (if two they need to be separated by a &quot;-&quot;), before the .conf or .efi suffix is subject to boot counting: the first of the two numbers (&#8216;tries left&#8217;) is decreased by one on every boot attempt, the second of the two numbers (&#8216;tries done&#8217;) is increased by one (if &#8216;tries done&#8217; is absent it is considered equivalent to 0). Depending on the current value of these two counters the boot entry is considered to be in one of three states: </p>
<dl>
<dd>1. If the &#8216;tries left&#8217; counter of an entry is greater than zero the entry is considered to be in &#8216;indeterminate&#8217; state. This means the entry has not completed booting successfully yet, but also hasn&#8217;t been determined not to work.</dl>
<dl>
<dd>2. If the &#8216;tries left&#8217; counter of an entry is zero it is considered to be in &#8216;bad&#8217; state. This means no further attempts to boot this item will be made (that is, unless all other boot entries are also in &#8216;bad&#8217; state), as all attempts to boot this entry have not completed successfully.</dl>
<dl>
<dd>3. If the &#8216;tries left&#8217; and &#8216;tries done&#8217; counters of an entry are absent it is considered to be in &#8216;good&#8217; state. This means further boot counting for the entry is turned off, as it successfully booted at least once. The <code><a href="/docs/linux/man/8-systemd-bless-boot-service/">systemd-bless-boot.service</a></code>(8) service moves the currently booted entry from &#8216;indeterminate&#8217; into &#8216;good&#8217; state when a boot attempt completed successfully.</dl>
<p> Generally, when new entries are added to the boot loader, they first start out in &#8216;indeterminate&#8217; state, i.e. with a &#8216;tries left&#8217; counter greater than zero. The boot entry remains in this state until either it managed to complete a full boot successfully at least once (in which case it will be in &#8216;good&#8217; state) &#8212; or the &#8216;tries left&#8217; counter reaches zero (in which case it will be in &#8216;bad&#8217; state). </p>
<p> Example: let&#8217;s say a boot loader entry file foo.conf is set up for 3 boot tries. The installer will hence create it under the name foo+3.conf. On first boot, the boot loader will rename it to foo+2-1.conf. If that boot does not complete successfully, the boot loader will rename it to foo+1-2.conf on the following boot. If that fails too, it will finally be renamed foo+0-3.conf by the boot loader on next boot, after which it will be considered &#8216;bad&#8217;. If the boot succeeds however the entry file will be renamed to foo.conf by the OS, so that it is considered &#8216;good&#8217; from then on. </p>
<p> The boot menu takes the &#8216;tries left&#8217; counter into account when sorting the menu entries: entries in &#8216;bad&#8217; state are ordered at the beginning of the list, and entries in &#8216;good&#8217; or &#8216;indeterminate&#8217; at the end. The user can freely choose to boot any entry of the menu, including those already marked &#8216;bad&#8217;. If the menu entry to boot is automatically determined, this means that &#8216;good&#8217; or &#8216;indeterminate&#8217; entries are generally preferred (as the bottom item of the menu is the one booted by default), and &#8216;bad&#8217; entries will only be considered if there are no &#8216;good&#8217; or &#8216;indeterminate&#8217; entries left. </p>
<p> The <code><a href="/docs/linux/man/8-kernel-install/">kernel-install</a></code>(8) kernel install framework optionally sets the initial &#8216;tries left&#8217; counter to the value specified in /etc/kernel/tries when a boot loader entry is first created.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1), <code><a href="/docs/linux/man/5-loader-conf/">loader.conf</a></code>(5), <code><a href="/docs/linux/man/8-systemd-bless-boot-service/">systemd-bless-boot.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-boot-system-token-service/">systemd-boot-system-token.service</a></code>(8), <code><a href="/docs/linux/man/8-kernel-install/">kernel-install</a></code>(8), m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>Boot Loader Interface</code>m[]<font SIZE="-2">[2]</font></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Boot Loader Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/BOOT_LOADER_SPECIFICATION">https://systemd.io/BOOT_LOADER_SPECIFICATION</a></dl>
<dt> 2.</p>
<dd>Boot Loader Interface</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/BOOT_LOADER_INTERFACE">https://systemd.io/BOOT_LOADER_INTERFACE</a></dl>
<dt> 3.</p>
<dd>Automatic Boot Assessment</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/AUTOMATIC_BOOT_ASSESSMENT">https://systemd.io/AUTOMATIC_BOOT_ASSESSMENT</a></dl>
<dt> 4.</p>
<dd>Random Seeds</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/RANDOM_SEEDS">https://systemd.io/RANDOM_SEEDS</a></dl>
