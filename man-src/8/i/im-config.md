---
title: "im-config(8)"
name: "im-config"
section: "8"
letter: "i"
url: "/docs/linux/man/8-im-config/"
description: "im-config – set up input method framework configuration"
---

<p>im-config &#8211; set up input method framework configuration</p>
<h2>Synopsis</h2>
<dl>
<dt><code>im-config [OPTION]</code></p>
<dd>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>List all; force to list all possible input method frameworks in menu or STDOUT even if any associated packages are not installed on the system.</p>
<dt><code>-c</code></p>
<dd>Use console dialogue.</p>
<dt><code>-x</code></p>
<dd>Use X dialogue with zenity.</p>
<dt><code>-s</code></p>
<dd>No action; perform a simulation of events that would occur but do not actually change configuration files.</p>
<dt><code>-l</code></p>
<dd>List all available input method frameworks to STDOUT. Unless <code>-a</code> is used, list only ones with associated packages installed.</p>
<dt><code>-m</code></p>
<dd>List configuration values to STDOUT:</p>
<dl>
<dd>&bull; active configuration (system)</dl>
<dl>
<dd>&bull; active configuration (user)</dl>
<dl>
<dd>&bull; automatic configuration for the current locale</dl>
<dl>
<dd>&bull; override configuration for the current locale</dl>
<dl>
<dd>&bull; automatic configuration for most locales</dl>
<dl>
<dd>If the active configuration is <code>custom</code>, the user made a custom configuration and im-config should not change it.</dl>
<dt><code>-n</code></p>
<dd><i>&lt;input method name&gt;</i> </p>
<p> Set input method framework to <i>&lt;input method name&gt;</i>. This option is for other configuration tool to set the input method. Since the default value of <i>&lt;input method name&gt;</i> is &quot;auto&quot; or &quot;cjkv&quot;, you usually do not need to use this from other configuration script. </p>
<p> Specifying invalid <i>&lt;input method name&gt;</i> causes the error exit. Updating the configuration file which was not updated by <code>im-config</code> also causes the error exit. </p>
<p> When this <i>&lt;input method name&gt;</i> is &quot;REMOVE&quot; then it always removes the configuration file even if it was not updated by <code>im-config</code>.</p>
<dt><code>-o</code></p>
<dd><i>&lt;input method name&gt;</i> </p>
<p> Print the localized description of the input method <i>&lt;input method name&gt;</i> to STDOUT.</dl>
<p> The <code>-l</code>, <code>-m</code>, <code>-n</code>, and <code>-o</code> options are meant to be API for other programs to control the im-config.</p>
<h2>Description</h2>
<p>This manual page very briefly documents <code>im-config</code> and the configuration of the input method. <code>im-config</code> provides the framework to configure the input method framework on GUI system (Wayland or original X Window) with its GUI or console terminal dialogue. If this is invoked without option, this lists available input methods as its choice while marking automatic choice with trailing @-mark. The listing is ordered by the priority of the input method framework. The input method framework with the highest priority comes first. The availability of the input method frameworks are judged by the installation of the input method framework packages. After you make a choice for the input method framework, this displays a guidance for associated input method engine packages which enables to input non-latin characters specific to the need of some languages to be installed. The activation of input method engines are out of scope for <code>im-config</code>. You need to activate them using the mechanism offered by the deployed input method framework. For GNOME Desktop which normally uses ibus as its input method framework, activate input method engines by &quot;Setting&quot; -&gt; &quot;Keyboard&quot; -&gt; &quot;Input Sources&quot; and click &quot;+&quot;-sign. For other Desktop environments, you should see something like a small tray icon for the input method framework which can be used to activate input method engines. If only a set of required input method packages along with the im-config package is installed, you do not need to use this command. Such a installation works well in its default and there is no need to use this command. When you wish to have multiple input method frameworks installed and wish to switch among them, you need to use this command. If you have no idea for what package to install, <code>im-config</code> invoked with both <code>-a</code> and <code>-s</code> is a good start. This input method is the essential mechanism for Japanese, Chinese and Korean (CJK) languages to enter their non-ASCII native characters. This is also useful to support specialized keyboard bindings for other non-European languages such as Indic and other Asian languages. Input method frameworks such as IBus, fcitx5, and uim support not only one of these CJK languages but support almost all languages simultaneously by dynamically switching keyboard modes with GUI on the fly. The im-config package installs a hook script <code>/etc/X11/Xsession.d/70im-config_launch</code>. At session start it sources this file as a POSIX shell code. Then this hook script tries to source the user configuration file <code>~/.xinputrc</code>, if it exists. Otherwise, this hook script sources the system configuration file <code>/etc/X11/xinit/xinputrc</code>. The im-config package also installs another hook script <code>/etc/profile.d/im-config_wayland.sh</code> and a desktop file <code>/usr/share/applications/im-config.desktop</code>. When a desktop system starts under wayland, it uses these files instead. Then this hook script and the desktop file tries to source the user configuration file <code>~/.xinputrc</code>, if it exists. Otherwise, this hook script sources the system configuration file <code>/etc/X11/xinit/xinputrc</code>. <code>im-config</code> invoked from a user account updates the user configuration file <code>~/.xinputrc</code>. <code>im-config</code> invoked from the root account updates the system configuration file <code>~/etc/X11/xinit/xinputrc</code>. The essential contents of generated files are: <code>run_im </code><i>&lt;input method name&gt;</i> When these files are sourced, the <code>run_im</code> shell function instructs to source the initialization code for the corresponding input method. This initialization code is defined in the <i>&lt;2 digits number&gt;</i>_<i>&lt;input method name&gt;</i>.<code>rc</code> file in <code>/usr/share/im-config/data</code>. The im-config hook script, <code>/etc/X11/Xsession.d/70im-config_launch</code>, exports following variables to programs: $XMODIFIERS, $GTK_IM_MODULE, $QT_IM_MODULE, and $CLUTTER_IM_MODULE. The im-config hook script, <code>/etc/X11/Xsession.d/70im-config_launch</code>, also set $STARTUP to use <code>/usr/bin/im-launch</code> for starting required daemons. If you wish to create a custom configuration beyond what <code>im-config</code> can do for you, please copy one of these initialization code files into <code>~/.xinputrc</code> or <code>/etc/X11/xinit/xinputrc</code> and edit it to suite your need. For example, <code>02_cjkv.rc</code> tells how input method can be customized for each locale. This script should be written to set environment variables if &quot;$IM_CONFIG_PHASE&quot; = 1 and to start daemon programs if &quot;$IM_CONFIG_PHASE&quot; = 2 . Please note that this <i>&lt;2 digits number&gt;</i> part of these configuration files may change for every new releases of the im-config package. When a user makes manual changes to <code>~/.xinputrc</code> or <code>/etc/X11/xinit/xinputrc</code> without using <code>im-config</code>, <code>im-config</code> will detect it using a md5sum hush value embedded in the shell comment and will not overwrite such files. You must erase them manually if you wish to replace them with ones created by <code>im-config</code>. The <i>&lt;2 digits number&gt;</i>_<i>&lt;input method name&gt;</i>.<code>conf</code> files in <code>/usr/share/im-config/data</code> provide the UI data for <code>im-config</code> and the heuristic logic of selecting desirable input method under the auto mode. The smaller number of the <i>&lt;2 digits number&gt;</i> indicates the higher priority of <i>&lt;input method name&gt;</i>. These <i>&lt;2 digits number&gt;</i>_<i>&lt;input method name&gt;</i>.<code>conf</code> files define few variables and functions. The value of <code>IM_CONFIG_SHORT</code> is the short description of the input method for the menu. The value of <code>IM_CONFIG_LONG</code> is the long description of the input method explaining its package dependency. The <code>package_menu</code> shell function defines as a function to return true if any associated input method packages are installed to activate its menu entry. The <code>package_auto</code> shell function defines as a function to return true if the sufficient input method packages are installed for the auto mode. These definitions use the <code>package_status</code> shell function which takes package name as its argument and returns true if it is installed properly. The menu lists input methods with the <i>&lt;2 digits number&gt;</i> between <code>00</code> and <code>89</code>. The auto mode considers its input method candidate from <i>&lt;2 digits number&gt;</i> between <code>10</code> and <code>79</code> in this order. The usage convention of <i>&lt;2 digits number&gt;</i> is:</p>
<dl>
<dt><code>00-09:</code></p>
<dd>Input Method choice mode (default/auto/cjkv/REMOVE)</p>
<dt><code>10-49:</code></p>
<dd>Input Method supporting multiple languages.(auto ready)</p>
<dt><code>50-79:</code></p>
<dd>Input Method supporting limited languages. (auto ready)</p>
<dt><code>80-89:</code></p>
<dd>Input Method (deprecated one) (not for auto)</p>
<dt><code>90-99:</code></p>
<dd>Used internally by <code>im-config</code> (not for auto)</dl>
<p> This structure ensures to have different input methods to be installed side-by-side with minimal user configurations. </p>
<h2>Troubleshoot</h2>
<p>If you have any problem, see the first part of <code>~/.xsession-errors</code> and look for the cause. If you are running <code>im-config</code> while Debian (sid) system is undergoing a major library transition, you may need to manually set up <code>~/.xinputrc</code> with adjusted library version number etc. Please file a bug report to the im-config package using <a href="/docs/linux/man/1-reportbug/">reportbug</a>(1) describing your resolution experience.</p>
<h2>See Also</h2>
<p><code>/usr/share/doc/im-config/README.Debian.gz</code></p>
<h2>Author</h2>
<p>This manual page was written by Osamu Aoki &lt;osamu [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
