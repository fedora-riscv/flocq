# This package is really noarch, but it has to be installed in an arch-specific
# location, so we build it as an arch-specific package.
%global debug_package %{nil}
%global flocqdir %{_libdir}/coq/user-contrib/Flocq
%global coqver 8.4pl6

Name:           flocq
Version:        2.4.0
Release:        8%{?dist}
Summary:        Formalization of floating point numbers for Coq

Group:          Applications/Engineering
License:        LGPLv3+
URL:            http://flocq.gforge.inria.fr/
Source0:        https://gforge.inria.fr/frs/download.php/file/33979/%{name}-%{version}.tar.gz

BuildRequires:  remake
BuildRequires:  coq%{?_isa} = %{coqver}
Requires:       coq%{?_isa} = %{coqver}

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package source
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description source
This package contains the source Coq files for flocq.  These files are
not needed to use flocq.  They are made available for informational
purposes.

%prep
%setup -q

%build
# We do NOT want to specify --libdir, and we don't need CFLAGS, etc.
./configure

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake
remake %{?_smp_mflags} all doc

%install
sed -i "s,%{_libdir},$RPM_BUILD_ROOT%{_libdir}," Remakefile
remake install

# Also install the source files
cp -p src/*.v $RPM_BUILD_ROOT%{flocqdir}
cp -p src/Appli/*.v $RPM_BUILD_ROOT%{flocqdir}/Appli
cp -p src/Calc/*.v $RPM_BUILD_ROOT%{flocqdir}/Calc
cp -p src/Core/*.v $RPM_BUILD_ROOT%{flocqdir}/Core
cp -p src/Prop/*.v $RPM_BUILD_ROOT%{flocqdir}/Prop

%files
%doc AUTHORS NEWS README html
%license COPYING
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
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 2.4.0-7
- Rebuild for coq 8.4pl6

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-6
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-5
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-4
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-3
- Rebuild with coq that was rebuilt with ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-2
- Rebuild for coq 8.4pl5

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- New upstream release

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-9
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-8
- Bump release and rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-7
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-5
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-4
- Bump and rebuild as part of ocaml rebuild
- Fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-2
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- New upstream release
- Remove ocaml_arches macro (bz 1087794)

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- New upstream release

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-2
- Rebuild for coq 8.4pl3

* Sat Aug 10 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- New upstream release
- Builds now done with remake instead of make

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 2.1.0-5
- Rebuild for coq 8.4pl2

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
