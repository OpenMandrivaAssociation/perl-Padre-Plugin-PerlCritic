%define upstream_name    Padre-Plugin-PerlCritic
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Analyze perl files with Perl::Critic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Padre)
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Install)
BuildArch:	noarch

%description
Padre plugin to analyze perl files with Perl::Critic.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
# no testing, wx dies on missing display
#make test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 657814
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 623000
- new version

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 562998
- update to 0.08

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 513477
- update to 0.07

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 401619
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-2mdv2010.0
+ Revision: 371827
- bumping mkrel to force re-submission

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-1mdv2010.0
+ Revision: 369799
- update to new version 0.06

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 328975
- removing testing (wx dies with wrong display
- import perl-Padre-Plugin-PerlCritic


* Tue Jan 13 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

