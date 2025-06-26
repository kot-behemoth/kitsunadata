---
title: Deployment
---

# Deploying to single host (Dokku)

Kitsuna reocmmends using [Dokku](https://dokku.com) for simple deployments to single-host environments.

Here are the steps to deploy Kitsuna (the Metabase and ELT services) using Dokku on a Digital Ocean droplet with your own domain.

## HOST setup

```bash
# usually your key is already available under the current user's `~/.ssh/authorized_keys` file
cat ~/.ssh/authorized_keys | dokku ssh-keys:add admin

# you can use any domain you already have access to
# this domain should have an A record or CNAME pointing at your server's IP
dokku domains:set-global <YOUR_DOMAIN>

# you can also use the ip of your server
dokku domains:set-global 46.101.6.245

# finally, you can use sslip.io to get subdomain support
# as you would with a regular domain name
# this would be done by appending `.sslip.io` to your ip address
dokku domains:set-global 10.0.0.2.sslip.io
```

## Initial setup (HOST)

```bash

# Create the applications
dokku apps:create metabase
dokku apps:create elt

# Apply app.json configurations
dokku app-json:set metabase appjson-path .dokku/metabase.app.json
dokku app-json:set elt appjson-path .dokku/elt.app.json

# Set up persistent storage for Metabase
dokku storage:ensure-directory metabase --path=/var/lib/dokku/data/storage/metabase-data
dokku storage:ensure-directory metabase --path=/var/lib/dokku/data/storage/db

dokku storage:ensure-directory elt --path=/var/lib/dokku/data/storage/db

# TODO: add the missing mount commands
```

## Domain Configuration (HOST)

```bash
# Install Let's Encrypt plugin (required by metabase app.json)
dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git

dokku domains:set metabase metabase.<YOUR_DOMAIN>

dokku letsencrypt:set metabase email <YOUR_EMAIL@ADDRESS>
dokku letsencrypt:enable metabase
```

## DNS Configuration

Add these DNS records in your Digital Ocean DNS settings for kitsunadata.com:

1. Add an A record pointing `metabase.<YOUR_DOMAIN>` to your Digital Ocean droplet's IP address

## Deployment (LOCAL)

These are run locally from your repo.

```bash
# Add Dokku as a remote to your Git repository
git remote add dokku-metabase dokku@<YOUR_DOMAIN>:metabase
git remote add dokku-elt dokku@<YOUR_DOMAIN>:elt

# Deploy your applications
git push dokku-metabase main
git push dokku-elt main
```

Replace `<YOUR_DOMAIN>` with your actual Dokku server address and `<YOUR_EMAIL@ADDRESS>` with your actual email.
