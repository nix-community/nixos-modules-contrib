# NixOS Modules: Contrib

Useful NixOS modules which may not belong in the Nixpkgs repository
itself.

# Contributing

Feel free to create a new directory with your module. Use CODEOWNERS
to add yourself as a required reviewer for changes to that directory.

# Modules

## auto-raid0

Automatically create LVM-based RAID-0 logical volumes on startup.
Originally in NixOps, removed in 2.0.

## auto-luks

Automatically create LUKS-encrypted volumes, decrypted with
`deployment.keys`. Originally in NixOps, removed in 2.0.
