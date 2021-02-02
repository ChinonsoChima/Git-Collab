# __GitFlow TL;DR/Summary:__
# GitFlow is a branching model for Git, created by Vincent Driessen. 
# It has attracted a lot of attention because it is very well suited to collaboration and scaling the development team.

# One of the great things about GitFlow is that it makes parallel development very easy, by isolating new development from finished work. 
# New development (such as features and non-emergency bug fixes) is done in feature branches, and is only merged back into main body of code
# when the developer(s) is happy that the code is ready for release.

# __How it works__:

# New development (new features, non-emergency bug fixes) are built in feature branches
# Feature branches are branched off of the develop branch, and finished features and fixes are merged back into the develop branch when they’re ready for release.
# When it is time to make a release, a release branch is created off of develop
# The code in the release branch is deployed onto a suitable test environment, tested, and any problems are fixed directly in the release branch.
# When the release is finished, the release branch is merged into master and into develop too, to make sure that any changes 
# made in the release branch aren’t accidentally lost by new development

# __GitFlow Explanation:__
# The GitFlow workflow consists of five branches: _Master/Main_, _Develop_, _Features_, _Release_, and _Hotfixes_.

# **The workflow of the five branches fall in a downward motion, parallel, with commits marked and labeled on each branch in accordance to their time of commit.**

# _Branchings:_
Master tracks release-code only! Only merges from Release and Hotfixes branches. 

# Feature branches make it easier for multiple developers to work on the same feature simultaneously. <br>New features and non-emergency bug fixes are built-i feature branches. <br>Features are branched off of the Developer branch, then merged to Release.

# New features and non-emergency bug fixes are built-in Feature branches. <br>New development is merged back onto the development branch as its completed. <br>The Development branch is the staging area for all unreleased and completed features.

# Hotfixes branches are made from a tagged release, typically used to make an emergency change but must only contain the emergency fix.

# When it's time for a release, a Release branch is made off of the Develop branch.

# Code from the Release branch is deployed in a proper environment for testing and bugs are fixed directly on the release branch in the Develop -> Test -> Fix -> Redeploy -> Retest cycle until the code is considered release-worthy.
