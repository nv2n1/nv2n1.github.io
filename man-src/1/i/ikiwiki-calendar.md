---
title: "ikiwiki-calendar(1)"
name: "ikiwiki-calendar"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ikiwiki-calendar/"
---

<h2>NAME</h2>

 ikiwiki-calendar - create calendar archive pages 

<h2>SYNOPSIS</h2>

 ikiwiki-calendar [-f] your.setup [pagespec] [startyear [endyear]] 

<h2>DESCRIPTION</h2>

 ikiwiki-calendar creates pages that use the ikiwiki/directive/calendar directive, allowing the archives to be browsed one month at a time, with calendar-based navigation. 

 You must specify the setup file for your wiki. The pages will be created inside its srcdir, beneath the archivebase directory used by the calendar plugin (default &quot;archives&quot;). 

 To control which pages are included on the calendars, a ikiwiki/PageSpec can be specified. The default is all pages, or the pages specified by the comments_pagespec setting in the config file. A pagespec can also be specified on the command line. To limit it to only posts in a blog, use something like &quot;posts/* and !*/Discussion&quot;. 

 It defaults to creating calendar pages for the current year. If you specify a year, it will create pages for that year. Specify a second year to create pages for a span of years. 

 Existing pages will not be overwritten by this command by default. Use the -f switch to force it to overwrite any existing pages. 

<h2>CRONTAB</h2>

 While this command only needs to be run once a year to update the archive pages for each new year, you are recommended to set up a cron job to run it daily, at midnight. Then it will also update the calendars to highlight the current day. 

 An example crontab: 

 0 0 * * * ikiwiki-calendar ~/ikiwiki.setup &quot;posts/* and !*/Discussion&quot; 

<h2>TEMPLATES</h2>

 This command uses two templates to generate the pages, calendarmonth.tmpl and calendaryear.tmpl. 

<h2>AUTHOR</h2>

 Joey Hess &lt;joey [at] ikiwiki.info&gt; 

 

 

 

<h2>Index</h2>


