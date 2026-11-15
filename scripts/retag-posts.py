#!/usr/bin/env python3
"""Re-tag posts so every category is a learning topic in _data/topics.yml.

Usage: python3 scripts/retag-posts.py [--apply]

Ground truth comes from the post lists under each topic heading on the path
and academy pages; everything else falls back to keyword rules. Prints a
distribution report; rewrites the `categories:` line of each post only with
--apply.
"""

import re
import sys
import glob
import collections

APPLY = '--apply' in sys.argv

# topic heading -> category slug (must match _data/topics.yml)
TOPIC_SLUGS = {
    'Command Line & Text Tools': 'command-line-text-tools',
    'Users & Permissions': 'users-permissions',
    'Files & Storage': 'files-storage',
    'Shell & Scripting': 'shell-scripting',
    'Packages, Desktop & Applications': 'packages-desktop-applications',
    'systemd & Services': 'systemd-services',
    'Networking': 'networking',
    'Storage & LVM': 'storage-lvm',
    'Virtualization & Containers': 'virtualization-containers',
    'Kernel': 'kernel',
    'Kernel History: Release Notes': 'kernel-release-notes',
    'Performance': 'performance',
    'Consensus': 'consensus',
    'Consistency Models': 'consistency-models',
    'Storage & File Systems': 'storage-file-systems',
    'Big Data Systems': 'big-data-systems',
    'Engineering Lessons': 'engineering-lessons',
    'Low-Level Systems': 'low-level-systems',
    'Cryptography & Keys': 'cryptography-keys',
    'TLS & Email Security': 'tls-email-security',
    'Data Protection': 'data-protection',
    'Model Fundamentals': 'model-fundamentals',
    'CLI + AI Integration': 'cli-ai-integration',
    'Prompt Engineering': 'prompt-engineering',
}

GROUND_TRUTH_PAGES = [
    'linux-essentials-path.md', 'linux-sysadmin-path.md',
    'advanced-systems-path.md', 'security-cryptography-path.md',
    'ai-engineering-hub.md',
]

# deterministic old-category merges
CATEGORY_MAP = {
    'languages-frameworks': 'programming-languages',
    'object-oriented-programming': 'programming-languages',
    'functional-programming': 'programming-languages',
    'code-optimization': 'algorithms-data-structures',
    'design-patterns-architecture': 'software-design',
    'development-best-practices': 'software-design',
}

# ordered keyword rules: (category, regex on slug+title)
LINUX_RULES = [
    ('kernel-release-notes', r'release-notes-for-linux|notes-for-linux-release|linux-kernel-\d|linux-v\d'),
    ('virtualization-containers', r'\bkvm\b|qemu|xen\b|vmware|virtualbox|virtual-?i[sz]|docker|container|podman|lxc\b|virt-|libvirt|domu|dom0'),
    ('storage-lvm', r'\blvm\b|volume-group|logical-volume|fstab|\bmount|\bdisk\b|partition|mdadm|\braid\b|\bswap\b|ext[234]\b|xfs|btrfs|\bnfs\b|iscsi|\bsr0\b|dvd'),
    ('networking', r'network|iptables|firewall|\btcp\b|\budp\b|socket|\bssh\b|\bscp\b|\bdns\b|\bdhcp\b|\bip\b|eth[0-9]|wifi|wireless|proxy|gateway|netem|netpoll|dnsmasq|nft'),
    ('kernel', r'kernel|module|driver|\bdrm\b|alsa|hda|cifs|syscall|\bbpf\b|netconsole|taskstats|xt_quota|grub2'),
    ('systemd-services', r'systemd|journalctl|daemon|\bservice\b|systemctl|\bboot\b|\binit\b|cron|tmpfiles|selinux'),
    ('performance', r'performance|faster|\bspeed\b|latency|benchmark|optimi|profil|monitor|\btop\b|sar\b|vmstat|\bebpf\b|fio\b|\bdd\b|cpu-affinity|throughput'),
    ('users-permissions', r'\buser\b|users\b|\bgroup\b|password|\bsudo\b|permission|chmod|chown|\broot\b|\bgpasswd\b|\bchage\b'),
    ('files-storage', r'\bfile\b|files\b|directory|sparse|compress|\bpng\b|\bjpg\b|\bjpeg\b|\bpdf\b|\bswap\b|inode|\bsync\b|rsync|\btar\b|\bgzip\b'),
    ('command-line-text-tools', r'command-line|cli\b|terminal|\bxxd\b|\bsed\b|\bawk\b|\bgrep\b|convert|encoding|\bascii\b|text'),
    ('shell-scripting', r'script|bash|\bzsh\b|shell|readline'),
    ('packages-desktop-applications', r'install|yum\b|dnf\b|\bapt\b|package|rpm\b|\bdeb\b|ubuntu|fedora|centos|rhel|gnome|desktop|font|wine\b|snap\b|flatpak|gsettings|thunderbird|mirror'),
]

# developer-tooling posts that used to sit in the linux/scripting categories
PROGRAMMING_RULES = [
    ('scripting-automation', r'\bgit\b|vim\b|emacs|\bmake\b|editor|cheatsheet|bbcode|readline'),
    ('web-development', r'mysql|wordpress|apache|\bphp\b|node-?js|jsp\b|mediawiki|\bcurl\b|\.js\b|html|kindle|chrome\b|firefox'),
    ('programming-languages', r'-in-c\b|\bc-code\b|cout|scanf|ocaml|\bjava\b|static-library|error-codes|mmaped|printf'),
]

WEB3_RULES = [
    ('self-custody-security', r'wallet|private-key|multisig|custody|sharding|hardware-wallet|key-derivation|seed|backup|cold-storage'),
    ('web3-defi', r'ethereum|evm|smart-contract|defi|\bdapp\b|web3|token|erc-?20|gas\b|uniswap|dex\b'),
    ('cryptocurrency-trading', r'bitcoin|btc\b|segwit|trading|options|futures|exchange|price|fee|litecoin|\bltc\b|cryptocurrenc|crypto\b'),
    ('blockchain-fundamentals', r'blockchain|consensus|hash|ledger|mining|\bpow\b|\bpos\b|fork|101\b'),
]

SECURITY_RULES = [
    ('tls-email-security', r'tls|ssl|certificate|letsencrypt|spf\b|dkim|dmarc|email|mail'),
    ('data-protection', r'ecryptfs|encrypt|luks|gpg\b|crypt\b'),
    ('cryptography-keys', r'.*'),
]

SYSTEMS_RULES = [
    ('consensus', r'raft|paxos|byzantine|consensus|zab\b|zookeeper'),
    ('consistency-models', r'consistency|coherence|quorum|replica'),
    ('storage-file-systems', r'gfs\b|colossus|leveldb|samba|file-system|filesystem|storage|s3\b|gcs\b|azure'),
    ('big-data-systems', r'hadoop|hdfs|mapreduce|spark|stream|benchmark|puma\b|amplab|cosmos|nosql'),
    ('low-level-systems', r'x86|assembly|instruction|encoding|isa\b'),
    ('engineering-lessons', r'.*'),
]


def parse_ground_truth():
    gt = {}
    for page in GROUND_TRUTH_PAGES:
        with open(page, encoding='utf-8') as f:
            text = f.read()
        topic = None
        for line in text.splitlines():
            m = re.match(r'^### (.+)$', line)
            if m:
                topic = m.group(1).strip()
                continue
            if topic in TOPIC_SLUGS:
                for url in re.findall(r'\]\((/([^/)]+)/)\)', line):
                    gt[url[1]] = TOPIC_SLUGS[topic]
    return gt


def classify(slug, title, old_cat, gt):
    if slug in gt:
        return gt[slug]
    if old_cat in CATEGORY_MAP:
        return CATEGORY_MAP[old_cat]
    hay = slug + ' ' + title.lower()
    if old_cat in ('linux-systems-administration', 'linux-system-configuration',
                   'system-administration-cloud'):
        for rules in (LINUX_RULES, PROGRAMMING_RULES):
            for cat, pattern in rules:
                if re.search(pattern, hay):
                    return cat
        return 'general-system-administration'
    if old_cat == 'scripting-utilities':
        for rules in (PROGRAMMING_RULES, LINUX_RULES):
            for cat, pattern in rules:
                if re.search(pattern, hay):
                    return cat
        return 'shell-scripting'
    rules = {
        'systems-architecture': SYSTEMS_RULES,
        'security-cryptography-2': SECURITY_RULES,
        'blockchain-cryptocurrency': WEB3_RULES,
        'ai-engineering': [('cli-ai-integration', r'openclaw|agent|cli|transformed|topic-tag'), ('model-fundamentals', r'.*')],
    }.get(old_cat)
    if rules:
        for cat, pattern in rules:
            if re.search(pattern, hay):
                return cat
    if old_cat in ('programming-languages', 'algorithms-data-structures', 'web-development',
                   'databases-storage', 'testing-devops', 'packages-desktop-applications'):
        return old_cat
    return 'general-system-administration' if old_cat.startswith(('linux', 'system')) else None


def main():
    gt = parse_ground_truth()
    print(f'ground truth: {len(gt)} posts')
    dist = collections.Counter()
    unmatched = []
    changed = 0
    for path in sorted(glob.glob('_posts/*.md')):
        with open(path, encoding='utf-8') as f:
            text = f.read()
        m = re.search(r'^categories: \[([a-z0-9-]+)(?:, ?[a-z0-9-]+)*\]$', text, re.M)
        if not m:
            unmatched.append(('no-categories-line', path))
            continue
        old_cat = m.group(1)
        fm = re.search(r'^title: ["\']?(.+?)["\']?$', text, re.M)
        title = fm.group(1) if fm else ''
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', path.split('/')[-1][:-3])
        new_cat = classify(slug, title, old_cat, gt)
        if new_cat is None:
            unmatched.append((old_cat, path))
            continue
        dist[new_cat] += 1
        if new_cat != old_cat:
            changed += 1
            if APPLY:
                text = text[:m.start()] + f'categories: [{new_cat}]' + text[m.end():]
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(text)
    print(f'\n{"applied" if APPLY else "dry run"}: {changed} posts re-tagged')
    for cat, n in dist.most_common():
        print(f'  {n:4d}  {cat}')
    if unmatched:
        print(f'\n{len(unmatched)} unmatched:')
        for reason, path in unmatched[:20]:
            print(f'  {reason}: {path}')


if __name__ == '__main__':
    main()
