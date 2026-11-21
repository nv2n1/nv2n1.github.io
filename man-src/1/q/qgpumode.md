---

title: "qgpumode(1)"
name: "qgpumode"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qgpumode/"
description: "qgpumode – change GPU mode"
---

<p> qgpumode &#8211; change GPU mode </p>
<h2>SYNOPSIS</h2>
<p> qgpumode -H host -g gpuid -m mode</p>
<h2>DESCRIPTION</h2>
<p> The <code>qgpumode </code> command will request a MOM to change the mode on one of it&#8217;s Nvidia GPUs. The GPU&#8217;s mode is changed by sending a <i>GPU Control</i> batch request to the batch server. </p>
<p> Changing the GPU mode requires PBS Operator or Manager privilege. It also requires that Torque be configured with &#8211;enable-nvidia-gpu. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-H host</dt>
<dd> Specifies the host within the cluster on which the GPU is located. The argument is the name of a host that is a member of the cluster of hosts managed by the server.</dd>
<dt>-g gpuid</dt>
<dd> Specifies the ID of the GPU.</dd>
<dt>-m mode</dt>
<dd> Specifies the new mode of the GPU. Valid Nvidia GPU modes are:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> &#8211; Normal mode.</dd>
<dt>1</dt>
<dd> &#8211; COMPUTE exclusive thread mode (only one COMPUTE thread is allowed to run on the GPU).</dd>
<dt>2</dt>
<dd> &#8211; COMPUTE prohibited mode (no COMPUTE contexts are allowed to run on the GPU).</dd>
<dt>3</dt>
<dd> &#8211; COMPUTE exclusive process mode (only one COMPUTE process is allowed to run on the GPU). This mode is new with Nvidia driver version 270.</dd></dl>
</dl>
</dl>
<h2>OPERANDS</h2>
<p> None </p>
<h2>STANDARD ERROR</h2>
<p> The qgpumode command will write a diagnostic messages to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qgpumode command, the exit status will be a value of zero. </p>
<p> If the qgpumode command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> pbs_mom(8B) and pbs_server(8B) </p>
