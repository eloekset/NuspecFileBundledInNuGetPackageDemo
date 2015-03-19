<?xml version="1.0" encoding="utf-8"?>
<!-- Todo:
        Copy this template file and name it whatever you like, but change file extension from .spec to .nuspec. 
        Then replace the following:
          -id
          -title
          -description
          -tags
          -dependencies
          -files
            
        Version is set automatically by the custom build script. Your nuspec file will be copied to a new nuspec file for every version.
-->
<package xmlns="http://schemas.microsoft.com/packaging/2011/08/nuspec.xsd">
  <metadata>
    <id>enter-nuget-package-id</id>
    <version>0.0.0</version>
    <title>enter-title-of-nuget-package-similar-to-package-id</title>
    <authors>eloekset</authors>
    <owners>My Company</owners>
    <requireLicenseAcceptance>false</requireLicenseAcceptance>
    <description>enter-description-for-this-nuget-package</description>
    <releaseNotes></releaseNotes>
    <copyright>My Company 2015</copyright>
    <tags>js, JavaScript</tags>
    <dependencies>
      <dependency id="jQuery" version="1.10.0" />
    </dependencies>
  </metadata>
  <files>
    <file src="..\..\bin\js\target-js-file-name.js" target="content\Scripts\target-js-file-name.js" />
  </files>
</package>