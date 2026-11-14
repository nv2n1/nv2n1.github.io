---
title: "collectd-java(5)"
name: "collectd-java"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-java/"
description: "collectd-java – Documentation of collectd’s \"java plugin\""
---

<p>collectd-java &#8211; Documentation of collectd&#8217;s &quot;java plugin&quot;</p>
<h2>Synopsis</h2>
<pre> LoadPlugin &quot;java&quot;
 &lt;Plugin &quot;java&quot;&gt;
 JVMArg &quot;-verbose:jni&quot;
 JVMArg &quot;-Djava.class.path=/opt/collectd/lib/collectd/bindings/java&quot;
 
 LoadPlugin &quot;org.collectd.java.Foobar&quot;
 &lt;Plugin &quot;org.collectd.java.Foobar&quot;&gt;
 # To be parsed by the plugin
 &lt;/Plugin&gt;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <i>Java</i> plugin embeds a <i>Java Virtual Machine</i> (<font SIZE="-1">JVM</font>) into <i>collectd</i> and provides a Java interface to part of collectd&#8217;s <font SIZE="-1">API.</font> This makes it possible to write additions to the daemon in Java. </p>
<p> This plugin is similar in nature to, but shares no code with, the <i>Perl</i> plugin by Sebastian Harl, see <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5) for details.</p>
<h2>Configuration</h2>
<p>A short outline of this plugin&#8217;s configuration can be seen in &#8220;<font SIZE="-1">SYNOPSIS&#8221;</font> above. For a complete list of all configuration options and their semantics please read &quot;Plugin <tt>&quot;java&quot;</tt>&quot; in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5).</p>
<h2>Overview</h2>
<p>When writing additions for collectd in Java, the underlying C base is mostly hidden from you. All complex data types are converted to their Java counterparts before they&#8217;re passed to your functions. These Java classes reside in the <i>org.collectd.api</i> namespace. </p>
<p> The <i>Java</i> plugin will create one object of each class configured with the <code>LoadPlugin</code> option. The constructor of this class can then register &#8220;callback methods&#8221;, i. e. methods that will be called by the daemon when appropriate. </p>
<p> The available classes are:</p>
<dl>
<dt><code>org.collectd.api.Collectd</code></p>
<dd>All <font SIZE="-1">API</font> functions exported to Java are implemented as static functions of this class. See &#8220;<font SIZE="-1">EXPORTED API FUNCTIONS&#8221;</font> below.</p>
<dt><code>org.collectd.api.OConfigValue</code></p>
<dd>Corresponds to <tt>&quot;oconfig_value_t&quot;</tt>, defined in <i>src/liboconfig/oconfig.h</i>.</p>
<dt><code>org.collectd.api.OConfigItem</code></p>
<dd>Corresponds to <tt>&quot;oconfig_item_t&quot;</tt>, defined in <i>src/liboconfig/oconfig.h</i>.</p>
<dt><code>org.collectd.api.DataSource</code></p>
<dd>Corresponds to <tt>&quot;data_source_t&quot;</tt>, defined in <i>src/plugin.h</i>.</p>
<dt><code>org.collectd.api.DataSet</code></p>
<dd>Corresponds to <tt>&quot;data_set_t&quot;</tt>, defined in <i>src/plugin.h</i>.</p>
<dt><code>org.collectd.api.ValueList</code></p>
<dd>Corresponds to <tt>&quot;value_list_t&quot;</tt>, defined in <i>src/plugin.h</i>.</p>
<dt><code>org.collectd.api.Notification</code></p>
<dd>Corresponds to <tt>&quot;notification_t&quot;</tt>, defined in <i>src/plugin.h</i>.</dl>
<p> In the remainder of this document, we&#8217;ll use the short form of these names, for example <code>ValueList</code>. In order to be able to use these abbreviated names, you need to <code>import</code> the classes.</p>
<h2>Exported Api Functions</h2>
<p>All collectd <font SIZE="-1">API</font> functions that are available to Java plugins are implemented as <i>public static</i> functions of the <code>Collectd</code> class. This makes calling these functions pretty straight forward. For example, to send an error message to the daemon, you&#8217;d do something like this: </p>
<pre> Collectd.logError (&quot;That wasn't chicken!&quot;);</pre>
<p>The following are the currently exported functions.</p>
<h3>registerConfig</h3>
<p>Signature: <i>int</i> <code>registerConfig</code> (<i>String</i> name, <i>CollectdConfigInterface</i> object); </p>
<p> Registers the <code>config</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;config callback&#8221; below.</p>
<h3>registerInit</h3>
<p>Signature: <i>int</i> <code>registerInit</code> (<i>String</i> name, <i>CollectdInitInterface</i> object); </p>
<p> Registers the <code>init</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;init callback&#8221; below.</p>
<h3>registerRead</h3>
<p>Signature: <i>int</i> <code>registerRead</code> (<i>String</i> name, <i>CollectdReadInterface</i> object) </p>
<p> Registers the <code>read</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;read callback&#8221; below.</p>
<h3>registerWrite</h3>
<p>Signature: <i>int</i> <code>registerWrite</code> (<i>String</i> name, <i>CollectdWriteInterface</i> object) </p>
<p> Registers the <code>write</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;write callback&#8221; below.</p>
<h3>registerFlush</h3>
<p>Signature: <i>int</i> <code>registerFlush</code> (<i>String</i> name, <i>CollectdFlushInterface</i> object) </p>
<p> Registers the <code>flush</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;flush callback&#8221; below.</p>
<h3>registerShutdown</h3>
<p>Signature: <i>int</i> <code>registerShutdown</code> (<i>String</i> name, <i>CollectdShutdownInterface</i> object); </p>
<p> Registers the <code>shutdown</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;shutdown callback&#8221; below.</p>
<h3>registerLog</h3>
<p>Signature: <i>int</i> <code>registerLog</code> (<i>String</i> name, <i>CollectdLogInterface</i> object); </p>
<p> Registers the <code>log</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;log callback&#8221; below.</p>
<h3>registerNotification</h3>
<p>Signature: <i>int</i> <code>registerNotification</code> (<i>String</i> name, <i>CollectdNotificationInterface</i> object); </p>
<p> Registers the <code>notification</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;notification callback&#8221; below.</p>
<h3>registerMatch</h3>
<p>Signature: <i>int</i> <code>registerMatch</code> (<i>String</i> name, <i>CollectdMatchFactoryInterface</i> object); </p>
<p> Registers the <code>createMatch</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;match callback&#8221; below.</p>
<h3>registerTarget</h3>
<p>Signature: <i>int</i> <code>registerTarget</code> (<i>String</i> name, <i>CollectdTargetFactoryInterface</i> object); </p>
<p> Registers the <code>createTarget</code> function of <i>object</i> with the daemon. </p>
<p> Returns zero upon success and non-zero when an error occurred. </p>
<p> See &#8220;target callback&#8221; below.</p>
<h3>dispatchValues</h3>
<p>Signature: <i>int</i> <code>dispatchValues</code> (<i>ValueList</i>) </p>
<p> Passes the values represented by the <code>ValueList</code> object to the <tt>&quot;plugin_dispatch_values&quot;</tt> function of the daemon. The &#8220;data set&#8221; (or list of &#8220;data sources&#8221;) associated with the object are ignored, because <tt>&quot;plugin_dispatch_values&quot;</tt> will automatically lookup the required data set. It is therefore absolutely okay to leave this blank. </p>
<p> Returns zero upon success or non-zero upon failure.</p>
<h3>getDS</h3>
<p>Signature: <i>DataSet</i> <code>getDS</code> (<i>String</i>) </p>
<p> Returns the appropriate <i>type</i> or <code>null</code> if the type is not defined.</p>
<h3>logError</h3>
<p>Signature: <i>void</i> <code>logError</code> (<i>String</i>) </p>
<p> Sends a log message with severity <font SIZE="-1"><code>ERROR</code></font> to the daemon.</p>
<h3>logWarning</h3>
<p>Signature: <i>void</i> <code>logWarning</code> (<i>String</i>) </p>
<p> Sends a log message with severity <font SIZE="-1"><code>WARNING</code></font> to the daemon.</p>
<h3>logNotice</h3>
<p>Signature: <i>void</i> <code>logNotice</code> (<i>String</i>) </p>
<p> Sends a log message with severity <font SIZE="-1"><code>NOTICE</code></font> to the daemon.</p>
<h3>logInfo</h3>
<p>Signature: <i>void</i> <code>logInfo</code> (<i>String</i>) </p>
<p> Sends a log message with severity <font SIZE="-1"><code>INFO</code></font> to the daemon.</p>
<h3>logDebug</h3>
<p>Signature: <i>void</i> <code>logDebug</code> (<i>String</i>) </p>
<p> Sends a log message with severity <font SIZE="-1"><code>DEBUG</code></font> to the daemon.</p>
<h2>Registering Callbacks</h2>
<p>When starting up, collectd creates an object of each configured class. The constructor of this class should then register &#8220;callbacks&#8221; with the daemon, using the appropriate static functions in <code>Collectd</code>, see &#8220;<font SIZE="-1">EXPORTED API FUNCTIONS&#8221;</font> above. To register a callback, the object being passed to one of the register functions must implement an appropriate interface, which are all in the <code>org.collectd.api</code> namespace. </p>
<p> A constructor may register any number of these callbacks, even none. An object without callback methods is never actively called by collectd, but may still call the exported <font SIZE="-1">API</font> functions. One could, for example, start a new thread in the constructor and dispatch (submit to the daemon) values asynchronously, whenever one is available. </p>
<p> Each callback method is now explained in more detail:</p>
<h3>config callback</h3>
<p>Interface: <code>org.collectd.api.CollectdConfigInterface</code> </p>
<p> Signature: <i>int</i> <code>config</code> (<i>OConfigItem</i> ci) </p>
<p> This method is passed a <code>OConfigItem</code> object, if both, method and configuration, are available. <code>OConfigItem</code> is the root of a tree representing the configuration for this plugin. The root itself is the representation of the <code>&lt;Plugin&nbsp;<wbr>/&gt;</code> block, so in next to all cases the children of the root are the first interesting objects. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and the plugin will be disabled entirely. </p>
<p> See &#8220;registerConfig&#8221; above.</p>
<h3>init callback</h3>
<p>Interface: <code>org.collectd.api.CollectdInitInterface</code> </p>
<p> Signature: <i>int</i> <code>init</code> () </p>
<p> This method is called after the configuration has been handled. It is supposed to set up the plugin. e. g. start threads, open connections, or check if can do anything useful at all. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and the plugin will be disabled entirely. </p>
<p> See &#8220;registerInit&#8221; above.</p>
<h3>read callback</h3>
<p>Interface: <code>org.collectd.api.CollectdReadInterface</code> </p>
<p> Signature: <i>int</i> <code>read</code> () </p>
<p> This method is called periodically and is supposed to gather statistics in whatever fashion. These statistics are represented as a <code>ValueList</code> object and sent to the daemon using dispatchValues. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and cause an appropriate message to be logged. Currently, returning non-zero does not have any other effects. In particular, Java &#8220;read&#8221;-methods are not suspended for increasing intervals like C &#8220;read&#8221;-functions. </p>
<p> See &#8220;registerRead&#8221; above.</p>
<h3>write callback</h3>
<p>Interface: <code>org.collectd.api.CollectdWriteInterface</code> </p>
<p> Signature: <i>int</i> <code>write</code> (<i>ValueList</i> vl) </p>
<p> This method is called whenever a value is dispatched to the daemon. The corresponding C &#8220;write&#8221;-functions are passed a <tt>&quot;data_set_t&quot;</tt>, so they can decide which values are absolute values (gauge) and which are counter values. To get the corresponding <tt>&quot;List&lt;DataSource&gt;&quot;</tt>, call the <code>getDataSource</code> method of the <code>ValueList</code> object. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and cause an appropriate message to be logged. </p>
<p> See &#8220;registerWrite&#8221; above.</p>
<h3>flush callback</h3>
<p>Interface: <code>org.collectd.api.CollectdFlushInterface</code> </p>
<p> Signature: <i>int</i> <code>flush</code> (<i>int</i> timeout, <i>String</i> identifier) </p>
<p> This method is called when the daemon received a flush command. This can either be done using the <tt>&quot;USR1&quot;</tt> signal (see <i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1)) or using the <i>unixsock</i> plugin (see <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5)). </p>
<p> If <i>timeout</i> is greater than zero, only values older than this number of seconds should be flushed. To signal that all values should be flushed regardless of age, this argument is set to a negative number. </p>
<p> The <i>identifier</i> specifies which value should be flushed. If it is not possible to flush one specific value, flush all values. To signal that all values should be flushed, this argument is set to <i>null</i>. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and cause an appropriate message to be logged. </p>
<p> See &#8220;registerFlush&#8221; above.</p>
<h3>shutdown callback</h3>
<p>Interface: <code>org.collectd.api.CollectdShutdownInterface</code> </p>
<p> Signature: <i>int</i> <code>shutdown</code> () </p>
<p> This method is called when the daemon is shutting down. You should not rely on the destructor to clean up behind the object but use this function instead. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and cause an appropriate message to be logged. </p>
<p> See &#8220;registerShutdown&#8221; above.</p>
<h3>log callback</h3>
<p>Interface: <code>org.collectd.api.CollectdLogInterface</code> </p>
<p> Signature: <i>void</i> <code>log</code> (<i>int</i> severity, <i>String</i> message) </p>
<p> This callback can be used to receive log messages from the daemon. </p>
<p> The argument <i>severity</i> is one of:</p>
<dl>
<dt>&bull;</p>
<dd>org.collectd.api.Collectd.LOG_ERR</p>
<dt>&bull;</p>
<dd>org.collectd.api.Collectd.LOG_WARNING</p>
<dt>&bull;</p>
<dd>org.collectd.api.Collectd.LOG_NOTICE</p>
<dt>&bull;</p>
<dd>org.collectd.api.Collectd.LOG_INFO</p>
<dt>&bull;</p>
<dd>org.collectd.api.Collectd.LOG_DEBUG</dl>
<p> The function does not return any value. </p>
<p> See &#8220;registerLog&#8221; above.</p>
<h3>notification callback</h3>
<p>Interface: <code>org.collectd.api.CollectdNotificationInterface</code> </p>
<p> Signature: <i>int</i> <code>notification</code> (<i>Notification</i> n) </p>
<p> This callback can be used to receive notifications from the daemon. </p>
<p> To signal success, this method has to return zero. Anything else will be considered an error condition and cause an appropriate message to be logged. </p>
<p> See &#8220;registerNotification&#8221; above.</p>
<h3>match callback</h3>
<p>The match (and target, see &#8220;target callback&#8221; below) callbacks work a bit different from the other callbacks above: You don&#8217;t register a match callback with the daemon directly, but you register a function which, when called, creates an appropriate object. The object creating the &#8220;match&#8221; objects is called &#8220;match factory&#8221;. </p>
<p> See &#8220;registerMatch&#8221; above. </p>
<p> <i>Factory object</i> </p>
<p> Interface: <code>org.collectd.api.CollectdMatchFactoryInterface</code> </p>
<p> Signature: <i>CollectdMatchInterface</i> <code>createMatch</code> (<i>OConfigItem</i> ci); </p>
<p> Called by the daemon to create &#8220;match&#8221; objects. </p>
<p> Returns: A new object which implements the <code>CollectdMatchInterface</code> interface. </p>
<p> <i>Match object</i> </p>
<p> Interface: <code>org.collectd.api.CollectdMatchInterface</code> </p>
<p> Signature: <i>int</i> <code>match</code> (<i>DataSet</i> ds, <i>ValueList</i> vl); </p>
<p> Called when processing a chain to determine whether or not a <i>ValueList</i> matches. How values are matches is up to the implementing class. </p>
<p> Has to return one of:</p>
<dl>
<dt>&bull;</p>
<dd><code>Collectd.FC_MATCH_NO_MATCH</code></p>
<dt>&bull;</p>
<dd><code>Collectd.FC_MATCH_MATCHES</code></dl>
<h3>target callback</h3>
<p>The target (and match, see &#8220;match callback&#8221; above) callbacks work a bit different from the other callbacks above: You don&#8217;t register a target callback with the daemon directly, but you register a function which, when called, creates an appropriate object. The object creating the &#8220;target&#8221; objects is called &#8220;target factory&#8221;. </p>
<p> See &#8220;registerTarget&#8221; above. </p>
<p> <i>Factory object</i> </p>
<p> Interface: <code>org.collectd.api.CollectdTargetFactoryInterface</code> </p>
<p> Signature: <i>CollectdTargetInterface</i> <code>createTarget</code> (<i>OConfigItem</i> ci); </p>
<p> Called by the daemon to create &#8220;target&#8221; objects. </p>
<p> Returns: A new object which implements the <code>CollectdTargetInterface</code> interface. </p>
<p> <i>Target object</i> </p>
<p> Interface: <code>org.collectd.api.CollectdTargetInterface</code> </p>
<p> Signature: <i>int</i> <code>invoke</code> (<i>DataSet</i> ds, <i>ValueList</i> vl); </p>
<p> Called when processing a chain to perform some action. The action performed is up to the implementing class. </p>
<p> Has to return one of:</p>
<dl>
<dt>&bull;</p>
<dd><code>Collectd.FC_TARGET_CONTINUE</code></p>
<dt>&bull;</p>
<dd><code>Collectd.FC_TARGET_STOP</code></p>
<dt>&bull;</p>
<dd><code>Collectd.FC_TARGET_RETURN</code></dl>
<h2>Example</h2>
<p>This short example demonstrates how to register a read callback with the daemon: </p>
<pre> import org.collectd.api.Collectd;
 import org.collectd.api.ValueList;
 
 import org.collectd.api.CollectdReadInterface;
 
 public class Foobar implements CollectdReadInterface
 {
 public Foobar ()
 {
 Collectd.registerRead (&quot;Foobar&quot;, this);
 }
 
 public int read ()
 {
 ValueList vl;
 
 /* Do something... */
 
 Collectd.dispatchValues (vl);
 }
 }</pre>
<h2>Plugins</h2>
<p>The following plugins are implemented in <i>Java</i>. Both, the <code>LoadPlugin</code> option and the <code>Plugin</code> block must be inside the <code>&lt;Plugin java&gt;</code> block (see above).</p>
<h3>GenericJMX plugin</h3>
<p>The GenericJMX plugin reads <i>Managed Beans</i> (MBeans) from an <i>MBeanServer</i> using <font SIZE="-1">JMX. JMX</font> is a generic framework to provide and query various management information. The interface is used by Java processes to provide internal statistics as well as by the <i>Java Virtual Machine</i> (<font SIZE="-1">JVM</font>) to provide information about the memory used, threads and so on. </p>
<p> The configuration of the <i>GenericJMX plugin</i> consists of two blocks: <i>MBean</i> blocks that define a mapping of MBean attributes to the XtypesX used by <i>collectd</i>, and <i>Connection</i> blocks which define the parameters needed to connect to an <i>MBeanServer</i> and what data to collect. The configuration of the <i></i><font SIZE="-1"><i>SNMP</i></font><i> plugin</i> is similar in nature, in case you know it. </p>
<p> <i>MBean blocks</i> </p>
<p> <i>MBean</i> blocks specify what data is retrieved from <i>MBeans</i> and how that data is mapped on the <i>collectd</i> data types. The block requires one string argument, a name. This name is used in the <i>Connection</i> blocks (see below) to refer to a specific <i>MBean</i> block. Therefore, the names must be unique. </p>
<p> The following options are recognized within <i>MBean</i> blocks:</p>
<dl>
<dt><code>ObjectName</code> <i>pattern</i></p>
<dd>Sets the pattern which is used to retrieve <i>MBeans</i> from the <i>MBeanServer</i>. If more than one MBean is returned you should use the <code>InstanceFrom</code> option (see below) to make the identifiers unique. </p>
<p> See also: &lt;<a rel="nofollow" href="http://java.sun.com/javase/6/docs/api/javax/management/ObjectName.html">http://java.sun.com/javase/6/docs/api/javax/management/ObjectName.html</a>&gt;</p>
<dt><code>InstancePrefix</code> <i>prefix</i></p>
<dd>Prefixes the generated <i>plugin instance</i> with <i>prefix</i>. <i>(optional)</i></p>
<dt><code>InstanceFrom</code> <i>property</i></p>
<dd>The <i>object names</i> used by <font SIZE="-1">JMX</font> to identify <i>MBeans</i> include so called <i>XpropertiesX</i> which are basically key-value-pairs. If the given object name is not unique and multiple MBeans are returned, the values of those properties usually differ. You can use this option to build the <i>plugin instance</i> from the appropriate property values. This option is optional and may be repeated to generate the <i>plugin instance</i> from multiple property values.</p>
<dt><code>&lt;value /&gt;</code> blocks</p>
<dd>The <i>value</i> blocks map one or more attributes of an <i>MBean</i> to a value list in <i>collectd</i>. There must be at least one Value block within each <i>MBean</i> block.</p>
<dl>
<dd>
<dl>
<dt><code>Type</code> type</p>
<dd>Sets the data set used within <i>collectd</i> to handle the values of the <i>MBean</i> attribute.</p>
<dt><code>InstancePrefix</code> <i>prefix</i></p>
<dd>Works like the option of the same name directly beneath the <i>MBean</i> block, but sets the type instance instead. <i>(optional)</i></p>
<dt><code>InstanceFrom</code> <i>prefix</i></p>
<dd>Works like the option of the same name directly beneath the <i>MBean</i> block, but sets the type instance instead. <i>(optional)</i></p>
<dt><code>PluginName</code> <i>name</i></p>
<dd>When set, overrides the default setting for the <i>plugin</i> field (<tt>&quot;GenericJMX&quot;</tt>).</p>
<dt><code>Table</code> <code>true</code>|<code>false</code></p>
<dd>Set this to true if the returned attribute is a <i>composite type</i>. If set to true, the keys within the <i>composite type</i> is appended to the <i>type instance</i>.</p>
<dt><code>Attribute</code> <i>path</i></p>
<dd>Sets the name of the attribute from which to read the value. You can access the keys of composite types by using a dot to concatenate the key name to the attribute name. For example: Xattrib0.key42X. If <code>Table</code> is set to <code>true</code> <i>path</i> must point to a <i>composite type</i>, otherwise it must point to a numeric type.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<p> <i>Connection blocks</i> </p>
<p> Connection blocks specify <i>how</i> to connect to an <i>MBeanServer</i> and what data to retrieve. The following configuration options are available:</p>
<dl>
<dt><code>Host</code> <i>name</i></p>
<dd>Host name used when dispatching the values to <i>collectd</i>. The option sets this field only, it is <i>not</i> used to connect to anything and doesn&#8217;t need to be a real, resolvable name.</p>
<dt><code>ServiceURL</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd>Specifies how the <i>MBeanServer</i> can be reached. Any string accepted by the <i>JMXServiceURL</i> is valid. </p>
<p> See also: &lt;<a rel="nofollow" href="http://java.sun.com/javase/6/docs/api/javax/management/remote/JMXServiceURL.html">http://java.sun.com/javase/6/docs/api/javax/management/remote/JMXServiceURL.html</a>&gt;</p>
<dt><code>User</code> <i>name</i></p>
<dd>Use <i>name</i> to authenticate to the server. If not configured, XmonitorRoleX will be used.</p>
<dt><code>Password</code> <i>password</i></p>
<dd>Use <i>password</i> to authenticate to the server. If not given, unauthenticated access is used.</p>
<dt><code>InstancePrefix</code> <i>prefix</i></p>
<dd>Prefixes the generated <i>plugin instance</i> with <i>prefix</i>. If a second <i>InstancePrefix</i> is specified in a referenced <i>MBean</i> block, the prefix specified in the <i>Connection</i> block will appear at the beginning of the <i>plugin instance</i>, the prefix specified in the <i>MBean</i> block will be appended to it.</p>
<dt><code>Collect</code> <i>mbean_block_name</i></p>
<dd>Configures which of the <i>MBean</i> blocks to use with this connection. May be repeated to collect multiple <i>MBeans</i> from this server.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5), <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5)</p>
<h2>Author</h2>
<p>Florian Forster &lt;octo at collectd.org&gt;</p>
