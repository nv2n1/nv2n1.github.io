---
title: "amanda-devices(7)"
name: "amanda-devices"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-devices/"
description: "amanda-devices – Configuring and Using Amanda Devices"
---

<p>amanda-devices &#8211; Configuring and Using Amanda Devices</p>
<h2>Description</h2>
<p>The Device API specifies a generic interface between Amanda and storage devices such as tapes or disks. This manual page describes the device drivers included with Amanda. </p>
<p> This is a <i>user-level</i> description of the API, and does not address details that are only of concern to developers. For that purpose, consult the Amanda source code and <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a> </p>
<p> The term &quot;device driver&quot; describes the software that can communicate with some kind of backend storage, e.g., a tape driver. A &quot;device&quot; is the storage element itself, usually a piece of hardware. When discussing a device and its driver as a unit, the term &quot;device&quot; is sometimes also used to refer to the combination of device and driver.</p>
<h2>Specifying Devices</h2>
<p>Device names take the form <i>TYPE:NODE</i>, where <i>TYPE</i> selects a device driver, and <i>NODE</i> provides further information to that driver. The syntax for each device driver is given in the corresponding section below. </p>
<p> Devices can be described in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) with &quot;device&quot; sections, e.g., </p>
<pre>define device top_drive {
 tapedev &quot;tape:/dev/nst0&quot;
 device-property &quot;BLOCK_SIZE&quot; &quot;131072&quot;
}</pre>
<p>Such a device defininition creates a device &quot;alias&quot;, in this case named <i>top_drive</i>, which can then be named in the global <i>tapedev</i> or <i>tpchanger</i> parameter: </p>
<pre>tapedev &quot;top_drive&quot;</pre>
<p>The global <i>tapedev</i> parameter can also specify a literal device name. For example, </p>
<pre>tapedev &quot;file:/amdisks&quot;</pre>
<p>is equivalent to </p>
<pre>tapedev &quot;default&quot;
define device default {
 tapedev &quot;file:/amdisks&quot;
}</pre>
<p>Note that, in both cases, the specified devices are actually accessed through the <i>chg-single</i> changer driver; see <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7) for more information. </p>
<p> Device properties specified outside of any device definition apply to all devices. This syntax is provided mainly for backward compatibility, and for simple Amanda configurations. Note that there is no way to provide properties specific to a device without defining a device alias. </p>
<p> See <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7) for details on how devices are configured, and in particular on how device properties are specified. See <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) for more information on Amanda configuration in general. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> There is no way to reset a device property to its default value. </p>
</dl>
<h2>Properties</h2>
<p>Device drivers use <i>properties</i> as a generic means to interact with other parts of Amanda. Some properties are set by the device driver and used by Amanda to determine how its devices should be used. Other properties can be set by Amanda or by the user to influence the driver&#8217;s behavior. Properties are set for a particular device, so that if you have two tape devices, they will not share property values. </p>
<p> Properties are specified in <i>amanda.conf</i> with the <i>device-property</i> parameter. The syntax looks like this: </p>
<pre>device-property &quot;FROBNICATOR_PATH&quot; &quot;/var/frobd/state&quot;
device-property &quot;BYTES_PER_FORTNIGHT&quot; &quot;128k&quot;
device-property &quot;USE_QUBITS&quot; &quot;no&quot;</pre>
<p>Both the property name and the property value are always quoted. Property names, like Amanda configuration parameters, are not case-sensitive, and &#8211; (dash) and _ (underscore) may be used interchangeably. String values are given as simple strings, like FROBNICATOR_PATH in the example above. Integer values can be specified with any of the suffixes given in the &quot;VALUE SUFFIXES&quot; section of <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), like BYTES_PER_FORTNIGHT, above. Boolean values can be specified using the same names as in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), like USE_QUBITS, above. Some properties have special formats, as described below. </p>
<p> Some properties are set based on other configuration values, such as tapetype parameters. These special cases are detailed under the appropriate property, below. </p>
<p> The order in which device properties are set is as follows: </p>
<dl>
<dd>1. Tapetype parameters (including length, blocksize, and readblocksize) are translated into device properties and set accordingly.</dl>
<dl>
<dd>2. Device properties from any device-property configuration parameters are set, in the order they appear in the configuration file.</dl>
<p> Properties described as read-only are not accessible to users. They are listed here for completeness.</p>
<h3>Common Properties</h3>
<p>Note that some of these properties are currently unused, and present only for future expansion. Not all devices implement all of these properties. </p>
<p> APPENDABLE</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This boolean property indicates whether this device supports appending data to volumes.</dl>
<p> BLOCK_SIZE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This property gives the block size, in bytes, that will be used to write to the device.&nbsp;<wbr>&nbsp;<wbr>The usual suffixes&nbsp;<wbr>(&quot;kbytes&quot;, etc.)&nbsp;<wbr>are allowed.&nbsp;<wbr>&nbsp;<wbr>The tapetype parameter&nbsp;<wbr><i>blocksize</i>&nbsp;<wbr>sets this property.</dl>
<p> CANONICAL_NAME</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property contains the full canonical name for this device.&nbsp;<wbr>&nbsp;<wbr>This name may not be the same as the user-supplied name, but is a valid name by which to access this device.</dl>
<p> COMMENT</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This string property is entirely for the user&#8217;s convenience.&nbsp;<wbr>&nbsp;<wbr>It is supported by all devices, but no device interprets its value in any way.</dl>
<p> COMPRESSION</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property represents the compression status of the device, and can be used to enable and disable such compression.&nbsp;<wbr>&nbsp;<wbr>This applies mostly to tape devices, although many tape devices do not support setting compression from software.</dl>
<p> COMPRESSION_RATE</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property gives the compression rate, as a decimal ratio.&nbsp;<wbr>&nbsp;<wbr>It may be a measured value over some unspecified period or a simple estimate.</dl>
<p> CONCURRENCY</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property indicates the level of concurrent access that this device supports.</dl>
<p> FULL_DELETION</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property indicates whether the device supports erasing the entire volume.&nbsp;<wbr>&nbsp;<wbr>Aside from S3 and VFS, most devices cannot support this feature.</dl>
<p> LEOM</p>
<dl>
<dd>(read-write) If this property is true, then the device can detect an EOM condition before actually running out of space, allowing Amanda to forgo caching parts while writing. For some devices, it is necessary to override the conservative default value of this property.</dl>
<p> MAX_BLOCK_SIZE</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property gives the maximum block size this device can support.&nbsp;<wbr>&nbsp;<wbr>See BLOCK SIZES, below.</dl>
<p> MEDIUM_ACCESS_TYPE</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property gives the type of the media in the device: read only, WORM&nbsp;<wbr>(Write Once, Read Many), read/write, or write only.&nbsp;<wbr>&nbsp;<wbr>Write-only devices do not support recovery, but the data are not necessarily thrown out.</dl>
<p> MIN_BLOCK_SIZE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This property gives the minimum block size this device can support.&nbsp;<wbr>&nbsp;<wbr>See BLOCK SIZES, below.</dl>
<p> MAX_VOLUME_USAGE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>On devices that support it, this property will limit the total amount of data written to a volume;&nbsp;<wbr>attempts to write beyond this point will cause the device to simulate&nbsp;<wbr>&quot;out of space.&quot;&nbsp;<wbr>&nbsp;<wbr>Zero means no limit.&nbsp;<wbr>&nbsp;<wbr>The tapetype parameter&nbsp;<wbr><i>length</i>&nbsp;<wbr>sets this property.</dl>
<p> ENFORCE_MAX_VOLUME_USAGE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>If this property is false, limit set by MAX_VOLUME_USAGE property&nbsp;<wbr>(and thus the tapetype LENGTH parameter)&nbsp;<wbr>will not be verified while writing to device, allowing the volume to expand without limit. If this property is true, then MAX_VOLUME_USAGE willbe enforced, limiting the total size of the volume. This property is not available on all devices;&nbsp;<wbr>see below.</dl>
<p> PARTIAL_DELETION</p>
<dl>
<dd>&nbsp;<wbr>(read-only)&nbsp;<wbr>This property indicates whether the device supports deletion of specific files.&nbsp;<wbr>&nbsp;<wbr>Aside from linear tapes and S3, most devices can support this feature.&nbsp;<wbr>&nbsp;<wbr>It is currently unused by Amanda.</dl>
<p> STREAMING</p>
<dl>
<dd>(read-only) This property gives the streaming requirement for this device. For example, tape drives often require a steady supply of data to avoid shoe-shining, while disk devices have no such requirement. Streaming is accomplished by buffering <code>device-output-buffer-size</code> bytes of data. The allowed values are &quot;none&quot; (no streaming buffer necessary), &quot;required&quot; (fill the buffer before starting to write), or &quot;desired&quot; (fill the buffer before starting to write, and if the buffer becomes empty, stop writing until it is completely full again).</dl>
<p> VERBOSE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>If this boolean property is set, then the device will produce verbose debugging output.&nbsp;<wbr>&nbsp;<wbr>This property is not recognized by most devices.</dl>
<h3>Block Sizes</h3>
<p>Amanda writes device data in blocks. On most devices the block boundaries are embedded in the media along with the data itself, so subsequent reads must use the same block sizes. On tape devices, the block size is dictated by the capabilities of the hardware &#8212; buffer sizes, physical format, and so on. </p>
<p> Amanda has historically supported a single, fixed block size &#8212; usually 32k. The Device API adds the ability to specify a block size at runtime, using the BLOCK_SIZE property. Devices provide MIN_BLOCK_SIZE and MAX_BLOCK_SIZE as a guide to the range of acceptable block sizes. Note that this does not imply that all sizes in the range MIN_BLOCK_SIZE &#8211; MAX_BLOCK_SIZE are available &#8212; the device may require that block sizes are even multiples of some power of two, for example. Consult the documentation for your hardware and operating system for more information. </p>
<p> Most devices are flexible enough to read a volume using a different block size than that with which it was written. This can be useful when handling old volumes written with a smaller blocksize, or volumes of unknown blocksize. Unfortunately, some tape devices do not detect oversized blocks correctly, and may lose data if the configured block size is smaller than the volume&#8217;s block size. The tape device driver has a READ_BLOCK_SIZE property which specifies the minimum buffer size that will be allocated for reads from tape. If the hardware supports it, setting this property allows Amanda to correctly read from tapes written with any blocksize less than or equal to READ_BLOCK_SIZE. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The RAIT device does not support flexible block sizes, as its parity algorithm requires that all child devices have the same, fixed block size. </p>
</dl>
<h3>Leom Detection</h3>
<p>Some Amanda devices can detect end-of-medium (running out of space on the device) before it occurs. This early warning is referred to as logical EOM, and where it is supported Amanda can operate more efficiently, since the possibility for data loss is reduced. </p>
<p> The boolean LEOM property indicates whether or not a particular device supports LEOM detection. The sections below also describe the degree of support.</p>
<h2>Devices</h2>
<p>This section lists the device drivers included with Amanda, and basic instructions for using them. For complete How-To information, consult the Amanda wiki at <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a></p>
<h3>Null Device</h3>
<pre>tapedev &quot;null:&quot;</pre>
<p>The null device driver only supports writing, and discards all data. It is generally only useful for testing purposes.</p>
<h3>RAIT Device</h3>
<pre>tapedev &quot;rait:tape:/dev/rmt/tps0d{4,5,6}n&quot;</pre>
<p>The RAIT device driver mirrors or stripes data over multiple &quot;child&quot; devices. The child devices are specified using a shell-like syntax, where alternatives are enclosed in braces and separated by commas. Braces and commas can be escaped with a backslash. Note that the backslash itself must be escaped in most contexts. For example: </p>
<pre>tapedev &quot;rait:{file:/var/amanda/vtapes,tape:/dev/nst0}&quot;
tapedev &quot;rait:{comma-dev:foo\,bar,brace-dev:foo\}bar}&quot; # quoting</pre>
<p>If the braces contain a numeric range separated with two dots, that range will be filled in sequentially. If the first number has a leading zero, then the results will be zero-padded to the maximum length. For example: </p>
<pre>tapedev &quot;rait:file:/var/amanda/vtapes/drive{01..04}&quot;</pre>
<p>With two child devices, the RAIT device driver mirrors data such that the two devices contain identical data and can be used singly for recovery. With more than two devices, the RAIT device &quot;stripes&quot; data across all but one device and writes a parity block to the final device, usable for data recovery in the event of a device or volume failure. The RAIT device scales its blocksize as necessary to match the number of children that will be used to store data. </p>
<p> When a child device is known to have failed, the RAIT device should be reconfigured to replace that device with the text &quot;ERROR&quot;, e.g., </p>
<pre>tapedev &quot;rait:{tape:/dev/st0,ERROR,tape:/dev/st2}&quot;</pre>
<p>This will cause the RAIT device to start up in degraded mode, reconstructing the data from the missing device. </p>
<p> Like ordinary RAID drivers, the RAIT device driver can automatically enter degraded mode when one of its child devices fails. However, the RAIT device cannot automatically recover from any write error nor write any data in degraded mode. When reading, certain errors may be fatal (rather than causing degraded mode). And in any case, labels on all volumes must initially match (labeled or otherwise). If you have lost one volume from a set, explicitly start the device in degraded mode as described above. </p>
<p> This device can detect LEOM if and only if all of the child devices can detect LEOM.</p>
<h3>Child Device Block Sizes</h3>
<p>The RAIT device driver requires that all of its child devices use the same block size. If no block sizes are specified, the driver selects the block size closest to 32k that is within the MIN_BLOCK_SIZE &#8211; MAX_BLOCK_SIZE range of all child devices, and calculates its own blocksize according to the formula <i>rait_blocksize = child_blocksize * (num_children &#8211; 1)</i>. If a block size is specified for the RAIT device, then it calculates its child block sizes according to the formula <i>child_blocksize = rait_blocksize / (num_children &#8211; 1)</i>. Either way, it sets the BLOCK_SIZE property of each child device accordingly.</p>
<h3>S3 Device</h3>
<pre>tapedev &quot;s3:foocorp-backups/DailySet1-&quot;
device-property &quot;S3_ACCESS_KEY&quot; &quot;MYACCESSKEY&quot;
device-property &quot;S3_SECRET_KEY&quot; &quot;MYSECRETKEY&quot;</pre>
<p>The S3 device driver uploads data to the Amazon S3 &quot;storage cloud&quot;. Its device name is a slash-sparated combination of bucket name and prefix: &quot;s3:BUCKET/PREFIX&quot;. Since buckets must be unique across all Amazon S3 users, and since the number of buckets allowed to each user is limited, the driver can store multiple Amanda volumes in a single S3 bucket, distinguished by prefix. The prefix and slash can be omitted if they are not needed: &quot;s3:BUCKET&quot;. </p>
<p> The access and secret keys used to authenticate to Amazon S3 are provided as properties. </p>
<p> The S3 device driver stores each block in a distinct S3 object. Due to high HTTP overhead for each request, use of larger than normal block sizes (&gt; 1 megabyte) is recommended with the S3 device. </p>
<p> Amanda automatically creates a bucket when writing, if the bucket doesn&#8217;t already exist. At that time, it specifies where Amazon should store the data based on the S3_BUCKET_LOCATION property. If this property is not set, Amazon&#8217;s default value (equivalent to &quot;*&quot;) is used. The bucket location has both billing and legal concerns, so you are encouraged to consult Amazon&#8217;s documentation for details. </p>
<p> Amazon does not permit changes to bucket locations, so this is a permanent specification. If the bucket already exists and the property is set, then Amanda checks the property against the location of the bucket, and produces an error if they do not match. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If a location constraint is set, the bucket name must consist only of lower-case letters, numbers, dashes, and dots. </p>
</dl>
<p> This driver supports the VERBOSE property, but use it carefully &#8212; it produces a great deal of output, and may cause spurious failures by filling your debug log partition. Its logging is generally only useful for developers chasing down a problem in communications with Amazon&#8217;s servers. </p>
<p> Since Amazon storage is unlimited, the device never encounteres EOM, so LEOM detection is trivially enabled for this device. </p>
<p> This driver supports the ENFORCE_MAX_VOLUME_USAGE property. Default value is false. See COMMON_PROPERTIES, above.</p>
<h3>Device-Specific Properties</h3>
<p>In addition to the common properties, the S3 device supports the properties listed in this section. </p>
<p> Most Amanda devices work just fine without any properties, but not the S3 device. A typical S3 configuration will have an access key and secret key specified: </p>
<pre>device-property &quot;S3_ACCESS_KEY&quot; &quot;27D3B8C6C4E7AA423C2B37C72A0D22C8&quot;
device-property &quot;S3_SECRET_KEY&quot; &quot;agphc2Q7Zmxragphc2RmO2xragpzZGY7a2xqCgr&quot;</pre>
<p>CLIENT_ID</p>
<dl>
<dd>(read-write) The client_id for oauth2.</dl>
<p> CLIENT_SECRET</p>
<dl>
<dd>(read-write) The client_secret for oauth2.</dl>
<p> CREATE-BUCKET</p>
<dl>
<dd>(read-write) Default: yes. If amanda create/delete the bucket.</dl>
<p> REFRESH_TOKEN</p>
<dl>
<dd>(read-write) The refresh-token for oauth2.</dl>
<p> MAX_RECV_SPEED</p>
<dl>
<dd>(read-write) Maximum speed, in bytes per second, that this device will receive data from S3. If the average speed exceeds this value, the device will stop reading long enough to bring the average below this value.</dl>
<p> MAX_SEND_SPEED</p>
<dl>
<dd>(read-write) Maximum speed, in bytes per second, that this device will send data to S3. If the average speed exceeds this value, the device will stop writing long enough to bring the average below this value.</dl>
<p> S3_MULTI_DELETE</p>
<dl>
<dd>(read-write) If the server support the multi delete protocol (only Amazon S3), default is &quot;YES&quot;. If it fail, it revert to single delete.</dl>
<p> NB_THREADS_BACKUP</p>
<dl>
<dd>(read-write) The number of thread that send data to the s3 device, higher value can provide more throutput.</dl>
<p> NB_THREADS_RECOVERY</p>
<dl>
<dd>(read-write) The number of thread that read data from the s3 device, higher value can provide more throutput.</dl>
<p> OPENSTACK_SWIFT_API</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Deprecated, set&nbsp;<wbr>&quot;STORAGE_API to&nbsp;<wbr>&quot;SWIFT-1.0&quot;.</dl>
<p> PROXY</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>The proxy hostname or IP in the format&nbsp;<wbr>&quot;host[:port]&quot;.</dl>
<p> PASSWORD</p>
<dl>
<dd>(read-write) The password (for swift v2).</dl>
<p> PROJECT-ID</p>
<dl>
<dd>(read-write) The projectid (for google).</dl>
<p> REUSE-CONNECTION</p>
<dl>
<dd>(read-write) Default: YES. Set it to &quot;NO&quot; if reusing a connection cause some bug, this is sometime the case with big block size.</dl>
<p> S3_ACCESS_KEY</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This property gives the Amazon S3 access key used to access the service.</dl>
<p> S3_BUCKET_LOCATION</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Location constraint for buckets on Amazon S3. As of this writing, it can be set to &quot;*&quot; (US Standard, i.e. lowest-latency choice of US East or West), &quot;us-west-1&quot; (US West, Northern California), &quot;EU&quot; (European Union), or &quot;ap-southeast-1&quot; (Asia Pacific). See : <a rel="nofollow" href="http://docs.amazonwebservices.com/general/latest/gr/index.html?rande.html">http://docs.amazonwebservices.com/general/latest/gr/index.html?rande.html</a> for the most up-to-date list.</dl>
<p> SSL_CA_INFO</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Path to CA certificate to use to verify the identity of the S3 server. Only applicable when SSL/TLS is in use. The certificate should be in PEM format if OpenSSL or GnuTLS is being used with libcurl. Multiple certificates can be bundled together simply by concatenating them. If NSS is being used, then it is the directory that the database resides in. The value is passed to <a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3) as CURLOPT_CAINFO.</dl>
<p> S3_HOST</p>
<dl>
<dd>(read-write) The host name to connect, in the form &quot;hostname:port&quot; or &quot;ip:port&quot;, default is &quot;s3.amazonaws.com&quot;</dl>
<p> S3_SECRET_KEY</p>
<dl>
<dd>(read-write) This property gives the Amazon S3 secret key used to access the service.</dl>
<p> S3_SERVER_SIDE_ENCRYPTION</p>
<dl>
<dd>(read-write) Set to the server side encryption algorithm to use. There is actually only one algorithm, it is &quot;AES256&quot;. The encryption is done by Amazon on their server. See : <a rel="nofollow" href="http://docs.amazonwebservices.com/AmazonS3/latest/API/index.html?RESTObjectPUT.html">http://docs.amazonwebservices.com/AmazonS3/latest/API/index.html?RESTObjectPUT.html</a> for the most up-to-date list.</dl>
<p> S3_SERVICE_PATH</p>
<dl>
<dd>(read-write) A path to add at the beginning of the URL.</dl>
<p> S3_STORAGE_CLASS</p>
<dl>
<dd>(read-write) Storage class for new objects, currently one of &quot;STANDARD&quot; (the default) or &quot;REDUCED_REDUNDANCY&quot; (cheaper, but less redundant). See : <a rel="nofollow" href="http://docs.amazonwebservices.com/AmazonS3/latest/dev/index.html?DataDurability.html">http://docs.amazonwebservices.com/AmazonS3/latest/dev/index.html?DataDurability.html</a> for the most up-to-date list.</dl>
<p> S3_SSL</p>
<dl>
<dd>(read-write) Whether or not to use SSL/TLS to secure communications with Amazon S3.</dl>
<p> S3_SUBDOMAIN</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Whether or not to use subdomain hostname.</dl>
<p> S3_USER_TOKEN</p>
<dl>
<dd>(read-write) This property specifies the user token for Amanda Enterprise Edition customers.</dl>
<p> STORAGE_API</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Which API to use for the cloud: </p>
<pre> S3 Amanzon S3 api
 SWIFT-1.0 Openstack swift v1.0
 SWIFT-2.0 Openstack swift v2.0
 OAUTH2 Google
 CASTOR Caringo CAStor</pre>
</dl>
<p> TENANT_ID</p>
<dl>
<dd>(read-write) The tenant_id (for swift v2).</dl>
<p> TENANT_NAME</p>
<dl>
<dd>(read-write) The tenant_name (for swift v2).</dl>
<p> USERNAME</p>
<dl>
<dd>(read-write) The username (for swift v2).</dl>
<p> VERBOSE</p>
<dl>
<dd>(read-write) If true, verbose data about each HTTP transaction is sent to the debug log.</dl>
<h3>S3 Url</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>SSL&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>&nbsp;<wbr>SUBDOMAIN:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://bucket.host/service_path/file">https://bucket.host/service_path/file</a><br />
&nbsp;<wbr>&nbsp;<wbr>SSL&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>!SUBDOMAIN:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://host/service_path/bucket/file">https://host/service_path/bucket/file</a><br />
&nbsp;<wbr>!SSL&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>&nbsp;<wbr>SUBDOMAIN:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://bucket.host/service_path/file">http://bucket.host/service_path/file</a><br />
&nbsp;<wbr>!SSL&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>!SUBDOMAIN:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://host/service_path/bucket/file">http://host/service_path/bucket/file</a></p>
<h3>Tape Device</h3>
<pre>tapedev &quot;tape:/dev/nst0&quot;</pre>
<p>The tape device driver interacts with a tape drive. The device uses the operating system&#8217;s built-in tape support, which is generally similar to that available via the command-line utilities <a href="/docs/linux/man/1-dd/">dd</a>(1) and <a href="/docs/linux/man/1-mt/">mt</a>(1). </p>
<p> The tape device name should specify a path to the operating system&#8217;s device file. </p>
<p> There is no simple way to determine whether a particular system (operating system and tape hardware) supports LEOM, so as a safe default the tape device has LEOM detection disabled. However, on modern hardware and common operating systems (Linux, *BSD, and Solaris, at least), LEOM support is functional. On these systems, enable LEOM by setting the LEOM property to &quot;true&quot; at the appropriate place in the Amanda configuration.</p>
<h3>Device-Specific Properties</h3>
<p>Most of these properties are automatically detected, but can be overridden in the configuration file if the autodetection fails. Note that tape drives are required to at least support the MTREW (rewind) operation; all other operations can be emulated with the MTREW and read data operations. </p>
<p> BROKEN_GMT_ONLINE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Set this boolean property if the system&#8217;s GMT_ONLINE macro gives incorrect results.&nbsp;<wbr>&nbsp;<wbr>This is currently true for the Linux IDE-TAPE driver.</dl>
<p> BSF</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device<br />
&nbsp;<wbr>driver may execute the MTBSF operation&nbsp;<wbr>(backward seek file).</dl>
<p> BSF_AFTER_EOM</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device<br />
&nbsp;<wbr>driver should execute an MTBSF&nbsp;<wbr>(backward seek file)&nbsp;<wbr>operation after<br />
&nbsp;<wbr>MTEOM&nbsp;<wbr>(seek to end of recorded data)&nbsp;<wbr>in order to append.</dl>
<p> BSR</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device<br />
&nbsp;<wbr>driver may use the MTBSR operation&nbsp;<wbr>(backward seek record).</dl>
<p> EOM</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device<br />
&nbsp;<wbr>driver may use the MTEOM command&nbsp;<wbr>(seek to end of recorded data).</dl>
<p> FINAL_FILEMARKS</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This integer property gives the number of filemarks that should be written at EOD.&nbsp;<wbr>&nbsp;<wbr>It is usually 1 or 2.</dl>
<p> FSF</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device driver may use the MTFSF operation&nbsp;<wbr>(forward seek file).</dl>
<p> FSF_AFTER_FILEMARK</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device driver needs a FSF to go the next file after the filemark is read. Default to&nbsp;<wbr>&quot;TRUE&quot;&nbsp;<wbr>on Solaris and&nbsp;<wbr>&quot;FALSE&quot;&nbsp;<wbr>on all others machines.</dl>
<p> FSR</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This boolean property specifies whether the device driver may use the MTFSR operation&nbsp;<wbr>(forward seek record).</dl>
<p> NONBLOCKING_OPEN</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Set this boolean property to&nbsp;<wbr>&quot;true&quot;&nbsp;<wbr>if O_NONBLOCK must be used on the open call. Default to&nbsp;<wbr>&quot;true&quot;&nbsp;<wbr>on Linux and&nbsp;<wbr>&quot;false&quot;&nbsp;<wbr>on all others machines. Without it, Linux wait for a few seconds if no tape are loaded. Solaris have strange error it is set to&nbsp;<wbr>&quot;yes&quot;.</dl>
<p> READ_BLOCK_SIZE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This property&nbsp;<wbr>(previously known as&nbsp;<wbr><i>READ_BUFFER_SIZE</i>)&nbsp;<wbr>specifies the block size that will be used for reads;&nbsp;<wbr>this should be large enough to contain any block that may be read from the device&nbsp;<wbr>(for example, from a tape containing variable-sized blocks), and must be larger than BLOCK_SIZE.&nbsp;<wbr>&nbsp;<wbr>This property is most often used when overwriting tapes using a new, smaller block size.<br />
&nbsp;<wbr>The tapetype parameter&nbsp;<wbr><i>READBLOCKSIZE</i>&nbsp;<wbr>sets this property.&nbsp;<wbr>&nbsp;<wbr>See BLOCK SIZES, above.</dl>
<h3>NDMP Device</h3>
<pre>tapedev &quot;ndmp:my.filer.com:10000@st1&quot;
device-property &quot;NDMP_USERNAME&quot; &quot;jimmy&quot;
device-property &quot;NDMP_PASSWORD&quot; &quot;thelock&quot;</pre>
<p>This device enables Amanda to communicate with a tape service on an NDMP server. The device name specifies the hostname and optionally the TCP port of the NDMP server, followed by the name of the tape device on the server (<code>st1</code> in the example above). </p>
<p> This device supports LEOM detection.</p>
<h3>Device-Specific Properties</h3>
<p>The properties <code>NDMP_USERNAME</code> and <code>NDMP_PASSWORD</code> set the username and password with which to access the NDMP server. The default for both is &quot;ndmp&quot;. </p>
<p> INDIRECT</p>
<dl>
<dd>(read-write) Set to &quot;yes&quot; if the ndmp server doesn&#8217;t allow to set a window length to 0. The default is &quot;no&quot;.</dl>
<p> NDMP_AUTH</p>
<dl>
<dd>(read-write) Authentication method to use to connect to the NDMP server. One of &quot;md5&quot; (default), &quot;text&quot;, &quot;none&quot; (for an empty authentication attempt) or &quot;void&quot; (for no authentication attempt at all).</dl>
<p> NDMP_PASSWORD</p>
<dl>
<dd>(read-write) Password for md5 or text authentications.</dl>
<p> NDMP_USERNAME</p>
<dl>
<dd>(read-write) Username for md5 or text authentications.</dl>
<p> READ_BLOCK_SIZE</p>
<dl>
<dd>(read-write) This property specifies the block size that will be used for reads; this should be large enough to contain any block that may be read from the device and must be larger than BLOCK_SIZE. See BLOCK_SIZES, above.</dl>
<h3>VFS Device</h3>
<pre>tapedev &quot;file:/path/to/vtape&quot;</pre>
<p>The VFS device driver stores data on a UNIX filesystem. Note that although one typically uses the VFS device driver to store data on hard disks, the driver does not interface with any hardware on a block level. </p>
<p> The device name specifies a path to a directory which must exist and contain a &quot;data/&quot; subdirectory. Each tape file is stored as a distinct file in this directory, the name of which reflects the Amanda header in the tape file. Block boundaries are not maintained: the driver supports reads of arbitrary size, regardless of the blocksize used to write the data. </p>
<p> This device supports LEOM detection. LEOM will be indicated when the MAX_VOLUME_USAGE is nearly met, or when the filesystem is nearly out of space. The latter circumstance is detected by monitoring the available space on the filesystem, and this monitoring can be disabled with the MONITOR_FREE_SPACE property. Note that the device cannot detect other circumstances that may cause a write to fail, such as a filesystem quota. LEOM detection can be disabled by setting the LEOM property to false. </p>
<p> This device supports the ENFORCE_MAX_VOLUME_USAGE property. Default value is true. See COMMON PROPERTIES, above.</p>
<h3>Device-Specific Properties</h3>
<p>MONITOR_FREE_SPACE</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (read-write) This property controls whether the device will monitor<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> the filesystem&#8217;s free space to detect a full filesystem before an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> error occurs, and defaults to true. The monitoring operation works on<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> most filesystems, but if it causes problems, use this property to<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> disable it.
</dl>
<h3>DVD-RW Device</h3>
<pre>tapedev &quot;dvdrw:/var/cache/amanda/dvd-cache:/dev/scd0&quot;
device-property &quot;DVDRW_MOUNT_POINT&quot; &quot;/media/dvd&quot;
device-property &quot;DVDRW_KEEP_CACHE&quot; &quot;false&quot;
device-property &quot;DVDRW_UNLABELLED_WHEN_UNMOUNTABLE&quot; &quot;true&quot;</pre>
<p>The DVD-RW device driver reads and writes optical media such as DVDs and CDs. The device name must specify a cache directory for data to be temporarily stored, followed by the operating system name for the optical drive. The cache directory must contain a &quot;data/&quot; subdirectory. </p>
<p> The DVDRW_MOUNT_POINT property is required, and specifies a directory where the optical media can be mounted. This directory must be configured to enable non-root users to mount the optical media. On Linux, that means a line similar to the following in /etc/fstab: </p>
<pre>/dev/scd0 /media/dvd auto ro,user,noauto 0 0</pre>
<p>Note the &quot;user&quot; option. </p>
<p> When writing data, the device acts as a VFS device using the given cache directory. On completion of writing the tape, the cache directory is written to optical media. The DVDRW_KEEP_CACHE property controls whether the cache contents are immediately deleted. When reading, the optical media is first mounted and read as a VFS device. </p>
<p> Attempting to mount unformatted media or media that is formatted but contains no filesystem will usually result in an error. The boolean DVDRW_UNLABELLED_WHEN_UNMOUNTABLE property specifies whether media that cannot be mounted should be treated as an empty, unlabelled volume when attempting to read the volume label. It is necessary to set this property to &quot;true&quot; when labelling such media. </p>
<p> This device does not support LEOM detection.</p>
<h3>Device-Specific Properties</h3>
<p>The properties DVDRW_GROWISOFS_COMMAND, DVDRW_MOUNT_COMMAND and DVDRW_UMOUNT_COMMAND specify alternative commands for writing, mounting and unmounting optical media. The default is to find the programs using the PATH environment variable. </p>
<p> The CDRW device supports all of the properties of the VFS device, as well as the properties given below. The DVDRW_MOUNT_POINT property is required. Other properties are optional. </p>
<p> DVDRW_KEEP_CACHE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Set this boolean property to&nbsp;<wbr>&quot;true&quot;&nbsp;<wbr>if the disk cache directory should be kept after successfully writing tape data to optical media. The default is false, which causes the cache contents to be deleted immediately after a successful write operation.</dl>
<p> DVDRW_MOUNT_POINT</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>This property specifies the filesystem mount point for the optical media. Non-root users must be able to mount optical media by invoking&nbsp;<wbr>&quot;mount&quot;&nbsp;<wbr>and specifying this mount point.</dl>
<p> DVDRW_UNLABELLED_WHEN_UNMOUNTABLE</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>Treat unmountable media as empty, unlabelled media. This is necessary when attempting to label freshly formatted media.</dl>
<p> DVDRW_GROWISOFS_COMMAND</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>The command to invoke to burn the DVD.</dl>
<p> DVDRW_MOUNT_COMMAND</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>The command to invoke to mount the DVD.</dl>
<p> DVDRW_UMOUNT_COMMAND</p>
<dl>
<dd>&nbsp;<wbr>(read-write)&nbsp;<wbr>The command to invoke to unmount the DVD.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Ian Turner</code> &lt;ian [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
