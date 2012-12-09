# revision 24965
# category Package
# catalog-ctan /info/pictex/summary
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-pictexsum
Version:	20060827
Release:	1
Summary:	A summary of PicTeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/pictex/summary
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictexsum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictexsum.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060827-1
+ Revision: 759001
- texlive-pictexsum
- texlive-pictexsum

