---
title: "git-review(1)"
name: "git-review"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-review/"
description: "git-review – Submit changes to Gerrit for review"
---

<h2>NAME</h2>
<p> <code>git-review</code> &#8211; Submit changes to Gerrit for review</p>
<h2>SYNOPSIS</h2>
<p> [-<code>r </code><i>remote</i> ] [-<code>uv</code> ] &#8211;<code>d </code><i>change</i> [<i>branch</i> ]<br />
 [-<code>r </code><i>remote</i> ] [-<code>uv</code> ] &#8211;<code>x </code><i>change</i> [<i>branch</i> ]<br />
 [-<code>r </code><i>remote</i> ] [-<code>uv</code> ] &#8211;<code>N </code><i>change</i> [<i>branch</i> ]<br />
 [-<code>r </code><i>remote</i> ] [-<code>uv</code> ] &#8211;<code>X </code><i>change</i> [<i>branch</i> ]<br />
 [-<code>r </code><i>remote</i> ] [-<code>uv</code> ] &#8211;<code>m</code> <i>change-ps-range</i> [<i>branch</i> ]<br />
 [-<code>r </code><i>remote</i> ] [-<code>fnuv</code> ] &#8211;<code>s</code> [<i>branch</i> ]<br />
 [-<code>fnuvDR</code> ] [-<code>r </code><i>remote</i> ] [-<code>t </code><i>topic</i> ] [<i>branch</i> ]<br />
 &#8211;<code>-version</code></p>
<h2>DESCRIPTION</h2>
<p> automates and streamlines some of the tasks involved with submitting local changes to a Gerrit server for review. It is designed to make it easier to comprehend Gerrit, especially for users that have recently switched to Git from another version control system. </p>
<p> <i>change</i> can be <i>changeNumber</i> as obtained using &#8211;<code>&#8211;list</code> option, or it can be <i>changeNumber,patchsetNumber</i> for fetching exact patchset from the change. In that case local branch name will have a -patch[patchsetNumber] suffix. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-d </code><i>change , &#8211;</i><code>-download= </code><i>change</i></p>
<dd> Download <i>change</i> from Gerrit into a local branch. The branch will be named after the patch author and the name of a topic. If the local branch already exists, it will attempt to update with the latest patchset for this change.</p>
<dt><code>-x </code><i>change , &#8211;</i><code>-cherrypick= </code><i>change</i></p>
<dd> Apply <i>change</i> from Gerrit and commit into the current local branch (&quot;cherry pick&quot;). No additional branch is created. </p>
<p> This makes it possible to review a change without creating a local branch for it. On the other hand, be aware: if you are not careful, this can easily result in additional patch sets for dependent changes. Also, if the current branch is different enough, the change may not apply at all or produce merge conflicts that need to be resolved by hand.</p>
<dt><code>-N </code><i>change , &#8211;</i><code>-cherrypickonly= </code><i>change</i></p>
<dd> Apply <i>change</i> from Gerrit into the current working directory, add it to the staging area (&quot;git index&quot;), but do not commit it. </p>
<p> This makes it possible to review a change without creating a local commit for it. Useful if you want to merge several commits into one that will be submitted for review. </p>
<p> If the current branch is different enough, the change may not apply at all or produce merge conflicts that need to be resolved by hand.</p>
<dt><code>-X </code><i>change , &#8211;</i><code>-cherrypickindicate= </code><i>change</i></p>
<dd> Apply <i>change</i> from Gerrit and commit into the current local branch (&quot;cherry pick&quot;), indicating which commit this change was cherry-picked from. </p>
<p> This makes it possible to re-review a change for a different branch without creating a local branch for it. </p>
<p> If the current branch is different enough, the change may not apply at all or produce merge conflicts that need to be resolved by hand.</p>
<dt><code>-m </code><i>change-ps-range , &#8211;</i><code>-compare= </code><i>change-ps-range</i></p>
<dd> Download the specified patchsets for <i>change</i> from Gerrit, rebase both on master and display differences (git-diff). </p>
<p> <i>change-ps-range</i> can be specified as <i>changeNumber, </i><i>oldPatchSetNumber </i>[<i>-newPatchSetNumber</i> ] </p>
<p> <i>oldPatchSetNumber</i> is mandatory, and if <i>newPatchSetNumber</i> is not specified, the latest patchset will be used. </p>
<p> This makes it possible to easily compare what has changed from last time you reviewed the proposed change. </p>
<p> If the master branch is different enough, the rebase can produce merge conflicts. If that happens rebasing will be aborted and diff displayed for not-rebased branches. You can also use <i>&#8211;no-rebase ( -R</i> to always skip rebasing.</p>
<dt><code>-f , &#8211;finish</code></p>
<dd> Close down the local branch and switch back to the target branch on successful submission.</p>
<dt><code>-n , &#8211;dry-run</code></p>
<dd> Don&#8217;t actually perform any commands that have direct effects. Print them instead.</p>
<dt><code>-r </code><i>remote , &#8211;</i><code>-remote= </code><i>remote</i></p>
<dd> Git remote to use for Gerrit.</p>
<dt><code>-s , &#8211;setup</code></p>
<dd> Just run the repo setup commands but don&#8217;t submit anything.</p>
<dt><code>-t </code><i>topic , &#8211;</i><code>-topic= </code><i>topic</i></p>
<dd> Sets the target topic for this change on the gerrit server. If not specified, a bug number from the commit summary will be used. Alternatively, the local branch name will be used if different from remote branch.</p>
<dt><code>-u , &#8211;update</code></p>
<dd> Skip cached local copies and force updates from network resources.</p>
<dt><code>-l , &#8211;list</code></p>
<dd> List the available reviews on the gerrit server for this project.</p>
<dt><code>-y , &#8211;yes</code></p>
<dd> Indicate that you do, in fact, understand if you are submitting more than one patch.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Turns on more verbose output.</p>
<dt><code>-D , &#8211;draft</code></p>
<dd> Submit review as a draft. Requires Gerrit 2.3 or newer.</p>
<dt><code>-R , &#8211;no-rebase</code></p>
<dd> Do not automatically perform a rebase before submitting the change to Gerrit. </p>
<p> When submitting a change for review, you will usually want it to be based on the tip of upstream branch in order to avoid possible conflicts. When amending a change and rebasing the new patchset, the Gerrit web interface will show a difference between the two patchsets which contains all commits in between. This may confuse many reviewers that would expect to see a much simpler difference. </p>
<p> Also can be used for &#8211;<code>-compare</code> to skip automatic rebase of fetched reviews.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit.</dl>
<h2>CONFIGURATION</h2>
<p> This utility can be configured by adding entries to Git configuration. </p>
<p> The following configuration keys are supported:</p>
<dl>
<dt><code>gitreview.username</code></p>
<dd> Default username used to access the repository. If not specified in the Git configuration, Git remote or .gitreview file, the user will be prompted to specify the username. </p>
<p> Example entry in the .gitconfig file: </p>
<blockquote>
<pre>
[gitreview]
username=<i>mygerrituser</i>
</pre>
</blockquote>
<dt><code>gitreview.rebase</code></p>
<dd> This setting determines whether changes submitted will be rebased to the newest state of the branch. </p>
<p> A value of &#8216;true&#8217; or &#8216;false&#8217; should be specified.</p>
<dl>
<dt><code>false</code></p>
<dd> Do not rebase changes on submit &#8211; equivalent to setting &#8211;<code>R</code> when submitting changes.</p>
<dt><code>true</code></p>
<dd> Do rebase changes on submit. This is the default value unless overridden by .gitreview file.</dl>
<p> This setting takes precedence over repository-specific configuration in the .gitreview file.</dl>
<h2>FILES</h2>
<p> To use with your project, it is recommended that you create a file at the root of the repository named .gitreview and place information about your gerrit installation in it. The format is similar to the Windows .ini file format: </p>
<blockquote>
<pre>
[gerrit]
host=<i>hostname</i>
port=<i>TCP port number of gerrit</i>
project=<i>project name</i>
defaultbranch=<i>branch to work on</i>
</pre>
</blockquote>
<p> It is also possible to specify optional default name for the Git remote using the <code>defaultremote</code> configuration parameter. </p>
<p> Setting <code>defaultrebase</code> to zero will make not to rebase changes by default (same as the &#8211;<code>R</code> command line option) </p>
<blockquote>
<pre>
[gerrit]
host=review.example.com
port=29418
project=department/project.git
defaultbranch=master
defaultremote=review
defaultrebase=0
</pre>
</blockquote>
<h2>DIAGNOSTICS</h2>
<p> Normally, exit status is 0 if executed successfully. Exit status 1 indicates general error, sometimes more specific error codes are available:</p>
<dl>
<dt><code>2</code></p>
<dd> Gerrit <i>commit-msg</i> hook could not be successfully installed.</p>
<dt><code>32</code></p>
<dd> Cannot fetch list of open changesets from Gerrit.</p>
<dt><code>33</code></p>
<dd> Cannot parse list of open changesets received from Gerrit.</p>
<dt><code>34</code></p>
<dd> Cannot query information about changesets.</p>
<dt><code>35</code></p>
<dd> Cannot fetch information about the changeset to be downloaded.</p>
<dt><code>36</code></p>
<dd> Changeset not found.</p>
<dt><code>37</code></p>
<dd> Particular patchset cannot be fetched from the remote git repository.</p>
<dt><code>38</code></p>
<dd> Specified patchset number not found in the changeset.</p>
<dt><code>39</code></p>
<dd> Invalid patchsets for comparison.</p>
<dt><code>64</code></p>
<dd> Cannot checkout downloaded patchset into the new branch.</p>
<dt><code>65</code></p>
<dd> Cannot checkout downloaded patchset into existing branch.</p>
<dt><code>66</code></p>
<dd> Cannot hard reset working directory and git index after download.</p>
<dt><code>67</code></p>
<dd> Cannot switch to some other branch when trying to finish the current branch.</p>
<dt><code>68</code></p>
<dd> Cannot delete current branch.</p>
<dt><code>69</code></p>
<dd> Requested patchset cannot be fully applied to the current branch. This exit status will be returned when there are merge conflicts with the current branch. Possible reasons include an attempt to apply patchset from the different branch or code. This exit status will also be returned if the patchset is already applied to the current branch.</p>
<dt><code>70</code></p>
<dd> Cannot determine top level Git directory or .git subdirectory path.</dl>
<p> Exit status larger than 31 indicates problem with communication with Gerrit or remote Git repository, exit status larger than 63 means there was a problem with a local repository or a working copy. </p>
<p> Exit status larger than or equal to 128 means internal error in running the &quot;git&quot; command. </p>
<h2>EXAMPLES</h2>
<p> To fetch a remote change number 3004: </p>
<blockquote>
<pre>
$ git-review -d 3004
Downloading refs/changes/04/3004/1 from gerrit into
review/someone/topic_name
Switched to branch 'review/someone/topic_name
$ git branch
  master
* review/author/topic_name
</pre>
</blockquote>
<p> Gerrit looks up both name of the author and the topic name from Gerrit to name a local branch. This facilitates easier identification of changes. </p>
<p> To fetch a remote patchset number 5 from change number 3004: </p>
<blockquote>
<pre>
$ git-review -d 3004,5
Downloading refs/changes/04/3004/5 from gerrit into
review/someone/topic_name-patch5
Switched to branch 'review/someone/topic_name-patch5
$ git branch
  master
* review/author/topic_name-patch5
</pre>
</blockquote>
<p> To send a change for review and delete local branch afterwards: </p>
<blockquote>
<pre><code>
$ git-review -f
remote: Resolving deltas:   0% (0/8)
To ssh://username@review.example.com/department/project.git
 * [new branch]      HEAD -&gt; refs/for/master/topic_name
Switched to branch 'master'
Deleted branch 'review/someone/topic_name'
$ git branch
* master
</code></pre>
</blockquote>
<p> An example .gitreview configuration file for a project department/project hosted on <code>review.example.com</code> port <code>29418</code> in the branch <code>master</code> : </p>
<blockquote>
<pre>
[gerrit]
host=review.example.com
port=29418
project=department/project.git
defaultbranch=master
</pre>
</blockquote>
<h2>BUGS</h2>
<p> Bug reports can be submitted to Lk <a rel="nofollow" href="https://launchpad.net/git-review">https://launchpad.net/git-review</a></p>
<h2>AUTHORS</h2>
<p> is maintained by An OpenStack, LLC </p>
<p> This manpage has been enhanced by: An Antoine Musso Aq hashar [at] free.fr An Marcin Cieslak Aq saper [at] saper.info An Pavel Sedlák Aq psedlak [at] redhat.com </p>
<h2>Index</h2>
