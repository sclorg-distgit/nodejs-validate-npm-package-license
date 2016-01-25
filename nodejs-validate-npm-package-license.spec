%{?scl:%scl_package nodejs-validate-npm-package-license}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-validate-npm-package-license

%global npm_name validate-npm-package-license
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-validate-npm-package-license
Version:	3.0.1
Release:	1%{?dist}
Summary:	Give me a string and I'll tell you if it's a valid npm package license string
Url:		https://github.com/kemitchell/validate-npm-package-license.js#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	Apache-2.0

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(defence-cli)
BuildRequires:	%{?scl_prefix}npm(replace-require-self)
%endif

BuildRequires:	%{?scl_prefix}npm(spdx-correct)
BuildRequires:	%{?scl_prefix}npm(spdx-expression-parse)

Requires:	%{?scl_prefix}npm(spdx-correct)
Requires:	%{?scl_prefix}npm(spdx-expression-parse)

%description
Give me a string and I'll tell you if it's a valid npm package license string

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/validate-npm-package-license

%doc README.md
%doc LICENSE

%changelog
* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-1
- Initial build
