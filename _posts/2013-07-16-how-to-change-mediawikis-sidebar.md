---
title: "Customizing MediaWiki\u2019s Sidebar: A Configuration Guide"
date: 2013-07-16 01:32:09 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-mediawikis-sidebar/
---

MediaWiki’s sidebar is managed through the `MediaWiki:Sidebar` special page, a simple text-based system that controls navigation for your entire wiki. Changes take effect immediately across all pages.

## Accessing the Sidebar Configuration

Navigate to the sidebar editor using one of these methods:

**Direct URL** (replace example.com with your domain):

- With pretty URLs: `https://example.com/w/MediaWiki:Sidebar`
- Without pretty URLs: `https://example.com/w/index.php?title=MediaWiki:Sidebar&action=edit`

**Via the wiki interface**:

1.  Go to Special:AllPages
2.  Select the MediaWiki namespace
3.  Search for “Sidebar”

Or access Special:SpecialPages and look for “Sidebar” under the MediaWiki namespace section.

## Sidebar Syntax

The sidebar uses asterisk-based markup to define its structure:

- Single asterisk (`*`) — creates a collapsible section header
- Double asterisks (`**`) — creates menu items within that section

### Default Sidebar Structure

    * navigation
    ** mainpage|mainpage-description
    ** recentchanges-url|recentchanges
    ** randompage-url|randompage
    ** currentevents-url|currentevents
    ** portal-url|portal
    ** helppage|help
    * SEARCH
    * TOOLBOX
    * LANGUAGES

The keywords `SEARCH`, `TOOLBOX`, and `LANGUAGES` are special directives that render built-in MediaWiki components. They must be capitalized and appear on their own line.

## Link Format and Message Keys

Links follow the pattern `target|display-text`:

- `target` — the destination (wiki page, special page, or full URL)
- `display-text` — what users see (can be a message key or plain text)

**Message keys** (lowercase, with hyphens) are automatically translated to the user’s language:

    ** mainpage|mainpage-description
    ** recentchanges-url|recentchanges
    ** randompage-url|randompage
    ** currentevents-url|currentevents
    ** portal-url|portal
    ** helppage|help

**Plain text labels** work for any target and don’t require translation:

    ** Special:RecentChanges|Recent Changes
    ** Special:Random|Random Article
    ** https://example.com/docs|Documentation
    ** Help:Contents|Getting Started

**Mixed usage**:

    * Navigation
    ** mainpage|mainpage-description
    ** Special:RecentChanges|Recent Changes
    ** https://github.com/yourproject|GitHub Repository
    ** Help:Contents|help

## Practical Sidebar Examples

### Adding a Custom Documentation Section

    * Documentation
    ** Help:Contents|Getting Started
    ** Help:Editing|How to Edit
    ** Help:Formatting|Text Formatting
    ** Help:Templates|Using Templates
    ** Special:Upload|Upload Files

### Adding External Links

    * Community
    ** https://forum.example.com|Discussion Forum
    ** https://github.com/yourproject|GitHub Repository
    ** https://discord.gg/yourserver|Discord Server
    ** https://example.com/roadmap|Project Roadmap

### Removing Unwanted Sections

Delete lines you don’t need. For example, if your wiki is single-language, remove the LANGUAGES section:

    * navigation
    ** mainpage|mainpage-description
    ** recentchanges-url|recentchanges
    ** randompage-url|randompage
    * SEARCH
    * TOOLBOX

Similarly, remove `SEARCH` or `TOOLBOX` if your users don’t need them.

## Making and Testing Changes

1.  Click “Edit” on the `MediaWiki:Sidebar` page
2.  Modify the sidebar content
3.  Click “Publish changes”

Changes take effect immediately for all users, though users may need to clear their browser cache or do a hard refresh (Ctrl+F5 or Cmd+Shift+R) to see updates.

**Test carefully in a non-production wiki first**, especially if you’re removing sections or reorganizing major navigation elements.

## Permissions and Protection

Only users with edit permissions on the MediaWiki namespace can modify the sidebar. By default, this requires administrator status.

### Restricting Further

1.  Go to `MediaWiki:Sidebar`
2.  Click the “Protect” tab
3.  Set restrictions to “Sysops only” to prevent changes by less privileged admins

### Allowing Trusted Non-Admins

Grant sidebar editing permission via Special:UserRights by adding users to a custom group with the `edit` permission on the MediaWiki namespace. This requires configuration in `LocalSettings.php`:

``` php
$wgGroupPermissions['sidebar-editors']['edit'] = true;
$wgGroupPermissions['sidebar-editors']['editinterface'] = true;
```

## Finding Available Message Keys

MediaWiki has hundreds of built-in message keys. View available keys at Special:AllMessages and filter by “sidebar” to find sidebar-specific translations.

Common keys include:

- `mainpage|mainpage-description`
- `recentchanges|recentchanges`
- `randompage-url|randompage`
- `portal-url|portal`
- `help|helppage`

## Advanced Customization with Extensions

For complex sidebars beyond static links, consider these approaches:

**Extension:DynamicPageList** — Populate sidebar links from category or namespace queries:

    * Recent Articles
    <DPL>
    namespace = 0
    count = 5
    orderby = modification date
    order = descending
    format = ,** %PAGE%|%TITLE%,
    </DPL>

**Conditional sections** — Some extensions like Extension:SidebarDynamicFunctions allow logic-based sections, though this adds complexity and isn’t necessary for most wikis.

**CSS and JavaScript** — Edit `MediaWiki:Sidebar.css` and `MediaWiki:Common.js` to style or add JavaScript behavior to sidebar elements without installing extensions.

For the vast majority of installations, the raw `MediaWiki:Sidebar` text format handles all typical requirements cleanly and without additional dependencies.
