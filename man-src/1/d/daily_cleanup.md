---
title: "daily_cleanup(1)"
name: "daily_cleanup"
section: "1"
letter: "d"
url: "/docs/linux/man/1-daily_cleanup/"
description: "daily_cleanup.py – Database clean-up for the Django Web framework"
---

<h2>NAME</h2>
<p> daily_cleanup.py &#8211; Database clean-up for the Django Web framework</p>
<h2>SYNOPSIS</h2>
<p> <code>daily_cleanup.py</code> </p>
<h2>DESCRIPTION</h2>
<p> Removes stale session data from a Django database. This means, any session data which has an expiry date prior to the date the script is run. </p>
<p> The script can be run manually or can be scheduled to run at regular intervals as a <code>cron</code> job. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>DJANGO_SETTINGS_MODULE</i></p>
<dd> This environment variable defines the settings module to be read. It should be in Python-import form, e.g. &quot;myproject.settings&quot;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> The sessions documentation: </p>
<p> <i><a rel="nofollow" href="http://docs.djangoproject.com/en/dev/topics/http/sessions/">http://docs.djangoproject.com/en/dev/topics/http/sessions/</a></i> </p>
<h2>AUTHORS/CREDITS</h2>
<p> Originally developed at World Online in Lawrence, Kansas, USA. Refer to the AUTHORS file in the Django distribution for contributors. </p>
<h2>LICENSE</h2>
<p> New BSD license. For the full license text refer to the LICENSE file in the Django distribution. </p>
<h2>Index</h2>
