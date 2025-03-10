Name:		texlive-pictexsum
Version:	24965
Release:	2
Summary:	A summary of PicTeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/pictex/summary
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictexsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictexsum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document summarises the commands of PicTeX. While it is no
substitute for the PicTeX manual itself (available from
Personal TeX inc.), the document is a useful aide-memoire for
those who have read the manual.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/pictexsum/Makefile
%doc %{_texmfdistdir}/doc/latex/pictexsum/README
%doc %{_texmfdistdir}/doc/latex/pictexsum/a4mod.sty
%doc %{_texmfdistdir}/doc/latex/pictexsum/pictexsum.pdf
%doc %{_texmfdistdir}/doc/latex/pictexsum/pictexsum.tex
%doc %{_texmfdistdir}/doc/latex/pictexsum/useful.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
