---
title: "s3fs(1)"
name: "s3fs"
section: "1"
letter: "s"
url: "/docs/linux/man/1-s3fs/"
description: "s3fs – The S3 FUSE filesystem disk management utility"
---

<h2>NAME</h2>
<p> s3fs &#8211; The S3 FUSE filesystem disk management utility</p>
<h2>SYNOPSIS</h2>
<p> <code>s3fs </code> <code>[&lt;-C&gt; [-h] | [-cdrf &lt;bucket&gt;] [-p &lt;access_key&gt;] [-s secret_access_key] ] | [ -o &lt;options&gt; &lt;mountpoint&gt;]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>s3fs </i> is a FUSE filesystem application backed by amazon web services simple storage service (s3, <a rel="nofollow" href="http://aws.amazon.com">http://aws.amazon.com</a>). s3fs can operate in a command mode or a mount mode. </p>
<p> In mount mode, s3fs will mount an amazon s3 bucket (that has been properly formatted) as a local file system. </p>
<p> In command mode, s3fs is capable of manipulating amazon s3 buckets in various usefull ways</p>
<h2>OPTIONS</h2>
<p> Options are used in command mode. To enter command mode, you must specify -C as the first command line option. Note these options are only available in command mode </p>
<dl>
<dt><code>-C</code></p>
<dd> Enter command mode. This must be the first option on the command line when using s3fs in command mode </p>
<dt><code>-h</code></p>
<dd> Display usage information on command mode</p>
<dt><code>-c &lt;bucket&gt;</code></p>
<dd> Create the named s3 bucket</p>
<dt><code>-d &lt;bucket&gt;</code></p>
<dd> Delete the named s3 bucket (and any data contained there, use with caution!)</p>
<dt><code>-r &lt;bucket&gt;</code></p>
<dd> Interactively repair a broken s3 filesystem (not yet implemented)</p>
<dt><code>-f &lt;bucket&gt;</code></p>
<dd> Format an s3 bucket to make it suitable for mounting</p>
<dt><code>-k &lt;bucket&gt;</code></p>
<dd> Toggle the lock bit on a bucket. buckets must be unlocked to format or delete them</p>
<dt><code>-p &lt;access_key&gt;</code></p>
<dd> Provide the AWS access key if not set in your environment</p>
<dt><code>-s &lt;secret_access_key&gt;</code></p>
<dd> Provide the AWS secret access key if not set in your environment</p>
<dt><code>-o &lt;options&gt;</code></p>
<dd> Specify mount options when s3fs is operating in mount mode</dl>
<h2>MOUNT OPTIONS</h2>
<p> Note these options are only available when operating s3fs in mount mode</p>
<dl>
<dt><code>bucket=&lt;bucket&gt;</code></p>
<dd> Specify the name of the Amazon S3 bucket you wish to mount (default: none)</p>
<dt><code>preserve_cache=[no|yes]</code></p>
<dd> If set to yes, the cache for the given mount will not be deleted on unmount, saving the need for downloads on a subsequent remount (default: no)</p>
<dt><code>cachedir=&lt;directory&gt;</code></p>
<dd> Sets the base directory where cached s3fs files will be stored. (default=$HOME/.fuse-s3fs-cache/)</p>
<dt><code>host=&lt;host name&gt;</code></p>
<dd> Allows overriding of default amazon s3 hostname. defaults to s3.aws.amazon.com</p>
<dt><code>lazy_fsdata=[no|yes]</code></p>
<dd> If set to yes, filesystem metadata will only be written back to S3 on unmount (default: yes)</p>
<dt><code>writeback_time=&lt;seconds&gt;</code></p>
<dd> Number of seconds of hysteresis to pause when considering uploading a file to S3. If, after the pause, s3fs detects that other processes have opened a file, uploading is postponed (default=10)</p>
<dt><code>AWS_ACCESS_KEY_ID=&lt;key&gt;</code></p>
<dd> Specify the AWS_ACCESS_KEY_ID for your aws account if you don&#8217;t wish to place it in your environment (default: none)</p>
<dt><code>AWS_SECRET_ACCESS_KEY=&lt;key&gt;</code></p>
<dd> Specify your AWS_SECRET_ACCESS_KEY for your aws account if you don&#8217;t wish to place it in your environment. NOTE: If you add a mount to /etc/fstab, it is discouraged for you to use this option. Doing so will publish your secret key and allow others to use your account. (default: none)</dl>
<h2>UNMOUNTING</h2>
<p> Note that to unmount FUSE filesystems the fusermount utility should be used. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>AWS_ACCESS_KEY_ID </code></p>
<dd> This is your Amazon web service public key. It must be set so that s3fs can identify you to amazon</p>
<dt><code>AWS_SECRET_ACCESS_KEY</code></p>
<dd> This is your Amazon web service private key. It must be set so that s3fs can identify you to amazon.</p>
<dt>Both AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY must be set and exported by the</p>
<dd> user preforming a mount with s3fs in order to successfully use s3fs</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>Create an S3 Bucket </code></p>
<dd> s3fs -C -c &lt;bucket_name&gt;</p>
<dt><code>Format an S3 Bucket </code></p>
<dd> s3fs -C -f &lt;bucket_name&gt;</p>
<dt><code>Mount an S3 Bucket </code></p>
<dd> s3fs -o [other mount options],bucket=&lt;bucket_name&gt; &lt;mount point&gt;</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/fstab</code></p>
<dd></dl>
<p> The format for an s3fs entry in /etc/fstab should look like this </p>
<p> <code>fstab<tt>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;mntpoint&gt;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fuse<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[options],suid,dev,exec,noauto,users,bucket=&lt;s3_bucket&gt; 0 0</code> </p>
<p> Note that the &lt;mntpoint&gt; must be readable by the mounting user</p>
<h2>NOTES</h2>
<dl>
<dt><code>Multi User capability</code></p>
<dd> While it is possible to share s3 buckets among multiple users, the current data consistency model for Amazons S3 service prevent the safe usage of multiple mounts from multiple users. While s3fs will currently allow multiple mounts, data corruption may result from such activity. A future release will contain a locking mechanism to safely guard against multiple read-write mounts. multiple read-only mounts following a single read-write mount is safe, but will not reflect changes made by the writeable mount to any of the file or filesystem metadata, limiting its usefulness there </p>
<dt><code>File System Layout &amp; Limitations</code></p>
<dd> The s3fs filesystem is designed to be very, very simple. S3 maintains a flat storage system, meaning no directory heirarchy is allowed on the backing store. Directory information is stored in the filesystem metadata that is retrieved during the mount operation from a file called fsdata. This file is a python class that has been pickled, and maintains all the directory heirarchy. Files are stored against their fully qualified path names within the file system, which makes for easy file retrieval via any web based interface to S3, should the metadata become corrupted. Note that the metadata (stored on S3 in a file called fsdata), has a layout that is defined by the pyhon class definition in the s3fs executable. To understand or view the layout of this data, one must read the python code. Specifically the S3DriveMetaData class should be investigated, as that is the base class that is pickled. Given that files are stored as individual objects on S3, coupled with the fact that there is a 5GB limit to each object in S3, s3fs currently has a natural limit of 5GB per file </p>
<dt><code>Compatibility with other S3 Access mechanisms</code></p>
<dd> Amazon S3 is simply a storage back end. s3fs is simply a storage api that exports that storage in the form of a local file system. Note there are many other mechanisms for using S3, some filesystem oriented, like s3fs, as well as other methods. It is important to note, that this application creates a unique filesystem structure on the targeted S3 storage bucket. As such it is incompatible with other S3 fuse implementations. One should not use alternate s3fs clients (of which several are available) to mount buckets created with this utility. This is true for all S3 filesystem implementations, as each has a unique filesystem structure. That being said, the design of this particular S3 filesystem layout does make it compatible with web based S3 access mechanism. Using a web browser, it is possible to retrieve individual files from a bucket that has been formatted for use as an s3fs file system. </p>
</dl>
<h2>Index</h2>
