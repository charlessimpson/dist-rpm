# Overview

RPM specs for binary distributions of some common packages.

RPMs are typically built from source and tailored to their particular
distribution through RPM specs and packaging guidelines. Sometimes though,
we're just looking for a way to control an entire binary distribution of a
piece of software.  We want something more controlled than untar'ing a tarball
into a directory, but something less complicated than a distribution-specific
collection of RPMs.

The spec files provided certainly don't meet any distribution's packaging
guidelines that we're aware of, and are designed to be tailored for a
particular environment.  Don't need the documentation or the source code?  Just
`%exclude` the relevant directories.

## -dist Suffix

We chose the suffix `-dist` to distinguish packages built from their binary
distributions from the actual packages provided by OS vendors.

## -common Packages

Many large Java programs may have a few native components that could be package
separately from their architecture independent parts. Rather than repackage the
entire Java program, we package the noarch parts (the majority of the package)
into a -common package, put the native components their own architecture
dependent packages, then make the architecture dependent packages depend on the
common packages. This allows someone to get both the native and common parts by
installing a single RPM.

## RPATHs

Some pre-compiled libraries contain invalid RPATHs, which can cause the
packaging process to fail.  In those cases, we define `QA_SKIP_RPATHS=2` from
within the spec file to allow the packaging process to continue.

It would be preferable to use chrpath to remove rpaths from libraries, but that
doesn't work when building for a target other than the native one (i.e.
building for i686 on x86\_64).  Instead, redefine `__arch_install_post` to
allow invalid rpaths. This is a hack in case the behavior of `
__arch_install_post` ever changes in the future, but keeps us from having to
define an environment variable external to rpmbuild.  This results in the error
"Too many levels of recursion in macro expansion. It is likely caused by
recursive macro declaration.", but the build succeeds.

## Build IDs

Some pre-compiled libraries are missing [Build
ID's](https://fedoraproject.org/wiki/Releases/FeatureBuildId), which can cause
the packaging process to fail.  In those cases, we undefine
`_missing_build_ids_terminate_build` to allow the packaging process to
continue.

## Relocations

All of the provided specs build relocatable packages.  Pass `--prefix` to `rpm`
when installing to put the packages in the directory of your choice.  By
default, the packages are installed into `/opt/package-version`.

# quickbuild

quickbuild is a tool to simplify building RPMs from the provided specs.  In the
simplest case, just provide a copy of distribution tarballs (with names
matching the `Source` lines in the spec file) and quickbuild will create the
correct rpmbuild directory structure, copy the spec and source into the right
places, invoke rpmbuild, and copy the packaged artifacts to a destination
directory.

## Usage

    quickbuild [-k] [-v] [-d DST] [-t TOPDIR] [-o OPT...] SPEC SOURCE...

## Options

    -k          keep rpmbuild directory
    -v          make the rpmbuild command verbose
    -d DST      copy RPMs into directory DST (default is .)
    -t TOPDIR   use TOPDIR as rpmbuild directory instead of creating one
    -o OPT      pass OPT to rpmbuild
    -h          show help

## Examples

Build jetty from the tarball `jetty-distribution-9.1.0.v20131115.tar.gz`:

    quickbuild jetty9-dist.spec jetty-distribution-9.1.0.v20131115.tar.gz

Build Hadoop native components (which are distributed only in 32-bit) on a
64-bit host:

    quickbuild -o "--target i686" hadoop2-dist-native.spec hadoop-2.2.0.tar.gz
