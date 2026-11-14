---
title: "ibportstate(8)"
name: "ibportstate"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibportstate/"
description: "IBPORTSTATE – handle port (physical) state and link speed of an InfiniBand port"
---

<p>IBPORTSTATE &#8211; handle port (physical) state and link speed of an InfiniBand port</p>
<h2>Synopsis</h2>
<p>ibportstate [options] &lt;dest dr_path|lid|guid&gt; &lt;portnum&gt; [&lt;op&gt;]</p>
<h2>Description</h2>
<p>ibportstate allows the port state and port physical state of an IB port to be queried (in addition to link width and speed being validated relative to the peer port when the port queried is a switch port), or a switch port to be disabled, enabled, or reset. It also allows the link speed/width enabled on any IB port to be adjusted.</p>
<h2>Options</h2>
<dl>
<dt><code>&lt;op&gt;</code></p>
<dd>
<dt><code>Supported ops: enable, disable, reset, speed, espeed, fdr10, width, query,</code></p>
<dd>on, off, down, arm, active, vls, mtu, lid, smlid, lmc, mkey, mkeylease, mkeyprot (Default is query) </p>
<p> <code>enable, disable, and reset</code> are only allowed on switch ports (An error is indicated if attempted on CA or router ports) </p>
<p> <code>off</code> change the port state to disable. </p>
<p> <code>on</code> change the port state to enable(only when the current state is disable). </p>
<p> <code>speed and width</code> are allowed on any port </p>
<p> <code>speed</code> values are the legal values for PortInfo:LinkSpeedEnabled (An error is indicated if PortInfo:LinkSpeedSupported does not support this setting) </p>
<p> <code>espeed</code> is allowed on any port supporting extended link speeds </p>
<p> <code>fdr10</code> is allowed on any port supporting fdr10 (An error is indicated if port&#8217;s capability mask indicates extended link speeds are not supported or if PortInfo:LinkSpeedExtSupported does not support this setting) </p>
<p> <code>width</code> values are legal values for PortInfo:LinkWidthEnabled (An error is indicated if PortInfo:LinkWidthSupported does not support this setting) (NOTE: Speed and width changes are not effected until the port goes through link renegotiation) </p>
<p> <code>query</code> also validates port characteristics (link width, speed, espeed, and fdr10) based on the peer port. This checking is done when the port queried is a switch port as it relies on combined routing (an initial LID route with directed routing to the peer) which can only be done on a switch. This peer port validation feature of query op requires LID routing to be functioning in the subnet. </p>
<p> <code>mkey, mkeylease, and mkeyprot</code> are only allowed on CAs, routers, or switch port 0 (An error is generated if attempted on external switch ports). Hexadecimal and octal mkeys may be specified by prepending the key with &#8216;0x&#8217; or &#8216;0&#8217;, respectively. If a non-numeric value (like &#8216;x&#8217;) is specified for the mkey, then ibportstate will prompt for a value.</dl>
<h3>Addressing Flags</h3>
<p><code>-L, &#8211;Lid</code> The address specified is a LID </p>
<p> <code>-G, &#8211;Guid</code> The address specified is a Port GUID </p>
<p> <code>-D, &#8211;Direct</code> The address specified is a directed route </p>
<pre>Examples:
 [options] -D [options] &quot;0&quot; # self port
 [options] -D [options] &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-s, &#8211;sm_port &lt;smlid&gt;</code> use &#8216;smlid&#8217; as the target lid for SA queries.</p>
<h3>Port Selection flags</h3>
<p><code>-C, &#8211;Ca &lt;ca_name&gt;</code> use the specified ca_name. </p>
<p> <code>-P, &#8211;Port &lt;ca_port&gt;</code> use the specified ca_port.</p>
<h3>Local port Selection</h3>
<p>Multiple port/Multiple CA support: when no IB device or port is specified (see the &quot;local umad parameters&quot; below), the libibumad library selects the port to use by the following criteria:</p>
<dl>
<dt>1.</p>
<dd>the first port that is ACTIVE.</p>
<dt>2.</p>
<dd>if not found, the first port that is UP (physical link up). </p>
<p> If a port and/or CA name is specified, the libibumad library attempts to fulfill the user request, and will fail if it is not possible. </p>
<p> For example: </p>
<pre>ibaddr # use the first port (criteria #1 above)
ibaddr -C mthca1 # pick the best port from &quot;mthca1&quot; only.
ibaddr -P 2 # use the second (active/up) port from the first available IB device.
ibaddr -C mthca0 -P 2 # use the specified port only.</pre>
</dl>
<h3>Configuration flags</h3>
<p><code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf </p>
<p> <code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads.</p>
<dl>
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for.</dl>
<h3>Debugging flags</h3>
<p><code>-h, &#8211;help</code> show the usage message</p>
<dl>
<dt><code>-d</code></p>
<dd>raise the IB debugging level. May be used several times (-ddd or -d -d -d).</p>
<dt><code>-e</code></p>
<dd>show send and receive errors (timeouts and others)</p>
<dt><code>-K, &#8211;show_keys</code></p>
<dd>show security keys (mkey, smkey, etc.) associated with the request.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>increase the application verbosity level. May be used several times (-vv or -v -v -v) </p>
<p> <code>-V, &#8211;version</code> show the version info.</dl>
<h2>Files</h2>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h2>Examples</h2>
<dl>
<dt><code>::</code></p>
<dd>ibportstate 3 1 disable # by lid ibportstate -G 0x2C9000100D051 1 enable # by guid ibportstate -D 0 1 # (query) by direct route ibportstate 3 1 reset # by lid ibportstate 3 1 speed 1 # by lid ibportstate 3 1 width 1 # by lid ibportstate -D 0 1 lid 0x1234 arm # by direct route</dl>
<h2>Author</h2>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>hal.rosenstock [at] gmail.com</i> &gt; </p>
</dl>
