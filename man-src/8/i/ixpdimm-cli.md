---
title: "ixpdimm-cli(8)"
name: "ixpdimm-cli"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ixpdimm-cli/"
description: "ixpdimm-cli – CLI to manage Intel(R) DIMMs"
---

<p>ixpdimm-cli &#8211; CLI to manage Intel(R) DIMMs </p>
<h2>Synopsis</h2>
<p><code>ixpdimm-cli</code> &lt;verb&gt; [&lt;options&gt;] [&lt;targets&gt;] [&lt;properties&gt;] verb</p>
<dl>
<dd>A command has a single verb which represents the action to be taken. Verb choices are <code>create</code>, <code>delete</code>, <code>dump</code>, <code>help</code>, <code>load</code>, <code>set</code>, <code>show</code>, <code>start</code>, and <code>version</code>. Use</p>
<dl>
<dd>&lt;verb&gt; <code>-help</code></dl>
<p> to see available commands for a specific verb.</dl>
<p> options</p>
<dl>
<dd>Following the verb are zero or more options which modify the action of the verb; overriding the default behavior with explicitly requested behavior.</dl>
<p> targets</p>
<dl>
<dd>Generally one or more targets are required to indicate the object of the action. Use</p>
<dl>
<dd>&lt;verb&gt; <code>-help</code> &lt;target&gt;</dl>
<p> to see available commands for a verb/target pair.</dl>
<p> properties</p>
<dl>
<dd>Finally, zero or more properties defined as a key/value pair can be used to modify the target.</dl>
<h2>Description</h2>
<p>Command line access to DIMM Management functionality is available through the ixpdimm-cli component. The NVMCLI exposes all available management features of the underlying DIMM. The Command Line Interface is an end-user, manufacturing and validation utility. <code>Show Device Firmware:</code></p>
<dl>
<dd><code>show</code> [<code>-all</code>|<code>-a</code>] [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-firmware</code> <code>-dimm</code> [(DimmIDs)]</dl>
<p> <code>Update Firmware:</code></p>
<dl>
<dd><code>load</code> <code>-source</code> (path) [<code>-force</code>|<code>-f</code>] [<code>-examine</code>|<code>-x</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)]</dl>
<p> <code>Show Device Performance:</code></p>
<dl>
<dd><code>show</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] <code>-performance</code> [(<code>BytesRead</code>|<code>BytesWritten</code>|<code>HostReads</code>|<code>HostWrites</code>|<code>BlockWrites</code>|<code>BlockReads</code>)]</dl>
<p> <code>Run Diagnostic:</code></p>
<dl>
<dd><code>start</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-diagnostic</code> [(<code>Quick</code>|<code>Config</code>|<code>PM</code>|<code>Security</code>|<code>FW</code>)] [<code>-dimm</code> (DimmIDs)]</dl>
<p> <code>Create Support Snapshot:</code></p>
<dl>
<dd><code>create</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-support</code> [<code>Name</code> <code>=</code> (string)]</dl>
<p> <code>Dump Support Data:</code></p>
<dl>
<dd><code>dump</code> <code>-destination</code> (path) [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-support</code></dl>
<p> <code>Delete Support Data:</code></p>
<dl>
<dd><code>delete</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-support</code></dl>
<p> <code>Toggle Software Logging:</code></p>
<dl>
<dd><code>set</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-system</code> <code>LogLevel</code> <code>=</code> (<code>0</code>|<code>1</code>)</dl>
<p> <code>Version:</code></p>
<dl>
<dd><code>version</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)]</dl>
<p> <code>Acknowledge event:</code></p>
<dl>
<dd><code>set</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-event</code> (EventID) <code>ActionRequired</code> <code>=</code> (<code>false</code>|<code>0</code>)</dl>
<p> <code>Show Events:</code></p>
<dl>
<dd><code>show</code> [<code>-starttime</code> (MM:dd:yyyy:hh:mm:ss)] [<code>-endtime</code> (MM:dd:yyyy:hh:mm:ss)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-event</code> [(EventID)] [<code>-dimm</code> (DimmID)] [<code>-namespace</code> (NamespaceID)] [<code>Severity</code> <code>=</code> (<code>Info</code>|<code>Warn</code>|<code>Critical</code>|<code>Fatal</code>)] [<code>Category</code> <code>=</code> (<code>Diag</code>|<code>FW</code>|<code>PlatformConfig</code>|<code>PM</code>|<code>Quick</code>|<code>Security</code>|<code>Health</code>|<code>Mgmt</code>)] [<code>ActionRequired</code> <code>=</code> (<code>1</code>|<code>0</code>)]</dl>
<p> <code>Show Preferences:</code></p>
<dl>
<dd><code>show</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-preferences</code></dl>
<p> <code>Change Preferences:</code></p>
<dl>
<dd><code>set</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-preferences</code> [<code>CLI_DEFAULT_DIMM_ID</code> <code>=</code> (<code>HANDLE</code>|<code>UID</code>)] [<code>CLI_DEFAULT_SIZE</code> <code>=</code> (<code>Auto</code>|<code>B</code>|<code>MiB</code>|<code>GiB</code>)] [<code>PERFORMANCE_MONITOR_ENABLED</code> <code>=</code> (<code>0</code>|<code>1</code>)] [<code>PERFORMANCE_MONITOR_INTERVAL_MINUTES</code> <code>=</code> (minutes)] [<code>EVENT_MONITOR_ENABLED</code> <code>=</code> (<code>0</code>|<code>1</code>)] [<code>EVENT_MONITOR_INTERVAL_MINUTES</code> <code>=</code> (minutes)] [<code>EVENT_LOG_MAX</code> <code>=</code> (count)] [<code>LOG_MAX</code> <code>=</code> (count)] [<code>SUPPORT_SNAPSHOT_MAX</code> <code>=</code> (count)]</dl>
<p> <code>Help:</code></p>
<dl>
<dd><code>help</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] [<code>Name</code> <code>=</code> (command)] [<code>verb</code> <code>=</code> (verb)]</dl>
<p> <code>Show Namespace:</code></p>
<dl>
<dd><code>show</code> [<code>-all</code>|<code>-a</code>] [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-units</code> [(GB|GiB)]] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-namespace</code> [(NamespaceIDs)] [<code>-pool</code> (PoolIDs)] [<code>Type</code> <code>=</code> (<code>Unknown</code>|<code>AppDirect</code>|<code>Storage</code>)] [<code>HealthState</code> <code>=</code> (<code>Unknown</code>|<code>Healthy</code>|<code>Warning</code>|<code>Critical</code>|<code>BrokenMirror</code>)]</dl>
<p> <code>Create Namespace:</code></p>
<dl>
<dd><code>create</code> [<code>-force</code>|<code>-f</code>] [<code>-units</code> [(GB|GiB)]] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-namespace</code> [<code>-pool</code> [(PoolIDs)]] <code>Type</code> <code>=</code> (<code>AppDirect</code>|<code>Storage</code>) [<code>BlockSize</code> <code>=</code> (size)] [<code>BlockCount</code> <code>=</code> (count)] [<code>Name</code> <code>=</code> (string)] [<code>Optimize</code> <code>=</code> (<code>CopyOnWrite</code>|<code>None</code>)] [<code>Enabled</code> <code>=</code> (<code>0</code>|<code>1</code>|<code>False</code>|<code>True</code>)] [<code>Encryption</code> <code>=</code> (<code>0</code>|<code>1</code>|<code>False</code>|<code>True</code>)] [<code>EraseCapable</code> <code>=</code> (<code>0</code>|<code>1</code>|<code>False</code>|<code>True</code>)] [<code>AppDirectSetting</code> <code>=</code> (value)] [<code>Capacity</code> <code>=</code> (capacity)] [<code>MemoryPageAllocation</code> <code>=</code> (<code>None</code>|<code>DRAM</code>|<code>AppDirect</code>)]</dl>
<p> <code>Modify Namespace:</code></p>
<dl>
<dd><code>set</code> [<code>-force</code>|<code>-f</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-namespace</code> [(NamespaceIDs)] [<code>Name</code> <code>=</code> (string)] [<code>BlockCount</code> <code>=</code> (count)] [<code>Enabled</code> <code>=</code> (<code>0</code>|<code>1</code>)] [<code>Capacity</code> <code>=</code> (capacity)]</dl>
<p> <code>Delete Namespace:</code></p>
<dl>
<dd><code>delete</code> [<code>-force</code>|<code>-f</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-namespace</code> [(NamespaceIDs)]</dl>
<p> <code>Show Memory Allocation Goal:</code></p>
<dl>
<dd><code>show</code> [<code>-all</code>|<code>-a</code>] [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] [<code>-dimm</code> (DimmIDs)] <code>-goal</code> [<code>-socket</code> (SocketIDs)]</dl>
<p> <code>Delete Memory Allocation Goal:</code></p>
<dl>
<dd><code>delete</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] [<code>-dimm</code> (DimmIDs)] <code>-goal</code> [<code>-socket</code> (SocketIDs)]</dl>
<p> <code>Create Memory Allocation Goal:</code></p>
<dl>
<dd><code>create</code> [<code>-force</code>|<code>-f</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] [<code>-dimm</code> (DimmIDs)] [<code>-socket</code> (SocketIDs)] <code>-goal</code> [<code>MemorySize</code> <code>=</code> (GiB)] [<code>AppDirectSize</code> <code>=</code> (GiB)] [<code>AppDirectSetting</code> <code>=</code> (value)] [<code>AppDirect1Size</code> <code>=</code> (GiB)] [<code>AppDirect1Setting</code> <code>=</code> (value)] [<code>AppDirect2Size</code> <code>=</code> (GiB)] [<code>AppDirect2Setting</code> <code>=</code> (value)] [<code>ReserveDimm</code> <code>=</code> (<code>0</code>|<code>1</code>)] [<code>StorageCapacity</code> <code>=</code> (Remaining)]</dl>
<p> <code>Show Persistent Memory:</code></p>
<dl>
<dd><code>show</code> [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-all</code>|<code>-a</code>] [<code>-units</code> [(GB|GiB)]] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-pool</code> [(PoolIDs)] [<code>-socket</code> (SocketIDs)]</dl>
<p> <code>Dump Memory Allocation Settings:</code></p>
<dl>
<dd><code>dump</code> <code>-destination</code> (path) [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-system</code> <code>-config</code></dl>
<p> <code>Load Memory Allocation Goal:</code></p>
<dl>
<dd><code>load</code> [<code>-force</code>|<code>-f</code>] <code>-source</code> (path) [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-goal</code> [<code>-dimm</code> (DimmIDs)] [<code>-socket</code> (SocketIDs)]</dl>
<p> <code>Show Sensor:</code></p>
<dl>
<dd><code>show</code> [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-all</code>|<code>-a</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-sensor</code> [(<code>MediaTemperature</code>|<code>ControllerTemperature</code>|<code>SpareCapacity</code>|<code>WearLevel</code>|<code>UnsafeShutdowns</code>|<code>PowerOnTime</code>|<code>UpTime</code>|<code>PowerCycles</code>|<code>FWErrorCount</code>|<code>PowerLimited</code>|<code>MediaErrorsUncorrectable</code>|<code>MediaErrorsCorrected</code>|<code>MediaErrorsErasureCoded</code>|<code>WriteCountMax</code>|<code>)]</code> [<code>-dimm</code> (DimmIDs)]</dl>
<p> <code>Change Sensor Settings:</code></p>
<dl>
<dd><code>set</code> [<code>-force</code>|<code>-f</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-sensor</code> (<code>MediaTemperature</code>|<code>ControllerTemperature</code>|<code>SpareCapacity</code>) [<code>-dimm</code> (DimmIDs)] [<code>NonCriticalThreshold</code> <code>=</code> (value)] [<code>EnabledState</code> <code>=</code> (<code>0</code>|<code>1</code>)]</dl>
<p> <code>Load Simulator:</code></p>
<dl>
<dd><code>load</code> [<code>-source</code> (path)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-system</code> [<code>unload</code> <code>=</code> (<code>0</code>|<code>1</code>)]</dl>
<p> <code>Show Host Server:</code></p>
<dl>
<dd><code>show</code> [<code>-all</code>|<code>-a</code>] [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-system</code></dl>
<p> <code>Show Device:</code></p>
<dl>
<dd><code>show</code> [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-all</code>|<code>-a</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] [<code>-socket</code> (SocketIDs)]</dl>
<p> <code>Modify Device:</code></p>
<dl>
<dd><code>set</code> [<code>-force</code>|<code>-f</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] [<code>FirstFastRefresh</code> <code>=</code> (<code>0</code>|<code>1</code>)] [<code>ViralPolicy</code> <code>=</code> (<code>0</code>|<code>1</code>)]</dl>
<p> <code>Set Firmware Logging:</code></p>
<dl>
<dd><code>set</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] <code>FwLogLevel</code> <code>=</code> (<code>Disabled</code>|<code>Error</code>|<code>Warning</code>|<code>Info</code>|<code>Debug</code>)</dl>
<p> <code>Change Device Passphrase:</code></p>
<dl>
<dd><code>set</code> [<code>-source</code> (path)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] <code>Passphrase</code> <code>=</code> [(string)] <code>NewPassphrase</code> <code>=</code> [(string)] <code>ConfirmPassphrase</code> <code>=</code> [(string)]</dl>
<p> <code>Enable Device Security:</code></p>
<dl>
<dd><code>set</code> [<code>-source</code> (path)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] <code>NewPassphrase</code> <code>=</code> [(string)] <code>ConfirmPassphrase</code> <code>=</code> [(string)]</dl>
<p> <code>Change Device Security:</code></p>
<dl>
<dd><code>set</code> [<code>-source</code> (path)] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] <code>LockState</code> <code>=</code> (<code>Unlocked</code>|<code>Disabled</code>) <code>Passphrase</code> <code>=</code> [(string)]</dl>
<p> <code>Erase Device Data:</code></p>
<dl>
<dd><code>delete</code> [<code>-source</code> (path)] [<code>-force</code>|<code>-f</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] <code>Passphrase</code> <code>=</code> [(string)]</dl>
<p> <code>Show Memory Resources:</code></p>
<dl>
<dd><code>show</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-memoryresources</code></dl>
<p> <code>Show System Capabilities:</code></p>
<dl>
<dd><code>show</code> [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-all</code>|<code>-a</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-system</code> <code>-capabilities</code></dl>
<p> <code>Show Topology:</code></p>
<dl>
<dd><code>show</code> [<code>-display</code>|<code>-d</code> (Attributes)] [<code>-all</code>|<code>-a</code>] [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-topology</code> [<code>-dimm</code> (DimmIDs)] [<code>-socket</code> (SocketIDs)]</dl>
<p> <code>Inject Error:</code></p>
<dl>
<dd><code>set</code> [<code>-help</code>|<code>-h</code>] [<code>-output</code>|<code>-o</code> (<code>text</code>|<code>nvmxml</code>)] <code>-dimm</code> [(DimmIDs)] [<code>Clear</code> <code>=</code> <code>1</code> [<code>Temperature</code> <code>=</code> (degrees)] [<code>Poison</code> <code>=</code> (address)] [<code>DieSparing</code> <code>=</code> <code>1</code> [<code>SpareAlarm</code> <code>=</code> <code>1</code> [<code>FatalMediaError</code> <code>=</code> <code>1</code></dl>
<h2>Options</h2>
<p><code>-all|-a</code> </p>
<dl>
<dd>Show all attributes. Note: The all and display options are exclusive and may not be used together.</dl>
<p> <code>-display|-d </code> <i>(Attributes)</i> </p>
<dl>
<dd>Filter the returned attributes by explicitly specifying a comma separated list of any of the attributes defined in the Return Data section. Note: The all and display options are exclusive and may not be used together.</dl>
<p> <code>-help|-h</code> </p>
<dl>
<dd>Display help for the command.</dl>
<p> <code>-output|-o text|nvmxml</code> </p>
<dl>
<dd>Change the output format. One of: &quot;text&quot; (default) or &quot;nvmxml&quot;.</dl>
<h2>Exit Codes</h2>
<dl>
<dt><code>0</code></p>
<dd>The operation succeeded.</p>
<dt><code>1</code></p>
<dd>A general error occurred when executing the operation.</p>
<dt><code>2</code></p>
<dd>There was not enough memory to complete the requested operation.</p>
<dt><code>3</code></p>
<dd>The command is not supported in the current context. </p>
</dl>
<h2>Example</h2>
<p><code>ixpdimm-cli show -dimm</code></p>
<dl>
<dd>Show default information about all DIMMs</dl>
<p> <code>ixpdimm-cli show -a -dimm 1234</code></p>
<dl>
<dd>Show all information about DIMM 1234.</dl>
<p> <code>ixpdimm-cli show -d HealthState,LockState -dimm</code></p>
<dl>
<dd>Show HealthState and LockState information for all DIMMs.</dl>
<p> <code>ixpdimm-cli set -source mypassphrase.file -dimm 1234</code><br />
 <code>NewPassphrase= ConfirmPassphrase=</code></p>
<dl>
<dd>Set a passphrase on DIMM 1234 by supplying the passphrase in the file mypassphrase.file. The format of the file would be:</p>
<dl>
<dd>#ascii<br />
 NewPassphrase=myNewPassphrase</dl>
</dl>
<p> <code>ixpdimm-cli create -goal VolatileSize=32 PersistentSize=Remaining PersistentSettings=4KB_4KB</code></p>
<dl>
<dd>Configure the capacity on each DIMM with 32 GiB of volatile memory, and the remaining persistent memory with specific QoS attributes.</dl>
<p> <code>nvncli set -sensor MediaTemperature -dimm 1234 CriticalThreshold=51 EnabledState=1</code></p>
<dl>
<dd>Change the media temperature threshold to 51 on the specified DIMM and enable the alarm.</dl>
<p> <code>ixpdimm-cli show -dimm -performance BytesRead</code></p>
<dl>
<dd>Show the number of bytes read for all DIMMs in the server.</dl>
<p> <code>nvncli set -sensor MediaTemperature -dimm 1234 CriticalThreshold=51 EnabledState=1</code></p>
<dl>
<dd>Change the media temperature threshold to 51 on the specified DIMM and enable the alarm.</dl>
<p> <code>ixpdimm-cli show -a -namspace 12345678-1234-1234-1234-123456789012</code></p>
<dl>
<dd>Show all attributes for the specified namespace</dl>
<p> <code>ixpdimm-cli create -namespace -pool 12345678-1234-1234-1234-123456789012</code><br />
 <code>Type=Storage BlockSize=512 BlockCount=2097152</code></p>
<dl>
<dd>Create a 1 GB Storage namespace on pool 12345678-1234-1234-1234-123456789012 with a block size of 512</dl>
<h2>Files</h2>
<p>/usr/share/nvdimm-mgmt/apss.dat<br />
 /usr/share/nvdimm-mgmt/public.rev0.pem</p>
<h2>See Also</h2>
<p>ixpdimm-monitor (8) </p>
<h2>Author</h2>
<p>Created by Intel Corporation.</p>
