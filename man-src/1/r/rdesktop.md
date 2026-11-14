---
title: "rdesktop(1)"
name: "rdesktop"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdesktop/"
description: "rdesktop – Remote Desktop Protocol client"
---

<h2>NAME</h2>
<p> <i>rdesktop</i> &#8211; Remote Desktop Protocol client</p>
<h2>SYNOPSIS</h2>
<p> <code>rdesktop [options] server[:port]</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>rdesktop</i> is a client for Remote Desktop Protocol (RDP), used in a number of Microsoft products including Windows NT Terminal Server, Windows 2000 Server, Windows XP and Windows 2003 Server. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u &lt;username&gt;</code></p>
<dd> Username for authentication on the server.</p>
<dt><code>-d &lt;domain&gt;</code></p>
<dd> Domain for authentication.</p>
<dt><code>-s &lt;shell&gt;</code></p>
<dd> Startup shell for the user &#8211; starts a specific application instead of Explore. If SeamlessRDP is enabled this is the application which i started in seamless mode.</p>
<dt><code>-c &lt;directory&gt;</code></p>
<dd> The initial working directory for the user. Often used in combination with -s to set up a fixed login environment.</p>
<dt><code>-p &lt;password&gt;</code></p>
<dd> The password to authenticate with. Note that this may have no effect if &quot;Always prompt for password&quot; is enabled on the server. WARNING: if you specify a password on the command line it may be visible to other users when they use tools like ps. Use -p &#8211; to make rdesktop request a password at startup (from standard input).</p>
<dt><code>-n &lt;hostname&gt;</code></p>
<dd> Client hostname. Normally rdesktop automatically obtains the hostname of the client.</p>
<dt><code>-k &lt;keyboard-map&gt;</code></p>
<dd> Keyboard layout to emulate. This requires a corresponding keymap file to be installed. The standard keymaps provided with rdesktop follow the RFC1766 naming scheme: a language code followed by a country code if necessary &#8211; e.g. en-us, en-gb, de, fr, sv, etc. </p>
<p> The default keyboard map depends on the current locale (LC_* and LANG environment variables). If the current locale is unknown, the default keyboard map is en-us (a US English keyboard). </p>
<p> The keyboard maps are file names, which means that they are case sensitive. The standard keymaps are all in lowercase. </p>
<p> The keyboard maps are searched relative to the directories $HOME/.rdesktop/keymaps, KEYMAP_PATH (specified at build time), and $CWD/keymaps, in this order. The keyboard-map argument can also be an absolute filename. </p>
<p> The special value `none&#8217; can be used instead of a keyboard map. In this case, rdesktop will guess the scancodes from the X11 event key codes using an internal mapping method. This method only supports the basic alphanumeric keys and may not work properly on all platforms so its use is discouraged.</p>
<dt><code>-g &lt;geometry&gt;</code></p>
<dd> Desktop geometry (WxH). If geometry is the special word &quot;workarea&quot;, the geometry will be fetched from the extended window manager hints property _NET_WORKAREA, from the root window. The geometry can also be specified as a percentage of the whole screen, e.g. &quot;-g 80%&quot;. </p>
<p> If the specified geometry depends on the screen size, and the screen size is changed, rdesktop will automatically reconnect using the new screen size. This requires that rdesktop has been compiled with RandR support.</p>
<dt><code>-i</code></p>
<dd> Use password as smartcard pin. If a valid user certificate is matched in smart card reader the password passed with p argument is used as pin for the smart card. This feature also requires that smart card redirection is used using r scard argument.</p>
<dt><code>-f</code></p>
<dd> Enable fullscreen mode. This overrides the window manager and causes the rdesktop window to fully cover the current screen. Fullscreen mode can be toggled at any time using Ctrl-Alt-Enter.</p>
<dt><code>-b</code></p>
<dd> Force the server to send screen updates as bitmaps rather than using higher-level drawing operations.</p>
<dt><code>-t</code></p>
<dd> Disable use of remote control. This will disable features like seamless connection sharing.</p>
<dt><code>-A &lt;seamlessrdpshell&gt;</code></p>
<dd> Enable SeamlessRDP by specifying the path to seamless rdp shell. In this mode, rdesktop creates a X11 window for each window on the server side. This mode requires the SeamlessRDP server side component, which is available from <i><a rel="nofollow" href="http://www.cendio.com/seamlessrdp/">http://www.cendio.com/seamlessrdp/</a></i>. </p>
<p> When using this option, you should normally specify a startup shell which launches the desired application through SeamlessRDP. </p>
<p> Example: rdesktop -A &#8216;c:\seamlessrdp\seamlessrdpshell.exe&#8217; -s &#8216;notepad&#8217; mywts.domain.com </p>
<p> Any subsequential call to the above commandline example will make use of the seamless connection sharing feature which spawns another notepad in the current connection to the specified server and then exit. </p>
<dt><code>-B</code></p>
<dd> Use the BackingStore of the Xserver instead of the integrated one in rdesktop.</p>
<dt><code>-e</code></p>
<dd> Disable encryption. This option is only needed (and will only work) if you have a French version of NT TSE.</p>
<dt><code>-E</code></p>
<dd> Disable encryption from client to server. This sends an encrypted login packet, but everything after this is unencrypted (including interactive logins).</p>
<dt><code>-m</code></p>
<dd> Do not send mouse motion events. This saves bandwidth, although some Windows applications may rely on receiving mouse motion.</p>
<dt><code>-C</code></p>
<dd> Use private colourmap. This will improve colour accuracy on an 8-bit display, but rdesktop will appear in false colour when not focused.</p>
<dt><code>-D</code></p>
<dd> Hide window manager decorations, by using MWM hints.</p>
<dt><code>-K</code></p>
<dd> Do not override window manager key bindings. By default rdesktop attempts to grab all keyboard input when it is in focus.</p>
<dt><code>-S &lt;button size&gt;</code></p>
<dd> Enable single application mode. This option can be used when running a single, maximized application (via -s). When the minimize button of the windows application is pressed, the rdesktop window is minimized instead of the remote application. The maximize/restore button is disabled. For this to work, you must specify the correct button size, in pixels. The special word &quot;standard&quot; means 18 pixels.</p>
<dt><code>-T &lt;title&gt;</code></p>
<dd> Sets the window title. The title must be specified using an UTF-8 string.</p>
<dt><code>-N</code></p>
<dd> Enable numlock syncronization between the Xserver and the remote RDP session. This is useful with applications that looks at the numlock state, but might cause problems with some Xservers like Xvnc.</p>
<dt><code>-X &lt;windowid&gt;</code></p>
<dd> Embed rdesktop-window in another window. The windowid is expected to be decimal or hexadecimal (prefixed by 0x).</p>
<dt><code>-a &lt;bpp&gt;</code></p>
<dd> Sets the colour depth for the connection (8, 15, 16, 24 or 32). More than 8 bpp are only supported when connecting to Windows XP (up to 16 bpp) or newer. Note that the colour depth may also be limited by the server configuration. The default value is the depth of the root window.</p>
<dt><code>-z</code></p>
<dd> Enable compression of the RDP datastream.</p>
<dt><code>-x &lt;experience&gt;</code></p>
<dd> Changes default bandwidth performance behaviour for RDP5. By default only theming is enabled, and all other options are disabled (corresponding to modem (56 Kbps)). Setting experience to b[roadband] enables menu animations and full window dragging. Setting experience to l[an] will also enable the desktop wallpaper. Setting experience to m[odem] disables all (including themes). Experience can also be a hexidecimal number containing the flags.</p>
<dt><code>-P</code></p>
<dd> Enable caching of bitmaps to disk (persistent bitmap caching). This generally improves performance (especially on low bandwidth connections) and reduces network traffic at the cost of slightly longer startup and some disk space. (10MB for 8-bit colour, 20MB for 15/16-bit colour, 30MB for 24-bit colour and 40MB for 32-bit colour sessions)</p>
<dt><code>-r &lt;device&gt;</code></p>
<dd> Enable redirection of the specified device on the client, such that it appears on the server. Note that the allowed redirections may be restricted by the server configuration. </p>
<p> Following devices are currently supported:</p>
<dt><code>-r comport:&lt;comport&gt;=&lt;device&gt;,&#8230;</code></p>
<dd> Redirects serial devices on your client to the server. Note that if you need to change any settings on the serial device(s), do so with an appropriate tool before starting rdesktop. In most OSes you would use stty. Bidirectional/Read support requires Windows XP or newer. In Windows 2000 it will create a port, but it&#8217;s not seamless, most shell programs will not work with it.</p>
<dt><code>-r disk:&lt;sharename&gt;=&lt;path&gt;,&#8230;</code></p>
<dd> Redirects a path to the share \tsclient\&lt;sharename&gt; on the server (requires Windows XP or newer). The share name is limited to 8 characters.</p>
<dt><code>-r lptport:&lt;lptport&gt;=&lt;device&gt;,&#8230;</code></p>
<dd> Redirects parallel devices on your client to the server. Bidirectional/Read support requires Windows XP or newer. In Windows 2000 it will create a port, but it&#8217;s not seamless, most shell programs will not work with it.</p>
<dt><code>-r printer:&lt;printername&gt;[=&lt;driver&gt;],&#8230;</code></p>
<dd> Redirects a printer queue on the client to the server. The &lt;printername&gt; is the name of the queue in your local system. &lt;driver&gt; defaults to a simple PS-driver unless you specify one. Keep in mind that you need a 100% match in the server environment, or the driver will fail. The first printer on the command line will be set as your default printer.</p>
<dt><code>-r sound:[local|off|remote]</code></p>
<dd> Redirects sound generated on the server to the client. &quot;remote&quot; only has any effect when you connect to the console with the -0 option. (Requires Windows XP or newer).</p>
<dt><code>-r lspci</code></p>
<dd> Activates the lspci channel, which allows the server to enumerate the clients PCI devices. See the file lspci-channel.txt in the documentation for more information.</p>
<dt><code>-r scard[:&lt;Scard Name&gt;=&lt;Alias Name&gt;[;&lt;Vendor Name&gt;][,&#8230;]]</code></p>
<dd> Enables redirection of one or more smart-cards. You can provide static name binding between linux and windows. To do this you can use optional parameters as described: &lt;Scard Name&gt; &#8211; device name in Linux/Unix enviroment, &lt;Alias Name&gt; &#8211; device name shown in Windows enviroment &lt;Vendor Name&gt; &#8211; optional device vendor name. For list of examples run rdesktop without parameters.</p>
<dt><code>-0</code></p>
<dd> Attach to the console of the server (requires Windows Server 2003 or newer).</p>
<dt><code>-4</code></p>
<dd> Use RDP version 4.</p>
<dt><code>-5</code></p>
<dd> Use RDP version 5 (default).</dl>
<h2>CredSSP Smartcard options</h2>
<dl>
<dt><code>&#8211;sc-csp-name &lt;name&gt;</code></p>
<dd> Specify the CSP (Crypto Service Provider) to use on the windows side for the smartcard authentication. CSP is the driver for your smartcard and it seems like this is required to be specified for CredSSP authentication. For swedish NetID the following CSP name is used; &quot;Net iD &#8211; CSP&quot;.</p>
<dt><code>&#8211;sc-container-name &lt;name&gt;</code></p>
<dd> Specify the container name, usally this is the username for default container and it seems like this is required to be specified for CredSSP authentication.</p>
<dt><code>&#8211;sc-reader-name &lt;name&gt;</code></p>
<dd> Specify the reader name to be used to prevent the pin code being sent to wrong card if there are several readers.</p>
<dt><code>&#8211;sc-card-name &lt;name&gt;</code></p>
<dd> Specify the card name for example; &quot;Telia EID IP5a&quot;.</dl>
<h2>EXIT VALUES</h2>
<dl>
<dt><code>0</code></p>
<dd> RDP session terminated normally</p>
<dt><code>1</code></p>
<dd> Server initiated disconnect (also returned for logoff by XP joined to a domain)</p>
<dt><code>2</code></p>
<dd> Server initiated logoff</p>
<dt><code>3</code></p>
<dd> Server idle timeout reached</p>
<dt><code>4</code></p>
<dd> Server logon timeout reached</p>
<dt><code>5</code></p>
<dd> The session was replaced</p>
<dt><code>6</code></p>
<dd> The server is out of memory</p>
<dt><code>7</code></p>
<dd> The server denied the connection</p>
<dt><code>8</code></p>
<dd> The server denied the connection for security reason</p>
<dt><code>9</code></p>
<dd> The user cannot connect to the server due to insufficient access privileges</p>
<dt><code>10</code></p>
<dd> The server does not accept saved user credentials and requires that the user enter their credentials for each connection</p>
<dt><code>11</code></p>
<dd> Disconnect initiated by administration tool</p>
<dt><code>12</code></p>
<dd> Disconnect initiated by user</p>
<dt><code>16</code></p>
<dd> Internal licensing error</p>
<dt><code>17</code></p>
<dd> No license server available</p>
<dt><code>18</code></p>
<dd> No valid license available</p>
<dt><code>19</code></p>
<dd> Invalid licensing message</p>
<dt><code>20</code></p>
<dd> Hardware id doesn&#8217;t match software license</p>
<dt><code>21</code></p>
<dd> Client license error</p>
<dt><code>22</code></p>
<dd> Network error during licensing protocol</p>
<dt><code>23</code></p>
<dd> Licensing protocol was not completed</p>
<dt><code>24</code></p>
<dd> Incorrect client license enryption</p>
<dt><code>25</code></p>
<dd> Can&#8217;t upgrade license</p>
<dt><code>26</code></p>
<dd> The server is not licensed to accept remote connections</p>
<dt><code>62</code></p>
<dd> The local client window was closed</p>
<dt><code>63</code></p>
<dd> Some other, unknown error occured</p>
<dt><code>64</code></p>
<dd> Command line usage error</p>
<dt><code>69</code></p>
<dd> A service or resource (such as memory) is unavailable</p>
<dt><code>70</code></p>
<dd> An internal software error has been detected</p>
<dt><code>71</code></p>
<dd> Operating system error</p>
<dt><code>76</code></p>
<dd> Protocol error or unable to connect to remote host. </p>
</dl>
<h2>LINKS</h2>
<p> Main website of rdesktop<br />
 <i><a rel="nofollow" href="http://www.rdesktop.org/">http://www.rdesktop.org/</a> </p>
<p> </i></p>
<h2>Index</h2>
