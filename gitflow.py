# __GitFlow TL;DR/Summary:__
# GitFlow is a branching model for Git, created by Vincent Driessen. 
# It has attracted a lot of attention because it is very well suited to collaboration and scaling the development team.

# One of the great things about GitFlow is that it makes parallel development very easy, by isolating new development from finished work. 
# New development (such as features and non-emergency bug fixes) is done in feature branches, and is only merged back into main body of code
# when the developer(s) is happy that the code is ready for release.

# How it works:

# New development (new features, non-emergency bug fixes) are built in feature branches
# Feature branches are branched off of the develop branch, and finished features and fixes are merged back into the develop branch when they’re ready for release.
# When it is time to make a release, a release branch is created off of develop
# The code in the release branch is deployed onto a suitable test environment, tested, and any problems are fixed directly in the release branch.
# When the release is finished, the release branch is merged into master and into develop too, to make sure that any changes 
# made in the release branch aren’t accidentally lost by new development
