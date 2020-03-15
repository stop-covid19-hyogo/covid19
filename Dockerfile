FROM node:10.19-alpine

ARG project_dir=/app

WORKDIR ${project_dir}

COPY package.json yarn.lock ./

RUN set -x && \
    yarn install

COPY . ${project_dir}

EXPOSE 3000
ENV HOST 0.0.0.0

CMD ["yarn", "dev"]
