FROM plone/plone:4.3.15

ARG PLONEGOVBR_VERSION=${PLONEGOVBR_VERSION:-latest}

LABEL Name="Identidade Digital para o Governo Brasileiro Federal para Plone" \
      maintainer="https://github.com/plonegovbr" \
      PloneGovBR.Version="$PLONEGOVBR_VERSION" \
      Architecture="x86_64" \
      Dockerfile_location="/root/buildinfo"

USER plone
COPY site.cfg /plone/instance/

USER root
COPY Dockerfile /root/buildinfo

# Para Pillow
RUN set -ex; \
 buildDeps="build-essential=11.7 \ 
               curl=7.38.0-4+deb8u7 \
               libbz2-dev=1.0.6-7+b3 \
               libjpeg62-turbo-dev=1:1.3.1-12 \
               libssl-dev=1.0.1t-1+deb8u7 \
               libxml2-dev=2.9.1+dfsg1-5+deb8u5 \
               libxslt1-dev=1.1.28-2+deb8u3 \
               libyaml-dev=0.1.6-3 \
               python-setuptools=5.5.1-1 \
               python-dev=2.7.9-1 \
               sudo=1.8.10p3-1+deb8u4"; \
 apt-get update; \
 apt-get -y --no-install-recommends install $buildDeps; \
 sed -i -e "s/PLONEGOVBR_VERSION/$PLONEGOVBR_VERSION/g" site.cfg; \
 sudo -u plone bin/buildout -c site.cfg -t 300; \
 SUDO_FORCE_REMOVE=yes apt-get -y --auto-remove purge $buildDeps; \
 rm -rf /var/lib/apt/lists/*; \
 rm -rf /plone/buildout-cache/downloads/*; \
 apt-get clean; \
 find /plone \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' +

USER plone
