FROM plone:4.3.18

ARG PLONEGOVBR_VERSION=${PLONEGOVBR_VERSION:-latest}

LABEL Name="Identidade Digital para o Governo Brasileiro Federal para Plone" \
      maintainer="https://github.com/plonegovbr" \
      PloneGovBR.Version="$PLONEGOVBR_VERSION" \
      Architecture="x86_64" \
      Dockerfile_location="/root/buildinfo"

COPY site.cfg /plone/instance/
COPY Dockerfile /root/buildinfo

# Para Pillow
RUN set -ex; \
 buildDeps="build-essential \
              zlib1g-dev \
              libbz2-dev \
              libjpeg62-turbo-dev \
              libssl-dev \
              libxml2-dev \
              libxslt1-dev \
              libyaml-dev \
              python-setuptools \
              python-dev"; \
 apt-get update; \
 apt-get -y --no-install-recommends install $buildDeps; \
 sed -i -e "s/PLONEGOVBR_VERSION/$PLONEGOVBR_VERSION/g" site.cfg; \
 gosu plone buildout -c site.cfg -t 300; \
 SUDO_FORCE_REMOVE=yes apt-get -y --auto-remove purge $buildDeps; \
 rm -rf /var/lib/apt/lists/*; \
 rm -rf /plone/buildout-cache/downloads/*; \
 apt-get clean; \
 find /plone \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' +
