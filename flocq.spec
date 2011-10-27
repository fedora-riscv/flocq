# This package is really noarch, but it has to be installed in an arch-specific
# location, so we build it as an arch-specific package.
%global debug_package %{nil}
%global flocqdir %{_libdir}/coq/user-contrib/Flocq

Name:           flocq
Version:        1.4.0
Release:        2%{?dist}
Summary:        Formalization of floating point numbers for Coq

Group:          Applications/Engineering
License:        LGPLv3+
URL:            http://flocq.gforge.inria.fr/
Source0:        https://gforge.inria.fr/frs/download.php/28389/%{name}-%{version}.tar.gz

BuildRequires:  coq
Requires:       coq = %(coqc -v | sed -nr "s/.* version ([[:alnum:]\.]+) .*/\1/p")

# This must match the corresponding line in the coq spec
ExclusiveArch: %{ocaml_arches}

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package devel
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the source Coq files for flocq.  These files are
not needed by consuming packages.

%prep
%setup -q

%build
# We do NOT want to specify --libdir, and we don't need CFLAGS, etc.
./configure

# %%{?_smp_mflags} sometimes succeeds, sometimes fails...
make all html

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Also install the source files
cp -p src/Appli/*.v $RPM_BUILD_ROOT%{flocqdir}/Appli
cp -p src/Calc/*.v $RPM_BUILD_ROOT%{flocqdir}/Calc
cp -p src/Core/*.v $RPM_BUILD_ROOT%{flocqdir}/Core
cp -p src/Prop/*.v $RPM_BUILD_ROOT%{flocqdir}/Prop

%files
%doc AUTHORS COPYING NEWS README html
%dir %{flocqdir}
%dir %{flocqdir}/Appli
%dir %{flocqdir}/Calc
%dir %{flocqdir}/Core
%dir %{flocqdir}/Prop
%{flocqdir}/Appli/*.vo
%{flocqdir}/Calc/*.vo
%{flocqdir}/Core/*.vo
%{flocqdir}/Prop/*.vo

%files devel
%{flocqdir}/Appli/*.v
%{flocqdir}/Calc/*.v
%{flocqdir}/Core/*.v
%{flocqdir}/Prop/*.v

%changelog
* Wed Oct 26 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Split out a -devel subpackage

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Initial RPM
