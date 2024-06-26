Name:         	VMN
Version:      	0.3.4
Release:      	1
Summary:      	Version manager for node and python
License:      	MIT
URL: 			https://github.com/vineelsai26/VMN
Source: 		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	go
BuildRequires:	git

%description
Version manager for Node.js and Python

%define debug_package %{nil}

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
go build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 vmn %{buildroot}/usr/bin/vmn

%files
/usr/bin/vmn

%changelog
* Sun Apr 28 2024 Vineel Sai <mail@vineelsai.com> 0.3.4-1
- remove redundant checks + print extraction path (mail@vineelsai.com)
- run release repo under environment (mail@vineelsai.com)
- remove verbose tar log and run on mac and cache builds for all of 3.12-3.9
  (mail@vineelsai.com)
- run precompile steps for macos and linux (mail@vineelsai.com)
- run tests on macos (mail@vineelsai.com)
- fix version issue python (mail@vineelsai.com)
- run tests on windows and test compiled an precompiled python installes
  (mail@vineelsai.com)
- only run tests on ubuntu for now (mail@vineelsai.com)

* Wed Apr 24 2024 Vineel Sai <mail@vineelsai.com> 0.3.3-1
- only test with one version (mail@vineelsai.com)

* Wed Apr 24 2024 Vineel Sai <mail@vineelsai.com> 0.3.2-1
- fix spec file (mail@vineelsai.com)
- Automatic commit of package [VMN] release [0.3.1-1]. (mail@vineelsai.com)

* Wed Apr 24 2024 Vineel Sai <mail@vineelsai.com> 0.3.1-1
- remove .copr (mail@vineelsai.com)

* Wed Apr 24 2024 Vineel Sai <mail@vineelsai.com> 0.3.0-1
- make rpm package test1 (mail@vineelsai.com)
- Delete .github/workflows/codeql.yml (mail@vineelsai.com)
- set go version to 1.22 and python install fixes (mail@vineelsai.com)
- trim prefix (mail@vineelsai.com)
- update go version (mail@vineelsai.com)
- Create codeql.yml (mail@vineelsai.com)
- gomod: bump golang.org/x/sys from 0.17.0 to 0.19.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- fix some linux issues (mail@vineelsai.com)
- security issue fix for ".." in filename (mail@vineelsai.com)
- gomod: bump golang.org/x/sys from 0.16.0 to 0.17.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- remove --enable-loadable-sqlite-extensions flag (mail@vineelsai.com)
- change default flags (mail@vineelsai.com)
- fix bash syntax issue (mail@vineelsai.com)
- fix linux eval issue (mail@vineelsai.com)
- python install from precompiled package (mail@vineelsai.com)
- make command detection (mail@vineelsai.com)
- move current python implementation behind a flag (mail@vineelsai.com)
- gomod: bump golang.org/x/sys from 0.15.0 to 0.16.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- github-actions: bump actions/setup-go from 4 to 5
  (49699333+dependabot[bot]@users.noreply.github.com)
- gomod: bump golang.org/x/sys from 0.14.0 to 0.15.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- gomod: bump golang.org/x/sys from 0.13.0 to 0.14.0
  (49699333+dependabot[bot]@users.noreply.github.com)

* Wed Apr 24 2024 Vineel Sai <mail@vineelsai.com>
- make rpm package test1 (mail@vineelsai.com)
- Delete .github/workflows/codeql.yml (mail@vineelsai.com)
- set go version to 1.22 and python install fixes (mail@vineelsai.com)
- trim prefix (mail@vineelsai.com)
- update go version (mail@vineelsai.com)
- Create codeql.yml (mail@vineelsai.com)
- gomod: bump golang.org/x/sys from 0.17.0 to 0.19.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- fix some linux issues (mail@vineelsai.com)
- security issue fix for ".." in filename (mail@vineelsai.com)
- gomod: bump golang.org/x/sys from 0.16.0 to 0.17.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- remove --enable-loadable-sqlite-extensions flag (mail@vineelsai.com)
- change default flags (mail@vineelsai.com)
- fix bash syntax issue (mail@vineelsai.com)
- fix linux eval issue (mail@vineelsai.com)
- python install from precompiled package (mail@vineelsai.com)
- make command detection (mail@vineelsai.com)
- move current python implementation behind a flag (mail@vineelsai.com)
- gomod: bump golang.org/x/sys from 0.15.0 to 0.16.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- github-actions: bump actions/setup-go from 4 to 5
  (49699333+dependabot[bot]@users.noreply.github.com)
- gomod: bump golang.org/x/sys from 0.14.0 to 0.15.0
  (49699333+dependabot[bot]@users.noreply.github.com)
- gomod: bump golang.org/x/sys from 0.13.0 to 0.14.0
  (49699333+dependabot[bot]@users.noreply.github.com)

* Wed Apr 24 2024 Vineel Sai <mail@vineelsai.com> - 0.2.4-1
- Initial srpm build
