---
title: "euca2ools(7)"
name: "euca2ools"
section: "7"
letter: "e"
url: "/docs/linux/man/7-euca2ools/"
description: "euca2ools – eucalyptus command line client tools"
---

<p><code>euca2ools</code> &#8211; eucalyptus command line client tools</p>
<h2>Description</h2>
<p>The suite is a set of command line tools that interact with &#8220;Amazon Web Services&#8221; (AWS) Eucalyptus, and other AWS-compatible clouds using the REST- and query-based APIs for numerous web services. The URL for each web service can be set with a <i>SERVICE </i><code>-url</code> region option, where <i>SERVICE</i> is the name of the service, in euca2ools.ini5 configuration files and then chosen with the &#8211;<code>-region</code> command line option or the <code>EUCA_DEFAULT_REGION</code> or <code>AWS_DEFAULT_REGION</code> environment variables. Alternatively, the URL can be set at the command line or with an environment variable that is specific to the service. Environment variables take precedence over configuration file data. are designed to make it as easy as possible to work with multiple AWS-compatible clouds from the command line using euca2ools.ini5 configuration files, command line options, and shortcuts.</p>
<h3>List of Web Services</h3>
<dl>
<dt><code>Name Ta </code><code>Version Ta </code><code>Environment variable Ta </code><code>Commands</code></p>
<dd>
<dt><code>autoscaling Ta </code>2011-01-01 Ta AWS_AUTO_SCALING_URL Ta euscale-*</p>
<dd>
<dt><code>bootstrap Ta </code>Ta EUCA_BOOTSTRAP_URL Ta euca-bundle-image1,</p>
<dd>euca-bundle-and-upload-image1, euca-install-image1, euimage-install-pack1</p>
<dt><code>cloudformation Ta </code>2010-05-15 Ta AWS_CLOUDFORMATION_URL Ta euform-*</p>
<dd>
<dt><code>ec2 Ta </code>2015-10-01 Ta EC2_URL Ta euca-*</p>
<dd>
<dt><code>elasticloadbalancing Ta </code>2012-06-01 Ta AWS_ELB_URL Ta eulb-*</p>
<dd>
<dt><code>iam Ta </code>2010-05-08 Ta AWS_IAM_URL Ta euare-*</p>
<dd>
<dt><code>monitoring Ta </code>2010-08-01 Ta AWS_CLOUDWATCH_URL Ta euwatch-*</p>
<dd>
<dt><code>s3 Ta </code>2006-03-01 Ta S3_URL Ta euca-bundle-and-upload-image1,</p>
<dd>euca-download-and-unbundle1, euca-download-bundle1, euca-install-image1, euca-upload-bundle1, euimage-install-pack1</p>
<dt><code>sts Ta </code>2011-06-15 Ta TOKENS_URL Ta euare-assumerole1</p>
<dd></dl>
<h2>Notes</h2>
<p>The &#8220;bootstrap&#8221; service, also known as the &#8220;Empyrean&#8221; service, is specific to eucalyptus. Commands that bundle images can optionally use it to obtain the cloud&#8217;s signing certificate automatically, provided the cloud runs eucalyptus 4.2 or later.</p>
<h2>See Also</h2>
<p>euca2ools.ini5 </p>
