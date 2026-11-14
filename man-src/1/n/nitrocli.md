---
title: "nitrocli(1)"
name: "nitrocli"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nitrocli/"
description: "nitrocli – access Nitrokey devices"
---

<h2 class="name">NAME</h2>
<p> nitrocli &#8211; access Nitrokey devices </p>
<h2>SYNOPSIS</h2>
<p> <code>nitrocli</code> <i>command</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>nitrocli</code> provides access to Nitrokey devices. It supports the Nitrokey Pro, the Nitrokey Storage, and the Librem Key. It can be used to access the encrypted volume, the one-time password generator, and the password safe.</p>
<h3>Device selection</h3>
<p> Per default, <code>nitrocli</code> connects to any attached Nitrokey device. You can use the <code>&#8211;model</code>, <code>&#8211;serial-number</code> and <code>&#8211;usb-path</code> options to select the device to connect to. <code>nitrocli</code> fails if more than one attached Nitrokey device matches this filter or if multiple Nitrokey devices are attached and none of the filter options is set. Use the <code>list</code> command to list all attached devices with their USB path, model, and serial number (if available).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code>, <code>&#8211;model librem</code>|<code>pro</code>|<code>storage</code></p>
<dd> Restrict connections to the given device model, see the Device selection section.</p>
<dt><code>&#8211;serial-number </code><i>serial-number</i></p>
<dd> Restrict connections to the given serial number, see the Device selection section. <i>serial-number</i> must be a hex string with an optional 0x prefix. This option can be set multiple times to allow any of the given serial numbers. Nitrokey Storage devices never match this restriction as they do not expose their serial number in the USB device descriptor.</p>
<dt><code>&#8211;usb-path </code><i>usb-path</i></p>
<dd> Restrict connections to the given USB path, see the Device selection section.</p>
<dt><code>&#8211;no-cache</code></p>
<dd> If this option is set, nitrocli will not cache any inquired secrets using <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1) but ask for them each time they are needed. Note that this option does not cause any cached secrets to be cleared. If a secret is already in the cache it will be ignored, but left otherwise untouched. Use the <code>pin clear</code> command to clear secrets from the cache.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Enable additional logging and control its verbosity. Logging enabled through this option will appear on the standard error stream. This option can be supplied multiple times. A single occurrence will show additional warnings. Commands sent to the device will be shown when supplied three times and full device communication is available with four occurrences. Supplying this option five times enables the highest verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the nitrocli version and exit.</dl>
<h2>COMMANDS</h2>
<h3>General</h3>
<dl>
<dt><code>nitrocli list </code>[<code>-n</code>|<code>&#8211;no-connect</code>]</p>
<dd> List all attached Nitrokey devices. This command prints a list of the USB path, the model and the serial number of all attached Nitrokey devices. To access the serial number of a Nitrokey Storage device, <code>nitrocli</code> has to connect to it. To omit the serial number of Nitrokey Storage devices instead of connecting to them, set the <code>&#8211;no-connect</code> option.</p>
<dt><code>nitrocli status</code></p>
<dd> Print the status of the connected Nitrokey device, including the stick serial number, the firmware version, and the PIN retry count. If the device is a Nitrokey Storage, also print storage related information including the SD card serial number, the SD card usage during this power cycle, the encryption status, and the status of the volumes.</p>
<dt><code>nitrocli lock</code></p>
<dd> Lock the Nitrokey. This command locks the password safe (see the Password safe section). On the Nitrokey Storage, it will also close any active encrypted or hidden volumes (see the Storage section).</p>
<dt><code>nitrocli reset </code>[<code>&#8211;only-aes-key</code>]</p>
<dd> Perform a factory reset on the Nitrokey. This command performs a factory reset on the OpenPGP smart card, clears the flash storage and builds a new AES key. The user PIN is reset to 123456, the admin PIN to 12345678. </p>
<p> If the <code>&#8211;only-aes-key</code> option is set, the command does not perform a full factory reset but only creates a new AES key. The AES key is for example used to encrypt the password safe. </p>
<p> This command requires the admin PIN. To avoid accidental calls of this command, the user has to enter the PIN even if it has been cached. </p>
</dl>
<h3>Storage</h3>
<p> The Nitrokey Storage comes with a storage area. This area is comprised of an <i>unencrypted</i> region and an <i>encrypted</i> one of fixed sizes, each made available to the user in the form of block devices. The encrypted region can optionally further be overlayed with up to four <i>hidden</i> volumes. Because of this overlay (which is required to achieve plausible deniability of the existence of hidden volumes), the burden of ensuring that data on the encrypted volume does not overlap with data on one of the hidden volumes is on the user.</p>
<dl>
<dt><code>nitrocli unencrypted set </code><i>mode</i></p>
<dd> Change the read-write mode of the volume. <i>mode</i> is the type of the mode to change to: <code>read-write</code> to make the volume readable and writable or <code>read-only</code> to make it only readable. This command requires the admin PIN. </p>
<p> Note that this command requires firmware version 0.51 or higher. Earlier versions are not supported.</p>
<dt><code>nitrocli encrypted open</p>
<dd> Open the encrypted volume on the Nitrokey Storage. The user PIN that is required to open the volume is queried using <a href="/docs/linux/man/1-pinentry/">pinentry</a></code>(1) and cached by <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1).</p>
<dt><code>nitrocli encrypted close</p>
<dd> Close the encrypted volume on the Nitrokey Storage.</p>
<dt>nitrocli hidden create </code><i>slot</i> <i>start</i> <i>end</i></p>
<dd> Create a new hidden volume inside the encrypted volume. <i>slot</i> must indicate one of the four available slots. <i>start</i> and <i>end</i> represent, respectively, the start and end position of the hidden volume inside the encrypted volume, as a percentage of the encrypted volume&#8217;s size. This command requires a password which is later used to look up the hidden volume to open. Unlike a PIN, this password is not cached by <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1). </p>
<p> As a guide line for creating new hidden volumes, the <code>status</code> command provides a range of the SD card that has not been written to during this power cycle.</p>
<dt><code>nitrocli hidden open</p>
<dd> Open a hidden volume. The volume to open is determined based on the password entered, which must have a minimum of six characters. Only one hidden volume can be active at any point in time and previously opened volumes will be automatically closed. Similarly, the encrypted volume will be closed if it was open.</p>
<dt>nitrocli hidden close</p>
<dd> Close a hidden volume.</p>
<dt>nitrocli fill </code>[<code>-a</code>|<code>&#8211;attach</code></p>
<dd> Fills the SD card with random data, overwriting all existing data. This operation takes about one hour to finish for a 16 GiB SD card. It cannot be canceled, even if the <code>nitrocli</code> process is terminated before it finishes. </p>
<p> This command requires the admin PIN. To avoid accidental calls of this command, the user has to enter the PIN even if it has been cached. </p>
<p> If the <code>&#8211;attach</code> option is set, this command will not start a new fill operation. Instead it checks whether a fill operation is currently running on the device and shows its progress. </p>
</dl>
<h3>One-time passwords</h3>
<p> The Nitrokey Pro, the Nitrokey Storage, and the Librem Key support the generation of one-time passwords using the HOTP algorithm according to RFC 4226 or the TOTP algorithm according to RFC 6238. The required data &#8211; a name and the secret &#8211; is stored in slots. Currently, the Nitrokey devices provide three HOTP slots and 15 TOTP slots. The slots are numbered per algorithm starting at zero. </p>
<p> The TOTP algorithm is a modified version of the HOTP algorithm that also uses the current time. Therefore, the Nitrokey clock must be synchronized with the clock of the application that requests the one-time password.</p>
<dl>
<dt><code>nitrocli otp get </code><i>slot </i>[<code>-a</code>|<code>&#8211;algorithm </code><i>algorithm</i>] <code>[-t</code>|<code>&#8211;time </code><i>time</i>]</p>
<dd> Generate a one-time password. <i>slot</i> is the number of the slot to generate the password from. <i>algorithm</i> is the OTP algorithm to use. Possible values are <code>hotp</code> for the HOTP algorithm according to RFC 4226 and <code>totp</code> for the TOTP algorithm according to RFC 6238 (default). Per default, this commands sets the Nitrokey&#8217;s time to the system time if the TOTP algorithm is selected. If <code>&#8211;time</code> is set, it is set to <i>time</i> instead, which must be a Unix timestamp (i.e., the number of seconds since 1970-01-01 00:00:00 UTC). This command might require the user PIN (see the Configuration section).</p>
<dt><code>nitrocli otp set </code><i>slot name secret</i>|<code>&#8211;</code> [<code>-a</code>|<code>&#8211;algorithm </code><i>algorithm</i>] [<code>-d</code>|<code>&#8211;digits </code><i>digits</i>] [<code>-c</code>|<code>&#8211;counter </code><i>counter</i>] [<code>-t</code>|<code>&#8211;time-window </code><i>time-window</i>] [<code>-f</code>|<code>&#8211;format ascii</code>|<code>base32</code>|<code>hex</code>]</p>
<dd> Configure a one-time password slot. <i>slot</i> is the number of the slot to configure. <i>name</i> is the name of the slot (may not be empty). <i>secret</i> is the secret value to store in that slot. If <i>secret</i> is set to <code>&#8211;</code>, the secret is read from the standard input. </p>
<p> The <code>&#8211;format</code> option specifies the format of the secret. If it is set to <code>ascii</code>, each character of the given secret is interpreted as the ASCII code of one byte. If it is set to <code>base32</code>, the secret is interpreted as a base32 string according to RFC 4648. If it is set to <code>hex</code>, every two characters are interpreted as the hexadecimal value of one byte. The default value is <code>base32</code>. </p>
<p> <i>algorithm</i> is the OTP algorithm to use. Possible values are <code>hotp</code> for the HOTP algorithm according to RFC 4226 and <code>totp</code> for the TOTP algorithm according to RFC 6238 (default). <i>digits</i> is the number of digits the one-time password should have. Allowed values are 6 and 8 (default: 6). <i>counter</i> is the initial counter if the HOTP algorithm is used (default: 0). <i>time-window</i> is the time window used with TOTP in seconds (default: 30).</p>
<dt><code>nitrocli otp clear </code><i>slot </i>[<code>-a</code>|<code>&#8211;algorithm </code><i>algorithm</i>]</p>
<dd> Delete the name and the secret stored in a one-time password slot. <i>slot</i> is the number of the slot to clear. <i>algorithm</i> is the OTP algorithm to use. Possible values are <code>hotp</code> for the HOTP algorithm according to RFC 4226 and <code>totp</code> for the TOTP algorithm according to RFC 6238 (default).</p>
<dt><code>nitrocli otp status </code>[<code>-a</code>|<code>&#8211;all</code>]</p>
<dd> List all OTP slots. If <code>&#8211;all</code> is not set, empty slots are ignored. </p>
</dl>
<h3>Configuration</h3>
<p> Nitrokey devices have four configuration settings: the Num Lock, Caps Lock and Scroll Lock keys can be mapped to an HOTP slot, and OTP generation can be set to require the user PIN.</p>
<dl>
<dt><code>nitrocli config get</code></p>
<dd> Print the current Nitrokey configuration.</p>
<dt><code>nitrocli config set </code>[[<code>-n</code>|<code>&#8211;num-lock </code><i>slot</i>] | [<code>-N</code>|<code>&#8211;no-num-lock</code>]] [[<code>-c</code>|<code>&#8211;caps-lock </code><i>slot</i>] | [<code>-C</code>|<code>&#8211;no-caps-lock</code>]] [[<code>-s</code>|<code>&#8211;scroll-lock </code><i>slot</i>] | [<code>-S</code>|<code>&#8211;no-scroll-lock</code>]] [[<code>-o</code>|<code>&#8211;otp-pin</code>] | [<code>-O</code>|<code>&#8211;no-otp-pin</code>]]</p>
<dd> Update the Nitrokey configuration. This command requires the admin PIN. </p>
<p> With the <code>&#8211;num-lock</code>, <code>&#8211;caps-lock</code> and <code>&#8211;scroll-lock</code> options, the respective bindings can be set. <i>slot</i> is the number of the HOTP slot to bind the key to. If <code>&#8211;no-num-lock</code>, <code>&#8211;no-caps-lock</code> or <code>&#8211;no-scroll-lock</code> is set, the respective binding is disabled. The two corresponding options are mutually exclusive. </p>
<p> If <code>&#8211;otp-pin</code> is set, the user PIN will be required to generate one-time passwords using the <code>otp get</code> command. If <code>&#8211;no-otp-pin</code> is set, OTP generation can be performed without PIN. These two options are mutually exclusive. </p>
</dl>
<h3>Password safe</h3>
<p> The Nitrokey Pro, the Nitrokey Storage, and the Librem Key provide a password safe (PWS) with 16 slots. In each of these slots you can store a name, a login, and a password. The PWS is not encrypted, but it is protected with the user PIN by the firmware. Once the PWS is unlocked by one of the commands listed below, it can be accessed without authentication. You can use the <code>lock</code> command to lock the password safe.</p>
<dl>
<dt><code>nitrocli pws get </code><i>slot </i>[<code>-n</code>|<code>&#8211;name</code>] [<code>-l</code>|<code>&#8211;login</code>] [<code>-p</code>|<code>&#8211;password</code>] [<code>-q</code>|<code>&#8211;quiet</code>]</p>
<dd> Print the content of one PWS slot. <i>slot</i> is the number of the slot. Per default, this command prints the name, the login and the password (in that order). If one or more of the options <code>&#8211;name</code>, <code>&#8211;login</code>, and <code>&#8211;password</code> are set, only the selected fields are printed. The order of the fields never changes. </p>
<p> The fields are printed together with a label. Use the <code>&#8211;quiet</code> option to suppress the labels and to only output the values stored in the PWS slot.</p>
<dt><code>nitrocli pws add </code>[<code>-s</code>|<code>&#8211;slot </code><i>slot</i>] <i>name login password</i>|<code>&#8211;</code></p>
<dd> Add a new PWS slot. If the <code>&#8211;slot</code> option is set, this command writes the data to the given slot and fails if the slot is already programmed. If the <code>&#8211;slot</code> option is not set, this command locates the first free PWS slot and sets its content to the given values. It fails if all PWS slots are programmed. </p>
<p> If <i>password</i> is set to <code>&#8211;</code>, the password is read from the standard input.</p>
<dt><code>nitrocli pws update </code><i>slot</i> [<code>-n</code>|<code>&#8211;name </code><i>name</i>] [<code>-l</code>|<code>&#8211;login </code><i>login</i>] [<code>-p</code>|<code>&#8211;password </code><i>password</i>|<code>&#8211;</code>]</p>
<dd> Update the content of a programmed PWS slot. <i>slot</i> is the number of the slot to write. This command only sets the data given with the <code>&#8211;name</code>, <code>&#8211;login</code>, and <code>&#8211;password</code> options and does not overwrite the other fields of the slot. </p>
<p> If <i>password</i> is set to <code>&#8211;</code>, the password is read from the standard input.</p>
<dt><code>nitrocli pws clear </code><i>slot</i></p>
<dd> Delete the data stored in a PWS slot. <i>slot</i> is the number of the slot clear.</p>
<dt><code>nitrocli pws status </code>[<code>-a</code>|<code>&#8211;all</code>]</p>
<dd> List all PWS slots. If <code>&#8211;all</code> is not set, empty slots are ignored. </p>
</dl>
<h3>PINs</h3>
<p> Nitrokey devices have two PINs: the user PIN and the admin PIN. The user PIN must have at least six, the admin PIN at least eight characters. The user PIN is required for commands such as <code>otp get</code> (depending on the configuration) and for all <code>pws</code> commands. The admin PIN is usually required to change the device configuration. </p>
<p> Each PIN has a retry counter that is decreased with every wrong PIN entry and reset if the PIN was entered correctly. The initial retry counter is three. If the retry counter for the user PIN is zero, you can use the <code>pin unblock</code> command to unblock and reset the user PIN. If the retry counter for the admin PIN is zero, you have to perform a factory reset using the <code>reset</code> command or <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1). Use the <code>status</code> command to check the retry counters.</p>
<dl>
<dt><code>nitrocli pin clear</code></p>
<dd> Clear the PINs cached by the other commands. Note that cached PINs are associated with the device they belong to and the <code>clear</code> command will only clear the PIN for the currently used device, not all others.</p>
<dt><code>nitrocli pin set </code><i>type</i></p>
<dd> Change a PIN. <i>type</i> is the type of the PIN that will be changed: <code>admin</code> to change the admin PIN or <code>user</code> to change the user PIN. This command only works if the retry counter for the PIN type is at least one. (Use the <code>status</code> command to check the retry counters.)</p>
<dt><code>nitrocli pin unblock</code></p>
<dd> Unblock and reset the user PIN. This command requires the admin PIN. The admin PIN cannot be unblocked. This operation is equivalent to the unblock PIN option provided by <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) (using the <code>&#8211;change-pin</code> option). </p>
</dl>
<h3>Extensions</h3>
<p> In addition to the above built-in commands, <code>nitrocli</code> supports user-provided functionality in the form of extensions. An extension can be any executable file whose filename starts with &quot;nitrocli-&quot; and that is discoverable through lookup via the <code>PATH</code> environment variable. Those executables can be invoked as regular subcommands (without the need of the prefix; e.g., an extension with the name &quot;nitrocli-otp-cache&quot; could be invoked as &quot;nitrocli otp-cache&quot;). </p>
<p> More information on how to write extensions can be found in the Extensions section below. </p>
<h2>CONFIG FILE</h2>
<p> <code>nitrocli</code> tries to read the configuration file at <code>${XDG_CONFIG_HOME}/nitrocli/config.toml</code> (or <code>${HOME}/nitrocli/config.toml</code> if the <code>XDG_CONFIG_HOME</code> environment variable is not set). It is used to set default values for the options listed below. </p>
<p> You can also set the environment variable <code>NITROCLI_</code><i>KEY</i> to overwrite the configuration for <i>key</i> (see the Environment section). Note that command-line arguments overwrite both the configuration file and the environment variables. </p>
<p> The following values can be set in the configuration file:</p>
<dl>
<dt><code>model</code></p>
<dd> Restrict connections to the given device model (string, default: not set, see <code>&#8211;model</code>).</p>
<dt><code>serial_numbers</code></p>
<dd> Restrict connections to the given serial numbers (list of strings, default: empty, see <code>&#8211;serial-number</code>).</p>
<dt><code>usb_path</code></p>
<dd> Restrict connections to the given USB path (string, default: not set, see <code>&#8211;usb-path</code>).</p>
<dt><code>no_cache</code></p>
<dd> If set to true, do not cache any inquired secrets (boolean, default: false, see <code>&#8211;no-cache</code>).</p>
<dt><code>verbosity</code></p>
<dd> Set the log level (integer, default: 0, see <code>&#8211;verbose</code>).</dl>
<p> The configuration file must use the TOML format, for example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;model&nbsp;=&nbsp;&quot;pro&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;serial_numbers&nbsp;=&nbsp;[&quot;0xf00baa&quot;,&nbsp;&quot;deadbeef&quot;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usb_path&nbsp;=&nbsp;&quot;0001:0006:02&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no_cache&nbsp;=&nbsp;false<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;verbosity&nbsp;=&nbsp;0 </p>
<h2>ENVIRONMENT</h2>
<p> The program honors two sets of environment variables, all prefixed by &quot;NITROCLI_&quot;.</p>
<h3>Configuration</h3>
<p> The first set controls basic configuration of the program. These variables mirror the respective command line options and configuration file settings. They are:</p>
<dl>
<dt><code>NITROCLI_MODEL</code></p>
<dd> Restrict connections to the given device model (string, default: not set, see <code>&#8211;model</code>).</p>
<dt><code>NITROCLI_SERIAL_NUMBERS</code></p>
<dd> Restrict connections to the given list of serial numbers (comma-separated list of strings, default: empty, see <code>&#8211;serial-number</code>).</p>
<dt><code>NITROCLI_USB_PATH</code></p>
<dd> Restrict connections to the given USB path (string, default: not set, see <code>&#8211;usb-path</code>).</p>
<dt><code>NITROCLI_NO_CACHE</code></p>
<dd> If set to true, do not cache any inquired secrets (boolean, default: false, see <code>&#8211;no-cache</code>).</p>
<dt><code>NITROCLI_VERBOSITY</code></p>
<dd> Set the log level (integer, default: 0, see <code>&#8211;verbose</code>).</dl>
<h3>Password &amp; PIN entry</h3>
<p> The second set can be used to provide password &amp; PIN data to the program to suppress interactive entry through <code><a href="/docs/linux/man/1-pinentry/">pinentry</a></code>(1) for operations that otherwise would ask for it. The following variables are recognized:</p>
<dl>
<dt><code>NITROCLI_ADMIN_PIN</code></p>
<dd> The admin PIN to use.</p>
<dt><code>NITROCLI_USER_PIN</code></p>
<dd> The user PIN to use.</p>
<dt><code>NITROCLI_NEW_ADMIN_PIN</code></p>
<dd> The new admin PIN to set. This variable is only used by the <code>pin set</code> command for the <code>admin</code> type.</p>
<dt><code>NITROCLI_NEW_USER_PIN</code></p>
<dd> The new user PIN to set. This variable is only used by the <code>pin set</code> command for the <code>user</code> type.</p>
<dt><code>NITROCLI_PASSWORD</code></p>
<dd> A password used by commands that require one (e.g., <code>hidden open</code>). </p>
</dl>
<h2>EXTENSIONS</h2>
<p> <code>nitrocli</code> supports user-provided extensions that are executable files whose filename starts with &quot;nitrocli-&quot; and that are discoverable through lookup via the <code>PATH</code> environment variable. </p>
<p> The program conveys basic configuration information to any extension being started this way. Specifically, it will set each environment variable as described in the Configuration subsection of the Environment section above, if the corresponding <code>nitrocli</code> program configuration was set. In addition, the following variables will be set:</p>
<dl>
<dt><code>NITROCLI_BINARY</code></p>
<dd> The absolute path to the <code>nitrocli</code> binary through which the extension was invoked. This path may be used to recursively invoke <code>nitrocli</code> to implement certain functionality.</p>
<dt><code>NITROCLI_RESOLVED_USB_PATH</code></p>
<dd> The USB path of the device that <code>nitrocli</code> would connect to based on the <code>&#8211;model</code>, <code>&#8211;serial-number</code>, and <code>&#8211;usb-path</code> options. If there is no matching Nitrokey device, or if multiple devices match the options, the environment variable is not set. </p>
</dl>
<p> All other variables present in the environment will be passed through to the extension verbatim. </p>
<p> Newer versions of the program reserve the right to set additional environment variables inside the &quot;NITROCLI_&quot; namespace. As such, extensions are advised to not define custom variables with this prefix. However, &quot;NITROCLI_EXT_&quot; is provided specifically for this purpose. To further avoid conflicts between extensions, it is recommended that this prefix be followed by the extension&#8217;s name (uppercased). </p>
<p> Extensions may optionally read or write persistent data of various forms. Similar to the main program, extensions should follow the XDG Base Directory Specification as a guideline where to store such data. More specifically, the following conventions should be followed: </p>
<p> For configuration data, <code>${XDG_CONFIG_HOME}/</code><i>extension/</i> is the preferred directory, where <i>extension</i> is the full extension name, including the &quot;nitrocli-&quot; prefix. The recommended configuration format is TOML. If only a single configuration file is used, <code>config.toml</code> is the recommended name. </p>
<p> Similarly, regular data should reside in <code>${XDG_DATA_HOME}/</code><i>extension/</i> and cached data be stored in <code>${XDG_CACHE_HOME}/</code><i>extension/</i>. </p>
<h2>FILES</h2>
<dl>
<dt><code>${XDG_CONFIG_HOME}/nitrocli/config.toml</code></p>
<dd>
<dt><code>${HOME}/nitrocli/config.toml</code></p>
<dd> User configuration file, see the Config file section. </p>
</dl>
<h2>EXAMPLES</h2>
<h3>Storage</h3>
<p> Create a hidden volume in the first available slot, starting at half the size of the encrypted volume (i.e., 50%) and stretching all the way to its end (100%):<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli hidden create 0 50 100</code> </p>
<h3>One-time passwords</h3>
<p> Configure a one-time password slot with a hexadecimal secret representation:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 0 test-rfc4226 3132333435363738393031323334353637383930 &#8211;format hex &#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 1 test-foobar 666F6F626172 &#8211;format hex &#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 0 test-rfc6238 3132333435363738393031323334353637383930 &#8211;format hex &#8211;algorithm totp &#8211;digits 8</code> </p>
<p> Configure a one-time password slot with an ASCII secret representation:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 0 test-rfc4226 12345678901234567890 &#8211;format ascii &#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 1 test-foobar foobar &#8211;format ascii &#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 0 test-rfc6238 12345678901234567890 &#8211;format ascii &#8211;algorithm totp &#8211;digits 8</code> </p>
<p> Configure a one-time password slot with a base32 secret representation:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 0 test-rfc4226 gezdgnbvgy3tqojqgezdgnbvgy3tqojq &#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 1 test-foobar mzxw6ytboi======&nbsp;&#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp set 0 test-rfc6238 gezdgnbvgy3tqojqgezdgnbvgy3tqojq &#8211;algorithm totp &#8211;digits 8</code> </p>
<p> Generate a one-time password:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp get 0 &#8211;algorithm hotp</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;755224<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp get 0 &#8211;algorithm totp &#8211;time 1234567890</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;89005924 </p>
<p> Clear a one-time password slot:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli otp clear 0 &#8211;algorithm hotp</code> </p>
<h3>Configuration</h3>
<p> Query the configuration:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli config get</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Config:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;numlock binding:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;not set<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;capslock binding:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;not set<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;scrollock binding:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;not set<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;require user PIN for OTP: true </p>
<p> Change the configuration:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli config set &#8211;otp-pin</code> </p>
<h3>Password safe</h3>
<p> Configure a PWS slot:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli pws add example.org john.doe passw0rd</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Added PWS slot 0 </p>
<p> Get the data from a slot:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli pws get 0</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;example.org<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;login:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;john.doe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;password: passw0rd </p>
<p> Copy the password to the clipboard (requires <code><a href="/docs/linux/man/1-xclip/">xclip</a></code>(1)).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>nitrocli pws get 0 &#8211;password &#8211;quiet | xclip -in</code> </p>
<p> Query the PWS slots:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;<code>&nbsp;nitrocli pws status</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;slot<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>example.org</p>
<h2>Index</h2>
