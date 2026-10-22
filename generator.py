#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clash Dual Fusion Configuration Generator
双订阅合体智能分流生成器

用法:
    python generator.py
或:
    python generator.py --premium "https://..." --cheap "https://..." -o dual_fusion.yaml
"""

import sys
import os
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

TEMPLATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.template.yaml")

def print_banner():
    print("=" * 65)
    print(" 🚀 Clash Dual Fusion: 双订阅合体智能分流生成器")
    print(" 📌 AI 严格走优质纯净节点 | 日常视频与常规外网走一般节点 | 国内游戏与 B 站全直连")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Clash 双订阅合体智能分流配置生成器")
    parser.add_argument("-p", "--premium", help="纯净/优质 AI 订阅链接 (如 TAG / 原生住宅 / 纯净专线)")
    parser.add_argument("-c", "--cheap", help="一般/劣质节点订阅链接 (如日常高流量 / 廉价机场)")
    parser.add_argument("-o", "--output", default="dual_fusion.yaml", help="输出文件名 (默认: dual_fusion.yaml)")
    parser.add_argument("--port", type=int, default=7897, help="Clash 混合代理端口 (默认: 7897)")
    
    args = parser.parse_args()

    if not os.path.exists(TEMPLATE_FILE):
        print(f"❌ 错误：找不到模板文件 {TEMPLATE_FILE}")
        sys.exit(1)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    premium_url = args.premium
    cheap_url = args.cheap

    if not premium_url or not cheap_url:
        print_banner()
        print("\n请分别输入你的两个订阅链接：\n")
        while not premium_url:
            premium_url = input("👉 1. 请粘贴【纯净 AI 优质订阅链接】 (如 TAG / 原生住宅): ").strip()
            if not premium_url.startswith("http"):
                print("   ⚠️ 订阅链接必须以 http:// 或 https:// 开头，请重新输入！")
                premium_url = None

        while not cheap_url:
            cheap_url = input("👉 2. 请粘贴【便宜日常一般/劣质节点订阅链接】 (如 160G/几百G 廉价机场): ").strip()
            if not cheap_url.startswith("http"):
                print("   ⚠️ 订阅链接必须以 http:// 或 https:// 开头，请重新输入！")
                cheap_url = None

    print("\n⏳ 正在生成合体分流配置...")

    # 替换变量
    final_content = template_content.replace("__PREMIUM_AI_SUBSCRIPTION_URL__", premium_url)
    final_content = final_content.replace("__GENERAL_SUBSCRIPTION_URL__", cheap_url)
    if args.port != 7897:
        final_content = final_content.replace("mixed-port: 7897", f"mixed-port: {args.port}")

    output_path = os.path.abspath(args.output)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    print("\n" + "=" * 65)
    print(f"✅ 生成成功！文件已保存至：")
    print(f"👉 {output_path}")
    print("=" * 65)
    print("\n📖 使用方法 (以 Clash Verge Rev 为例)：")
    print("  1. 打开 Clash Verge Rev -> 进入【订阅】(Profiles)")
    print("  2. 点击右上角【新建】 -> 类型选择【Local (本地配置)】")
    print("  3. 将生成的 dual_fusion.yaml 拖入窗口中，或点击导入并选择该文件")
    print("  4. 右键该配置卡片 -> 选择【使用】(Select)")
    print("  5. 在【代理】界面中：")
    print("     - 🤖 纯净AI专用：选择你的优质节点 (如 美国/日本/新加坡)")
    print("     - 🌐 日常浏览(一般节点)：选择你的便宜节点 (避开香港，建议日本/新加坡)")
    print("  6. 搞定！Claude/OpenAI 绝无 403 封锁，看 YouTube 满血消耗便宜流量！\n")

if __name__ == "__main__":
    main()
