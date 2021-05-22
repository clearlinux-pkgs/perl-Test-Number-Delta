#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Number-Delta
Version  : 1.06
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Number-Delta-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Number-Delta-1.06.tar.gz
Summary  : 'Compare the difference between numbers against a given tolerance'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Test-Number-Delta-license = %{version}-%{release}
Requires: perl-Test-Number-Delta-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::Number::Delta - Compare the difference between numbers against a
given tolerance

%package dev
Summary: dev components for the perl-Test-Number-Delta package.
Group: Development
Provides: perl-Test-Number-Delta-devel = %{version}-%{release}
Requires: perl-Test-Number-Delta = %{version}-%{release}

%description dev
dev components for the perl-Test-Number-Delta package.


%package license
Summary: license components for the perl-Test-Number-Delta package.
Group: Default

%description license
license components for the perl-Test-Number-Delta package.


%package perl
Summary: perl components for the perl-Test-Number-Delta package.
Group: Default
Requires: perl-Test-Number-Delta = %{version}-%{release}

%description perl
perl components for the perl-Test-Number-Delta package.


%prep
%setup -q -n Test-Number-Delta-1.06
cd %{_builddir}/Test-Number-Delta-1.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Number-Delta
cp %{_builddir}/Test-Number-Delta-1.06/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Number-Delta/5304bf21bd261ac05d4427fc4d0b971e8b2731cc
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Number::Delta.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Number-Delta/5304bf21bd261ac05d4427fc4d0b971e8b2731cc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/Number/Delta.pm
