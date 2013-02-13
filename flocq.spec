# This package is really noarch, but it has to be installed in an arch-specific
# location, so we build it as an arch-specific package.
%global debug_package %{nil}
%global flocqdir %{_libdir}/coq/user-contrib/Flocq
%global coqver 8.4pl1

Name:           flocq
Version:        2.1.0
Release:        4%{?dist}
Summary:        Formalization of floating point numbers for Coq

Group:          Applications/Engineering
License:        LGPLv3+
URL:            http://flocq.gforge.inria.fr/
Source0:        https://gforge.inria.fr/frs/download.php/30884/%{name}-%{version}.tar.gz

BuildRequires:  coq%{?_isa} = %{coqver}
Requires:       coq%{?_isa} = %{coqver}

ExclusiveArch: %{ocaml_arches}

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package source
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

# Remove this once F16 reaches EOL.
Obsoletes:      %{name}-devel < 2.0.0
Provides:       %{name}-devel = %{version}-%{release}

%description source
This package contains the source Coq files for flocq.  These files are
not needed to use flocq.  They are made available for informational
purposes.

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
cp -p src/*.v $RPM_BUILD_ROOT%{flocqdir}
cp -p src/Appli/*.v $RPM_BUILD_ROOT%{flocqdir}/Appli
cp -p src/Calc/*.v $RPM_BUILD_ROOT%{flocqdir}/Calc
cp -p src/Core/*.v $RPM_BUILD_ROOT%{flocqdir}/Core
cp -p src/Prop/*.v $RPM_BUILD_ROOT%{flocqdir}/Prop

%files
%doc AUTHORS COPYING NEWS README html
%{flocqdir}
%exclude %{flocqdir}/*.v
%exclude %{flocqdir}/*/*.v

%files source
%{flocqdir}/*.v
%{flocqdir}/Appli/*.v
%{flocqdir}/Calc/*.v
%{flocqdir}/Core/*.v
%{flocqdir}/Prop/*.v

%changelog
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 2.1.0-3
- Rebuild for coq 8.4pl1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 2.1.0-2
- Rebuild for coq 8.4

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- New upstream release
- Build for OCaml 4.0.0 and coq 8.3pl4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 2.0.0-3
- Rebuild for OCaml 3.12.1

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 2.0.0-2
- Rebuild for coq 8.3pl3

* Mon Dec 12 2011 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- New upstream release
- Change subpackage from -devel to -source to match gappalib-coq.

* Fri Oct 28 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-3
- Fix broken version numbers in BR and Requires

* Wed Oct 26 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Split out a -devel subpackage

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Initial RPM
