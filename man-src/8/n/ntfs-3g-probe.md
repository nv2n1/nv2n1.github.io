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
<dt><code>-r, &#8211;readonly</code></dt>
<dd>Test if the volume can be mounted read-only.</dd>
<dt><code>-w, &#8211;readwrite</code></dt>
<dd>Test if the volume can be mounted read-write.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display help and exit.</dd></dl>
<h2>Example</h2>
<p>Test if /dev/sda1 can be mounted read-write:</p>
<dl>
<dd><code>ntfs-3g.probe &#8211;readwrite /dev/sda1</code> </dd>
<h2>Exit Codes</h2>
<p>The exit codes are as follows:</p>
<dl>
<dt>0</dt>
<dd>Volume is mountable.</dd>
<dt>11</dt>
<dd>Syntax error, command line parsing failed.</dd>
<dt>12</dt>
<dd>The volume doesn&#8217;t have a valid NTFS.</dd>
<dt>13</dt>
<dd>Inconsistent NTFS, hardware or device driver fault, or unsetup SoftRAID/FakeRAID hardware.</dd>
<dt>14</dt>
<dd>The NTFS partition is hibernated.</dd>
<dt>15</dt>
<dd>The volume was not cleanly unmounted.</dd>
<dt>16</dt>
<dd>The volume is already exclusively opened and in use by a kernel driver or software.</dd>
<dt>17</dt>
<dd>Unsetup SoftRAID/FakeRAID hardware.</dd>
<dt>18</dt>
<dd>Unknown reason.</dd>
<dt>19</dt>
<dd>Not enough privilege to mount.</dd>
<dt>20</dt>
<dd>Out of memory.</dd>
<dt>21</dt>
<dd>Unclassified FUSE error.</dd></dl>
<h2>Known Issues</h2>
<p>Please see</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ">https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ</a> </dd>
</dl>
<p> for common questions and known issues. If you think you have found an undocumented problem in the latest release of the software then please post an ntfs-3g issue describing it in detail so that the development team can be aware of the issue and take care of it:</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/issues">https://github.com/tuxera/ntfs-3g/issues</a> </dd>
</dl>
<h2>Authors</h2>
<p><code>ntfs-3g.probe </code> was written by Szabolcs Szakacsits.</p>
<h2>Thanks</h2>
<p>Alon Bar-Lev has integrated the utility into the NTFS-3G build process and tested it with Erik Larsson before the public release.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8) </p>
</dl>