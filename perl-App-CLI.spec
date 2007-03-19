#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	App
%define	pnam	CLI
Summary:	App::CLI - Dispatcher module for command line interface programs
#Summary(pl):	
Name:		perl-App-CLI
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CL/CLKAO/App-CLI-0.07.tar.gz
# Source0-md5:	8981b0628874bb7e83b00b00e58a7259
URL:		http://search.cpan.org/dist/App-CLI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Getopt::Long) >= 2.35
BuildRequires:	perl(Locale::Maketext::Simple)
BuildRequires:	perl(Pod::Simple::Text)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
App::CLI dispatches CLI (command line interface) based commands
into command classes.  It also supports subcommand and per-command
options.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/App/*.pm
%{perl_vendorlib}/App/CLI
%{_mandir}/man3/*