---
title: "ntfs-3g-probe(8)"
name: "ntfs-3g-probe"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfs-3g-probe/"
description: "ntfs-3g.probe – Probe an NTFS volume mountability"
---

<p>ntfs-3g.probe &#8211; Probe an NTFS volume mountability</p>
<h2>Synopsis</h2>
<p><code>ntfs-3g.probe</code> <i>&lt;&#8211;readonly|&#8211;readwrite&gt;</i> <i>volume </i></p>
<h2>Description</h2>
<p>The <code>ntfs-3g.probe</code> utility tests a volume if it&#8217;s NTFS mountable read-only or read-write, and exits with a status value accordingly. The <i>volume</i> can be a block device or image file.</p>
<h2>Options</h2>
<p>Below is a summary of the options that <code>ntfs-3g.probe</code> accepts.</p>
<dl>
<dt><code>-r, &#8211;readonly</code></p>
<dd>Test if the volume can be mounted read-only.</p>
<dt><code>-w, &#8211;readwrite</code></p>
<dd>Test if the volume can be mounted read-write.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display help and exit.</dl>
<h2>Example</h2>
<p>Test if /dev/sda1 can be mounted read-write:</p>
<dl>
<dd><code>ntfs-3g.probe &#8211;readwrite /dev/sda1</code> </p>
<h2>Exit Codes</h2>
<p>The exit codes are as follows:</p>
<dl>
<dt>0</p>
<dd>Volume is mountable.</p>
<dt>11</p>
<dd>Syntax error, command line parsing failed.</p>
<dt>12</p>
<dd>The volume doesn&#8217;t have a valid NTFS.</p>
<dt>13</p>
<dd>Inconsistent NTFS, hardware or device driver fault, or unsetup SoftRAID/FakeRAID hardware.</p>
<dt>14</p>
<dd>The NTFS partition is hibernated.</p>
<dt>15</p>
<dd>The volume was not cleanly unmounted.</p>
<dt>16</p>
<dd>The volume is already exclusively opened and in use by a kernel driver or software.</p>
<dt>17</p>
<dd>Unsetup SoftRAID/FakeRAID hardware.</p>
<dt>18</p>
<dd>Unknown reason.</p>
<dt>19</p>
<dd>Not enough privilege to mount.</p>
<dt>20</p>
<dd>Out of memory.</p>
<dt>21</p>
<dd>Unclassified FUSE error.</dl>
<h2>Known Issues</h2>
<p>Please see</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ">https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ</a> </p>
</dl>
<p> for common questions and known issues. If you think you have found an undocumented problem in the latest release of the software then please post an ntfs-3g issue describing it in detail so that the development team can be aware of the issue and take care of it:</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/issues">https://github.com/tuxera/ntfs-3g/issues</a> </p>
</dl>
<h2>Authors</h2>
<p><code>ntfs-3g.probe </code> was written by Szabolcs Szakacsits.</p>
<h2>Thanks</h2>
<p>Alon Bar-Lev has integrated the utility into the NTFS-3G build process and tested it with Erik Larsson before the public release.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8) </p>
