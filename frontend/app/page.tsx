"use client";

import { useState } from "react";
import { convertSkill, ConversionResponse } from "@/lib/api";

export default function Home() {
  const [sourceContent, setSourceContent] = useState("");
  const [sourcePlatform, setSourcePlatform] = useState("claude");
  const [targetPlatform, setTargetPlatform] = useState("chatgpt");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ConversionResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleConvert = async () => {
    if (!sourceContent.trim()) {
      setError("Please enter skill content");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await convertSkill({
        source_content: sourceContent,
        source_platform: sourcePlatform,
        target_platform: targetPlatform,
      });
      setResult(response);
    } catch (err: any) {
      setError(err.response?.data?.detail || "Conversion failed");
    } finally {
      setLoading(false);
    }
  };

  const downloadResult = () => {
    if (!result) return;

    const blob = new Blob([result.converted_content], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `converted-skill-${targetPlatform}.${targetPlatform === "claude" ? "md" : "txt"}`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            AI Skill Converter
          </h1>
          <p className="text-xl text-gray-600">
            Convert your AI skills between Claude, ChatGPT, and Gemini
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Input Section */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-2xl font-semibold mb-4">Source Skill</h2>

            <div className="mb-4">
              <label className="block text-sm font-medium mb-2">From Platform</label>
              <select
                value={sourcePlatform}
                onChange={(e) => setSourcePlatform(e.target.value)}
                className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                <option value="claude">Claude Skills</option>
                <option value="chatgpt">ChatGPT Custom GPTs</option>
                <option value="gemini">Gemini Gems</option>
              </select>
            </div>

            <div className="mb-4">
              <label className="block text-sm font-medium mb-2">To Platform</label>
              <select
                value={targetPlatform}
                onChange={(e) => setTargetPlatform(e.target.value)}
                className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                <option value="claude">Claude Skills</option>
                <option value="chatgpt">ChatGPT Custom GPTs</option>
                <option value="gemini">Gemini Gems</option>
              </select>
            </div>

            <div className="mb-4">
              <label className="block text-sm font-medium mb-2">
                Paste Your Skill Content
              </label>
              <textarea
                value={sourceContent}
                onChange={(e) => setSourceContent(e.target.value)}
                placeholder="Paste your skill/prompt/gem content here..."
                className="w-full h-64 p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 font-mono text-sm"
              />
            </div>

            <button
              onClick={handleConvert}
              disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition disabled:bg-gray-400"
            >
              {loading ? "Converting..." : "Convert Now"}
            </button>

            {error && (
              <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
                {error}
              </div>
            )}
          </div>

          {/* Result Section */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-2xl font-semibold mb-4">Converted Result</h2>

            {!result && (
              <div className="h-full flex items-center justify-center text-gray-400">
                <p>Results will appear here...</p>
              </div>
            )}

            {result && (
              <div className="space-y-4">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-2">
                    <span className="text-sm font-medium">Confidence:</span>
                    <div className="flex items-center gap-1">
                      <div className="w-24 h-2 bg-gray-200 rounded-full overflow-hidden">
                        <div
                          className="h-full bg-green-500 rounded-full"
                          style={{ width: `${result.confidence_score * 100}%` }}
                        />
                      </div>
                      <span className="text-sm text-gray-600">
                        {(result.confidence_score * 100).toFixed(0)}%
                      </span>
                    </div>
                  </div>
                  <button
                    onClick={downloadResult}
                    className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg text-sm"
                  >
                    Download
                  </button>
                </div>

                <div>
                  <label className="block text-sm font-medium mb-2">
                    Converted Content
                  </label>
                  <textarea
                    value={result.converted_content}
                    readOnly
                    className="w-full h-48 p-3 border rounded-lg font-mono text-sm bg-gray-50"
                  />
                </div>

                {result.conversion_notes.length > 0 && (
                  <div>
                    <h3 className="font-semibold mb-2">Conversion Notes</h3>
                    <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                      {result.conversion_notes.map((note, i) => (
                        <li key={i}>{note}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {result.warnings.length > 0 && (
                  <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                    <h3 className="font-semibold mb-2 text-yellow-800">Warnings</h3>
                    <ul className="list-disc list-inside text-sm text-yellow-700 space-y-1">
                      {result.warnings.map((warning, i) => (
                        <li key={i}>{warning}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {result.incompatible_features.length > 0 && (
                  <div className="bg-red-50 border border-red-200 rounded-lg p-3">
                    <h3 className="font-semibold mb-2 text-red-800">
                      Incompatible Features
                    </h3>
                    <ul className="list-disc list-inside text-sm text-red-700 space-y-1">
                      {result.incompatible_features.map((feature, i) => (
                        <li key={i}>{feature}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
