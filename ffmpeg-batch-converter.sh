#!/bin/bash

# Project Page: https://github.com/NodeWee/macOS-Workflow
# Author: 穿卡芦苇（nodewee@gmail.com , http://nodewee.github.io/）
# License: MIT License
# Version: 2020.01.28

# TODO
# - 目的文件夹的路径为空，则默认使用源文件夹的路径
# - 支持使用 ffmpeg 的参数
# - 检查是否安装了 ffmpeg
# - 自动安装 ffmpeg

clear

# 获取当前解释器名称
cur_interpreter=`ps h -p $$ -o args='' | cut -f1 -d' '`
cur_interpreter=${cur_interpreter##*/}

# 指定使用 bash 解释器
[ "$cur_interpreter" != 'bash' ] && (
  bash "$0"
  exit 0
)

echo '===== FFMPEG 批量转换媒体文件 ==='

read -p "请输入源（待转换）文件夹路径：" src_dir
if [ -z "$src_dir" ]; then
  exit 0
fi

if [ ! -d $src_dir ]; then
  echo "路径不存在: $src_dir"
  exit 1
fi

cd $src_dir

read -p "请输入目的（转换后）文件夹的路径：" dest_dir
if [ -z "$dest_dir" ]; then
  exit 0
fi

if [ ! -d $dest_dir ]; then
  echo "路径不存在: $dest_dir"
  exit 1
fi


read -p "请输入源文件格式(例如：.avi):" src_type
[ -z "$src_type" ] && (
  echo "源文件格式不能为空"
  exit 1
)

read -p "请输入目标格式(例如：.mp3):" dest_type
[ -z "$dest_type" ] && (
  echo "目标格式不能为空"
  exit 1
)

extname="*$src_type"
for file in $(ls $extname); do
  if [[ -f $file ]]; then
    filename=$(basename "$file")
    noextname="${filename%.*}"
    dest_path="$dest_dir/$noextname$dest_type"
    echo "$dest_path"
    ffmpeg -i "$file" "$noextname$dest_type"
  else
    echo "not file: $file"
  fi
done
